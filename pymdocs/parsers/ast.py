import ast
import os

import parsers.docstring.google as doc

BINOPS = {
    ast.BitOr: '|'
}


class DocElement:
    """Base class for Python AST element wrapper"""

    _properties: tuple[str, ...] = (
        'lineno',
    )

    def __init__(self, ast_element: (ast.AST | None)):
        self.ast_element = ast_element

    @property
    def lineno(self) -> (int | None):
        """
        Returns line number of the element in file

        Returns: int, line number
        """

        if self.ast_element is None:
            return None

        return self.ast_element.lineno

    def properties(self) -> dict:
        """
        Returns dict of object properties values
        """

        return {
            property: self.__getattribute__(property)
            for property in self._properties
        }

    def dict(self) -> dict:
        """
        Returns element dict representation (and all subelements recursively)
        """
        d = {}
        for property in self._properties:
            value = self.__getattribute__(property)
            if isinstance(value, list):
                d[property] = [
                    (element if isinstance(element, str) else element.dict())
                    for element in value
                ]
            else:
                d[property] = (
                    value
                    if isinstance(value, (str, doc.Docstring))
                    else value.dict()
                )

        return d


class Typing(DocElement):
    """Class for Python typing annotations representation"""

    _properties: tuple[str, ...] = (
        'annotation',
    )

    @property
    def annotation(self) -> str:
        """
        Returns string representation of typing annotation
        """
        if self.ast_element is None:
            return 'Any'
        if isinstance(self.ast_element, ast.Name):
            return self.ast_element.id
        if isinstance(self.ast_element, ast.Constant):
            return str(self.ast_element.value)
        elif isinstance(self.ast_element, ast.Subscript):
            value = Typing(self.ast_element.value).annotation
            value_slice = Typing(self.ast_element.slice).annotation
            return f'{value}[{value_slice}]'
        elif isinstance(self.ast_element, ast.Attribute):
            value = Typing(self.ast_element.value).annotation
            value_attr = self.ast_element.attr
            return f'{value}.{value_attr}'
        elif isinstance(self.ast_element, ast.Tuple):
            return ', '.join(
                Typing(element).annotation
                for element in self.ast_element.elts
            )
        elif isinstance(self.ast_element, ast.BinOp):
            left = Typing(self.ast_element.left).annotation
            right = Typing(self.ast_element.right).annotation
            op = '|'
            for binop, symbol in BINOPS.items():
                if isinstance(self.ast_element.op, binop):
                    op = symbol

            return '(' + ' '.join((left, op, right)) + ')'

        raise ValueError(f'Unknown annotation type: {self.ast_element}')


class Argument(DocElement):
    """Class for function argument representation"""

    _properties: tuple[str, ...] = (
        'name',
        'type'
    )

    def __init__(self, ast_element: ast.arg):
        self.ast_element = ast_element

    @property
    def name(self) -> str:
        """Returns name of function argument"""
        return self.ast_element.arg

    @property
    def type(self) -> Typing:
        """
        Returns typing annotation of function argument

        Returns: Typing, typing annotation
        """
        return Typing(self.ast_element.annotation)


class FunctionDefinition(DocElement):
    """Class for function representation"""

    _properties: tuple[str, ...] = (
        'name',
        'arguments',
        'returns',
        'docstring'
    )

    def __init__(
        self,
        ast_element: ast.FunctionDef
    ):
        self.ast_element = ast_element

    @property
    def name(self) -> str:
        """Returns function name"""
        return self.ast_element.name

    @property
    def arguments(self) -> list[Argument]:
        """Returns list of function arguments"""
        return [
            Argument(element)
            for element in self.ast_element.args.args
        ]

    @property
    def returns(self) -> Typing:
        """Returns function return typing annotation"""
        return Typing(self.ast_element.returns)

    @property
    def docstring(self) -> (doc.Docstring | None):
        """Returns function docstring if exists"""
        if self.ast_element.body:
            potentional_docstring = self.ast_element.body[0]
            if isinstance(potentional_docstring, ast.Expr):
                potentional_docstring_value = potentional_docstring.value
                if isinstance(potentional_docstring_value, ast.Constant):
                    return doc.parse(potentional_docstring_value.value)


class ClassDefinition(DocElement):
    """Class for Python class representation"""

    _properties: tuple[str, ...] = (
        'name',
        'inherits',
        'methods',
        'docstring'
    )

    def __init__(
        self,
        ast_element: ast.ClassDef
    ):
        self.ast_element = ast_element

    @property
    def name(self) -> str:
        """Returns class name"""
        return self.ast_element.name

    @property
    def inherits(self) -> list[str]:
        """Returns class bases"""
        return [
            base.id
            for base in self.ast_element.bases
            if isinstance(base, ast.Name)
        ]

    @property
    def docstring(self) -> (doc.Docstring | None):
        """Retuns class docstring if exists"""
        if self.ast_element.body:
            potentional_docstring = self.ast_element.body[0]
            if isinstance(potentional_docstring, ast.Expr):
                potentional_docstring_value = potentional_docstring.value
                if isinstance(potentional_docstring_value, ast.Constant):
                    return doc.parse(potentional_docstring_value.value)

    @property
    def methods(self) -> list[FunctionDefinition]:
        """Returns list of class methods"""
        return [
            FunctionDefinition(element)
            for element in self.ast_element.body
            if isinstance(element, ast.FunctionDef)
        ]


class ModuleDefinition(DocElement):

    _properties: tuple[str, ...] = (
        'name',
        'classes',
        'functions',
        'docstring'
    )

    def __init__(self, ast_element: ast.Module, path: str):
        self.path = path
        self.ast_element = ast_element

    @property
    def name(self):
        """Returns module name"""
        return os.path.basename(self.path).replace('.py', '')

    @property
    def docstring(self) -> (doc.Docstring | None):
        """Retuns module docstring if exists"""
        if self.ast_element.body:
            potentional_docstring = self.ast_element.body[0]
            if isinstance(potentional_docstring, ast.Expr):
                potentional_docstring_value = potentional_docstring.value
                if isinstance(potentional_docstring_value, ast.Constant):
                    return doc.parse(potentional_docstring_value.value)

    @property
    def classes(self) -> list[ClassDefinition]:
        """Returns list of module classes"""
        return [
            ClassDefinition(element)
            for element in self.ast_element.body
            if isinstance(element, ast.ClassDef)
        ]

    @property
    def functions(self) -> list[FunctionDefinition]:
        """Returns list of module functions"""
        return [
            FunctionDefinition(element)
            for element in self.ast_element.body
            if isinstance(element, ast.FunctionDef)
        ]


def parse(path: str) -> ModuleDefinition:
    """
    Parses Python module content

    Args:
        path: pathlib.Path, Python module path

    Returns:
        ModuleDefinition: module objects definition
    """

    with open(path) as f:
        source = f.read()

    tree = ast.parse(source)
    return ModuleDefinition(tree, path)
