import pymdocs.formatters.markdown_constructor as md
from pymdocs.formatters.base import BaseFormatter
from pymdocs.parsers.docstring.google import Docstring


class DocstringFormatter(BaseFormatter):
    """
    Formatter for ClassDefinition objects

    Attributes:
        _requires: tuple[FormatterType, ...], data attribute,tuple of
            required formatters
        formatters: (dict[FormatterType, BaseFormatter] | None), formatters
            to be used inside
    """

    def format(
        self,
        docstring: (Docstring | None)
    ) -> (md.MarkdownContainer | None):
        """
        Returns Markdown element for function definition

        Args:
            docstring: Docstring, python docstring definition

        Returns:
            (MarkdownContainer | None): Markdown element for docstring or None
        """
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
