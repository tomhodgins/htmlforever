import sys
from string import Template

# HTML Definitions
def doctype(rhs=""):

  return "<!DOCTYPE html>\n"\
         + rhs

def tag(name="div", attrs=[], content="", rhs=""):

  voidTags = ["area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"]

  def attributes(attrs):

    return "".join(map(lambda attr:
             " " + attr[0] + "=\"" + attr[1] + "\"", attrs
           ))

  return (
           "<" + name + attributes(attrs) + ">\n" + content
           if (name in voidTags)
           else "<" + name + attributes(attrs) + ">" + content + "</" + name + ">\n"
         )\
         + rhs

def lineBreak(rhs=""):

  return "\n"\
         + rhs

# HTML Helpers
def siblings(name="p", content=[], rhs=""):

  return "\n"\
         + "".join(map(lambda sibling:
           tag(name, sibling[0], sibling[1])
           if isinstance(sibling, list)
           else tag(name, [], sibling)
         , content))\
         + rhs

def link(url="#", text="", title="", rhs=""):

  url = url or "#"
  text = text or url
  title = title or text

  return tag("a", [["url", url], ["title", title]], text)\
         + rhs

def embed(url="#", width="560", height="315", rhs=""):

  return tag('div', [
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
          '''],
         ],
           tag('iframe', [
             ['style', Template('''
               position: relative;
               width: 100%;
               padding-bottom: calc(100% / ($width / $height));
             ''').safe_substitute(width=width, height=height)]
           ]))\
         + rhs

# Templating Snippets
def defaultHead(title="", rhs=""):

  return doctype(
           tag("meta", [["charset", "utf-8"]],
             tag("meta", [
               ["name", "viewport"],
               ["content", "width=device-width, initial-scale=1"]
             ],
               tag("title", [], title))))\
         + rhs

def mixin(name="mixin", rhs=""):

  return tag("script", [], Template('''
  function $name(selector, rule) {

    let styles = ''
    let count = 0

    document.querySelectorAll(selector).forEach(tag => {

      const attr = selector.replace(/\W/+, '')

      styles += `[data-$name-${attr}='${count}'] { ${rule} }\\n`
      tag.setAttribute(`data-$name-${attr}`, count)
      count++

    })

    return styles

  }
''').safe_substitute(name=name))\
+ rhs

def eqcss(rhs=""):

  return tag("script", [
           ["src", "https://elementqueries.com/EQCSS.js"]
         ])\
         + rhs

def eqcssDemo(rhs=""):

  return tag("style", [], "\n\n  \n\n",
           eqcss())\
         + rhs

def reprocss(rhs=""):

  return tag("script", [
           ["src", "https://unpkg.com/reprocss/reprocss.js"]
         ])\
         + rhs

def reprocssDemo(rhs=""):

  return tag("style", [["process", "auto"]], "\n\n  \n\n",
           reprocss())\
         + rhs

def selectory(rhs=""):

  return tag("script", [["src", "https://unpkg.com/cssplus/selectory.js"]])\
         + rhs

def selectoryDemo(rhs=""):

  return tag("style", [], "\n\n  \n\n",
           selectory())\
         + rhs

def jsincss(plugins=[], content="", rhs=""):

  return tag("script", [["type", "module"]],\
    "\n"\
    + "  import jsincss from 'https://unpkg.com/jsincss/index.js'\n"\
    + "".join(map(lambda plugin:
      "  import " + plugin[1] + " from 'https://unpkg.com/jsincss-" + plugin[0] + "/index.js'\n", plugins))
    + "\n"\
    + "  jsincss(()=>`\n"\
    + "\n"\
    + "    " + content + "\n"\
    + "\n"\
    + "  `)\n")\
    + rhs

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

''').safe_substitute(title=title))))))))))\
+ rhs

# Dummy Content
def dummyHeadlines(rhs=""):

  return tag("h1", [], "I'm an H1 Headline",
           tag("h2", [], "I'm an H2 Headline",
             tag("h3", [], "I'm an H3 Headline",
               tag("h4", [], "I'm an H4 Headline",
                 tag("h5", [], "I'm an H5 Headline",
                   tag("h6", [], "I'm an H6 Headline"))))))\
         + rhs

def dummyLi(rhs=""):

  return siblings("li", ["one", [[["class", "target"]], "two"], "three"])\
         + rhs

def dummyUl(rhs=""):

  return tag("ul", [], dummyLi())\
         + rhs

def dummyOl(rhs=""):

  return tag("ol", [], dummyLi())\
         + rhs

def lorem(rhs=""):

  return tag("p", [], "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")\
         + rhs

def loremIpsum(rhs=""):

  return tag("p", [], "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate.")\
         + rhs

def loremIpsumDolor(rhs=""):

  return tag("p", [], "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")\
         + rhs

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
                            dummyOl()))))))))))\
         + rhs

# CLI ability
if len(sys.argv) > 1:

  print(eval(sys.argv[1]))

# example: python3 htmlforever.py 'tag("p", [["class", "demo"]], "Demo")'
# returns: <p class="demo">Demo</p>