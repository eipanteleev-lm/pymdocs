from pymdocs.formatters.base import (
    BaseFormatter,
    FORMATTERS_HIERARCHY,
    FormatterType
)
from pymdocs.formatters.class_formatter import ClassFormatter
from pymdocs.formatters.docstring_formatter import DocstringFormatter
from pymdocs.formatters.function_formatter import FunctionFormatter
from pymdocs.formatters.module_formatter import ModuleFormatter
from pymdocs.formatters.package_formatter import PackageFormatter
from pymdocs.parsers.ast import (
    AstWrapper,
    ClassDefinition,
    FunctionDefinition,
    ModuleDefinition,
    PackageDefinition
)
from pymdocs.parsers.docstring.google import Docstring


_FORMATTERS_TARGET_MAP = {
    FormatterType.DOCSTRING: Docstring,
    FormatterType.FUNCTION: FunctionDefinition,
    FormatterType.CLASS: ClassDefinition,
    FormatterType.MODULE: ModuleDefinition,
    FormatterType.PACKAGE: PackageDefinition
}

_DEFAULT_FORMATTERS = {
    FormatterType.DOCSTRING: DocstringFormatter,
    FormatterType.FUNCTION: FunctionFormatter,
    FormatterType.CLASS: ClassFormatter,
    FormatterType.MODULE: ModuleFormatter,
    FormatterType.PACKAGE: PackageFormatter
}


class Formatter(BaseFormatter):
    """
    Common formatter for all objects

    Attributes:
        _requires: tuple[FormatterType, ...], data attribute,tuple of
            required formatters
        formatters: (dict[FormatterType, BaseFormatter] | None), formatters
            to be used inside
    """

    def __init__(
        self,
        formatters: (dict[FormatterType, BaseFormatter] | None) = None
    ):
        formatters = formatters or {}
        for formatter_type in FORMATTERS_HIERARCHY:
            if formatter_type not in formatters:
                formatter = _DEFAULT_FORMATTERS[formatter_type](
                    formatters
                )

                formatters[formatter_type] = formatter

        super().__init__(formatters)

    def format(self, obj: AstWrapper, **kwargs):
        """
        Formats object tom Markdown

        Args:
            obj: AstWrapper, object needed to format
            **kwargs: additional arguments for object formatter

        Returns:
            MarkdownContainer: Markdown element for object

        Raises:
            ValueError: if object formatter is not set
        """
        for formatter_type, obj_type in _FORMATTERS_TARGET_MAP.items():
            if isinstance(obj, obj_type):
                return self.format_by(
                    formatter_type,
                    obj,
                    **kwargs
                )

        raise ValueError(
            f'Formatter for type {type(obj)} is not set'
        )
