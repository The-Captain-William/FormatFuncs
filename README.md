# CAPTAIN WILLIAM'S FORMAT FUNC's

This is a collection of functions used to format string files. 
Current Functions: 
* string_format
* copy_write_maker
* push

string_format and copy_write_maker are both built around recieving 
strings without tabs or linebreaks, as from .JSON files or csv files 
and breaking them up to shape paragraphs. 

string_format and copy_write_maker can both make paragraphs. 

The difference between the two is that 
paragraph_maker adds linebreaks after every sentance, and
string_format adds linebreaks roughly at the the end of every nth 
character specified by the length parameter. 

push works in much the same way but is used for string data that is smaller, where the string_format function may
produce an index error.

This works well for GUI applications where you may have issues
where the text runs off the page. 

## How to Install:
`pip install formatfuncs-Captain-William`

### ⚠ Note: 
If you're using small strings or require short width I recommend using the push function included. 
It produces similar outputs, but as of 0.1.1 either produces a space after every line like the copywrite function, 
or no spaces at all.
## Examples of modified outputs

**Long ass sentance input**
<img src="https://github.com/The-Captain-William/FormatFuncs/blob/main/examples/long%20ass%20sentance.JPG?raw=true" width="1000" height= "45" />

**Paragraph Style with String_Format**

![](https://github.com/The-Captain-William/FormatFuncs/blob/main/examples/paragraph%20style.JPG?raw=true)

**Formatted without Spaces**

![](https://github.com/The-Captain-William/FormatFuncs/blob/main/examples/length%20formatted.JPG?raw=true)

**Copywrite Style Text**

![](https://github.com/The-Captain-William/FormatFuncs/blob/main/examples/copy-write%20style.JPG?raw=true)
