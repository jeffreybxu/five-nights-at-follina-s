from yattag import Doc, indent
doc, tag, text = Doc().tagtext()

doc.asis('<!doctype html>')
doc.asis('<html lang="en">')
with tag('html'):
    with tag('body'):
        with tag('script'):
            for i in range(1,70):
                doc.nl()
                doc.asis('//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA should be repeated >60 times')
            doc.nl()
            doc.asis('location.href = ')
            doc.asis(';')
result = indent(doc.getvalue(), indent_text = True)
with open('test.html', "w") as file:
    file.write(result)