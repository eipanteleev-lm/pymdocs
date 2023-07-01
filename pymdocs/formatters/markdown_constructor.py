import urllib.parse
from enum import Enum
from typing import Any, List, Union

MARKDOWN_QUOTE_SYMBOLS = list('_*`')


class MarkdownContainer:
    """
    Base class for list of Markdown elements, also usefull for groupping
        other elements

    Attributes:
        elemens: List[Union[MarkdownContainer, str]], list of inner elements,
            could be another MarkdownContainer or python string
        sep: Union[MarkdownContainer, str], elements separator, could be
            another MarkdownContainer or python string

    Examples:
        Rendering multiple lines splitted by paragraph break

        >> element = MarkdownContainer(
        >>     ['first paragraph', LINE, 'second paragraph'],
        >>     PARAGRAPH_BREAK
        >> )
        >> element.render()
        first paragraph

        ---

        second paragraph
    """

    @staticmethod
    def _validate(element: Any) -> Any:
        if isinstance(element, (MarkdownContainer, str)):
            return element

        raise ValueError(
            f'Obj of {type(element)} is not MarkdownContainer or string'
        )

    def _validate_elements(self, elements: List[Any]) -> List[Any]:
        for element in elements:
            self._validate(element)

        return elements

    def _validate_sep(self, sep: 'Union[MarkdownContainer, str]'):
        self._validate(sep)
        return sep

    def __init__(
        self,
        elements: 'List[Union[MarkdownContainer, str]]',
        sep: 'Union[MarkdownContainer, str]' = ''
    ):
        self.elements = self._validate_elements(elements)
        self.sep = self._validate_sep(sep)

    def render(self) -> str:
        """
        Returns Markdown representation all inner elements,
        joined by separator
        """
        sep = (
            self.sep.render()
            if isinstance(self.sep, MarkdownContainer)
            else self.sep
        )

        return sep.join(
            (
                element.render()
                if isinstance(element, MarkdownContainer)
                else element
            )
            for element in self.elements
        )


WHITESPACE = MarkdownContainer([' '])
NEWLINE = MarkdownContainer(['\n'])
PARAGRAPH_BREAK = MarkdownContainer(['\n\n'])
LINE = MarkdownContainer(['\n\n---\n\n'])

# Line break for table cells
HTML_LINEBREAK = MarkdownContainer(['</br>'])


class Quote(MarkdownContainer):
    """
    Class for quoting Markdown symbols

    Attributes:
        text: str, element text

    Examples:
        Rendering string with quoted markdown symbols

        >> element = Quote('text_with_dashes')
        >> element.render()
        text\\_with\\_dashes
    """

    def __init__(self, text: str):
        self.text = text

    def render(self) -> str:
        """Returns markdown quoted text"""
        quoted_text = self.text

        for symbol in MARKDOWN_QUOTE_SYMBOLS:
            quoted_text = quoted_text.replace(symbol, '\\' + symbol)

        return quoted_text


class Link(MarkdownContainer):
    """
    Class for Markdown link element

    Attributes:
        text: str, link text
        link: str, link address
        quote: bool, need to quote link address, False by default

    Examples:
        Rendering link

        >> element = Link('Go here', 'README.md')
        >> element.render()
        [Go here](README.md)
    """

    def __init__(
        self,
        text: str,
        link: str,
        quote: bool = False
    ):
        self.text = text
        self.link = link
        self.quote = quote

    def render(self) -> str:
        """Returns Markdown link"""
        link = (
            urllib.parse.quote(self.link)
            if self.quote
            else self.link
        )
        return f'[{self.text}]({link})'


class Image(Link):
    """
    Class for Markdown image element

    Attributes:
        text: str, image text
        link: str, image address
        quote: bool, need to quote image address, False by default

    Examples:
        Rendering image

        >> element = Image('Beautiful picture', 'image.png')
        >> element.render()
        ![Beautiful picture](image.png)
    """

    def render(self):
        """Returns Markdown image"""
        return f'!{super().render()}'


class Paragraph(MarkdownContainer):
    """Class for Markdown paragraph element"""

    def render(self) -> str:
        """Renders inner elements, with paragraph break in the end"""
        return (
            super().render()
            + PARAGRAPH_BREAK.render()
        )


class Header(MarkdownContainer):
    """
    Base class for Markdown header element

    Attributes:
        elements: List[Union[MarkdownContainer, str]], list of inner elements
        sep: Union[MarkdownContainer, str], elements separator
        level: int, optional, level of the header, 1 by default

    Examples:
        Rendering first level header

        >> element = Header(
        >>     ['module', WHITESPACE, Quote(['markdown_constructor'])]
        >> )
        >> element.render()
        # module markdown\\_constructor
    """

    def __init__(
        self,
        elements: List[Union[MarkdownContainer, str]],
        sep: Union[MarkdownContainer, str] = '',
        level: int = 1
    ):
        self.level = level
        super().__init__(elements, sep)

    def render(self) -> str:
        """Returns Markdown header with inner elelements"""
        return (
            '#' * self.level
            + f' {super().render()}'
            + PARAGRAPH_BREAK.render()
        )


class H1(Header):
    """Class for 1 level Markdown header"""

    def __init__(
        self,
        elements: List[Union[MarkdownContainer, str]],
        sep: Union[MarkdownContainer, str] = '',
    ):
        super().__init__(elements, sep, 1)


class H2(Header):
    """Class for 2 level Markdown header"""

    def __init__(
        self,
        elements: List[Union[MarkdownContainer, str]],
        sep: Union[MarkdownContainer, str] = '',
    ):
        super().__init__(elements, sep, 2)


class H3(Header):
    """Class for 3 level Markdown header"""

    def __init__(
        self,
        elements: List[Union[MarkdownContainer, str]],
        sep: Union[MarkdownContainer, str] = '',
    ):
        super().__init__(elements, sep, 3)


class H4(Header):
    """Class for 4 level Markdown header"""

    def __init__(
        self,
        elements: List[Union[MarkdownContainer, str]],
        sep: Union[MarkdownContainer, str] = '',
    ):
        super().__init__(elements, sep, 4)


class H5(Header):
    """Class for 5 level Markdown header"""

    def __init__(
        self,
        elements: List[Union[MarkdownContainer, str]],
        sep: Union[MarkdownContainer, str] = '',
    ):
        super().__init__(elements, sep, 5)


class H6(Header):
    """Class for 6 level Markdown header"""

    def __init__(
        self,
        elements: List[Union[MarkdownContainer, str]],
        sep: Union[MarkdownContainer, str] = '',
    ):
        super().__init__(elements, sep, 6)


class Bold(MarkdownContainer):
    """
    Class for Markdown bold element

    Examples:
        Rendering bold text

        >> element = Bold(['some bold text'])
        >> element.render()
        **some bold text**
    """

    def render(self) -> str:
        """Returns bolded inner elements"""
        return f'**{super().render()}**'


class Italic(MarkdownContainer):
    """
    Class for Markdown italic element

    Examples:
        Rendering italic text

        >> element = Italic(['some italic text'])
        >> element.render()
        *some italic text*
    """

    def render(self) -> str:
        """Returns italic inner elements"""
        return f'*{super().render()}*'


class BoldItalic(MarkdownContainer):
    """
    Class for Markdown bold italic element

    Examples:
        Rendering bold and italic text

        >> element = BoldItalic(['some text'])
        >> element.render()
        **some text**
    """

    def render(self) -> str:
        """Returns bolded italic inner elements"""
        return f'***{super().render()}***'


class Strikethrough(MarkdownContainer):
    """
    Class for Markdown strikethrough element

    Examples:
        Rendering strikethrough text

        >> element = Strikethrough(['some text'])
        >> element.render()
        ~~some text~~
    """

    def render(self):
        return f'~~{super().render()}~~'


class Blockquotes(MarkdownContainer):
    """
    Class for Markdown blockquotes element

    Examples:
        Rendering block quotes

        >> element = Blockquotes(['some text'])
        >> element.render()
        > some text
    """

    def render(self) -> str:
        """Returns blockquotes with inner elements"""
        return '\n'.join(
            ('> ' + line)
            for line in super().render().split('\n')
        )


class OrderedList(MarkdownContainer):
    """
    Class for Markdown ordered list element

    Attributes:
        elements: List[Union[MarkdownContainer, str]], list of inner elements

    Examples:
        Rendering ordered list

        >> element = OrderedList(['first item', 'second item', 'third item'])
        >> element.render()
        1. first item
        2. second item
        3. third item
    """

    def __init__(self, elements: List[Union[MarkdownContainer, str]]):
        self.elements = elements

    def render(self) -> str:
        """Returns Markdown ordered list with inner elements as items"""
        return '\n'.join(
            f'{i}. '
            + (
                element.render()
                if isinstance(element, MarkdownContainer)
                else f'{element}'
            )
            for i, element in enumerate(self.elements, 1)
        )


class UnorderedList(MarkdownContainer):
    """
    Class for Markdown unordered list element

    Attributes:
        elements: List[Union[MarkdownContainer, str]], list of inner elements

    Examples:
        Rendering unordered list

        >> element = UnorderedList(['first item', 'second item', 'third item'])
        >> element.render()
        - first item
        - second item
        - third item
    """

    def render(self) -> str:
        """Returns Markdown unordered list with inner elements as items"""
        return '\n'.join(
            '- '
            + (
                element.render()
                if isinstance(element, MarkdownContainer)
                else f'{element}'
            )
            for i, element in enumerate(self.elements, 1)
        )


class TaskItem(MarkdownContainer):
    """
    Class for Markdown task list item element

    Attributes:
        elements: List[Union[MarkdownContainer, str]], list of inner elements
        sep: Union[MarkdownContainer, str], elements separator
        is_done: bool, is the task done or not, False by default
    """

    def __init__(
        self,
        elements: List[Union[MarkdownContainer, str]],
        sep: Union[MarkdownContainer, str] = '',
        is_done: bool = False
    ):
        self.is_done = is_done
        super().__init__(elements, sep)

    def render(self):
        """Returns Markdown task list item with inner elements"""
        return (
            ('[x] ' if self.is_done else '[ ] ')
            + f'{super().render()}'
        )


class TaskList(UnorderedList):
    """
    Class for Markdown task list element

    Attributes:
        elements: list[TaskItem], list of tasks

    Examples:
        Render task list

        >> element = TaskList([
        >>     TaskItem(['First task'], is_done=True),
        >>     TaskItem(['Second task']),
        >>     TaskItem(['Third task'])
        >> ])
        >> element.render()
        - [x] First task
        - [ ] Second task
        - [ ] Third task
    """

    def __init__(self, elements: list[TaskItem]):
        super().__init__(elements)


class InlineCode(MarkdownContainer):
    """
    Class for Markdown inline code element

    Examples:
        Rendering inline code

        >> element = InlineCode(['code'])
        >> element.render()
        `code`
    """

    def render(self) -> str:
        """Returns Mrkdown inline code with inner elements"""
        return f'`{super().render()}`'


class Code(MarkdownContainer):
    """
    Class for Markdown multiline code block

    Attributes:
        elements: List[Union[MarkdownContainer, str]], list of inner elements
        sep: Union[MarkdownContainer, str], elements separator
        language: str, language to highlight in code block

    Examples:
        Rendering multiline code block

        >> element = Code(
        >>     [
        >>         'import pandas as pd\\n'
        >>         'import numpy as np'
        >>     ],
        >>     language='py'
        >> )
        >> element.render()
        ```py
        import pandas as pd
        import numpy as np
        ```
    """

    def __init__(
        self,
        elements: List[Union[MarkdownContainer, str]],
        sep: Union[MarkdownContainer, str] = '',
        language: str = ''
    ):
        self.language = language
        super().__init__(elements, sep)

    def render(self) -> str:
        """Returns markdown code block with inner elements"""
        return (
            f'```{self.language}\n'
            + f'{super().render()}\n'
            + '```'
        )


class ColumnOrientation(str, Enum):
    """Markdown table column orientation"""
    LEFT = ':--'
    RIGHT = '--:'
    MIDDLE = ':-:'


_TABLE_BORDER = MarkdownContainer([' | '])


class TableRow(MarkdownContainer):
    """
    Class for Markdown table row element

    Attributes:
        elements: List[Union[MarkdownContainer, str]], table row elements

    Examples:
        Rendering table row

        >> element = TableRow(['1', 'one'])
        >> element.render()
        1 | one
    """

    def __init__(self, elements: List[Union[MarkdownContainer, str]]):
        super().__init__(elements, sep=_TABLE_BORDER)


class Table(MarkdownContainer):
    """
    Class for Markdown table element

    Attributes:
        header: TableRow, table columns names
        rows: list[TableRow], list of table rows
        orientation: list[ColumnOrientation] or None, columns orientations,
            will be left for every column by default

    Examples:
        Rendering table

        >> table = Table(
        >>     header=TableRow(['name', 'value']),
        >>     rows=[
        >>         TableRow(['1', 'one']),
        >>         TableRow(['2', 'two'])
        >>     ],
        >>     orientation=[
        >>         ColumnOrientation.LEFT,
        >>         ColumnOrientation.RIGHT
        >>     ]
        >> )
        >> table.render()
        name | value
        :-- | --:
        1 | one
        2 | two
    """

    def __init__(
        self,
        header: TableRow,
        rows: list[TableRow],
        orientation: (list[ColumnOrientation] | None) = None
    ):
        self.header = header
        self.orientation = orientation
        super().__init__(rows, NEWLINE)

    def render(self):
        """Returns Markdown table"""
        orientation = self.orientation
        if orientation is None:
            orientation = [ColumnOrientation.LEFT] * len(self.header.elements)

        orientation_row = TableRow([
            el.value
            for el in orientation
        ])

        return (
            f'{self.header.render()}\n'
            + f'{orientation_row.render()}\n'
            + f'{super().render()}'
        )


class HTMLComment(MarkdownContainer):
    """
    Class for HTML comment

    Examples:
        Rendering an HTML comment (not visible in Markdown)

        >> element = HTMLComment(['very usefull information'])
        >> element.render()
        <!--very usefull information-->
    """

    def render(self) -> str:
        """Returns markdown HTML comment with inner elements"""
        return (
            '<!--'
            + f'{super().render()}'
            + '-->'
        )


class Raw(MarkdownContainer):
    """
    Class for raw text
    """

    def render(self) -> str:
        """Returns raw text"""
        return (
            '<pre>'
            + f'{super().render()}'
            + '</pre>'
        )


class HTMLAnchor(MarkdownContainer):
    """
    Class for html anchor
    """

    def __init__(self, id: str):
        self.id = id

    def render(self):
        return (
            f'<a class="anchor" id="{self.id}"></a>'
        )


class Latex(MarkdownContainer):
    """
    Class for Latex formulas
    """

    def render(self):
        return f'${super().render()}$'
