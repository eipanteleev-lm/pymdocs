from typing import List, Tuple

import pymdocs.formatters.markdown_constructor as md
from pymdocs.formatters.base import BaseFormatter, FormatterType
from pymdocs.formatters.module_formatter import ModuleFormatter
from pymdocs.parsers.ast import PackageDefinition


class PackageFormatter(BaseFormatter[PackageDefinition]):
    """
    Formatter for ModuleDefinition objects

    Attributes:
        _requires: tuple[FormatterType, ...], data attribute,tuple of
            required formatters (DOCSTRING, FUNCTION, CLASS, MODULE)
        formatters: (dict[FormatterType, BaseFormatter] | None), formatters
            to be used inside
    """

    _requires: Tuple[FormatterType, ...] = (
        FormatterType.DOCSTRING,
        FormatterType.FUNCTION,
        FormatterType.CLASS,
        FormatterType.MODULE
    )

    def flatten_modules(
        self,
        package_def: PackageDefinition,
        doc_path: str,
        prefix: str = ''
    ) -> List[Tuple[md.MarkdownContainer, md.Link]]:
        """
        Formats package definition as a list of formatted module definitions
        recursively

        Args:
            package_def: PackageDefinition, python package definition
            doc_path: str, path to documentation file
            prefix: str, prefix to add to package inner objects names

        Returns:
            (list[tuple[md.MarkdownContainer, md.Link]]): list of tuples of
                markdown element for module and module link for Contents
                section
        """
        modules_md = []

        package_name = (
            f'{prefix}.{package_def.name}'
            if prefix
            else package_def.name
        )

        for module_def in package_def.modules:
            if module_def.name.startswith('_'):
                continue

            module_name = f'{package_name}.{module_def.name}'

            module_formatter: ModuleFormatter = (
                self.formatters[FormatterType.MODULE]
            )

            module_md = module_formatter.format(
                module_def,
                doc_path,
                package_name
            )

            module_link = module_formatter.module_link(module_name)
            modules_md.append((module_md, module_link))

        for inner_package_def in package_def.packages:
            modules_md.extend(
                self.flatten_modules(
                    inner_package_def,
                    doc_path,
                    package_name
                )
            )

        return modules_md

    def format(
        self,
        obj: PackageDefinition,
        doc_path: str = ''
    ) -> md.MarkdownElement:
        """
        Returns Markdown element for package definition

        Args:
            package_def: PackageDefinition, python package definition
            doc_path: str, path to documentation file

        Returns:
            MarkdownContainer: Markdown element for package
        """

        modules_md = self.flatten_modules(
            obj,
            doc_path
        )

        return md.MarkdownContainer([
            md.H1(['Package', md.WHITESPACE, md.Quote(obj.name)]),
            md.H2(['Contents']),
            md.Paragraph([
                md.UnorderedList([
                    module_link
                    for _, module_link in modules_md
                ])
            ]),
            md.Paragraph([
                module_md
                for module_md, _ in modules_md
            ])
        ])
