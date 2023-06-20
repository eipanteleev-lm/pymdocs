# Package pymdocs

## Contents

- [pymdocs.markdown_constructor](#pymdocs-markdown_constructor)
- [pymdocs.cli](#pymdocs-cli)
- [pymdocs.markdown_formatter](#pymdocs-markdown_formatter)
- [pymdocs.parsers.ast](#pymdocs-parsers-ast)
- [pymdocs.parsers.docstring.google](#pymdocs-parsers-docstring-google)

# <a class="anchor" id="pymdocs-markdown_constructor"></a>*module* pymdocs.markdown\_constructor

## Classes

### *class* `pymdocs.markdown_constructor.MarkdownContainer` [[source]](../pymdocs/markdown_constructor.py#L7)



Base class for list of Markdown elements, also usefull for groupping
other elements

**Attributes:**

- *elemens*: list[MarkdownContainer | str], list of inner elements,
could be another MarkdownContainer or python string
- *sep*: (MarkdownContainer | str), elements separator, could be another
MarkdownContainer or python string

**Examples:**

<pre>Rendering multiple lines splitted by paragraph break

>> element = MarkdownContainer(
>>     ['first paragraph', LINE, 'second paragraph'],
>>     PARAGRAPH_BREAK
>> )
>> element.render()
first paragraph

---

second paragraph</pre>



#### Methods

> **pymdocs.markdown\_constructor.MarkdownContainer.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L60)

Returns Markdown representation all inner elements,
joined by separator





### *class* `pymdocs.markdown_constructor.Quote` [[source]](../pymdocs/markdown_constructor.py#L90)

Base: `MarkdownContainer`

Class for quoting Markdown symbols

**Attributes:**

- *text*: str, element text

**Examples:**

<pre>Rendering string with quoted markdown symbols

>> element = Quote('text_with_dashes')
>> element.render()
text\_with\_dashes</pre>



#### Methods

> **pymdocs.markdown\_constructor.Quote.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L108)

Returns markdown quoted text





### *class* `pymdocs.markdown_constructor.Link` [[source]](../pymdocs/markdown_constructor.py#L118)

Base: `MarkdownContainer`

Class for Markdown link element

**Attributes:**

- *text*: str, link text
- *link*: str, link address
- *quote*: bool, need to quote link address, False by default

**Examples:**

<pre>Rendering link

>> element = Link('Go here', 'README.md')
>> element.render()
[Go here](README.md)</pre>



#### Methods

> **pymdocs.markdown\_constructor.Link.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L145)

Returns Markdown link





### *class* `pymdocs.markdown_constructor.Image` [[source]](../pymdocs/markdown_constructor.py#L155)

Base: `Link`

Class for Markdown image element

**Attributes:**

- *text*: str, image text
- *link*: str, image address
- *quote*: bool, need to quote image address, False by default

**Examples:**

<pre>Rendering image

>> element = Image('Beautiful picture', 'image.png')
>> element.render()
![Beautiful picture](image.png)</pre>



#### Methods

> **pymdocs.markdown\_constructor.Image.render**(*self: Any*) -> *Any* [[source]](../pymdocs/markdown_constructor.py#L172)

Returns Markdown image





### *class* `pymdocs.markdown_constructor.Paragraph` [[source]](../pymdocs/markdown_constructor.py#L177)

Base: `MarkdownContainer`

Class for Markdown paragraph element



#### Methods

> **pymdocs.markdown\_constructor.Paragraph.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L180)

Renders inner elements, with paragraph break in the end





### *class* `pymdocs.markdown_constructor.Header` [[source]](../pymdocs/markdown_constructor.py#L188)

Base: `MarkdownContainer`

Base class for Markdown header element

**Attributes:**

- *elements*: list[MarkdownContainer | str], list of inner elements
- *sep*: (MarkdownContainer | str), elements separator
- *level*: int, optional, level of the header, 1 by default

**Examples:**

<pre>Rendering first level header

>> element = Header(
>>     ['module', WHITESPACE, Quote(['markdown_constructor'])]
>> )
>> element.render()
# module markdown\_constructor</pre>



#### Methods

> **pymdocs.markdown\_constructor.Header.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L216)

Returns Markdown header with inner elelements





### *class* `pymdocs.markdown_constructor.H1` [[source]](../pymdocs/markdown_constructor.py#L225)

Base: `Header`

Class for 1 level Markdown header



#### Methods



### *class* `pymdocs.markdown_constructor.H2` [[source]](../pymdocs/markdown_constructor.py#L236)

Base: `Header`

Class for 2 level Markdown header



#### Methods



### *class* `pymdocs.markdown_constructor.H3` [[source]](../pymdocs/markdown_constructor.py#L247)

Base: `Header`

Class for 3 level Markdown header



#### Methods



### *class* `pymdocs.markdown_constructor.H4` [[source]](../pymdocs/markdown_constructor.py#L258)

Base: `Header`

Class for 4 level Markdown header



#### Methods



### *class* `pymdocs.markdown_constructor.H5` [[source]](../pymdocs/markdown_constructor.py#L269)

Base: `Header`

Class for 5 level Markdown header



#### Methods



### *class* `pymdocs.markdown_constructor.H6` [[source]](../pymdocs/markdown_constructor.py#L280)

Base: `Header`

Class for 6 level Markdown header



#### Methods



### *class* `pymdocs.markdown_constructor.Bold` [[source]](../pymdocs/markdown_constructor.py#L291)

Base: `MarkdownContainer`

Class for Markdown bold element

**Examples:**

<pre>Rendering bold text

>> element = Bold(['some bold text'])
>> element.render()
**some bold text**</pre>



#### Methods

> **pymdocs.markdown\_constructor.Bold.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L303)

Returns bolded inner elements





### *class* `pymdocs.markdown_constructor.Italic` [[source]](../pymdocs/markdown_constructor.py#L308)

Base: `MarkdownContainer`

Class for Markdown italic element

**Examples:**

<pre>Rendering italic text

>> element = Italic(['some italic text'])
>> element.render()
*some italic text*</pre>



#### Methods

> **pymdocs.markdown\_constructor.Italic.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L320)

Returns italic inner elements





### *class* `pymdocs.markdown_constructor.BoldItalic` [[source]](../pymdocs/markdown_constructor.py#L325)

Base: `MarkdownContainer`

Class for Markdown bold italic element

**Examples:**

<pre>Rendering bold and italic text

>> element = BoldItalic(['some text'])
>> element.render()
**some text**</pre>



#### Methods

> **pymdocs.markdown\_constructor.BoldItalic.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L337)

Returns bolded italic inner elements





### *class* `pymdocs.markdown_constructor.Strikethrough` [[source]](../pymdocs/markdown_constructor.py#L342)

Base: `MarkdownContainer`

Class for Markdown strikethrough element

**Examples:**

<pre>Rendering strikethrough text

>> element = Strikethrough(['some text'])
>> element.render()
~~some text~~</pre>



#### Methods

> **pymdocs.markdown\_constructor.Strikethrough.render**(*self: Any*) -> *Any* [[source]](../pymdocs/markdown_constructor.py#L354)





### *class* `pymdocs.markdown_constructor.Blockquotes` [[source]](../pymdocs/markdown_constructor.py#L358)

Base: `MarkdownContainer`

Class for Markdown blockquotes element

**Examples:**

<pre>Rendering block quotes

>> element = Blockquotes(['some text'])
>> element.render()
> some text</pre>



#### Methods

> **pymdocs.markdown\_constructor.Blockquotes.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L370)

Returns blockquotes with inner elements





### *class* `pymdocs.markdown_constructor.OrderedList` [[source]](../pymdocs/markdown_constructor.py#L378)

Base: `MarkdownContainer`

Class for Markdown ordered list element

**Attributes:**

- *elements*: list[MarkdownContainer | str], list of inner elements

**Examples:**

<pre>Rendering ordered list

>> element = OrderedList(['first item', 'second item', 'third item'])
>> element.render()
1. first item
2. second item
3. third item</pre>



#### Methods

> **pymdocs.markdown\_constructor.OrderedList.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L398)

Returns Markdown ordered list with inner elements as items





### *class* `pymdocs.markdown_constructor.UnorderedList` [[source]](../pymdocs/markdown_constructor.py#L411)

Base: `MarkdownContainer`

Class for Markdown unordered list element

**Attributes:**

- *elements*: list[MarkdownContainer | str], list of inner elements

**Examples:**

<pre>Rendering unordered list

>> element = UnorderedList(['first item', 'second item', 'third item'])
>> element.render()
- first item
- second item
- third item</pre>



#### Methods

> **pymdocs.markdown\_constructor.UnorderedList.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L428)

Returns Markdown unordered list with inner elements as items





### *class* `pymdocs.markdown_constructor.TaskItem` [[source]](../pymdocs/markdown_constructor.py#L441)

Base: `MarkdownContainer`

Class for Markdown task list item element

**Attributes:**

- *elements*: list[MarkdownContainer | str], list of inner elements
- *sep*: (MarkdownContainer | str), elements separator
- *is\_done*: bool, is the task done or not, False by default



#### Methods

> **pymdocs.markdown\_constructor.TaskItem.render**(*self: Any*) -> *Any* [[source]](../pymdocs/markdown_constructor.py#L460)

Returns Markdown task list item with inner elements





### *class* `pymdocs.markdown_constructor.TaskList` [[source]](../pymdocs/markdown_constructor.py#L468)

Base: `UnorderedList`

Class for Markdown task list element

**Attributes:**

- *elements*: list[TaskItem], list of tasks

**Examples:**

<pre>Render task list

>> element = TaskList([
>>     TaskItem(['First task'], is_done=True),
>>     TaskItem(['Second task']),
>>     TaskItem(['Third task'])
>> ])
>> element.render()
- [x] First task
- [ ] Second task
- [ ] Third task</pre>



#### Methods



### *class* `pymdocs.markdown_constructor.InlineCode` [[source]](../pymdocs/markdown_constructor.py#L493)

Base: `MarkdownContainer`

Class for Markdown inline code element

**Examples:**

<pre>Rendering inline code

>> element = InlineCode(['code'])
>> element.render()
`code`</pre>



#### Methods

> **pymdocs.markdown\_constructor.InlineCode.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L505)

Returns Mrkdown inline code with inner elements





### *class* `pymdocs.markdown_constructor.Code` [[source]](../pymdocs/markdown_constructor.py#L510)

Base: `MarkdownContainer`

Class for Markdown multiline code block

**Attributes:**

- *elements*: list[MarkdownContainer | str], list of inner elements
- *sep*: (MarkdownContainer | str), elements separator
- *language*: str, language to highlight in code block

**Examples:**

<pre>Rendering multiline code block

>> element = Code(
>>     [
>>         'import pandas as pd\n'
>>         'import numpy as np'
>>     ],
>>     language='py'
>> )
>> element.render()
```py
import pandas as pd
import numpy as np
```</pre>



#### Methods

> **pymdocs.markdown\_constructor.Code.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L545)

Returns markdown code block with inner elements





### *class* `pymdocs.markdown_constructor.ColumnOrientation` [[source]](../pymdocs/markdown_constructor.py#L554)

Base: `str, Enum`

Markdown table column orientation





### *class* `pymdocs.markdown_constructor.TableRow` [[source]](../pymdocs/markdown_constructor.py#L564)

Base: `MarkdownContainer`

Class for Markdown table row element

**Attributes:**

- *elements*: list[MarkdownContainer | str], table row elements

**Examples:**

<pre>Rendering table row

>> element = TableRow(['1', 'one'])
>> element.render()
1 | one</pre>



#### Methods



### *class* `pymdocs.markdown_constructor.Table` [[source]](../pymdocs/markdown_constructor.py#L583)

Base: `MarkdownContainer`

Class for Markdown table element

**Attributes:**

- *header*: TableRow, table columns names
- *rows*: list[TableRow], list of table rows
- *orientation*: list[ColumnOrientation] or None, columns orientations,
will be left for every column by default

**Examples:**

<pre>Rendering table

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
2 | two</pre>



#### Methods

> **pymdocs.markdown\_constructor.Table.render**(*self: Any*) -> *Any* [[source]](../pymdocs/markdown_constructor.py#L624)

Returns Markdown table





### *class* `pymdocs.markdown_constructor.HTMLComment` [[source]](../pymdocs/markdown_constructor.py#L642)

Base: `MarkdownContainer`

Class for HTML comment

**Examples:**

<pre>Rendering an HTML comment (not visible in Markdown)

>> element = HTMLComment(['very usefull information'])
>> element.render()
<!--very usefull information--></pre>



#### Methods

> **pymdocs.markdown\_constructor.HTMLComment.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L654)

Returns markdown HTML comment with inner elements





### *class* `pymdocs.markdown_constructor.Raw` [[source]](../pymdocs/markdown_constructor.py#L663)

Base: `MarkdownContainer`

Class for raw text



#### Methods

> **pymdocs.markdown\_constructor.Raw.render**(*self: Any*) -> *str* [[source]](../pymdocs/markdown_constructor.py#L668)

Returns raw text





### *class* `pymdocs.markdown_constructor.HTMLAnchor` [[source]](../pymdocs/markdown_constructor.py#L677)

Base: `MarkdownContainer`

Class for html anchor



#### Methods

> **pymdocs.markdown\_constructor.HTMLAnchor.render**(*self: Any*) -> *Any* [[source]](../pymdocs/markdown_constructor.py#L685)





### *class* `pymdocs.markdown_constructor.Latex` [[source]](../pymdocs/markdown_constructor.py#L691)

Base: `MarkdownContainer`

Class for Latex formulas



#### Methods

> **pymdocs.markdown\_constructor.Latex.render**(*self: Any*) -> *Any* [[source]](../pymdocs/markdown_constructor.py#L696)





# <a class="anchor" id="pymdocs-cli"></a>*module* pymdocs.cli

## Classes

### *class* `pymdocs.cli.Pymdocs` [[source]](../pymdocs/cli.py#L9)





#### Methods

> **pymdocs.cli.Pymdocs.doc**(*self: Any*) -> *Any* [[source]](../pymdocs/cli.py#L45)





# <a class="anchor" id="pymdocs-markdown_formatter"></a>*module* pymdocs.markdown\_formatter

## Classes

### *class* `pymdocs.markdown_formatter.Formatter` [[source]](../pymdocs/markdown_formatter.py#L14)



Class, representing how to render code into markdown

**Attributes:**

- *source\_path*: str, path to Python source code
- *doc\_path*: str, path to doc file
- *package\_name*: str, package name



#### Methods

> **pymdocs.markdown\_formatter.Formatter.module\_line\_path\_link**(*self: Any*, *element: DocElement*, *text: str*) -> *md.Link* [[source]](../pymdocs/markdown_formatter.py#L39)

Returns reference Markdown link to object

**Args:**

- *element*: DocElement, element needed to reference
- *text*: str, reference link text

**Returns:**

`Link`: reference link to object



> **pymdocs.markdown\_formatter.Formatter.docstring\_md**(*self: Any*, *docstring: (Docstring | None)*) -> *md.MarkdownContainer* [[source]](../pymdocs/markdown_formatter.py#L68)



> **pymdocs.markdown\_formatter.Formatter.function\_md**(*self: Any*, *function\_def: FunctionDefinition*, *prefix: str*) -> *md.MarkdownContainer* [[source]](../pymdocs/markdown_formatter.py#L186)

Returns Markdown element for function definition

**Args:**

- *function\_def*: FunctionDefinition, python function definition
- *prefix*: str, function name prefix
(module name or class name for methods)

**Returns:**

`MarkdownContainer`: Markdown element for function



> **pymdocs.markdown\_formatter.Formatter.class\_md**(*self: Any*, *class\_def: ClassDefinition*) -> *md.MarkdownContainer* [[source]](../pymdocs/markdown_formatter.py#L239)

Returns Markdown element for function definition

**Args:**

- *class\_def*: ClassDefinition, python class definition



> **pymdocs.markdown\_formatter.Formatter.module\_link**(*self: Any*) -> *Any* [[source]](../pymdocs/markdown_formatter.py#L297)



> **pymdocs.markdown\_formatter.Formatter.module\_anchor**(*self: Any*) -> *Any* [[source]](../pymdocs/markdown_formatter.py#L303)



> **pymdocs.markdown\_formatter.Formatter.module\_md**(*self: Any*, *module\_def: ModuleDefinition*) -> *md.MarkdownContainer* [[source]](../pymdocs/markdown_formatter.py#L308)

Parses module by path and returns Markdown element for
module definition





## Functions

> **pymdocs.markdown\_formatter.format\_package\_md**(*package\_name: str*, *modules: list[md.MarkdownContainer]*, *module\_links: list[md.Link]*) -> *Any* [[source]](../pymdocs/markdown_formatter.py#L351)



# <a class="anchor" id="pymdocs-parsers-ast"></a>*module* pymdocs.parsers.ast

## Classes

### *class* `pymdocs.parsers.ast.DocElement` [[source]](../pymdocs/parsers/ast.py#L11)



Base class for Python AST element wrapper



#### Methods

> **pymdocs.parsers.ast.DocElement.lineno**(*self: Any*) -> *(int | None)* [[source]](../pymdocs/parsers/ast.py#L22)

Returns line number of the element in file



> **pymdocs.parsers.ast.DocElement.properties**(*self: Any*) -> *dict* [[source]](../pymdocs/parsers/ast.py#L34)

Returns dict of object properties values



> **pymdocs.parsers.ast.DocElement.dict**(*self: Any*) -> *dict* [[source]](../pymdocs/parsers/ast.py#L44)

Returns element dict representation (and all subelements recursively)





### *class* `pymdocs.parsers.ast.Typing` [[source]](../pymdocs/parsers/ast.py#L66)

Base: `DocElement`

Class for Python typing annotations representation



#### Methods

> **pymdocs.parsers.ast.Typing.annotation**(*self: Any*) -> *str* [[source]](../pymdocs/parsers/ast.py#L74)

Returns string representation of typing annotation





### *class* `pymdocs.parsers.ast.Argument` [[source]](../pymdocs/parsers/ast.py#L110)

Base: `DocElement`

Class for function argument representation



#### Methods

> **pymdocs.parsers.ast.Argument.name**(*self: Any*) -> *str* [[source]](../pymdocs/parsers/ast.py#L122)

Returns name of function argument



> **pymdocs.parsers.ast.Argument.type**(*self: Any*) -> *Typing* [[source]](../pymdocs/parsers/ast.py#L127)

Returns typing annotation of function argument





### *class* `pymdocs.parsers.ast.FunctionDefinition` [[source]](../pymdocs/parsers/ast.py#L136)

Base: `DocElement`

Class for function representation



#### Methods

> **pymdocs.parsers.ast.FunctionDefinition.name**(*self: Any*) -> *str* [[source]](../pymdocs/parsers/ast.py#L153)

Returns function name



> **pymdocs.parsers.ast.FunctionDefinition.arguments**(*self: Any*) -> *list[Argument]* [[source]](../pymdocs/parsers/ast.py#L158)

Returns list of function arguments



> **pymdocs.parsers.ast.FunctionDefinition.returns**(*self: Any*) -> *Typing* [[source]](../pymdocs/parsers/ast.py#L166)

Returns function return typing annotation



> **pymdocs.parsers.ast.FunctionDefinition.docstring**(*self: Any*) -> *(doc.Docstring | None)* [[source]](../pymdocs/parsers/ast.py#L171)

Returns function docstring if exists





### *class* `pymdocs.parsers.ast.ClassDefinition` [[source]](../pymdocs/parsers/ast.py#L181)

Base: `DocElement`

Class for Python class representation



#### Methods

> **pymdocs.parsers.ast.ClassDefinition.name**(*self: Any*) -> *str* [[source]](../pymdocs/parsers/ast.py#L198)

Returns class name



> **pymdocs.parsers.ast.ClassDefinition.inherits**(*self: Any*) -> *list[str]* [[source]](../pymdocs/parsers/ast.py#L203)

Returns class bases



> **pymdocs.parsers.ast.ClassDefinition.docstring**(*self: Any*) -> *(doc.Docstring | None)* [[source]](../pymdocs/parsers/ast.py#L212)

Retuns class docstring if exists



> **pymdocs.parsers.ast.ClassDefinition.methods**(*self: Any*) -> *list[FunctionDefinition]* [[source]](../pymdocs/parsers/ast.py#L222)

Returns list of class methods





### *class* `pymdocs.parsers.ast.ModuleDefinition` [[source]](../pymdocs/parsers/ast.py#L231)

Base: `DocElement`



#### Methods

> **pymdocs.parsers.ast.ModuleDefinition.name**(*self: Any*) -> *Any* [[source]](../pymdocs/parsers/ast.py#L245)

Returns module name



> **pymdocs.parsers.ast.ModuleDefinition.docstring**(*self: Any*) -> *(doc.Docstring | None)* [[source]](../pymdocs/parsers/ast.py#L250)

Retuns module docstring if exists



> **pymdocs.parsers.ast.ModuleDefinition.classes**(*self: Any*) -> *list[ClassDefinition]* [[source]](../pymdocs/parsers/ast.py#L260)

Returns list of module classes



> **pymdocs.parsers.ast.ModuleDefinition.functions**(*self: Any*) -> *list[FunctionDefinition]* [[source]](../pymdocs/parsers/ast.py#L269)

Returns list of module functions





## Functions

> **pymdocs.parsers.ast.parse**(*path: str*) -> *ModuleDefinition* [[source]](../pymdocs/parsers/ast.py#L278)

Parses Python module content

**Args:**

- *path*: pathlib.Path, Python module path

**Returns:**

`ModuleDefinition`: module objects definition



# <a class="anchor" id="pymdocs-parsers-docstring-google"></a>*module* pymdocs.parsers.docstring.google

## Classes

### *class* `pymdocs.parsers.docstring.google.DocstringElement` [[source]](../pymdocs/parsers/docstring/google.py#L64)



Base class for docstring elements





### *class* `pymdocs.parsers.docstring.google.DocstringSection` [[source]](../pymdocs/parsers/docstring/google.py#L68)

Base: `DocstringElement`

Base class for docstring section



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringArg` [[source]](../pymdocs/parsers/docstring/google.py#L78)

Base: `DocstringElement`

Class for docstring 'Args' section element

**Attributes:**

- *name*: str, name of argument
- *typing\_annotation*: (str | None), argument type
- *description*: str, argument description



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringArgsSection` [[source]](../pymdocs/parsers/docstring/google.py#L99)

Base: `DocstringSection`

Class for docstring 'Args' section

**Attributes:**

- *attributes*: list[DocstringArg], list of arguments



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringAttribute` [[source]](../pymdocs/parsers/docstring/google.py#L111)

Base: `DocstringElement`

Class for docstring 'Attributes' section element

**Attributes:**

- *name*: str, name of attribute
- *typing\_annotation*: (str | None), attribute type
- *description*: str, attribute description



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringAttributesSection` [[source]](../pymdocs/parsers/docstring/google.py#L132)

Base: `DocstringSection`

Class for docstring 'Attributes' section

**Attributes:**

- *attributes*: list[DocstringAttribute], list of attributes



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringExample` [[source]](../pymdocs/parsers/docstring/google.py#L144)

Base: `DocstringElement`

Class for docstring 'Examples' section element

**Attributes:**

- *description*: str, docstring example



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringExamplesSection` [[source]](../pymdocs/parsers/docstring/google.py#L156)

Base: `DocstringSection`

Class for docstring 'Examples' section

**Attributes:**

- *attributes*: list[DocstringExample], list of docstring examples



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringRaises` [[source]](../pymdocs/parsers/docstring/google.py#L168)

Base: `DocstringElement`

Class for docstring 'Raises' section elements

**Attributes:**

- *exception*: str, exception name
- *description*: str, exception description



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringRaisesSection` [[source]](../pymdocs/parsers/docstring/google.py#L182)

Base: `DocstringSection`

Class for docstring 'Raises' section

**Attributes:**

- *attributes*: list[DocstringRaises], list of rasing exceptions



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringReturns` [[source]](../pymdocs/parsers/docstring/google.py#L194)

Base: `DocstringElement`

Class for docstring 'Returns' section elements

**Attributes:**

- *typing\_annotation*: str, returning value type
- *description*: str, returning value description



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringReturnsSection` [[source]](../pymdocs/parsers/docstring/google.py#L212)

Base: `DocstringSection`

Class for docstring 'Returns' section

**Attributes:**

- *attributes*: list[DocstringReturns], returning value description



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringYiedls` [[source]](../pymdocs/parsers/docstring/google.py#L224)

Base: `DocstringElement`

Class for docstring 'Yields' section elements

**Attributes:**

- *typing\_annotation*: str, yielding value type
- *description*: str, yielding value description



#### Methods



### *class* `pymdocs.parsers.docstring.google.DocstringYiedlsSection` [[source]](../pymdocs/parsers/docstring/google.py#L242)

Base: `DocstringSection`

Class for docstring 'Yields' section

**Attributes:**

- *attributes*: list[DocstringYields], yielding value description



#### Methods



### *class* `pymdocs.parsers.docstring.google.Docstring` [[source]](../pymdocs/parsers/docstring/google.py#L254)

Base: `DocstringSection`

Class for python docstring

**Attributes:**

- *attributes*: list[DocstringSection], list of docstring sections
- *description*: str, docstring title



#### Methods

> **pymdocs.parsers.docstring.google.Docstring.args**(*self: Any*) -> *list[DocstringArg]* [[source]](../pymdocs/parsers/docstring/google.py#L272)

Returns list of docstring 'Args' section elements



> **pymdocs.parsers.docstring.google.Docstring.attributes**(*self: Any*) -> *list[DocstringAttribute]* [[source]](../pymdocs/parsers/docstring/google.py#L281)

Returns list of docstring 'Attributes' section elements



> **pymdocs.parsers.docstring.google.Docstring.examples**(*self: Any*) -> *list[DocstringExample]* [[source]](../pymdocs/parsers/docstring/google.py#L290)

Returns list of docstring 'Examples' section elements



> **pymdocs.parsers.docstring.google.Docstring.raises**(*self: Any*) -> *list[DocstringRaises]* [[source]](../pymdocs/parsers/docstring/google.py#L299)

Returns list of docstring 'Raises' section elements



> **pymdocs.parsers.docstring.google.Docstring.returns**(*self: Any*) -> *list[DocstringReturns]* [[source]](../pymdocs/parsers/docstring/google.py#L308)

Returns list of docstring 'Returns' section elements



> **pymdocs.parsers.docstring.google.Docstring.yields**(*self: Any*) -> *list[DocstringYiedls]* [[source]](../pymdocs/parsers/docstring/google.py#L317)

Returns list of docstring 'Yields' section elements





## Functions

> **pymdocs.parsers.docstring.google.iter\_split**(*pattern: re.Pattern*, *text: str*) -> *Iterator[tuple[(re.Match | None), str, int, int]]* [[source]](../pymdocs/parsers/docstring/google.py#L345)

Iterates through pattern matches and yiedls text between them

**Args:**

- *pattern*: re.Pattern, pattern to search
- *text*: str, text to search pattern



> **pymdocs.parsers.docstring.google.parse\_section**(*text: str*, *section\_type: str*) -> *DocstringSection* [[source]](../pymdocs/parsers/docstring/google.py#L394)

Parses section from text by section type

**Args:**

- *text*: str, text to parse
- *section\_type*: str, section type (Args, Attributes, Raises, etc.)

**Returns:**

`DocstringSection`: DocstringSection object



> **pymdocs.parsers.docstring.google.parse**(*docstring: str*) -> *Any* [[source]](../pymdocs/parsers/docstring/google.py#L430)

Parses Google Style docstring

**Args:**

- *docstring*: Google Style docstring

**Returns:**

`Docstring`: Docstring object





