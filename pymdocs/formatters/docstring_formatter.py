import pymdocs.formatters.markdown_constructor as md
from pymdocs.formatters.base import BaseFormatter
from pymdocs.parsers.docstring.base import Docstring


class DocstringFormatter(BaseFormatter[Docstring]):
    """
    Formatter for ClassDefinition objects

    Attributes:
        _requires: tuple[FormatterType, ...], data attribute,tuple of
            required formatters
        formatters: (Dict[FormatterType, BaseFormatter] | None), formatters
            to be used inside
    """

    def format(
        self,
        obj: Docstring
    ) -> md.MarkdownContainer:
        """
        Returns Markdown element for function definition

        Args:
            docstring: Docstring, python docstring definition

        Returns:
            MarkdownContainer: Markdown element for docstring or None
        """

        return md.MarkdownContainer(
            (
                [
                    md.Paragraph([obj.description]),
                ]
                if obj.description is not None else []
            ) + ([
                md.Paragraph([
                    md.Bold(['Args:']),
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
                            md.StringLiteral(
                                arg.description
                                if arg.description is not None
                                else ''
                            )
                        ])
                        for arg in obj.args
                    ])
                ])]
                if obj.args else []
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
                            md.MarkdownContainer(
                                [
                                    ':',
                                    md.WHITESPACE,
                                    attribute.description
                                ]
                                if attribute.description is not None
                                else []
                            )
                        ])
                        for attribute in obj.attributes
                    ])
                ])]
                if obj.attributes else []
            ) + ([
                md.Paragraph([
                    md.Bold('Raises:'),
                    md.PARAGRAPH_BREAK,
                    md.UnorderedList([
                        md.MarkdownContainer([
                            md.InlineCode([raises.exception]),
                            md.MarkdownContainer(
                                [
                                    ':',
                                    md.WHITESPACE,
                                    raises.description
                                ]
                                if raises.description is not None
                                else []
                            )
                        ])
                        for raises in obj.raises
                    ])
                ])]
                if obj.raises else []
            ) + ([
                md.Paragraph([
                    md.Bold('Returns:'),
                    md.PARAGRAPH_BREAK,
                    md.MarkdownContainer([
                        md.MarkdownContainer([
                            md.InlineCode([returns.typing_annotation]),
                            md.MarkdownContainer(
                                [
                                    ':',
                                    md.WHITESPACE,
                                    returns.description
                                ]
                                if returns.description is not None
                                else []
                            )
                        ])
                        for returns in obj.returns
                    ])
                ])]
                if obj.returns else []
            ) + ([
                md.Paragraph([
                    md.Bold('Yields:'),
                    md.PARAGRAPH_BREAK,
                    md.MarkdownContainer([
                        md.MarkdownContainer([
                            md.InlineCode([yields.typing_annotation]),
                            md.MarkdownContainer(
                                [
                                    ':',
                                    md.WHITESPACE,
                                    yields.description
                                ]
                                if yields.description is not None
                                else []
                            )
                        ])
                        for yields in obj.yields
                    ])
                ])]
                if obj.yields else []
            ) + ([
                md.Paragraph([
                    md.Bold('Examples:'),
                    md.PARAGRAPH_BREAK,
                    md.MarkdownContainer([
                        md.Raw(example.description)
                        for example in obj.examples
                    ])
                ])]
                if obj.examples else []
            )
        )
