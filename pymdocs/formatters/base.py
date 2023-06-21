from enum import Enum

import pymdocs.formatters.markdown_constructor as md
from pymdocs.parsers.ast import AstWrapper


class FormatterType(int, Enum):
    """Enum for formatter types"""
    DOCSTRING = 1
    FUNCTION = 2
    CLASS = 3
    MODULE = 4
    PACKAGE = 5


FORMATTERS_HIERARCHY = list(
    member
    for member in sorted(FormatterType, key=lambda x: x.value)
)


class BaseFormatter:
    """
    Base class for markdown formatters

    Attributes:
        _requires: tuple[FormatterType, ...], data attribute,tuple of
            required formatters
        formatters: (dict[FormatterType, BaseFormatter] | None), formatters
            to be used inside
    """

    _requires: tuple[FormatterType, ...] = ()

    def _validate(
        self,
        formatters: '(dict[FormatterType, BaseFormatter] | None)'
    ):
        """
        Validates that all required formatters passed

        Raises:
            ValueError: if required formatter is not set
        """
        for formatter_type in self._requires:
            if formatter_type not in formatters:
                raise ValueError(
                    f'{formatter_type} formatter is not set'
                )

    def __init__(
        self,
        formatters: '(dict[FormatterType, BaseFormatter] | None)'
    ):
        self.formatters = (formatters or [])
        self._validate(self.formatters)

    def format(self, obj: AstWrapper, **kwargs) -> md.MarkdownContainer:
        """Returns markdown representation for obj"""

    def format_by(
        self,
        formatter_type: FormatterType,
        obj: AstWrapper,
        **kwargs
    ) -> md.MarkdownContainer:
        """
        Formats object by additional formatter

        Args:
            formatter_type: FormatterType, type of needed formatter
            obj: AstWrapper, object to format as Markdown

        Returns:
            MarkdownContainer: markdown representation of object

        Raises:
            ValueError: if needed formatter is not set
        """

        formatter = self.formatters.get(formatter_type)
        if formatter is None:
            raise ValueError(
                f'{formatter_type} formatter is not set'
            )

        return formatter.format(obj, **kwargs)
