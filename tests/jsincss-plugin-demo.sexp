(head("JSinCSS plugin demo",
  tag("div", [], "Demo",
    jsincss(
      [["element-query", "eq"]],
      "\$\{eq('div', {minWidth: 1000}, ':self {background: lime}')}"))))
