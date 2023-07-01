import ast
import os
from typing import Generic, List, Optional, TypeVar, Union

import pymdocs.parsers.docstring as doc

T = TypeVar('T', bound=ast.AST)

BINOPS = {
    ast.BitOr: '|'
}


class ElementDefinition:
    """Base class for Python code structures"""


class AstWrapper(ElementDefinition, Generic[T]):
    """
    Base class for Python AST element wrapper

    Attributes:
        ast_element: ast.AST, AST tree node
        path: str, path to file contains element
    """

    def __init__(
        self,
        ast_element: T,
        path: str
    ):
        self.ast_element = ast_element
        self.path = path

    @property
    def lineno(self) -> int:
        """
        Returns line number of the element in file

        Returns:
            int, line number
        """

        return self.ast_element.lineno


class Typing(AstWrapper):
    """Class for Python typing annotations representation"""

    @property
    def annotation(self) -> str:
        """
        Returns string representation of typing annotation
        """
        if isinstance(self.ast_element, ast.Name):
            return self.ast_element.id
        elif isinstance(self.ast_element, ast.Constant):
            return str(self.ast_element.value)
        elif isinstance(self.ast_element, ast.Subscript):
            value = Typing(self.ast_element.value, self.path).annotation
            value_slice = Typing(self.ast_element.slice, self.path).annotation
            return f'{value}[{value_slice}]'
        elif isinstance(self.ast_element, ast.Attribute):
            value = Typing(self.ast_element.value, self.path).annotation
            value_attr = self.ast_element.attr
            return f'{value}.{value_attr}'
        elif isinstance(self.ast_element, ast.Tuple):
            return ', '.join(
                Typing(element, self.path).annotation
                for element in self.ast_element.elts
            )
        elif isinstance(self.ast_element, ast.BinOp):
            left = Typing(self.ast_element.left, self.path).annotation
            right = Typing(self.ast_element.right, self.path).annotation
            op = '|'
            for binop, symbol in BINOPS.items():
                if isinstance(self.ast_element.op, binop):
                    op = symbol

            return '(' + ' '.join((left, op, right)) + ')'

        raise ValueError(f'Unknown annotation type: {self.ast_element}')


class Argument(AstWrapper[ast.arg]):
    """Class for function argument representation"""

    @property
    def name(self) -> str:
        """Returns name of function argument"""
        return self.ast_element.arg

    @property
    def type(self) -> Optional[Typing]:
        """
        Returns typing annotation of function argument

        Returns: Typing, typing annotation
        """
        if self.ast_element.annotation is None:
            return None

        return Typing(
            self.ast_element.annotation,
            self.path
        )


class FunctionDefinition(AstWrapper[ast.FunctionDef]):
    """Class for function representation"""

    @property
    def name(self) -> str:
        """Returns function name"""
        return self.ast_element.name

    @property
    def arguments(self) -> List[Argument]:
        """Returns list of function arguments"""
        return [
            Argument(element, self.path)
            for element in self.ast_element.args.args
        ]

    @property
    def returns(self) -> Optional[Typing]:
        """Returns function return typing annotation"""
        if self.ast_element.returns is None:
            return None

        return Typing(
            self.ast_element.returns,
            self.path
        )

    @property
    def docstring(self) -> Optional[doc.Docstring]:
        """Returns function docstring if exists"""
        if self.ast_element.body:
            potentional_docstring = self.ast_element.body[0]
            if isinstance(potentional_docstring, ast.Expr):
                potentional_docstring_value = potentional_docstring.value
                if isinstance(potentional_docstring_value, ast.Constant):
                    return doc.parse(potentional_docstring_value.value)

        return None


class ClassDefinition(AstWrapper[ast.ClassDef]):
    """Class for Python class representation"""

    @property
    def name(self) -> str:
        """Returns class name"""
        return self.ast_element.name

    @property
    def inherits(self) -> List[str]:
        """Returns class bases"""
        return [
            base.id
            for base in self.ast_element.bases
            if isinstance(base, ast.Name)
        ]

    @property
    def docstring(self) -> Optional[doc.Docstring]:
        """Retuns class docstring if exists"""
        if self.ast_element.body:
            potentional_docstring = self.ast_element.body[0]
            if isinstance(potentional_docstring, ast.Expr):
                potentional_docstring_value = potentional_docstring.value
                if isinstance(potentional_docstring_value, ast.Constant):
                    return doc.parse(potentional_docstring_value.value)

        return None

    @property
    def methods(self) -> List[FunctionDefinition]:
        """Returns list of class methods"""
        return [
            FunctionDefinition(element, self.path)
            for element in self.ast_element.body
            if isinstance(element, ast.FunctionDef)
        ]


class ModuleDefinition(AstWrapper[ast.Module]):
    """Class for Python module representation"""

    @property
    def name(self) -> str:
        """Returns module name"""
        return os.path.basename(self.path).replace('.py', '')

    @property
    def docstring(self) -> Optional[doc.Docstring]:
        """Retuns module docstring if exists"""
        if self.ast_element.body:
            potentional_docstring = self.ast_element.body[0]
            if isinstance(potentional_docstring, ast.Expr):
                potentional_docstring_value = potentional_docstring.value
                if isinstance(potentional_docstring_value, ast.Constant):
                    return doc.parse(potentional_docstring_value.value)

        return None

    @property
    def classes(self) -> List[ClassDefinition]:
        """Returns list of module classes"""
        return [
            ClassDefinition(element, self.path)
            for element in self.ast_element.body
            if isinstance(element, ast.ClassDef)
        ]

    @property
    def functions(self) -> List[FunctionDefinition]:
        """Returns list of module functions"""
        return [
            FunctionDefinition(element, self.path)
            for element in self.ast_element.body
            if isinstance(element, ast.FunctionDef)
        ]


class PackageDefinition(ElementDefinition):
    """Class for python package representation"""

    def __init__(
        self,
        modules: List[ModuleDefinition],
        packages: 'List[PackageDefinition]',
        path: str
    ):
        self.modules = modules
        self.packages = packages
        self.path = path

    @property
    def name(self) -> str:
        """Returns package name"""
        return os.path.basename(self.path)


def _is_python_module(path: str) -> bool:
    """Simple check if file is python module"""
    if os.path.isfile(path):
        if path.endswith('.py'):
            return True

    return False


def parse_module(path: str) -> ModuleDefinition:
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


def parse(path: str) -> Optional[Union[PackageDefinition, ModuleDefinition]]:
    """
    Parses Python module or package content

    Args:
        path: pathlib.Path, Python module path

    Returns:
        (ModuleDefinition | PackageDefinition | None): module or package
            objects definition
    """

    if _is_python_module(path):
        return parse_module(path)
    elif os.path.isdir(path):
        modules = []
        packages = []

        for entity in os.listdir(path):
            entity_path = os.path.join(path, entity)
            entity_def = parse(entity_path)

            if entity_def is None:
                continue
            elif isinstance(entity_def, ModuleDefinition):
                modules.append(entity_def)
            elif isinstance(entity_def, PackageDefinition):
                packages.append(entity_def)

        if modules or packages:
            return PackageDefinition(
                modules=modules,
                packages=packages,
                path=path
            )

    return None
