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

> **pymdocs.cli.Pymdocs.doc**(*self: Any*) -> *None* [[source]](../pymdocs/cli.py#L42)

Generates Code Reference for python code





## Functions

> **pymdocs.cli.main**() -> *None* [[source]](../pymdocs/cli.py#L59)



# <a class="anchor" id="pymdocs-parsers-ast"></a>*module* pymdocs.parsers.ast

## Classes

### *class* `pymdocs.parsers.ast.AstWrapper` [[source]](../pymdocs/parsers/ast.py#L12)



Base class for Python AST element wrapper

**Attributes:**

- *ast\_element*: ast.AST, AST tree node
- *path*: str, path to file contains element



#### Methods

> **pymdocs.parsers.ast.AstWrapper.lineno**(*self: Any*) -> *Optional[int]* [[source]](../pymdocs/parsers/ast.py#L34)

Returns line number of the element in file



> **pymdocs.parsers.ast.AstWrapper.properties**(*self: Any*) -> *dict* [[source]](../pymdocs/parsers/ast.py#L47)

Returns dict of object properties values



> **pymdocs.parsers.ast.AstWrapper.dict**(*self: Any*) -> *dict* [[source]](../pymdocs/parsers/ast.py#L57)

Returns element dict representation (and all subelements recursively)





### *class* `pymdocs.parsers.ast.Typing` [[source]](../pymdocs/parsers/ast.py#L79)

Base: `AstWrapper`

Class for Python typing annotations representation



#### Methods

> **pymdocs.parsers.ast.Typing.annotation**(*self: Any*) -> *str* [[source]](../pymdocs/parsers/ast.py#L87)

Returns string representation of typing annotation





### *class* `pymdocs.parsers.ast.Argument` [[source]](../pymdocs/parsers/ast.py#L123)

Base: `AstWrapper`

Class for function argument representation



#### Methods

> **pymdocs.parsers.ast.Argument.name**(*self: Any*) -> *str* [[source]](../pymdocs/parsers/ast.py#L140)

Returns name of function argument



> **pymdocs.parsers.ast.Argument.type**(*self: Any*) -> *Typing* [[source]](../pymdocs/parsers/ast.py#L145)

Returns typing annotation of function argument





### *class* `pymdocs.parsers.ast.FunctionDefinition` [[source]](../pymdocs/parsers/ast.py#L157)

Base: `AstWrapper`

Class for function representation



#### Methods

> **pymdocs.parsers.ast.FunctionDefinition.name**(*self: Any*) -> *str* [[source]](../pymdocs/parsers/ast.py#L176)

Returns function name



> **pymdocs.parsers.ast.FunctionDefinition.arguments**(*self: Any*) -> *List[Argument]* [[source]](../pymdocs/parsers/ast.py#L181)

Returns list of function arguments



> **pymdocs.parsers.ast.FunctionDefinition.returns**(*self: Any*) -> *Typing* [[source]](../pymdocs/parsers/ast.py#L189)

Returns function return typing annotation



> **pymdocs.parsers.ast.FunctionDefinition.docstring**(*self: Any*) -> *Optional[doc.Docstring]* [[source]](../pymdocs/parsers/ast.py#L197)

Returns function docstring if exists





### *class* `pymdocs.parsers.ast.ClassDefinition` [[source]](../pymdocs/parsers/ast.py#L207)

Base: `AstWrapper`

Class for Python class representation



#### Methods

> **pymdocs.parsers.ast.ClassDefinition.name**(*self: Any*) -> *str* [[source]](../pymdocs/parsers/ast.py#L226)

Returns class name



> **pymdocs.parsers.ast.ClassDefinition.inherits**(*self: Any*) -> *List[str]* [[source]](../pymdocs/parsers/ast.py#L231)

Returns class bases



> **pymdocs.parsers.ast.ClassDefinition.docstring**(*self: Any*) -> *Optional[doc.Docstring]* [[source]](../pymdocs/parsers/ast.py#L240)

Retuns class docstring if exists



> **pymdocs.parsers.ast.ClassDefinition.methods**(*self: Any*) -> *List[FunctionDefinition]* [[source]](../pymdocs/parsers/ast.py#L250)

Returns list of class methods





### *class* `pymdocs.parsers.ast.ModuleDefinition` [[source]](../pymdocs/parsers/ast.py#L259)

Base: `AstWrapper`

Class for Python module representation



#### Methods

> **pymdocs.parsers.ast.ModuleDefinition.name**(*self: Any*) -> *str* [[source]](../pymdocs/parsers/ast.py#L274)

Returns module name



> **pymdocs.parsers.ast.ModuleDefinition.docstring**(*self: Any*) -> *Optional[doc.Docstring]* [[source]](../pymdocs/parsers/ast.py#L279)

Retuns module docstring if exists



> **pymdocs.parsers.ast.ModuleDefinition.classes**(*self: Any*) -> *List[ClassDefinition]* [[source]](../pymdocs/parsers/ast.py#L289)

Returns list of module classes



> **pymdocs.parsers.ast.ModuleDefinition.functions**(*self: Any*) -> *List[FunctionDefinition]* [[source]](../pymdocs/parsers/ast.py#L298)

Returns list of module functions





### *class* `pymdocs.parsers.ast.PackageDefinition` [[source]](../pymdocs/parsers/ast.py#L307)

Base: `AstWrapper`

Class for python package representation



#### Methods

> **pymdocs.parsers.ast.PackageDefinition.name**(*self: Any*) -> *str* [[source]](../pymdocs/parsers/ast.py#L321)

Returns package name





## Functions

> **pymdocs.parsers.ast.parse\_module**(*path: str*) -> *ModuleDefinition* [[source]](../pymdocs/parsers/ast.py#L335)

Parses Python module content

**Args:**

- *path*: pathlib.Path, Python module path

**Returns:**

`ModuleDefinition`: module objects definition



> **pymdocs.parsers.ast.parse**(*path: str*) -> *Optional[Union[PackageDefinition, ModuleDefinition]]* [[source]](../pymdocs/parsers/ast.py#L353)

Parses Python module or package content

**Args:**

- *path*: pathlib.Path, Python module path

**Returns:**

`(ModuleDefinition | PackageDefinition | None)`: module or package
objects definition



# <a class="anchor" id="pymdocs-parsers-docstring-google"></a>*module* pymdocs.parsers.docstring.google

## Classes

### *class* `pymdocs.parsers.docstring.google.DocstringSections` [[source]](../pymdocs/parsers/docstring/google.py#L26)

Base: `str, Enum`





## Functions

> **pymdocs.parsers.docstring.google.parse\_section**(*text: str*, *section\_type: str*) -> *DocstringSection* [[source]](../pymdocs/parsers/docstring/google.py#L103)

Parses section from text by section type

**Args:**

- *text*: str, text to parse
- *section\_type*: str, section type (Args, Attributes, Raises, etc.)

**Returns:**

`DocstringSection`: DocstringSection object



> **pymdocs.parsers.docstring.google.parse**(*docstring: str*) -> *Docstring* [[source]](../pymdocs/parsers/docstring/google.py#L139)

Parses Google Style docstring

**Args:**

- *docstring*: Google Style docstring

**Returns:**

`Docstring`: Docstring object



# <a class="anchor" id="pymdocs-parsers-docstring-numpy"></a>*module* pymdocs.parsers.docstring.numpy

## Classes

### *class* `pymdocs.parsers.docstring.numpy.DocstringSections` [[source]](../pymdocs/parsers/docstring/numpy.py#L26)

Base: `str, Enum`





## Functions

> **pymdocs.parsers.docstring.numpy.parse\_section**(*text: str*, *section\_type: str*) -> *DocstringSection* [[source]](../pymdocs/parsers/docstring/numpy.py#L109)

Parses section from text by section type

**Returns:**

`DocstringSection`: DocstringSection object



> **pymdocs.parsers.docstring.numpy.parse**(*docstring: str*) -> *Docstring* [[source]](../pymdocs/parsers/docstring/numpy.py#L152)

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

### *class* `pymdocs.parsers.docstring.base.DocstringElement` [[source]](../pymdocs/parsers/docstring/base.py#L4)



Base class for docstring elements



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringSection` [[source]](../pymdocs/parsers/docstring/base.py#L11)



Base class for docstring section



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringArg` [[source]](../pymdocs/parsers/docstring/base.py#L21)

Base: `DocstringElement`

Class for docstring 'Args' section element

**Attributes:**

- *name*: str, name of argument
- *typing\_annotation*: (str | None), argument type
- *description*: str, argument description



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringArgsSection` [[source]](../pymdocs/parsers/docstring/base.py#L42)

Base: `DocstringSection`

Class for docstring 'Args' section

**Attributes:**

- *attributes*: List[DocstringArg], list of arguments



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringAttribute` [[source]](../pymdocs/parsers/docstring/base.py#L54)

Base: `DocstringElement`

Class for docstring 'Attributes' section element

**Attributes:**

- *name*: str, name of attribute
- *typing\_annotation*: (str | None), attribute type
- *description*: str, attribute description



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringAttributesSection` [[source]](../pymdocs/parsers/docstring/base.py#L78)

Base: `DocstringSection`

Class for docstring 'Attributes' section

**Attributes:**

- *attributes*: List[DocstringAttribute], list of attributes



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringExample` [[source]](../pymdocs/parsers/docstring/base.py#L90)

Base: `DocstringElement`

Class for docstring 'Examples' section element

**Attributes:**

- *description*: str, docstring example



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringExamplesSection` [[source]](../pymdocs/parsers/docstring/base.py#L102)

Base: `DocstringSection`

Class for docstring 'Examples' section

**Attributes:**

- *attributes*: List[DocstringExample], list of docstring examples



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringRaises` [[source]](../pymdocs/parsers/docstring/base.py#L114)

Base: `DocstringElement`

Class for docstring 'Raises' section elements

**Attributes:**

- *exception*: str, exception name
- *description*: str, exception description



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringRaisesSection` [[source]](../pymdocs/parsers/docstring/base.py#L131)

Base: `DocstringSection`

Class for docstring 'Raises' section

**Attributes:**

- *attributes*: List[DocstringRaises], list of rasing exceptions



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringReturns` [[source]](../pymdocs/parsers/docstring/base.py#L143)

Base: `DocstringElement`

Class for docstring 'Returns' section elements

**Attributes:**

- *typing\_annotation*: str, returning value type
- *description*: str, returning value description



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringReturnsSection` [[source]](../pymdocs/parsers/docstring/base.py#L164)

Base: `DocstringSection`

Class for docstring 'Returns' section

**Attributes:**

- *attributes*: List[DocstringReturns], returning value description



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringYiedls` [[source]](../pymdocs/parsers/docstring/base.py#L176)

Base: `DocstringElement`

Class for docstring 'Yields' section elements

**Attributes:**

- *typing\_annotation*: str, yielding value type
- *description*: str, yielding value description



#### Methods



### *class* `pymdocs.parsers.docstring.base.DocstringYiedlsSection` [[source]](../pymdocs/parsers/docstring/base.py#L197)

Base: `DocstringSection`

Class for docstring 'Yields' section

**Attributes:**

- *attributes*: List[DocstringYields], yielding value description



#### Methods



### *class* `pymdocs.parsers.docstring.base.Docstring` [[source]](../pymdocs/parsers/docstring/base.py#L209)

Base: `DocstringSection`

Class for python docstring

**Attributes:**

- *attributes*: List[DocstringSection], list of docstring sections
- *description*: str, docstring title



#### Methods

> **pymdocs.parsers.docstring.base.Docstring.args**(*self: Any*) -> *List[DocstringArg]* [[source]](../pymdocs/parsers/docstring/base.py#L227)

Returns list of docstring 'Args' section elements



> **pymdocs.parsers.docstring.base.Docstring.attributes**(*self: Any*) -> *List[DocstringAttribute]* [[source]](../pymdocs/parsers/docstring/base.py#L236)

Returns list of docstring 'Attributes' section elements



> **pymdocs.parsers.docstring.base.Docstring.examples**(*self: Any*) -> *List[DocstringExample]* [[source]](../pymdocs/parsers/docstring/base.py#L245)

Returns list of docstring 'Examples' section elements



> **pymdocs.parsers.docstring.base.Docstring.raises**(*self: Any*) -> *List[DocstringRaises]* [[source]](../pymdocs/parsers/docstring/base.py#L254)

Returns list of docstring 'Raises' section elements



> **pymdocs.parsers.docstring.base.Docstring.returns**(*self: Any*) -> *List[DocstringReturns]* [[source]](../pymdocs/parsers/docstring/base.py#L263)

Returns list of docstring 'Returns' section elements



> **pymdocs.parsers.docstring.base.Docstring.yields**(*self: Any*) -> *List[DocstringYiedls]* [[source]](../pymdocs/parsers/docstring/base.py#L272)

Returns list of docstring 'Yields' section elements





# <a class="anchor" id="pymdocs-formatters-class_formatter"></a>*module* pymdocs.formatters.class\_formatter

## Classes

### *class* `pymdocs.formatters.class_formatter.ClassFormatter` [[source]](../pymdocs/formatters/class_formatter.py#L9)

Base: `BaseFormatter`

Formatter for ClassDefinition objects

**Attributes:**

- *\_requires*: tuple[FormatterType, ...], data attribute,tuple of
required formatters (DOCSTRING, FUNCTION)
- *formatters*: (Dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.class\_formatter.ClassFormatter.format**(*self: Any*, *class\_def: ClassDefinition*, *doc\_path: str*, *package\_name: Optional[str]*, *module\_name: Optional[str]*) -> *Any* [[source]](../pymdocs/formatters/class_formatter.py#L25)

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

### *class* `pymdocs.formatters.markdown_constructor.MarkdownContainer` [[source]](../pymdocs/formatters/markdown_constructor.py#L8)



Base class for list of Markdown elements, also usefull for groupping
other elements

**Attributes:**

- *elemens*: List[Union[MarkdownContainer, str]], list of inner elements,
could be another MarkdownContainer or python string
- *sep*: Union[MarkdownContainer, str], elements separator, could be
another MarkdownContainer or python string

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

> **pymdocs.formatters.markdown\_constructor.MarkdownContainer.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L61)

Returns Markdown representation all inner elements,
joined by separator





### *class* `pymdocs.formatters.markdown_constructor.Quote` [[source]](../pymdocs/formatters/markdown_constructor.py#L91)

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

> **pymdocs.formatters.markdown\_constructor.Quote.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L109)

Returns markdown quoted text





### *class* `pymdocs.formatters.markdown_constructor.Link` [[source]](../pymdocs/formatters/markdown_constructor.py#L119)

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

> **pymdocs.formatters.markdown\_constructor.Link.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L146)

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

> **pymdocs.formatters.markdown\_constructor.Image.render**(*self: Any*) -> *Any* [[source]](../pymdocs/formatters/markdown_constructor.py#L173)

Returns Markdown image





### *class* `pymdocs.formatters.markdown_constructor.Paragraph` [[source]](../pymdocs/formatters/markdown_constructor.py#L178)

Base: `MarkdownContainer`

Class for Markdown paragraph element



#### Methods

> **pymdocs.formatters.markdown\_constructor.Paragraph.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L181)

Renders inner elements, with paragraph break in the end





### *class* `pymdocs.formatters.markdown_constructor.Header` [[source]](../pymdocs/formatters/markdown_constructor.py#L189)

Base: `MarkdownContainer`

Base class for Markdown header element

**Attributes:**

- *elements*: List[Union[MarkdownContainer, str]], list of inner elements
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

> **pymdocs.formatters.markdown\_constructor.Header.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L217)

Returns Markdown header with inner elelements





### *class* `pymdocs.formatters.markdown_constructor.H1` [[source]](../pymdocs/formatters/markdown_constructor.py#L226)

Base: `Header`

Class for 1 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.H2` [[source]](../pymdocs/formatters/markdown_constructor.py#L237)

Base: `Header`

Class for 2 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.H3` [[source]](../pymdocs/formatters/markdown_constructor.py#L248)

Base: `Header`

Class for 3 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.H4` [[source]](../pymdocs/formatters/markdown_constructor.py#L259)

Base: `Header`

Class for 4 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.H5` [[source]](../pymdocs/formatters/markdown_constructor.py#L270)

Base: `Header`

Class for 5 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.H6` [[source]](../pymdocs/formatters/markdown_constructor.py#L281)

Base: `Header`

Class for 6 level Markdown header



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.Bold` [[source]](../pymdocs/formatters/markdown_constructor.py#L292)

Base: `MarkdownContainer`

Class for Markdown bold element

**Examples:**

<pre>Rendering bold text

>> element = Bold(['some bold text'])
>> element.render()
**some bold text**</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.Bold.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L304)

Returns bolded inner elements





### *class* `pymdocs.formatters.markdown_constructor.Italic` [[source]](../pymdocs/formatters/markdown_constructor.py#L309)

Base: `MarkdownContainer`

Class for Markdown italic element

**Examples:**

<pre>Rendering italic text

>> element = Italic(['some italic text'])
>> element.render()
*some italic text*</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.Italic.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L321)

Returns italic inner elements





### *class* `pymdocs.formatters.markdown_constructor.BoldItalic` [[source]](../pymdocs/formatters/markdown_constructor.py#L326)

Base: `MarkdownContainer`

Class for Markdown bold italic element

**Examples:**

<pre>Rendering bold and italic text

>> element = BoldItalic(['some text'])
>> element.render()
**some text**</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.BoldItalic.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L338)

Returns bolded italic inner elements





### *class* `pymdocs.formatters.markdown_constructor.Strikethrough` [[source]](../pymdocs/formatters/markdown_constructor.py#L343)

Base: `MarkdownContainer`

Class for Markdown strikethrough element

**Examples:**

<pre>Rendering strikethrough text

>> element = Strikethrough(['some text'])
>> element.render()
~~some text~~</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.Strikethrough.render**(*self: Any*) -> *Any* [[source]](../pymdocs/formatters/markdown_constructor.py#L355)





### *class* `pymdocs.formatters.markdown_constructor.Blockquotes` [[source]](../pymdocs/formatters/markdown_constructor.py#L359)

Base: `MarkdownContainer`

Class for Markdown blockquotes element

**Examples:**

<pre>Rendering block quotes

>> element = Blockquotes(['some text'])
>> element.render()
> some text</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.Blockquotes.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L371)

Returns blockquotes with inner elements





### *class* `pymdocs.formatters.markdown_constructor.OrderedList` [[source]](../pymdocs/formatters/markdown_constructor.py#L379)

Base: `MarkdownContainer`

Class for Markdown ordered list element

**Attributes:**

- *elements*: List[Union[MarkdownContainer, str]], list of inner elements

**Examples:**

<pre>Rendering ordered list

>> element = OrderedList(['first item', 'second item', 'third item'])
>> element.render()
1. first item
2. second item
3. third item</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.OrderedList.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L399)

Returns Markdown ordered list with inner elements as items





### *class* `pymdocs.formatters.markdown_constructor.UnorderedList` [[source]](../pymdocs/formatters/markdown_constructor.py#L412)

Base: `MarkdownContainer`

Class for Markdown unordered list element

**Attributes:**

- *elements*: List[Union[MarkdownContainer, str]], list of inner elements

**Examples:**

<pre>Rendering unordered list

>> element = UnorderedList(['first item', 'second item', 'third item'])
>> element.render()
- first item
- second item
- third item</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.UnorderedList.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L429)

Returns Markdown unordered list with inner elements as items





### *class* `pymdocs.formatters.markdown_constructor.TaskItem` [[source]](../pymdocs/formatters/markdown_constructor.py#L442)

Base: `MarkdownContainer`

Class for Markdown task list item element

**Attributes:**

- *elements*: List[Union[MarkdownContainer, str]], list of inner elements
- *sep*: Union[MarkdownContainer, str], elements separator
- *is\_done*: bool, is the task done or not, False by default



#### Methods

> **pymdocs.formatters.markdown\_constructor.TaskItem.render**(*self: Any*) -> *Any* [[source]](../pymdocs/formatters/markdown_constructor.py#L461)

Returns Markdown task list item with inner elements





### *class* `pymdocs.formatters.markdown_constructor.TaskList` [[source]](../pymdocs/formatters/markdown_constructor.py#L469)

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



### *class* `pymdocs.formatters.markdown_constructor.InlineCode` [[source]](../pymdocs/formatters/markdown_constructor.py#L494)

Base: `MarkdownContainer`

Class for Markdown inline code element

**Examples:**

<pre>Rendering inline code

>> element = InlineCode(['code'])
>> element.render()
`code`</pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.InlineCode.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L506)

Returns Mrkdown inline code with inner elements





### *class* `pymdocs.formatters.markdown_constructor.Code` [[source]](../pymdocs/formatters/markdown_constructor.py#L511)

Base: `MarkdownContainer`

Class for Markdown multiline code block

**Attributes:**

- *elements*: List[Union[MarkdownContainer, str]], list of inner elements
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

> **pymdocs.formatters.markdown\_constructor.Code.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L546)

Returns markdown code block with inner elements





### *class* `pymdocs.formatters.markdown_constructor.ColumnOrientation` [[source]](../pymdocs/formatters/markdown_constructor.py#L555)

Base: `str, Enum`

Markdown table column orientation





### *class* `pymdocs.formatters.markdown_constructor.TableRow` [[source]](../pymdocs/formatters/markdown_constructor.py#L565)

Base: `MarkdownContainer`

Class for Markdown table row element

**Attributes:**

- *elements*: List[Union[MarkdownContainer, str]], table row elements

**Examples:**

<pre>Rendering table row

>> element = TableRow(['1', 'one'])
>> element.render()
1 | one</pre>



#### Methods



### *class* `pymdocs.formatters.markdown_constructor.Table` [[source]](../pymdocs/formatters/markdown_constructor.py#L584)

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

> **pymdocs.formatters.markdown\_constructor.Table.render**(*self: Any*) -> *Any* [[source]](../pymdocs/formatters/markdown_constructor.py#L625)

Returns Markdown table





### *class* `pymdocs.formatters.markdown_constructor.HTMLComment` [[source]](../pymdocs/formatters/markdown_constructor.py#L643)

Base: `MarkdownContainer`

Class for HTML comment

**Examples:**

<pre>Rendering an HTML comment (not visible in Markdown)

>> element = HTMLComment(['very usefull information'])
>> element.render()
<!--very usefull information--></pre>



#### Methods

> **pymdocs.formatters.markdown\_constructor.HTMLComment.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L655)

Returns markdown HTML comment with inner elements





### *class* `pymdocs.formatters.markdown_constructor.Raw` [[source]](../pymdocs/formatters/markdown_constructor.py#L664)

Base: `MarkdownContainer`

Class for raw text



#### Methods

> **pymdocs.formatters.markdown\_constructor.Raw.render**(*self: Any*) -> *str* [[source]](../pymdocs/formatters/markdown_constructor.py#L669)

Returns raw text





### *class* `pymdocs.formatters.markdown_constructor.HTMLAnchor` [[source]](../pymdocs/formatters/markdown_constructor.py#L678)

Base: `MarkdownContainer`

Class for html anchor



#### Methods

> **pymdocs.formatters.markdown\_constructor.HTMLAnchor.render**(*self: Any*) -> *Any* [[source]](../pymdocs/formatters/markdown_constructor.py#L686)





### *class* `pymdocs.formatters.markdown_constructor.Latex` [[source]](../pymdocs/formatters/markdown_constructor.py#L692)

Base: `MarkdownContainer`

Class for Latex formulas



#### Methods

> **pymdocs.formatters.markdown\_constructor.Latex.render**(*self: Any*) -> *Any* [[source]](../pymdocs/formatters/markdown_constructor.py#L697)





# <a class="anchor" id="pymdocs-formatters-package_formatter"></a>*module* pymdocs.formatters.package\_formatter

## Classes

### *class* `pymdocs.formatters.package_formatter.PackageFormatter` [[source]](../pymdocs/formatters/package_formatter.py#L8)

Base: `BaseFormatter`

Formatter for ModuleDefinition objects

**Attributes:**

- *\_requires*: tuple[FormatterType, ...], data attribute,tuple of
required formatters (DOCSTRING, FUNCTION, CLASS, MODULE)
- *formatters*: (dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.package\_formatter.PackageFormatter.flatten\_modules**(*self: Any*, *package\_def: PackageDefinition*, *doc\_path: str*, *prefix: str*) -> *List[Tuple[md.MarkdownContainer, md.Link]]* [[source]](../pymdocs/formatters/package_formatter.py#L26)

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



> **pymdocs.formatters.package\_formatter.PackageFormatter.format**(*self: Any*, *package\_def: PackageDefinition*, *doc\_path: str*) -> *Any* [[source]](../pymdocs/formatters/package_formatter.py#L82)

Returns Markdown element for package definition

**Args:**

- *package\_def*: PackageDefinition, python package definition
- *doc\_path*: str, path to documentation file

**Returns:**

`MarkdownContainer`: Markdown element for package





# <a class="anchor" id="pymdocs-formatters-function_formatter"></a>*module* pymdocs.formatters.function\_formatter

## Classes

### *class* `pymdocs.formatters.function_formatter.FunctionFormatter` [[source]](../pymdocs/formatters/function_formatter.py#L9)

Base: `BaseFormatter`

Formatter for FunctionDefinition objects

**Attributes:**

- *\_requires*: tuple[FormatterType, ...], data attribute,tuple of
required formatters (DOCSTRING)
- *formatters*: (Dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.function\_formatter.FunctionFormatter.format**(*self: Any*, *function\_def: FunctionDefinition*, *doc\_path: str*, *package\_name: Optional[str]*, *module\_name: Optional[str]*, *class\_name: Optional[str]*) -> *md.MarkdownContainer* [[source]](../pymdocs/formatters/function_formatter.py#L24)

Returns Markdown element for function definition

**Args:**

- *function\_def*: FunctionDefinition, python function definition
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

### *class* `pymdocs.formatters.docstring_formatter.DocstringFormatter` [[source]](../pymdocs/formatters/docstring_formatter.py#L8)

Base: `BaseFormatter`

Formatter for ClassDefinition objects

**Attributes:**

- *\_requires*: tuple[FormatterType, ...], data attribute,tuple of
required formatters
- *formatters*: (Dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.docstring\_formatter.DocstringFormatter.format**(*self: Any*, *docstring: Optional[Docstring]*) -> *Optional[md.MarkdownContainer]* [[source]](../pymdocs/formatters/docstring_formatter.py#L19)

Returns Markdown element for function definition

**Args:**

- *docstring*: Docstring, python docstring definition

**Returns:**

`(MarkdownContainer | None)`: Markdown element for docstring or None





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

> **pymdocs.formatters.common\_formatter.Formatter.format**(*self: Any*, *obj: AstWrapper*) -> *Any* [[source]](../pymdocs/formatters/common_formatter.py#L66)

Formats object tom Markdown

**Args:**

- *obj*: AstWrapper, object needed to format
- *\*\*kwargs*: additional arguments for object formatter

**Raises:**

- `ValueError`: if object formatter is not set

**Returns:**

`MarkdownContainer`: Markdown element for object





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

### *class* `pymdocs.formatters.base.FormatterType` [[source]](../pymdocs/formatters/base.py#L8)

Base: `int, Enum`

Enum for formatter types





### *class* `pymdocs.formatters.base.BaseFormatter` [[source]](../pymdocs/formatters/base.py#L23)



Base class for markdown formatters

**Attributes:**

- *\_requires*: Tuple[FormatterType, ...], data attribute,tuple of
required formatters
- *formatters*: (Dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.base.BaseFormatter.format**(*self: Any*, *obj: AstWrapper*) -> *md.MarkdownContainer* [[source]](../pymdocs/formatters/base.py#L59)

Returns markdown representation for obj



> **pymdocs.formatters.base.BaseFormatter.format\_by**(*self: Any*, *formatter\_type: FormatterType*, *obj: AstWrapper*) -> *md.MarkdownContainer* [[source]](../pymdocs/formatters/base.py#L62)

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

Base: `BaseFormatter`

Formatter for ModuleDefinition objects

**Attributes:**

- *\_requires*: tuple[FormatterType, ...], data attribute,tuple of
required formatters (DOCSTRING, FUNCTION, CLASS)
- *formatters*: (dict[FormatterType, BaseFormatter] | None), formatters
to be used inside



#### Methods

> **pymdocs.formatters.module\_formatter.ModuleFormatter.module\_link**(*module\_name: str*) -> *Any* [[source]](../pymdocs/formatters/module_formatter.py#L26)

Returns module link for Contents documentation section

**Args:**

- *module\_name*: str, module name

**Returns:**

`Link`: markdown link element



> **pymdocs.formatters.module\_formatter.ModuleFormatter.module\_anchor**(*module\_name: str*) -> *Any* [[source]](../pymdocs/formatters/module_formatter.py#L42)

Returns module anchor for Contents documentation section

**Args:**

- *module\_name*: str, module name

**Returns:**

`HTMLAnchor`: anchor for module documentation header



> **pymdocs.formatters.module\_formatter.ModuleFormatter.format**(*self: Any*, *module\_def: ModuleDefinition*, *doc\_path: str*, *package\_name: Optional[str]*) -> *Any* [[source]](../pymdocs/formatters/module_formatter.py#L56)

Returns Markdown element for module definition

**Args:**

- *module\_def*: ModuleDefinition, python module definition
- *doc\_path*: str, path to documentation file
- *package\_name*: (str | None), name of the class package

**Returns:**

`MarkdownContainer`: Markdown element for module







