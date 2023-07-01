from typing import Optional, Tuple

import pymdocs.formatters.markdown_constructor as md
from pymdocs.formatters.base import BaseFormatter, FormatterType
from pymdocs.formatters.helpers import module_line_path_link
from pymdocs.parsers.ast import FunctionDefinition


class FunctionFormatter(BaseFormatter):
    """
    Formatter for FunctionDefinition objects

    Attributes:
        _requires: tuple[FormatterType, ...], data attribute,tuple of
            required formatters (DOCSTRING)
        formatters: (Dict[FormatterType, BaseFormatter] | None), formatters
            to be used inside
    """

    _requires: Tuple[FormatterType, ...] = (
        FormatterType.DOCSTRING,
    )

    def format(
        self,
        function_def: FunctionDefinition,
        doc_path: str,
        package_name: Optional[str] = None,
        module_name: Optional[str] = None,
        class_name: Optional[str] = None
    ) -> md.MarkdownContainer:
        """
        Returns Markdown element for function definition

        Args:
            function_def: FunctionDefinition, python function definition
            doc_path: str, path to documentation file
            package_name: (str | None), name of the function package,
                None by default
            module_name: (str | None), name of the function module,
                None by default
            class_name: (str | None), name of function class, if function
                is a class method, None by default

        Returns:
            MarkdownContainer: Markdown element for function
        """

        function_name = '.'.join(
            element
            for element in (
                package_name,
                module_name,
                class_name,
                function_def.name
            )
            if element is not None
        )

        return md.Paragraph(
            [
                md.Blockquotes(
                    [
                        md.Bold([md.Quote(function_name)]),
                        '(',
                        md.MarkdownContainer(
                            [
                                md.Italic([
                                    md.Quote(argument.name),
                                    ': ',
                                    md.Quote(argument.type.annotation)
                                ])
                                for argument in function_def.arguments
                            ],
                            ', '
                        ),
                        ') -> ',
                        md.Italic([function_def.returns.annotation]),
                        md.WHITESPACE,
                        module_line_path_link(
                            function_def,
                            '[source]',
                            doc_path
                        )
                    ]
                ),
                md.PARAGRAPH_BREAK,
                (
                    self.format_by(
                        FormatterType.DOCSTRING,
                        function_def.docstring
                    )
                    or ''
                )
            ]
        )
