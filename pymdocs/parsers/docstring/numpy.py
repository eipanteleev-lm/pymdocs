import inspect
import re
from enum import Enum
from typing import Dict, Type, TypeVar

from pymdocs.parsers.docstring.base import (
    Docstring,
    DocstringArg,
    DocstringArgsSection,
    DocstringAttribute,
    DocstringAttributesSection,
    DocstringElement,
    DocstringExample,
    DocstringExamplesSection,
    DocstringRaises,
    DocstringRaisesSection,
    DocstringReturns,
    DocstringReturnsSection,
    DocstringSection,
    DocstringYiedls,
    DocstringYiedlsSection,
)
from pymdocs.parsers.docstring.helpers import iter_split


class DocstringSections(str, Enum):
    ARGS = 'Parameters'
    ATTRIBUTES = 'Attributes'
    EXAMPLES = 'Examples'
    NOTES = 'Notes'
    RAISES = 'Raises'
    RETURNS = 'Returns'
    SEE_ALSO = 'See Also'
    YIELDS = 'Yields'


SINGLE_SECTIONS = {
    DocstringSections.EXAMPLES,
    DocstringSections.NOTES,
    DocstringSections.SEE_ALSO
}


DOCSTRING_SECTION_PATTERN = re.compile(
    r'^(?P<type>('
    + '|'.join(
        member.value
        for member in DocstringSections
    )
    + r'))[ \t]*\n----*',
    re.MULTILINE
)

DOCSTRING_TYPING_ANNOTATION = re.compile(
    r'(?P<typing_annotation>('
    r'\([^\(\)]+\)|'
    r'[A-Za-z_][A-Za-z0-9_]*'
    r'))'
)

DOCSTRING_ARG_PATTERN = re.compile(
    r'^(?P<name>(\*{1,2})?[A-Za-z_][A-Za-z0-9_]*)[ \t]*:'
    rf'([ \t]*{DOCSTRING_TYPING_ANNOTATION}[ \t]*)?[ \t]*\n',
    re.MULTILINE
)

DOCSTRING_EXAMPLES_PATTERN = re.compile(r'(?!.*)')

DOCSTRING_RAISES_PATTERN = re.compile(
    r'^(?P<exception>[A-Za-z_][A-Za-z0-9_]*)[ \t]*\n',
    re.MULTILINE
)

DOCSTRING_RETURNS_PATTERN = re.compile(
    rf'^{DOCSTRING_TYPING_ANNOTATION.pattern}[ \t]*\n',
    re.MULTILINE
)


SECTION_ELEMENT_PATTERN_MAP: Dict[DocstringSections, re.Pattern] = {
    DocstringSections.ARGS: DOCSTRING_ARG_PATTERN,
    DocstringSections.ATTRIBUTES: DOCSTRING_ARG_PATTERN,
    DocstringSections.EXAMPLES: DOCSTRING_EXAMPLES_PATTERN,
    DocstringSections.RAISES: DOCSTRING_RAISES_PATTERN,
    DocstringSections.RETURNS: DOCSTRING_RETURNS_PATTERN,
    DocstringSections.YIELDS: DOCSTRING_RETURNS_PATTERN
}


SECTION_ELEMENT_CLASS_MAP: Dict[DocstringSections, Type[DocstringElement]] = {
    DocstringSections.ARGS: DocstringArg,
    DocstringSections.ATTRIBUTES: DocstringAttribute,
    DocstringSections.EXAMPLES: DocstringExample,
    DocstringSections.RAISES: DocstringRaises,
    DocstringSections.RETURNS: DocstringReturns,
    DocstringSections.YIELDS: DocstringYiedls
}

SECTION_CLASS_MAP: Dict[str, Type[DocstringSection]] = {
    DocstringSections.ARGS: DocstringArgsSection,
    DocstringSections.ATTRIBUTES: DocstringAttributesSection,
    DocstringSections.EXAMPLES: DocstringExamplesSection,
    DocstringSections.RAISES: DocstringRaisesSection,
    DocstringSections.RETURNS: DocstringReturnsSection,
    DocstringSections.YIELDS: DocstringYiedlsSection
}


def parse_section(text: str, section_type: str) -> DocstringSection:
    """
    Parses section from text by section type

    Parameters
    ----------

    text: str
        text to parse
    section_type: str
        section type (Parameters, Attributes, Raises, etc.)

    Returns
    -------

    DocstringSection
        DocstringSection object
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


def parse(docstring: str) -> Docstring:
    """
    Parses Numpy Style docstring

    Parameters
    ----------
    docstring: str
        Google Style docstring

    Returns
    -------
    Docstring
        Docstring object
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
