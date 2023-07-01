from typing import Optional, Tuple

import pymdocs.formatters.markdown_constructor as md
from pymdocs.formatters.base import BaseFormatter, FormatterType
from pymdocs.parsers.ast import ModuleDefinition


class ModuleFormatter(BaseFormatter):
    """
    Formatter for ModuleDefinition objects

    Attributes:
        _requires: tuple[FormatterType, ...], data attribute,tuple of
            required formatters (DOCSTRING, FUNCTION, CLASS)
        formatters: (dict[FormatterType, BaseFormatter] | None), formatters
            to be used inside
    """

    _requires: Tuple[FormatterType, ...] = (
        FormatterType.DOCSTRING,
        FormatterType.FUNCTION,
        FormatterType.CLASS
    )

    @staticmethod
    def module_link(module_name: str):
        """
        Returns module link for Contents documentation section

        Args:
            module_name: str, module name

        Returns:
            Link: markdown link element
        """
        return md.Link(
            module_name,
            f'#{module_name.replace(".", "-")}'
        )

    @staticmethod
    def module_anchor(module_name: str):
        """
        Returns module anchor for Contents documentation section

        Args:
            module_name: str, module name

        Returns:
            HTMLAnchor: anchor for module documentation header
        """
        return md.HTMLAnchor(
            module_name.replace('.', '-')
        )

    def format(
        self,
        module_def: ModuleDefinition,
        doc_path: str,
        package_name: Optional[str] = None
    ):
        """
        Returns Markdown element for module definition

        Args:
            module_def: ModuleDefinition, python module definition
            doc_path: str, path to documentation file
            package_name: (str | None), name of the class package

        Returns:
            MarkdownContainer: Markdown element for module
        """

        module_name = '.'.join(
            element
            for element in (
                package_name,
                module_def.name
            )
            if element
        )

        md_list = [
            md.H1([
                self.module_anchor(module_name),
                md.Italic(['module']),
                md.WHITESPACE,
                md.Quote(module_name)
            ])
        ]

        if module_def.classes:
            md_list += [
                md.H2(['Classes']),
                md.MarkdownContainer(
                    [
                        self.format_by(
                            FormatterType.CLASS,
                            class_def,
                            doc_path=doc_path,
                            package_name=package_name,
                            module_name=module_def.name
                        )
                        for class_def in module_def.classes
                    ]
                )
            ]

        if module_def.functions:
            md_list += [
                md.H2(['Functions']),
                md.MarkdownContainer(
                    [
                        self.format_by(
                            FormatterType.FUNCTION,
                            function_def,
                            doc_path=doc_path,
                            package_name=package_name,
                            module_name=module_def.name
                        )
                        for function_def in module_def.functions
                        if not function_def.name.startswith('_')
                    ]
                )
            ]

        return md.MarkdownContainer(md_list)
