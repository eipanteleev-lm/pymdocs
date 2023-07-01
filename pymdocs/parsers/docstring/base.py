from typing import Any, List, Optional


class DocstringElement:
    """Base class for docstring elements"""

    def __init__(self):
        ...


class DocstringSection:
    """Base class for docstring section"""

    def __init__(
        self,
        attributes: List[Any]
    ):
        self._attributes = attributes


class DocstringArg(DocstringElement):
    """
    Class for docstring 'Args' section element

    Attributes:
        name: str, name of argument
        typing_annotation: (str | None), argument type
        description: str, argument description
    """

    def __init__(
        self,
        name: str,
        typing_annotation: Optional[str] = None,
        description: Optional[str] = None
    ):
        self.name = name
        self.typing_annotation = typing_annotation
        self.description = description


class DocstringArgsSection(DocstringSection):
    """
    Class for docstring 'Args' section

    Attributes:
        attributes: List[DocstringArg], list of arguments
    """

    def __init__(self, attributes: List[DocstringArg]):
        super().__init__(attributes)


class DocstringAttribute(DocstringElement):
    """
    Class for docstring 'Attributes' section element

    Attributes:
        name: str, name of attribute
        typing_annotation: (str | None), attribute type
        description: str, attribute description
    """

    def __init__(
        self,
        name: str,
        typing_annotation: Optional[str] = None,
        description: Optional[str] = None
    ):
        self.name = name
        self.typing_annotation = typing_annotation
        self.description = description

    def __repr__(self):
        return f'{self.__name__}({self.name}, {self.typing_annotation})'


class DocstringAttributesSection(DocstringSection):
    """
    Class for docstring 'Attributes' section

    Attributes:
        attributes: List[DocstringAttribute], list of attributes
    """

    def __init__(self, attributes: List[DocstringArg]):
        super().__init__(attributes)


class DocstringExample(DocstringElement):
    """
    Class for docstring 'Examples' section element

    Attributes:
        description: str, docstring example
    """

    def __init__(self, description: Optional[str] = None):
        self.description = description


class DocstringExamplesSection(DocstringSection):
    """
    Class for docstring 'Examples' section

    Attributes:
        attributes: List[DocstringExample], list of docstring examples
    """

    def __init__(self, attributes: List[DocstringExample]):
        super().__init__(attributes)


class DocstringRaises(DocstringElement):
    """
    Class for docstring 'Raises' section elements

    Attributes:
        exception: str, exception name
        description: str, exception description
    """

    def __init__(self, exception: str, description: Optional[str] = None):
        self.exception = exception
        self.description = description

    def __repr__(self):
        return f'{self.__name__}({self.exception})'


class DocstringRaisesSection(DocstringSection):
    """
    Class for docstring 'Raises' section

    Attributes:
        attributes: List[DocstringRaises], list of rasing exceptions
    """

    def __init__(self, attributes: List[DocstringRaises]):
        super().__init__(attributes)


class DocstringReturns(DocstringElement):
    """
    Class for docstring 'Returns' section elements

    Attributes:
        typing_annotation: str, returning value type
        description: str, returning value description
    """

    def __init__(
        self,
        typing_annotation: str,
        description: Optional[str] = None
    ):
        self.typing_annotation = typing_annotation
        self.description = description

    def __repr__(self):
        return f'{self.__name__}({self.typing_annotation})'


class DocstringReturnsSection(DocstringSection):
    """
    Class for docstring 'Returns' section

    Attributes:
        attributes: List[DocstringReturns], returning value description
    """

    def __init__(self, attributes: List[DocstringReturns]):
        super().__init__(attributes)


class DocstringYiedls(DocstringElement):
    """
    Class for docstring 'Yields' section elements

    Attributes:
        typing_annotation: str, yielding value type
        description: str, yielding value description
    """

    def __init__(
        self,
        typing_annotation: str,
        description: Optional[str] = None
    ):
        self.typing_annotation = typing_annotation
        self.description = description

    def __repr__(self):
        return f'{self.__name__}({self.typing_annotation})'


class DocstringYiedlsSection(DocstringSection):
    """
    Class for docstring 'Yields' section

    Attributes:
        attributes: List[DocstringYields], yielding value description
    """

    def __init__(self, attributes: List[DocstringYiedls]):
        super().__init__(attributes)


class Docstring(DocstringSection):
    """
    Class for python docstring

    Attributes:
        attributes: List[DocstringSection], list of docstring sections
        description: str, docstring title
    """

    def __init__(
        self,
        attributes: List[DocstringSection],
        description: Optional[str] = None
    ):
        self.description = description
        super().__init__(attributes)

    @property
    def args(self) -> List[DocstringArg]:
        """Returns list of docstring 'Args' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringArgsSection):
                return section._attributes

        return []

    @property
    def attributes(self) -> List[DocstringAttribute]:
        """Returns list of docstring 'Attributes' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringAttributesSection):
                return section._attributes

        return []

    @property
    def examples(self) -> List[DocstringExample]:
        """Returns list of docstring 'Examples' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringExamplesSection):
                return section._attributes

        return []

    @property
    def raises(self) -> List[DocstringRaises]:
        """Returns list of docstring 'Raises' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringRaisesSection):
                return section._attributes

        return []

    @property
    def returns(self) -> List[DocstringReturns]:
        """Returns list of docstring 'Returns' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringReturnsSection):
                return section._attributes

        return []

    @property
    def yields(self) -> List[DocstringYiedls]:
        """Returns list of docstring 'Yields' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringYiedlsSection):
                return section._attributes

        return []
