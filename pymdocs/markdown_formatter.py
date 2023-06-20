import os
from pathlib import Path

import pymdocs.markdown_constructor as md
from pymdocs.parsers.ast import (
    ClassDefinition,
    DocElement,
    FunctionDefinition,
    ModuleDefinition
)
from pymdocs.parsers.docstring.google import Docstring


class Formatter:
    """
    Class, representing how to render code into markdown

    Attributes:
        source_path: str, path to Python source code
        doc_path: str, path to doc file
        package_name: str, package name
    """

    def __init__(
        self,
        source_path: str,
        doc_path: str,
        package_name: str = ''
    ):
        self.source_path = source_path
        self.doc_path = doc_path
        self.package_name = package_name
        self.short_module_name = (
            os.path.basename(self.source_path)
            .split('.')[0]
        )
        self.module_name = f'{self.package_name}.{self.short_module_name}'

    def module_line_path_link(
        self,
        element: DocElement,
        text: str
    ) -> md.Link:
        """
        Returns reference Markdown link to object

        Args:
            element: DocElement, element needed to reference
            text: str, reference link text

        Returns:
            Link: reference link to object
        """
        relpath = Path(
            os.path.relpath(
                self.source_path,
                os.path.dirname(self.doc_path)
            )
        ).as_posix()

        pos = element.lineno

        if pos is not None:
            relpath += f'#L{pos}'

        return md.Link(text, relpath)

    def docstring_md(
        self,
        docstring: (Docstring | None)
    ) -> md.MarkdownContainer:
        if docstring is None:
            return None

        return md.MarkdownContainer(
            [
                md.Paragraph([docstring.description]),
            ] + ([
                md.Paragraph([
                    md.Bold('Args:'),
                    md.PARAGRAPH_BREAK,
                    md.UnorderedList([
                        md.MarkdownContainer([
                            md.Italic([md.Quote(arg.name)]),
                            md.MarkdownContainer(
                                [
                                    md.WHITESPACE,
                                    md.InlineCode([
                                        arg.typing_annotation
                                    ])
                                ]
                                if arg.typing_annotation is not None
                                else []
                            ),
                            ':',
                            md.WHITESPACE,
                            arg.description
                        ])
                        for arg in docstring.args
                    ])
                ])]
                if docstring.args else []
            ) + ([
                md.Paragraph([
                    md.Bold('Attributes:'),
                    md.PARAGRAPH_BREAK,
                    md.UnorderedList([
                        md.MarkdownContainer([
                            md.Italic([md.Quote(attribute.name)]),
                            md.MarkdownContainer(
                                [
                                    md.WHITESPACE,
                                    md.InlineCode([
                                        attribute.typing_annotation
                                    ])
                                ]
                                if attribute.typing_annotation is not None
                                else []
                            ),
                            ':',
                            md.WHITESPACE,
                            attribute.description
                        ])
                        for attribute in docstring.attributes
                    ])
                ])]
                if docstring.attributes else []
            ) + ([
                md.Paragraph([
                    md.Bold('Raises:'),
                    md.PARAGRAPH_BREAK,
                    md.UnorderedList([
                        md.MarkdownContainer([
                            md.InlineCode([raises.exception]),
                            ':',
                            md.WHITESPACE,
                            raises.description
                        ])
                        for raises in docstring.raises
                    ])
                ])]
                if docstring.raises else []
            ) + ([
                md.Paragraph([
                    md.Bold('Returns:'),
                    md.PARAGRAPH_BREAK,
                    md.MarkdownContainer([
                        md.MarkdownContainer([
                            md.InlineCode([returns.typing_annotation]),
                            ':',
                            md.WHITESPACE,
                            returns.description
                        ])
                        for returns in docstring.returns
                    ])
                ])]
                if docstring.returns else []
            ) + ([
                md.Paragraph([
                    md.Bold('Yields:'),
                    md.PARAGRAPH_BREAK,
                    md.MarkdownContainer([
                        md.MarkdownContainer([
                            md.InlineCode([yields.typing_annotation]),
                            ':',
                            md.WHITESPACE,
                            yields.description
                        ])
                        for yields in docstring.yields
                    ])
                ])]
                if docstring.yields else []
            ) + ([
                md.Paragraph([
                    md.Bold('Examples:'),
                    md.PARAGRAPH_BREAK,
                    md.MarkdownContainer([
                        md.Raw([example.description])
                        for example in docstring.examples
                    ])
                ])]
                if docstring.examples else []
            )
        )

    def function_md(
        self,
        function_def: FunctionDefinition,
        prefix: str = ''
    ) -> md.MarkdownContainer:
        """
        Returns Markdown element for function definition

        Args:
            function_def: FunctionDefinition, python function definition
            prefix: str, function name prefix
                (module name or class name for methods)

        Returns:
            MarkdownContainer: Markdown element for function
        """
        return md.Paragraph(
            [
                md.Blockquotes(
                    [
                        md.Bold(
                            [
                                md.Quote(prefix),
                                '.',
                                md.Quote(function_def.name)
                            ]
                        ),
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
                        self.module_line_path_link(
                            function_def,
                            '[source]'
                        )
                    ]
                ),
                md.PARAGRAPH_BREAK,
                (self.docstring_md(function_def.docstring) or '')
            ]
        )

    def class_md(self, class_def: ClassDefinition) -> md.MarkdownContainer:
        """
        Returns Markdown element for function definition

        Args:
            class_def: ClassDefinition, python class definition

        Returns: MarkdownElement, Markdown element for class
        """
        return md.Paragraph(
            [
                md.H3([
                    md.Italic(['class']),
                    md.WHITESPACE,
                    md.InlineCode(
                        [
                            self.module_name,
                            class_def.name
                        ],
                        '.'
                    ),
                    md.WHITESPACE,
                    self.module_line_path_link(class_def, '[source]')
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
                (self.docstring_md(class_def.docstring) or ''),
                md.PARAGRAPH_BREAK,
                md.MarkdownContainer(
                    [
                        md.H4(['Methods']),
                        md.MarkdownContainer(
                            [
                                self.function_md(
                                    method,
                                    f'{self.module_name}.{class_def.name}'
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

    def module_link(self):
        return md.Link(
            self.module_name,
            f'#{self.module_name.replace(".", "-")}'
        )

    def module_anchor(self):
        return md.HTMLAnchor(
            self.module_name.replace('.', '-')
        )

    def module_md(self, module_def: ModuleDefinition) -> md.MarkdownContainer:
        """
        Parses module by path and returns Markdown element for
        module definition

        Returns: MarkdownElement, Markdown element for module
        """

        md_list = [
            md.H1([
                self.module_anchor(),
                md.Italic(['module']),
                md.WHITESPACE,
                md.Quote(self.module_name)
            ])
        ]

        if module_def.classes:
            md_list += [
                md.H2(['Classes']),
                md.MarkdownContainer(
                    [
                        self.class_md(class_def)
                        for class_def in module_def.classes
                    ]
                )
            ]

        if module_def.functions:
            md_list += [
                md.H2(['Functions']),
                md.MarkdownContainer(
                    [
                        self.function_md(function_def, self.module_name)
                        for function_def in module_def.functions
                        if not function_def.name.startswith('_')
                    ]
                )
            ]

        return md.MarkdownContainer(md_list)


def format_package_md(
    package_name: str,
    modules: list[md.MarkdownContainer],
    module_links: list[md.Link]
):
    return md.MarkdownContainer([
        md.H1(['Package', md.WHITESPACE, md.Quote(package_name)]),
        md.H2(['Contents']),
        md.Paragraph([
            md.UnorderedList([
                link
                for link in module_links
            ])
        ]),
        md.Paragraph([
            module_md
            for module_md in modules
        ])
    ])
