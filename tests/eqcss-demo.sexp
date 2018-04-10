(head("EQCSS Demo",
  lineBreak(
    tag("div", [], "I am a DIV",
      lineBreak(
        eqcssDemo("
@element div and (min-width: 500px;) {\n
   :self {\n
      background: lime;\n
   }\n
 }"))))))