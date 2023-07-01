from typing import Generic, List, Optional, TypeVar

T = TypeVar('T', bound='DocstringElement')


class DocstringElement:
    """Base class for docstring elements"""


class DocstringSection(Generic[T]):
    """Base class for docstring section"""

    def __init__(
        self,
        attributes: List[T]
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


class DocstringArgsSection(DocstringSection[DocstringArg]):
    """
    Class for docstring 'Args' section

    Attributes:
        attributes: List[DocstringArg], list of arguments
    """


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


class DocstringAttributesSection(DocstringSection[DocstringAttribute]):
    """
    Class for docstring 'Attributes' section

    Attributes:
        attributes: List[DocstringAttribute], list of attributes
    """


class DocstringExample(DocstringElement):
    """
    Class for docstring 'Examples' section element

    Attributes:
        description: str, docstring example
    """

    def __init__(self, description: str):
        self.description = description


class DocstringExamplesSection(DocstringSection[DocstringExample]):
    """
    Class for docstring 'Examples' section

    Attributes:
        attributes: List[DocstringExample], list of docstring examples
    """


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


class DocstringRaisesSection(DocstringSection[DocstringRaises]):
    """
    Class for docstring 'Raises' section

    Attributes:
        attributes: List[DocstringRaises], list of rasing exceptions
    """


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


class DocstringReturnsSection(DocstringSection[DocstringReturns]):
    """
    Class for docstring 'Returns' section

    Attributes:
        attributes: List[DocstringReturns], returning value description
    """


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


class DocstringYiedlsSection(DocstringSection[DocstringYiedls]):
    """
    Class for docstring 'Yields' section

    Attributes:
        attributes: List[DocstringYields], yielding value description
    """


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
