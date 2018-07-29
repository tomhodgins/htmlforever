import re # to use regex
import sys # to access cli arguments
from string import Template # to use multiline template strings

# HTML Definitions
def tag(name="div", attrs=[], content="", rhs=""):

  voidTags = ["area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"]

  def attributes(attrs):
    #needsQuotes = re.search("", attr[1])

    return "".join(map(lambda attr:
      " " + attr[0] + "='" + attr[1] + "'"
        if re.search("\"", attr[1])
        else " " + attr[0] + "=\"" + attr[1] + "\""
      if re.search("[\s\"'=<>`]", attr[1])
      else " " + attr[0] + "=" + attr[1]
      , attrs)
    )

  return (
    "<" + name + attributes(attrs) + ">\n" + content
    if (name in voidTags)
    else "<" + name + attributes(attrs) + ">" + content + "</" + name + ">\n"
  )\
  + rhs

# HTML Helpers
def data(rhs=""):

  return "data:text/html;charset=utf-8," + rhs

def doctype(rhs=""):

  return "<!DOCTYPE html>\n" + rhs

def lineBreak(rhs=""):

  return "\n" + rhs

def siblings(name="p", content=[], rhs=""):

  return "\n" + "".join(map(lambda sibling:
    tag(name, sibling[0], sibling[1])
    if isinstance(sibling, list)
    else tag(name, [], sibling)
  , content)) + rhs

def link(url="#", text="", title="", rhs=""):

  url = url or "#"
  text = text or url
  title = title or text

  return tag("a", [["href", url], ["title", title]], text) + rhs

def embed(url="#", width="560", height="315", rhs=""):

  return tag('div', [
    ['style', Template('''
      position: relative;
      width: 100%;
      padding-bottom: calc(100% / ($width / $height));
    ''').safe_substitute(width=width, height=height)]
  ],
    tag('iframe', [
      ['src', url],
      ['width', width],
      ['height', height],
      ['frameborder', "0"],
      ['style', '''
        position: absolute;
        width: 100%;
        height: 100%;
        top: 50%;
        left: 50%;
        transform: translateX(-50%) translateY(-50%);
     ''']
    ])) + rhs

# Templating Snippets
def head(title="", rhs=""):

  return doctype(
    tag("meta", [["charset", "utf-8"]],
      tag("meta", [
        ["name", "viewport"],
        ["content", "width=device-width, initial-scale=1"]
      ],
        tag("title", [], title)))) + rhs

def mixin(name="mixin", rhs=""):

  return tag("script", [], Template('''
  function $name(selector, rule) {

    return Array.from(document.querySelectorAll(selector))

      .reduce((styles, tag, count) => {

        const attr = (selector).replace(/\W/+, '')

        tag.setAttribute(`data-$name-${attr}`, count)
        styles += `[data-$name-${attr}="${count}"] { ${rule} }\\n`
        count++

        return styles

      }, '')

  }
''').safe_substitute(name=name)) + rhs

def eqcss(rhs=""):

  return tag("script", [
    ["src", "https://unpkg.com/eqcss/EQCSS.min.js"]
  ]) + rhs

def eqcssDemo(content="", rhs=""):

  return tag("style", [], "\n\n " + content + " \n\n",
    eqcss()) + rhs

def reprocss(rhs=""):

  return tag("script", [
    ["src", "https://unpkg.com/reprocss/reprocss.js"]
  ]) + rhs

def reprocssDemo(content="", rhs=""):

  return tag("style", [["process", "auto"]], "\n\n " + content + " \n\n",
    reprocss()) + rhs

def selectory(rhs=""):

  return tag("script", [["src", "https://unpkg.com/cssplus/selectory.js"]]) + rhs

def selectoryDemo(content="", rhs=""):

  return tag("style", [], "\n\n " + content + " \n\n",
           selectory()) + rhs

def jsincss(plugins=[], content="", rhs=""):

  return tag("script", [["type", "module"]],\
    "\n"\
    + "  import jsincss from 'https://unpkg.com/jsincss/index.vanilla.js'\n"\
    + "".join(map(lambda plugin:
      "  import " + plugin[1] + " from 'https://unpkg.com/jsincss-" + plugin[0] + "/index.vanilla.js'\n", plugins))
    + "\n"\
    + "  jsincss(()=>`\n"\
    + "\n"\
    + "    " + content + "\n"\
    + "\n"\
    + "  `)\n") + rhs

def todo(title="", rhs=""):

  return doctype(
    tag("meta", [["charset", "utf-8"]],
      tag("meta", [
        ["name", "viewport"],
        ["content", "width=device-width, initial-scale=1"]
      ],
        tag("link", [
          ["rel", "stylesheet"],
          ["href", "https://fonts.googleapis.com/css?family=Cormorant+Garamond|Crimson+Text"]
        ],
          tag("link", [
            ["rel", "stylesheet"],
            ["href", "https://tomhodgins.github.io/todoml/style.css"]
          ],
            tag("script", [
              ["src", "https://tomhodgins.github.io/todoml/todoml.js"]
            ], "",
              tag("title", [], title,
                tag("body", [],
                  "\n"
                  + tag("script", [["type", "text/todo"]], Template('''

  # $title

''').safe_substitute(title=title)))))))))) + rhs

# Dummy Content
def dummyHeadlines(rhs=""):

  return tag("h1", [], "I'm an H1 Headline",
    tag("h2", [], "I'm an H2 Headline",
      tag("h3", [], "I'm an H3 Headline",
        tag("h4", [], "I'm an H4 Headline",
          tag("h5", [], "I'm an H5 Headline",
            tag("h6", [], "I'm an H6 Headline")))))) + rhs

def dummyLi(rhs=""):

  return siblings("li", ["one", [[["class", "target"]], "two"], "three"]) + rhs

def dummyUl(rhs=""):

  return tag("ul", [], dummyLi()) + rhs

def dummyOl(rhs=""):

  return tag("ol", [], dummyLi()) + rhs

def lorem(rhs=""):

  return tag("p", [], "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.") + rhs

def loremIpsum(rhs=""):

  return tag("p", [], "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate.") + rhs

def loremIpsumDolor(rhs=""):

  return tag("p", [], "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.") + rhs

def dummyContent(rhs=""):

  return dummyHeadlines(
    lineBreak(
      loremIpsumDolor(
        lineBreak(
          loremIpsum(
            lineBreak(
              lorem(
                lineBreak(
                 dummyUl(
                   lineBreak(
                     dummyOl())))))))))) + rhs

def table(rhs=""):

  return tag("table", [],
    tag("thead", [],
      tag("tr", [],
        tag("th", [], "One",
        tag("th", [], "Two",
        tag("th", [], "Three")))),
          tag("tbody", [],
            tag("tr", [],
              tag("td", [], "One",
              tag("td", [], "Two",
              tag("td", [], "Three"))),
                tag("tr", [],
                  tag("td", [], "Four",
                  tag("td", [], "Five",
                  tag("td", [], "Six"))),
                    tag("tr", [],
                      tag("td", [], "Seven",
                      tag("td", [], "Eight",
                      tag("td", [], "Nine")))))),
                        tag("tfoot", [],
                          tag("tr", [],
                            tag("th", [], "One",
                            tag("th", [], "Two",
                            tag("th", [], "Three")))))))) + rhs

# CLI ability
if len(sys.argv) > 1:

  print(eval(sys.argv[1]))

# example: python3 htmlforever.py 'tag("p", [["class", "demo"]], "Demo")'
# returns: <p class="demo">Demo</p>