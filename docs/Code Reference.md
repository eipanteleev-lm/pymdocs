# Package pymdocs

## Contents

- [pymdocs.cli](#pymdocs-cli)
- [pymdocs.parsers.ast](#pymdocs-parsers-ast)
- [pymdocs.parsers.docstring.google](#pymdocs-parsers-docstring-google)
- [pymdocs.parsers.docstring.numpy](#pymdocs-parsers-docstring-numpy)
- [pymdocs.parsers.docstring.helpers](#pymdocs-parsers-docstring-helpers)
- [pymdocs.parsers.docstring.base](#pymdocs-parsers-docstring-base)
- [pymdocs.formatters.class_formatter](#pymdocs-formatters-class_formatter)
- [pymdocs.formatters.markdown_constructor](#pymdocs-formatters-markdown_constructor)
- [pymdocs.formatters.package_formatter](#pymdocs-formatters-package_formatter)
- [pymdocs.formatters.function_formatter](#pymdocs-formatters-function_formatter)
- [pymdocs.formatters.docstring_formatter](#pymdocs-formatters-docstring_formatter)
- [pymdocs.formatters.common_formatter](#pymdocs-formatters-common_formatter)
- [pymdocs.formatters.helpers](#pymdocs-formatters-helpers)
- [pymdocs.formatters.base](#pymdocs-formatters-base)
- [pymdocs.formatters.module_formatter](#pymdocs-formatters-module_formatter)

# <a class="anchor" id="pymdocs-cli"></a>*module* pymdocs.cli

## Classes

### *class* `pymdocs.cli.Pymdocs` [[source]](../pymdocs/cli.py#L9)

Class for rendering Markdown documentation

**Attributes:**

- *source\_path*: str, path to Python source code
- *doc\_path*: str, path to documentation file
- *formatter*: Formatter, markdown formatter



#### Methods

> **pymdocs.cli.Pymdocs.doc**(*self*) -> *None* [[source]](../pymdocs/cli.py#L42)

Generates Code Reference for python code





## Functions

> **pymdocs.cli.main**() -> *None* [[source]](../pymdocs/cli.py#L59)

# <a class="anchor" id="pymdocs-parsers-ast"></a>*module* pymdocs.parsers.ast

## Classes

### *class* `pymdocs.parsers.ast.ElementDefinition` [[source]](../pymdocs/parsers/ast.py#L14)

Base class for Python code structures





### *class* `pymdocs.parsers.ast.AstWrapper` [[source]](../pymdocs/parsers/ast.py#L18)

Base: `ElementDefinition`

Base class for Python AST element wrapper

**Attributes:**

- *ast\_element*: ast.AST, AST tree node
- *path*: str, path to file contains element



#### Methods

> **pymdocs.parsers.ast.AstWrapper.lineno**(*self*) -> *int* [[source]](../pymdocs/parsers/ast.py#L36)

Returns line number of the element in file





### *class* `pymdocs.parsers.ast.Typing` [[source]](../pymdocs/parsers/ast.py#L47)

Base: `AstWrapper`

Class for Python typing annotations representation



#### Methods

> **pymdocs.parsers.ast.Typing.annotation**(*self*) -> *str* [[source]](../pymdocs/parsers/ast.py#L51)

Returns string representation of typing annotation





### *class* `pymdocs.parsers.ast.Argument` [[source]](../pymdocs/parsers/ast.py#L85)

Class for function argument representation



#### Methods

> **pymdocs.parsers.ast.Argument.name**(*self*) -> *str* [[source]](../pymdocs/parsers/ast.py#L89)

Returns name of function argument



> **pymdocs.parsers.ast.Argument.type**(*self*) -> *Optional[Typing]* [[source]](../pymdocs/parsers/ast.py#L94)

Returns typing annotation of function argument





### *class* `pymdocs.parsers.ast.FunctionDefinition` [[source]](../pymdocs/parsers/ast.py#L109)

Class for function representation



#### Methods

> **pymdocs.parsers.ast.FunctionDefinition.name**(*self*) -> *str* [[source]](../pymdocs/parsers/ast.py#L113)

Returns function name



> **pymdocs.parsers.ast.FunctionDefinition.arguments**(*self*) -> *List[Argument]* [[source]](../pymdocs/parsers/ast.py#L118)

Returns list of function arguments



> **pymdocs.parsers.ast.FunctionDefinition.returns**(*self*) -> *Optional[Typing]* [[source]](../pymdocs/parsers/ast.py#L126)

Returns function return typing annotation



> **pymdocs.parsers.ast.FunctionDefinition.docstring**(*self*) -> *Optional[doc.Docstring]* [[source]](../pymdocs/parsers/ast.py#L137)

Returns function docstring if exists





### *class* `pymdocs.parsers.ast.ClassDefinition` [[source]](../pymdocs/parsers/ast.py#L149)

Class for Python class representation



#### Methods

> **pymdocs.parsers.ast.ClassDefinition.name**(*self*) -> *str* [[source]](../pymdocs/parsers/ast.py#L153)

Returns class name



> **pymdocs.parsers.ast.ClassDefinition.inherits**(*self*) -> *List[str]* [[source]](../pymdocs/parsers/ast.py#L158)

Returns class bases



> **pymdocs.parsers.ast.ClassDefinition.docstring**(*self*) -> *Optional[doc.Docstring]* [[source]](../pymdocs/parsers/ast.py#L167)

Retuns class docstring if exists



> **pymdocs.parsers.ast.ClassDefinition.methods**(*self*) -> *List[FunctionDefinition]* [[source]](../pymdocs/parsers/ast.py#L179)

Returns list of class methods





### *class* `pymdocs.parsers.ast.ModuleDefinition` [[source]](../pymdocs/parsers/ast.py#L188)

Class for Python module representation



#### Methods

> **pymdocs.parsers.ast.ModuleDefinition.name**(*self*) -> *str* [[source]](../pymdocs/parsers/ast.py#L192)

Returns module name



> **pymdocs.parsers.ast.ModuleDefinition.docstring**(*self*) -> *Optional[doc.Docstring]* [[source]](../pymdocs/parsers/ast.py#L197)

Retuns module docstring if exists



> **pymdocs.parsers.ast.ModuleDefinition.classes**(*self*) -> *List[ClassDefinition]* [[source]](../pymdocs/parsers/ast.py#L209)

Returns list of module classes



> **pymdocs.parsers.ast.ModuleDefinition.functions**(*self*) -> *List[FunctionDefinition]* [[source]](../pymdocs/parsers/ast.py#L218)

Returns list of module functions





### *class* `pymdocs.parsers.ast.PackageDefinition` [[source]](../pymdocs/parsers/ast.py#L227)

Base: `ElementDefinition`

Class for python package representation



#### Methods

> **pymdocs.parsers.ast.PackageDefinition.name**(*self*) -> *str* [[source]](../pymdocs/parsers/ast.py#L241)

Returns package name





## Functions

> **pymdocs.parsers.ast.parse\_module**(*path: str*) -> *ModuleDefinition* [[source]](../pymdocs/parsers/ast.py#L255)

Parses Python module content

**Args:**

- *path*: pathlib.Path, Python module path

**Returns:**

`ModuleDefinition`: module objects definition



> **pymdocs.parsers.ast.parse**(*path: str*) -> *Optional[Union[PackageDefinition, ModuleDefinition]]* [[source]](../pymdocs/parsers/ast.py#L273)

Parses Python module or package content

**Args:**

- *path*: pathlib.Path, Python module path

**Returns:**

`(ModuleDefinition | PackageDefinition | None)`: module or package
objects definition



# <a class="anchor" id="pymdocs-parsers-docstring-google"></a>*module* pymdocs.parsers.docstring.google

## Classes

### *class* `pymdocs.parsers.docstring.google.DocstringSections` [[source]](../pymdocs/parsers/docstring/google.py#L25)

Base: `StrEnum`



## Functions

> **pymdocs.parsers.docstring.google.parse\_section**(*text: str*, *section\_type: str*) -> *DocstringSection* [[source]](../pymdocs/parsers/docstring/google.py#L102)

Parses section from text by section type

**Args:**

- *text*: str, text to parse
- *section\_type*: str, section type (Args, Attributes, Raises, etc.)

**Returns:**

`DocstringSection`: DocstringSection object



> **pymdocs.parsers.docstring.google.parse**(*docstring: str*) -> *Docstring* [[source]](../pymdocs/parsers/docstring/google.py#L138)

Parses Google Style docstring

**Args:**

- *docstring*: Google Style docstring

**Returns:**

`Docstring`: Docstring object



# <a class="anchor" id="pymdocs-parsers-docstring-numpy"></a>*module* pymdocs.parsers.docstring.numpy

## Classes

### *class* `pymdocs.parsers.docstring.numpy.DocstringSections` [[source]](../pymdocs/parsers/docstring/numpy.py#L25)

Base: `str, Enum`



## Functions

> **pymdocs.parsers.docstring.numpy.parse\_section**(*text: str*, *section\_type: str*) -> *DocstringSection* [[source]](../pymdocs/parsers/docstring/numpy.py#L108)

Parses section from text by section type

**Returns:**

`DocstringSection`: DocstringSection object



> **pymdocs.parsers.docstring.numpy.parse**(*docstring: str*) -> *Docstring* [[source]](../pymdocs/parsers/docstring/numpy.py#L151)

Parses Numpy Style docstring

**Returns:**

`Docstring`: Docstring object



# <a class="anchor" id="pymdocs-parsers-docstring-helpers"></a>*module* pymdocs.parsers.docstring.helpers

## Functions

> **pymdocs.parsers.docstring.helpers.iter\_split**(*pattern: re.Pattern*, *text: str*) -> *Iterator[Tuple[Optional[re.Match], str, int, int]]* [[source]](../pymdocs/parsers/docstring/helpers.py#L5)

Iterates through pattern matches and yiedls text between them

**Args:**

- *pattern*: re.Pattern, pattern to search
- *text*: str, text to search pattern



# <a class="anchor" id="pymdocs-parsers-docstring-base"></a>*module* pymdocs.parsers.docstring.base

## Classes

### *class* `pymdocs.parsers.docstring.base.DocstringElement` [[source]](../pymdocs/parsers/docstring/base.py#L6)

Base class for docstring elements





### *class* `pymdocs.parsers.docstring.base.DocstringSection` [[source]](../pymdocs/parsers/docstring/base.py#L10)

Base class for docstring section



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringArg` [[source]](../pymdocs/parsers/docstring/base.py#L20)

Base: `DocstringElement`

Class for docstring 'Args' section element

**Attributes:**

- *name*: str, name of argument
- *typing\_annotation*: (str | None), argument type
- *description*: str, argument description



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringArgsSection` [[source]](../pymdocs/parsers/docstring/base.py#L41)

Class for docstring 'Args' section

**Attributes:**

- *attributes*: List[DocstringArg], list of arguments





### *class* `pymdocs.parsers.docstring.base.DocstringAttribute` [[source]](../pymdocs/parsers/docstring/base.py#L50)

Base: `DocstringElement`

Class for docstring 'Attributes' section element

**Attributes:**

- *name*: str, name of attribute
- *typing\_annotation*: (str | None), attribute type
- *description*: str, attribute description



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringAttributesSection` [[source]](../pymdocs/parsers/docstring/base.py#L71)

Class for docstring 'Attributes' section

**Attributes:**

- *attributes*: List[DocstringAttribute], list of attributes





### *class* `pymdocs.parsers.docstring.base.DocstringExample` [[source]](../pymdocs/parsers/docstring/base.py#L80)

Base: `DocstringElement`

Class for docstring 'Examples' section element

**Attributes:**

- *description*: str, docstring example



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringExamplesSection` [[source]](../pymdocs/parsers/docstring/base.py#L92)

Class for docstring 'Examples' section

**Attributes:**

- *attributes*: List[DocstringExample], list of docstring examples





### *class* `pymdocs.parsers.docstring.base.DocstringRaises` [[source]](../pymdocs/parsers/docstring/base.py#L101)

Base: `DocstringElement`

Class for docstring 'Raises' section elements

**Attributes:**

- *exception*: str, exception name
- *description*: str, exception description



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringRaisesSection` [[source]](../pymdocs/parsers/docstring/base.py#L115)

Class for docstring 'Raises' section

**Attributes:**

- *attributes*: List[DocstringRaises], list of rasing exceptions





### *class* `pymdocs.parsers.docstring.base.DocstringReturns` [[source]](../pymdocs/parsers/docstring/base.py#L124)

Base: `DocstringElement`

Class for docstring 'Returns' section elements

**Attributes:**

- *typing\_annotation*: str, returning value type
- *description*: str, returning value description



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringReturnsSection` [[source]](../pymdocs/parsers/docstring/base.py#L142)

Class for docstring 'Returns' section

**Attributes:**

- *attributes*: List[DocstringReturns], returning value description





### *class* `pymdocs.parsers.docstring.base.DocstringYiedls` [[source]](../pymdocs/parsers/docstring/base.py#L151)

Base: `DocstringElement`

Class for docstring 'Yields' section elements

**Attributes:**

- *typing\_annotation*: str, yielding value type
- *description*: str, yielding value description



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringYiedlsSection` [[source]](../pymdocs/parsers/docstring/base.py#L169)

Class for docstring 'Yields' section

**Attributes:**

- *attributes*: List[DocstringYields], yielding value description





### *class* `pymdocs.parsers.docstring.base.Docstring` [[source]](../pymdocs/parsers/docstring/base.py#L178)

Base: `DocstringSection`

Class for python docstring

**Attributes:**

- *attributes*: List[DocstringSection], list of docstring sections
- *description*: str, docstring title



#### Methods

> **pymdocs.parsers.docstring.base.Docstring.args**(*self*) -> *List[DocstringArg]* [[source]](../pymdocs/parsers/docstring/base.py#L196)

Returns list of docstring 'Args' section elements



> **pymdocs.parsers.docstring.base.Docstring.attributes**(*self*) -> *List[DocstringAttribute]* [[source]](../pymdocs/parsers/docstring/base.py#L205)

Returns list of docstring 'Attributes' section elements



> **pymdocs.parsers.docstring.base.Docstring.examples**(*self*) -> *List[DocstringExample]* [[source]](../pymdocs/parsers/docstring/base.py#L214)

Returns list of docstring 'Examples' section elements



> **pymdocs.parsers.docstring.base.Docstring.raises**(*self*) -> *List[DocstringRaises]* [[source]](../pymdocs/parsers/docstring/base.py#L223)

Returns list of docstring 'Raises' section elements



> **pymdocs.parsers.docstring.base.Docstring.returns**(*self*) -> *List[DocstringReturns]* [[source]](../pymdocs/parsers/docstring/base.py#L232)

Returns list of docstring 'Returns' section elements



> **pymdocs.parsers.docstring.base.Docstring.yields**(*self*) -> *List[DocstringYiedls]* [[source]](../pymdocs/parsers/docstring/base.py#L241)

Returns list of docstring 'Yields' section elements





# <a class="anchor" id="pymdocs-formatters-class_formatter"></a>*module* pymdocs.formatters.class\_formatter

## Classes

### *class* `pymdocs.formatters.class_formatter.ClassFormatter` [[source]](../pymdocs/formatters/class_formatter.py#L9)

Formatter for ClassDefinition objects

**Attributes:**

- *\_requires*: tuple[FormatterType, ...], data attribute,tuple of
required formatters (DOCSTRING, FUNCTION)
- *formatters*: (Dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.class\_formatter.ClassFormatter.format**(*self*, *obj: ClassDefinition*, *doc\_path: str*, *package\_name: Optional[str]*, *module\_name: Optional[str]*) -> *md.MarkdownElement* [[source]](../pymdocs/formatters/class_formatter.py#L25)

Returns Markdown element for function definition

**Args:**

- *class\_def*: ClassDefinition, python class definition
- *doc\_path*: str, path to documentation file
- *package\_name*: (str | None), name of the class package
- *module\_name*: (str | None), name of the class module

**Returns:**

`MarkdownContainer`: Markdown element for class





# <a class="anchor" id="pymdocs-formatters-markdown_constructor"></a>*module* pymdocs.formatters.markdown\_constructor

## Classes

### *class* `pymdocs.formatters.markdown_constructor.MarkdownElement` [[source]](../pymdocs/formatters/markdown_constructor.py#L8)

Base class for Markdown elements



#### Methods

> **pymdocs.formatters.markdown\_constructor.MarkdownElement.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L11)

Method for rendering Markdown





### *class* `pymdocs.formatters.markdown_constructor.StringLiteral` [[source]](../pymdocs/formatters/markdown_constructor.py#L16)

Base: `MarkdownElement`

Helper class for user defined strings



#### Methods

> **pymdocs.formatters.markdown\_constructor.StringLiteral.render**(*self*) [[source]](../pymdocs/formatters/markdown_constructor.py#L22)



### *class* `pymdocs.formatters.markdown_constructor.MarkdownContainer` [[source]](../pymdocs/formatters/markdown_constructor.py#L26)

Base: `MarkdownElement`

Base class for list of Markdown elements, also usefull for groupping
other elements

**Attributes:**

- *elemens*: Sequence[Union[MarkdownElement, str]], list of inner elements,
could be another MarkdownElement or python string
- *sep*: Union[MarkdownElement, str], elements separator, could be
another MarkdownElement or python string

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

> **pymdocs.formatters.markdown\_constructor.MarkdownContainer.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L72)

Returns Markdown representation all inner elements,
joined by separator





### *class* `pymdocs.formatters.markdown_constructor.Quote` [[source]](../pymdocs/formatters/markdown_constructor.py#L94)

Base: `StringLiteral`

Class for quoting Markdown symbols

**Attributes:**

- *text*: str, element text

**Examples:**

<pre>Rendering string with quoted markdown symbols

>> element = Quote('text_with_dashes')
>> element.render()
text\_with\_dashes</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.Quote.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L109)

Returns markdown quoted text





### *class* `pymdocs.formatters.markdown_constructor.Link` [[source]](../pymdocs/formatters/markdown_constructor.py#L119)

Base: `StringLiteral`

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

> **pymdocs.formatters.markdown\_constructor.Link.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L146)

Returns Markdown link





### *class* `pymdocs.formatters.markdown_constructor.Image` [[source]](../pymdocs/formatters/markdown_constructor.py#L156)

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

> **pymdocs.formatters.markdown\_constructor.Image.render**(*self*) [[source]](../pymdocs/formatters/markdown_constructor.py#L173)

Returns Markdown image





### *class* `pymdocs.formatters.markdown_constructor.Paragraph` [[source]](../pymdocs/formatters/markdown_constructor.py#L178)

Base: `MarkdownContainer`

Class for Markdown paragraph element



#### Methods

> **pymdocs.formatters.markdown\_constructor.Paragraph.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L181)

Renders inner elements, with paragraph break in the end





### *class* `pymdocs.formatters.markdown_constructor.Header` [[source]](../pymdocs/formatters/markdown_constructor.py#L189)

Base: `MarkdownContainer`

Base class for Markdown header element

**Attributes:**

- *elements*: Sequence[Union[MarkdownContainer, str]], list of inner
elements
- *sep*: Union[MarkdownContainer, str], elements separator
- *level*: int, optional, level of the header, 1 by default

**Examples:**

<pre>Rendering first level header

>> element = Header(
>>     ['module', WHITESPACE, Quote(['markdown_constructor'])]
>> )
>> element.render()
# module markdown\_constructor</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.Header.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L218)

Returns Markdown header with inner elelements





### *class* `pymdocs.formatters.markdown_constructor.H1` [[source]](../pymdocs/formatters/markdown_constructor.py#L227)

Base: `Header`

Class for 1 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.H2` [[source]](../pymdocs/formatters/markdown_constructor.py#L238)

Base: `Header`

Class for 2 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.H3` [[source]](../pymdocs/formatters/markdown_constructor.py#L249)

Base: `Header`

Class for 3 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.H4` [[source]](../pymdocs/formatters/markdown_constructor.py#L260)

Base: `Header`

Class for 4 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.H5` [[source]](../pymdocs/formatters/markdown_constructor.py#L271)

Base: `Header`

Class for 5 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.H6` [[source]](../pymdocs/formatters/markdown_constructor.py#L282)

Base: `Header`

Class for 6 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.Bold` [[source]](../pymdocs/formatters/markdown_constructor.py#L293)

Base: `MarkdownContainer`

Class for Markdown bold element

**Examples:**

<pre>Rendering bold text

>> element = Bold(['some bold text'])
>> element.render()
**some bold text**</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.Bold.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L305)

Returns bolded inner elements





### *class* `pymdocs.formatters.markdown_constructor.Italic` [[source]](../pymdocs/formatters/markdown_constructor.py#L310)

Base: `MarkdownContainer`

Class for Markdown italic element

**Examples:**

<pre>Rendering italic text

>> element = Italic(['some italic text'])
>> element.render()
*some italic text*</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.Italic.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L322)

Returns italic inner elements





### *class* `pymdocs.formatters.markdown_constructor.BoldItalic` [[source]](../pymdocs/formatters/markdown_constructor.py#L327)

Base: `MarkdownContainer`

Class for Markdown bold italic element

**Examples:**

<pre>Rendering bold and italic text

>> element = BoldItalic(['some text'])
>> element.render()
**some text**</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.BoldItalic.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L339)

Returns bolded italic inner elements





### *class* `pymdocs.formatters.markdown_constructor.Strikethrough` [[source]](../pymdocs/formatters/markdown_constructor.py#L344)

Base: `MarkdownContainer`

Class for Markdown strikethrough element

**Examples:**

<pre>Rendering strikethrough text

>> element = Strikethrough(['some text'])
>> element.render()
~~some text~~</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.Strikethrough.render**(*self*) [[source]](../pymdocs/formatters/markdown_constructor.py#L356)



### *class* `pymdocs.formatters.markdown_constructor.Blockquotes` [[source]](../pymdocs/formatters/markdown_constructor.py#L360)

Base: `MarkdownContainer`

Class for Markdown blockquotes element

**Examples:**

<pre>Rendering block quotes

>> element = Blockquotes(['some text'])
>> element.render()
> some text</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.Blockquotes.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L372)

Returns blockquotes with inner elements





### *class* `pymdocs.formatters.markdown_constructor.OrderedList` [[source]](../pymdocs/formatters/markdown_constructor.py#L380)

Base: `MarkdownContainer`

Class for Markdown ordered list element

**Attributes:**

- *elements*: Sequence[Union[MarkdownContainer, str]], list of inner
elements

**Examples:**

<pre>Rendering ordered list

>> element = OrderedList(['first item', 'second item', 'third item'])
>> element.render()
1. first item
2. second item
3. third item</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.OrderedList.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L401)

Returns Markdown ordered list with inner elements as items





### *class* `pymdocs.formatters.markdown_constructor.UnorderedList` [[source]](../pymdocs/formatters/markdown_constructor.py#L410)

Base: `MarkdownContainer`

Class for Markdown unordered list element

**Attributes:**

- *elements*: Sequence[Union[MarkdownContainer, str]], list of inner
elements

**Examples:**

<pre>Rendering unordered list

>> element = UnorderedList(['first item', 'second item', 'third item'])
>> element.render()
- first item
- second item
- third item</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.UnorderedList.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L431)

Returns Markdown unordered list with inner elements as items





### *class* `pymdocs.formatters.markdown_constructor.TaskItem` [[source]](../pymdocs/formatters/markdown_constructor.py#L439)

Base: `MarkdownContainer`

Class for Markdown task list item element

**Attributes:**

- *elements*: Sequence[Union[MarkdownContainer, str]], list of inner
elements
- *sep*: Union[MarkdownContainer, str], elements separator
- *is\_done*: bool, is the task done or not, False by default



#### Methods

> **pymdocs.formatters.markdown\_constructor.TaskItem.render**(*self*) [[source]](../pymdocs/formatters/markdown_constructor.py#L459)

Returns Markdown task list item with inner elements





### *class* `pymdocs.formatters.markdown_constructor.TaskList` [[source]](../pymdocs/formatters/markdown_constructor.py#L467)

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



### *class* `pymdocs.formatters.markdown_constructor.InlineCode` [[source]](../pymdocs/formatters/markdown_constructor.py#L492)

Base: `MarkdownContainer`

Class for Markdown inline code element

**Examples:**

<pre>Rendering inline code

>> element = InlineCode(['code'])
>> element.render()
`code`</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.InlineCode.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L504)

Returns Mrkdown inline code with inner elements





### *class* `pymdocs.formatters.markdown_constructor.Code` [[source]](../pymdocs/formatters/markdown_constructor.py#L509)

Base: `MarkdownContainer`

Class for Markdown multiline code block

**Attributes:**

- *elements*: Sequence[Union[MarkdownContainer, str]], list of inner
elements
- *sep*: Union[MarkdownContainer, str], elements separator
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

> **pymdocs.formatters.markdown\_constructor.Code.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L545)

Returns markdown code block with inner elements





### *class* `pymdocs.formatters.markdown_constructor.ColumnOrientation` [[source]](../pymdocs/formatters/markdown_constructor.py#L554)

Base: `str, Enum`

Markdown table column orientation





### *class* `pymdocs.formatters.markdown_constructor.TableRow` [[source]](../pymdocs/formatters/markdown_constructor.py#L564)

Base: `MarkdownContainer`

Class for Markdown table row element

**Attributes:**

- *elements*: Sequence[Union[MarkdownContainer, str]], table row elements

**Examples:**

<pre>Rendering table row

>> element = TableRow(['1', 'one'])
>> element.render()
1 | one</pre>



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.Table` [[source]](../pymdocs/formatters/markdown_constructor.py#L583)

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

> **pymdocs.formatters.markdown\_constructor.Table.render**(*self*) [[source]](../pymdocs/formatters/markdown_constructor.py#L624)

Returns Markdown table





### *class* `pymdocs.formatters.markdown_constructor.HTMLComment` [[source]](../pymdocs/formatters/markdown_constructor.py#L642)

Base: `StringLiteral`

Class for HTML comment

**Examples:**

<pre>Rendering an HTML comment (not visible in Markdown)

>> element = HTMLComment(['very usefull information'])
>> element.render()
<!--very usefull information--></pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.HTMLComment.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L654)

Returns markdown HTML comment with inner elements





### *class* `pymdocs.formatters.markdown_constructor.Raw` [[source]](../pymdocs/formatters/markdown_constructor.py#L663)

Base: `StringLiteral`

Class for raw text



#### Methods

> **pymdocs.formatters.markdown\_constructor.Raw.render**(*self*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L668)

Returns raw text





### *class* `pymdocs.formatters.markdown_constructor.HTMLAnchor` [[source]](../pymdocs/formatters/markdown_constructor.py#L677)

Base: `MarkdownElement`

Class for html anchor



#### Methods

> **pymdocs.formatters.markdown\_constructor.HTMLAnchor.render**(*self*) [[source]](../pymdocs/formatters/markdown_constructor.py#L685)



### *class* `pymdocs.formatters.markdown_constructor.Latex` [[source]](../pymdocs/formatters/markdown_constructor.py#L691)

Base: `StringLiteral`

Class for Latex formulas



#### Methods

> **pymdocs.formatters.markdown\_constructor.Latex.render**(*self*) [[source]](../pymdocs/formatters/markdown_constructor.py#L696)



# <a class="anchor" id="pymdocs-formatters-package_formatter"></a>*module* pymdocs.formatters.package\_formatter

## Classes

### *class* `pymdocs.formatters.package_formatter.PackageFormatter` [[source]](../pymdocs/formatters/package_formatter.py#L9)

Formatter for ModuleDefinition objects

**Attributes:**

- *\_requires*: tuple[FormatterType, ...], data attribute,tuple of
required formatters (DOCSTRING, FUNCTION, CLASS, MODULE)
- *formatters*: (dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.package\_formatter.PackageFormatter.flatten\_modules**(*self*, *package\_def: PackageDefinition*, *doc\_path: str*, *prefix: str*) -> *List[Tuple[md.MarkdownContainer, md.Link]]* [[source]](../pymdocs/formatters/package_formatter.py#L27)

Formats package definition as a list of formatted module definitions
recursively

**Args:**

- *package\_def*: PackageDefinition, python package definition
- *doc\_path*: str, path to documentation file
- *prefix*: str, prefix to add to package inner objects names

**Returns:**

`(list[tuple[md.MarkdownContainer, md.Link]])`: list of tuples of
markdown element for module and module link for Contents
section



> **pymdocs.formatters.package\_formatter.PackageFormatter.format**(*self*, *obj: PackageDefinition*, *doc\_path: str*) -> *md.MarkdownElement* [[source]](../pymdocs/formatters/package_formatter.py#L85)

Returns Markdown element for package definition

**Args:**

- *package\_def*: PackageDefinition, python package definition
- *doc\_path*: str, path to documentation file

**Returns:**

`MarkdownContainer`: Markdown element for package





# <a class="anchor" id="pymdocs-formatters-function_formatter"></a>*module* pymdocs.formatters.function\_formatter

## Classes

### *class* `pymdocs.formatters.function_formatter.FunctionFormatter` [[source]](../pymdocs/formatters/function_formatter.py#L9)

Formatter for FunctionDefinition objects

**Attributes:**

- *\_requires*: tuple[FormatterType, ...], data attribute,tuple of
required formatters (DOCSTRING)
- *formatters*: (Dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.function\_formatter.FunctionFormatter.format**(*self*, *obj: FunctionDefinition*, *doc\_path: str*, *package\_name: Optional[str]*, *module\_name: Optional[str]*, *class\_name: Optional[str]*) -> *md.MarkdownContainer* [[source]](../pymdocs/formatters/function_formatter.py#L24)

Returns Markdown element for function definition

**Args:**

- *obj*: FunctionDefinition, python function definition
- *doc\_path*: str, path to documentation file
- *package\_name*: (str | None), name of the function package,
None by default
- *module\_name*: (str | None), name of the function module,
None by default
- *class\_name*: (str | None), name of function class, if function
is a class method, None by default

**Returns:**

`MarkdownContainer`: Markdown element for function





# <a class="anchor" id="pymdocs-formatters-docstring_formatter"></a>*module* pymdocs.formatters.docstring\_formatter

## Classes

### *class* `pymdocs.formatters.docstring_formatter.DocstringFormatter` [[source]](../pymdocs/formatters/docstring_formatter.py#L6)

Formatter for ClassDefinition objects

**Attributes:**

- *\_requires*: tuple[FormatterType, ...], data attribute,tuple of
required formatters
- *formatters*: (Dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.docstring\_formatter.DocstringFormatter.format**(*self*, *obj: Docstring*) -> *md.MarkdownContainer* [[source]](../pymdocs/formatters/docstring_formatter.py#L17)

Returns Markdown element for function definition

**Args:**

- *docstring*: Docstring, python docstring definition

**Returns:**

`MarkdownContainer`: Markdown element for docstring or None





# <a class="anchor" id="pymdocs-formatters-common_formatter"></a>*module* pymdocs.formatters.common\_formatter

## Classes

### *class* `pymdocs.formatters.common_formatter.Formatter` [[source]](../pymdocs/formatters/common_formatter.py#L40)

Base: `BaseFormatter`

Common formatter for all objects

**Attributes:**

- *\_requires*: tuple[FormatterType, ...], data attribute,tuple of
required formatters
- *formatters*: (Dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.common\_formatter.Formatter.format**(*self*, *obj: Any*) -> *md.MarkdownElement* [[source]](../pymdocs/formatters/common_formatter.py#L66)

Formats object tom Markdown

**Args:**

- *obj*: Any, object needed to format
- *\*\*kwargs*: additional arguments for object formatter

**Raises:**

- `ValueError`: if object formatter is not set

**Returns:**

`MarkdownElement`: Markdown element for object





# <a class="anchor" id="pymdocs-formatters-helpers"></a>*module* pymdocs.formatters.helpers

## Functions

> **pymdocs.formatters.helpers.module\_line\_path\_link**(*element: AstWrapper*, *text: str*, *doc\_path: str*) -> *md.Link* [[source]](../pymdocs/formatters/helpers.py#L8)

Returns reference Markdown link to object

**Args:**

- *element*: AstWrapper, element needed to reference
- *text*: str, reference link text
- *doc\_path*: str, path to documentation file

**Returns:**

`Link`: reference link to object



# <a class="anchor" id="pymdocs-formatters-base"></a>*module* pymdocs.formatters.base

## Classes

### *class* `pymdocs.formatters.base.FormatterType` [[source]](../pymdocs/formatters/base.py#L11)

Base: `int, Enum`

Enum for formatter types





### *class* `pymdocs.formatters.base.BaseFormatter` [[source]](../pymdocs/formatters/base.py#L26)

Base class for markdown formatters

**Attributes:**

- *\_requires*: Tuple[FormatterType, ...], data attribute,tuple of
required formatters
- *formatters*: (Dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.base.BaseFormatter.format**(*self*, *obj: T*) -> *md.MarkdownElement* [[source]](../pymdocs/formatters/base.py#L62)

Returns markdown representation for obj



> **pymdocs.formatters.base.BaseFormatter.format\_by**(*self*, *formatter\_type: FormatterType*, *obj: Any*) -> *md.MarkdownElement* [[source]](../pymdocs/formatters/base.py#L69)

Formats object by additional formatter

**Args:**

- *formatter\_type*: FormatterType, type of needed formatter
- *obj*: AstWrapper, object to format as Markdown

**Raises:**

- `ValueError`: if needed formatter is not set

**Returns:**

`MarkdownContainer`: markdown representation of object





# <a class="anchor" id="pymdocs-formatters-module_formatter"></a>*module* pymdocs.formatters.module\_formatter

## Classes

### *class* `pymdocs.formatters.module_formatter.ModuleFormatter` [[source]](../pymdocs/formatters/module_formatter.py#L8)

Formatter for ModuleDefinition objects

**Attributes:**

- *\_requires*: tuple[FormatterType, ...], data attribute,tuple of
required formatters (DOCSTRING, FUNCTION, CLASS)
- *formatters*: (dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.module\_formatter.ModuleFormatter.module\_link**(*module\_name: str*) [[source]](../pymdocs/formatters/module_formatter.py#L26)

Returns module link for Contents documentation section

**Args:**

- *module\_name*: str, module name

**Returns:**

`Link`: markdown link element



> **pymdocs.formatters.module\_formatter.ModuleFormatter.module\_anchor**(*module\_name: str*) [[source]](../pymdocs/formatters/module_formatter.py#L42)

Returns module anchor for Contents documentation section

**Args:**

- *module\_name*: str, module name

**Returns:**

`HTMLAnchor`: anchor for module documentation header



> **pymdocs.formatters.module\_formatter.ModuleFormatter.format**(*self*, *obj: ModuleDefinition*, *doc\_path: str*, *package\_name: Optional[str]*) [[source]](../pymdocs/formatters/module_formatter.py#L56)

Returns Markdown element for module definition

**Args:**

- *module\_def*: ModuleDefinition, python module definition
- *doc\_path*: str, path to documentation file
- *package\_name*: (str | None), name of the class package

**Returns:**

`MarkdownContainer`: Markdown element for module







