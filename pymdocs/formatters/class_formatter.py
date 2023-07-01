from typing import Optional, Tuple

import pymdocs.formatters.markdown_constructor as md
from pymdocs.formatters.base import BaseFormatter, FormatterType
from pymdocs.formatters.helpers import module_line_path_link
from pymdocs.parsers.ast import ClassDefinition


class ClassFormatter(BaseFormatter):
    """
    Formatter for ClassDefinition objects

    Attributes:
        _requires: tuple[FormatterType, ...], data attribute,tuple of
            required formatters (DOCSTRING, FUNCTION)
        formatters: (Dict[FormatterType, BaseFormatter] | None), formatters
            to be used inside
    """

    _requires: Tuple[FormatterType, ...] = (
        FormatterType.DOCSTRING,
        FormatterType.FUNCTION
    )

    def format(
        self,
        class_def: ClassDefinition,
        doc_path: str,
        package_name: Optional[str] = None,
        module_name: Optional[str] = None
    ):
        """
        Returns Markdown element for function definition

        Args:
            class_def: ClassDefinition, python class definition
            doc_path: str, path to documentation file
            package_name: (str | None), name of the class package
            module_name: (str | None), name of the class module

        Returns:
            MarkdownContainer: Markdown element for class
        """

        class_name = '.'.join(
            element
            for element in (
                package_name,
                module_name,
                class_def.name
            )
            if element is not None
        )

        return md.Paragraph(
            [
                md.H3([
                    md.Italic(['class']),
                    md.WHITESPACE,
                    md.InlineCode([class_name]),
                    md.WHITESPACE,
                    module_line_path_link(
                        class_def,
                        '[source]',
                        doc_path
                    )
                ]),
                md.MarkdownContainer(
                    [
                        'Base: ',
                        md.InlineCode(
                            [
                                base
                                for base in class_def.inherits
                            ],
                            ', '
                        )
                    ] if class_def.inherits else []
                ),
                md.PARAGRAPH_BREAK,
                (
                    self.format_by(
                        FormatterType.DOCSTRING,
                        class_def.docstring
                    )
                    or ''
                ),
                md.PARAGRAPH_BREAK,
                md.MarkdownContainer(
                    [
                        md.H4(['Methods']),
                        md.MarkdownContainer(
                            [
                                self.format_by(
                                    FormatterType.FUNCTION,
                                    method,
                                    doc_path=doc_path,
                                    package_name=package_name,
                                    module_name=module_name,
                                    class_name=class_def.name
                                )
                                for method in class_def.methods
                                if not method.name.startswith('_')
                            ]
                        )
                    ]
                    if class_def.methods else []
                )
            ]
        )
