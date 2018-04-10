# htmlforever

**LISP-style HTML helper functions**

## About

These scripts are a set of string combinators written in a [Continuation-Passing style](https://en.wikipedia.org/wiki/Continuation-passing_style) in JS, Python, and Ruby that encapsulate the composition of HTML documents and allow you to do two things:

- define high-level abstractions working with HTML as functions in code
- generate HTML documents by evaluating documents described in [Symbolic Expressions](https://en.wikipedia.org/wiki/S-expression)

## Symbolic Expression Data Format

The data format used for describing HTML with these helper functions assumes that every helper function is written in a Continuation-Passing style, that means it accepts an additional "right-hand side" argument in addition to any other arguments it may require, and passes through anything on the right-hand side as it finds it.

Because of this, we can nest the calls to our helper functions as deeply as we like and it will begin evaluating at the deepest level of nesting and work its way outward. Here's an example of an S-Expression that expands to be an HTML document with some dummy content, a JavaScript plugin, and sample code for that plugin to run:

```js
(head("JSinCSS plugin demo",
  tag("div", [], "Demo",
    jsincss(
      [["element-query", "eq"]],
      "\$\{eq('div', {minWidth: 1000}, ':self {background: lime}')}"))))
```

This is a little more free-form than something like JSON, and it allows us to combine the output of our helper functions (and the arguments we give them) in a very flexible way. The added bonus is that when written inside of certain formatting constraints, this data can be read by many different programming languages: JavaScript, Python, Ruby, PHP, Perl, Swift, and more!

Here are the rules for formatting S-Expressions for use with `htmlforever`:

- use unquoted names to call functions
- surround arguments with rounded parentheses `()`
- surround lists with square brackets `[]`
- surround strings with `"double quotes"`
- separate arguments and strings with a comma `,`
- line breaks allowed (but not required) after any open paranthesis `(` or comma `,`
- optionally surround the entire expression with parentheses `()`

You'll notice that some of the existing helper functions included with the library make heavy use of these S-Expressions themselves for structuring data and act as helpful abstractions over the underlying HTML that they represent.

For more examples of HTML described in this S-Expression format, check out the `.sexp` files in the [tests/](tests/) folder.

## Usage

The simplest way to use `htmlforever` is to run either the JavaScript, Python, or Ruby files with the data you wish to evaluate quoted as the command-line argument given to the program. Here is how you would evaluate `tag("div", [], "demo")` and turn it into the HTML `<div>demo</div>` in JavaScript, Python, and Ruby:

### Node.js

```bash
node htmlforever.js 'tag("div", [], "demo")'
```

### Python

```bash
python3 htmlforever.py 'tag("div", [], "demo")'
```

### Ruby

```bash
ruby htmlforever.rb 'tag("div", [], "demo")'
```

### Installation

Alternatively, you can copy one of these scripts to a folder (I created a hidden folder in my home directory called `~/.scripts` for this) and to define aliases in your shell that can make running these scripts with command-line input or the output of a file.

I use [Fish shell](https://fishshell.com/) to the syntax of my helper functions is a little different than bash, but it should be equally easy to define these helper functions for any shell you use:

```sh
# html from argument
function htmli
  node ~/.scripts/htmlforever.js $argv
end

# html from .sexp file
function htmlf
  node ~/.scripts/htmlforever.js (echo (cat $argv))
end
```

In this case I'm using `node` to run the JavaScript version of the file. I can now evaluate command-line input from anywhere with a command like:

```sh
htmli 'tag("div", [], "demo")'
```

Or evaluate an S-Expression saved in a file like `example.sexp` with a command like:

```sh
htmlf example.sexp
```