// HTML Definitions
const tag = (name="div", attrs=[], content="", rhs="") => {

  const voidTags = ["area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"]

  const attributes = attrs =>
    attrs.map(
      attr => /[\s"'=<>`]/.test(attr[1])
        ? /["]/.test(attr[1])
          ? " " + attr[0] + "='" + attr[1] + "'"
          : " " + attr[0] + "=\"" + attr[1] + "\""
      : " " + attr[0] + "=" + attr[1]
    ).join("")

  return (
    voidTags.includes(name.toLowerCase())
    ? "<" + name + attributes(attrs) + ">\n" + content
    : "<" + name + attributes(attrs) + ">" + content + "</" + name + ">\n"
  ) + rhs

}

// HTML Helpers
const data = (rhs="") => 
  "data:text/html;charset=utf-8," + rhs

const doctype = (rhs="") =>
  "<!DOCTYPE html>\n" + rhs

const lineBreak = (rhs="") =>
  "\n" + rhs

const siblings = (name="p", content=[], rhs="") =>
  lineBreak(
    content.map(
      sibling => Array.isArray(sibling)
        ? tag(name, sibling[0], sibling[1])
        : tag(name, [], sibling)
    ).join("")
  ) + rhs

const link = (url="#", text=url, title=text, rhs="") =>
  tag("a", [["href", url], ["title", title]], text) + rhs

const embed = (url="#", width="560", height="315", rhs="") =>
  tag("div", [
    ["style", `
      position: relative;
      width: 100%;
      padding-bottom: calc(100% / (${width} / ${height}));
    `]
  ],
    tag("iframe", [
      ["src", url],
      ["width", width],
      ["height", height],
      ["frameborder", "0"],
      ["style", `
        position: absolute;
        width: 100%;
        height: 100%;
        top: 50%;
        left: 50%;
        transform: translateX(-50%) translateY(-50%);
      `]
    ])) + rhs

// Templating Snippets
const head = (title="", rhs="") =>
  doctype(
    tag("meta", [["charset", "utf-8"]],
      tag("meta", [
        ["name", "viewport"],
        ["content", "width=device-width, initial-scale=1"]
      ],
        tag("title", [], title)
      )
    )
  ) + rhs

const mixin = (name="mixin", rhs="") =>
  tag("script", [], `
  function ${name}(selector, rule) {

    return Array.from(document.querySelectorAll(selector))

      .reduce((styles, tag, count) => {

        const attr = (selector).replace(/\\W/+, '')

        tag.setAttribute(\`data-${name}-$\{attr}\`, count)
        styles += \`[data-${name}-$\{attr}="$\{count}"] { $\{rule} }\\n\`

        return styles

      }, '')

  }
`) + rhs

const eqcss = (rhs="") =>
  tag("script", [["src", "https://unpkg.com/eqcss/EQCSS.min.js"]]) + rhs

const eqcssDemo = (content="", rhs="") =>
  tag("style", [], "\n\n " + content + " \n\n",
    eqcss()
  ) + rhs

const reprocss = (rhs="") =>
  tag("script", [["src", "https://unpkg.com/reprocss/reprocss.js"]]) + rhs

const reprocssDemo = (content="", rhs="") =>
  tag("style", [["process", "auto"]], "\n\n " + content + " \n\n",
    reprocss()
  ) + rhs

const selectory = (rhs="") =>
  tag("script", [["src", "https://unpkg.com/cssplus/selectory.js"]]) + rhs

const selectoryDemo = (content="", rhs="") =>
  tag("style",  [], "\n\n " + content + " \n\n",
    selectory()
  ) + rhs

const jsincss = (plugins=[], content="", rhs="") =>
  tag("script", [["type", "module"]], `
  import jsincss from 'https://unpkg.com/jsincss/index.vanilla.js'
${plugins.map(plugin => `  import ${plugin[1]} from 'https://unpkg.com/jsincss-${plugin[0]}/index.vanilla.js'\n`).join("")}
  jsincss(()=>\`

    ${content}

  \`)
`)
+ rhs

const todo = (title="", rhs="") =>
  doctype(
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
                  + tag("script", [["type", "text/todo"]], `

  # ${title}

`))))))))) + rhs

// Dummy Content
const dummyHeadlines = (rhs="") =>
  tag("h1", [], "I'm an H1 Headline",
    tag("h2", [], "I'm an H2 Headline",
      tag("h3", [], "I'm an H3 Headline",
        tag("h4", [], "I'm an H4 Headline",
          tag("h5", [], "I'm an H5 Headline",
            tag("h6", [], "I'm an H6 Headline")))))) + rhs

const dummyLi = (rhs="") =>
  siblings("li", ["one", [[["class", "target"]], "two"], "three"]) + rhs

const dummyUl = (rhs="") =>
  tag("ul", [], dummyLi()) + rhs

const dummyOl = (rhs="") =>
  tag("ol", [], dummyLi()) + rhs

const lorem = (rhs="") =>
  tag("p", [], "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.") + rhs

const loremIpsum = (rhs="") =>
  tag("p", [], "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate.") + rhs

const loremIpsumDolor = (rhs="") =>
  tag("p", [], "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.") + rhs

const dummyContent = (rhs="") =>
  dummyHeadlines(
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

const table = (rhs="") =>
  tag("table", [],
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

// CLI ability
if (process.argv[2])
  console.log(eval(process.argv[2]))

// example: node htmlforever.js 'tag("p", [["class", "demo"]], "Demo")'
// returns: <p class=demo>Demo</p>