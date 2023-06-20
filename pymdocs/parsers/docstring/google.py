import inspect
import re
from typing import Iterator

DOCSTRING_SECTIONS = {
    'Args',
    'Attributes',
    'Examples',
    'Raises',
    'Returns',
    'Yields'
}

SINGLE_SECTIONS = {
    'Examples'
}

DOCSTRING_SECTION_PATTERN = re.compile(
    r'^(?P<type>('
    + '|'.join(
        section
        for section in DOCSTRING_SECTIONS
    )
    + r')):',
    re.MULTILINE
)

DOCSTRING_TYPING_ANNOTATION = re.compile(
    r'(?P<typing_annotation>('
    r'\([^\(\)]+\)|'
    r'[A-Za-z_][A-Za-z0-9_]*'
    r'))'
)

DOCSTRING_ARG_PATTERN = re.compile(
    r'^[ \t]+(?P<name>(\*{1,2})?[A-Za-z_][A-Za-z0-9_]*)'
    rf'(\s+{DOCSTRING_TYPING_ANNOTATION})?\s*:',
    re.MULTILINE
)

DOCSTRING_EXAMPLES_PATTERN = re.compile(r'(?!.*)')

DOCSTRING_RAISES_PATTERN = re.compile(
    r'^[ \t]+(?P<exception>[A-Za-z_][A-Za-z0-9_]*)\s*:',
    re.MULTILINE
)

DOCSTRING_RETURNS_PATTERN = re.compile(
    rf'^[ \t]+{DOCSTRING_TYPING_ANNOTATION.pattern}\s*:',
    re.MULTILINE
)


SECTION_ELEMENT_PATTERN_MAP = {
    'Args': DOCSTRING_ARG_PATTERN,
    'Attributes': DOCSTRING_ARG_PATTERN,
    'Examples': DOCSTRING_EXAMPLES_PATTERN,
    'Raises': DOCSTRING_RAISES_PATTERN,
    'Returns': DOCSTRING_RETURNS_PATTERN,
    'Yields': DOCSTRING_RETURNS_PATTERN
}


class DocstringElement:
    """Base class for docstring elements"""


class DocstringSection(DocstringElement):
    """Base class for docstring section"""

    def __init__(
        self,
        attributes: list[DocstringElement]
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
        typing_annotation: (str | None) = None,
        description: (str | None) = None
    ):
        self.name = name
        self.typing_annotation = typing_annotation
        self.description = description


class DocstringArgsSection(DocstringSection):
    """
    Class for docstring 'Args' section

    Attributes:
        attributes: list[DocstringArg], list of arguments
    """

    def __init__(self, attributes: list[DocstringArg]):
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
        typing_annotation: (str | None) = None,
        description: (str | None) = None
    ):
        self.name = name
        self.typing_annotation = typing_annotation
        self.description = description


class DocstringAttributesSection(DocstringSection):
    """
    Class for docstring 'Attributes' section

    Attributes:
        attributes: list[DocstringAttribute], list of attributes
    """

    def __init__(self, attributes: list[DocstringArg]):
        super().__init__(attributes)


class DocstringExample(DocstringElement):
    """
    Class for docstring 'Examples' section element

    Attributes:
        description: str, docstring example
    """

    def __init__(self, description: str):
        self.description = description


class DocstringExamplesSection(DocstringSection):
    """
    Class for docstring 'Examples' section

    Attributes:
        attributes: list[DocstringExample], list of docstring examples
    """

    def __init__(self, attributes: list[DocstringExample]):
        super().__init__(attributes)


class DocstringRaises(DocstringElement):
    """
    Class for docstring 'Raises' section elements

    Attributes:
        exception: str, exception name
        description: str, exception description
    """

    def __init__(self, exception: str, description: str):
        self.exception = exception
        self.description = description


class DocstringRaisesSection(DocstringSection):
    """
    Class for docstring 'Raises' section

    Attributes:
        attributes: list[DocstringRaises], list of rasing exceptions
    """

    def __init__(self, attributes: list[DocstringRaises]):
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
        description: str
    ):
        self.typing_annotation = typing_annotation
        self.description = description


class DocstringReturnsSection(DocstringSection):
    """
    Class for docstring 'Returns' section

    Attributes:
        attributes: list[DocstringReturns], returning value description
    """

    def __init__(self, attributes: list[DocstringReturns]):
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
        description: str
    ):
        self.typing_annotation = typing_annotation
        self.description = description


class DocstringYiedlsSection(DocstringSection):
    """
    Class for docstring 'Yields' section

    Attributes:
        attributes: list[DocstringYields], yielding value description
    """

    def __init__(self, attributes: list[DocstringYiedls]):
        super().__init__(attributes)


class Docstring(DocstringSection):
    """
    Class for python docstring

    Attributes:
        attributes: list[DocstringSection], list of docstring sections
        description: str, docstring title
    """

    def __init__(
        self,
        attributes: list[DocstringSection],
        description: str
    ):
        self.description = description
        super().__init__(attributes)

    @property
    def args(self) -> list[DocstringArg]:
        """Returns list of docstring 'Args' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringArgsSection):
                return section._attributes

        return []

    @property
    def attributes(self) -> list[DocstringAttribute]:
        """Returns list of docstring 'Attributes' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringAttributesSection):
                return section._attributes

        return []

    @property
    def examples(self) -> list[DocstringExample]:
        """Returns list of docstring 'Examples' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringExamplesSection):
                return section._attributes

        return []

    @property
    def raises(self) -> list[DocstringRaises]:
        """Returns list of docstring 'Raises' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringRaisesSection):
                return section._attributes

        return []

    @property
    def returns(self) -> list[DocstringReturns]:
        """Returns list of docstring 'Returns' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringReturnsSection):
                return section._attributes

        return []

    @property
    def yields(self) -> list[DocstringYiedls]:
        """Returns list of docstring 'Yields' section elements"""
        for section in self._attributes:
            if isinstance(section, DocstringYiedlsSection):
                return section._attributes

        return []


SECTION_ELEMENT_CLASS_MAP: dict[str, type[DocstringElement]] = {
    'Args': DocstringArg,
    'Attributes': DocstringAttribute,
    'Examples': DocstringExample,
    'Raises': DocstringRaises,
    'Returns': DocstringReturns,
    'Yields': DocstringYiedls
}

SECTION_CLASS_MAP: dict[str, type[DocstringSection]] = {
    'Args': DocstringArgsSection,
    'Attributes': DocstringAttributesSection,
    'Examples': DocstringExamplesSection,
    'Raises': DocstringRaisesSection,
    'Returns': DocstringReturnsSection,
    'Yields': DocstringYiedlsSection
}


def iter_split(
    pattern: re.Pattern,
    text: str
) -> Iterator[tuple[(re.Match | None), str, int, int]]:
    """
    Iterates through pattern matches and yiedls text between them

    Args:
        pattern: re.Pattern, pattern to search
        text: str, text to search pattern

    Yields:
        tuple[(re.Match | None), str, int, int]: tuple of match,
            text till next metch or text end, start of match and end of text
    """
    pos = 0
    last_group: re.Match = None

    for group in pattern.finditer(text):
        last_group_end = group.start()
        last_group_start = (
            0 if last_group is None
            else last_group.start()
        )

        yield (
            last_group,
            text[pos:last_group_end],
            last_group_start,
            last_group_end
        )

        pos = group.end()
        last_group = group

    last_group_end = len(text)
    last_group_start = (
        0 if last_group is None
        else last_group.start()
    )

    yield (
        last_group,
        text[pos:last_group_end],
        last_group_start,
        last_group_end
    )


def parse_section(text: str, section_type: str) -> DocstringSection:
    """
    Parses section from text by section type

    Args:
        text: str, text to parse
        section_type: str, section type (Args, Attributes, Raises, etc.)

    Returns:
        DocstringSection: DocstringSection object
    """

    element_pattern = SECTION_ELEMENT_PATTERN_MAP[section_type]
    section = SECTION_CLASS_MAP[section_type]
    section_element = SECTION_ELEMENT_CLASS_MAP[section_type]
    attributes = []

    for group, text, _, _ in iter_split(element_pattern, text):
        description = inspect.cleandoc(text)
        if section_type in SINGLE_SECTIONS:
            attributes.append(
                section_element(description=description)
            )
        elif group is not None:
            attributes.append(
                section_element(
                    description=description,
                    **group.groupdict()
                )
            )

    return section(
        attributes=attributes
    )


def parse(docstring: str):
    """
    Parses Google Style docstring

    Args:
        docstring: Google Style docstring

    Returns:
        Docstring: Docstring object
    """
    cleared_docstring = inspect.cleandoc(docstring)
    description = None
    sections = []

    for group, text, _, _ in iter_split(
        DOCSTRING_SECTION_PATTERN,
        cleared_docstring
    ):
        if group is None:
            description = inspect.cleandoc(text)
        else:
            section_type = group.group('type')
            sections.append(parse_section(text, section_type))

    return Docstring(
        attributes=sections,
        description=description
    )
