from enum import Enum
from typing import Any, Dict, Generic, List, Optional, Tuple, TypeVar, Union

import pymdocs.formatters.markdown_constructor as md
from pymdocs.parsers.ast import ElementDefinition
from pymdocs.parsers.docstring import Docstring

T = TypeVar('T', bound=Union[ElementDefinition, Docstring])


class FormatterType(int, Enum):
    """Enum for formatter types"""
    DOCSTRING = 1
    FUNCTION = 2
    CLASS = 3
    MODULE = 4
    PACKAGE = 5


FORMATTERS_HIERARCHY: List[FormatterType] = list(
    member
    for member in sorted(FormatterType, key=lambda x: x.value)
)


class BaseFormatter(Generic[T]):
    """
    Base class for markdown formatters

    Attributes:
        _requires: Tuple[FormatterType, ...], data attribute,tuple of
            required formatters
        formatters: (Dict[FormatterType, BaseFormatter] | None), formatters
            to be used inside
    """

    _requires: Tuple[FormatterType, ...] = ()

    def _validate(
        self,
        formatters: Dict[FormatterType, Any]
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
        formatters: Optional[Dict[FormatterType, Any]] = None
    ):
        self.formatters = (formatters or {})
        self._validate(self.formatters)

    def format(
        self,
        obj: T
    ) -> md.MarkdownElement:
        """Returns markdown representation for obj"""
        return md.MarkdownElement()

    def format_by(
        self,
        formatter_type: FormatterType,
        obj: Any,
        *args: Any,
        **kwargs: Any
    ) -> md.MarkdownElement:
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

        return formatter.format(obj, *args, **kwargs)
