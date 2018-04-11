# ------------------------------------------------------------------------------
# Reference for some palette items:
#
#  "namespace" : "import", "from", "using"
#  "operator"  : "+", "-", "=" etc.
#                NOTE: Does not include ".", which is assigned the type "source"
#  "argument"  : Function arguments
#  "builtin"   : "range", "dict", "set", "list", etc.
#  "pseudo"    : "None", "True", "False"
#                NOTE: Does not include "self", which is assigned the
#                type "source"
#  "dunder"    : Class method names of the form __<name>__ within
#               a class definition
#  "exception" : Exception names
#  "keyword"   : All keywords except those specifically assigned to "keyword2"
#                ("from", "and", "break", "is", "try", "pass", etc.)
#  "keyword2"  : "class", "def", "exec", "lambda", "print"
# ------------------------------------------------------------------------------

palette.update({
    # UI
    "header": ("black", "light blue", "standout"),
    "focused sidebar": ("yellow", "light blue", "standout"),
    "group head": ("black", "light blue"),
    "background": ("black", "light blue"),
    "label": ("black", "light blue"),
    "value": ("white", "dark blue"),
    "fixed value": ("black", "light blue"),

    "variables": ("light blue", "default"),

    "var label": ("dark blue", "default"),
    "var value": ("light blue", "default"),

    "focused var label": ("white", "dark blue"),
    "focused var value": ("black", "dark blue"),

    "highlighted var label": ("white", "light green"),
    "highlighted var value": ("white", "light green"),
    "focused highlighted var label": ("white", "light green"),
    "focused highlighted var value": ("white", "light green"),

    "stack": ("light blue", "default"),

    "frame name": ("dark blue", "default"),
    "frame class": ("light blue", "default"),
    "frame location": ("light green", "default"),

    "focused frame name": ("white", "dark blue"),
    "focused frame class": ("black", "dark blue"),
    "focused frame location": ("dark gray", "dark blue"),

    "focused current frame name": ("white", "light green"),
    "focused current frame class": ("black", "light green"),
    "focused current frame location": ("dark gray", "light green"),

    "current frame name": ("white", "light green"),
    "current frame class": ("black", "light green"),
    "current frame location": ("dark gray", "light green"),

    # breakpoints
    "breakpoint": ("light blue", "default"),
    "disabled breakpoint": ("light gray", "default"),
    "focused breakpoint": ("white", "light green"),
    "focused disabled breakpoint": ("light gray", "light green"),
    "current breakpoint": ("white", "dark blue"),
    "disabled current breakpoint": ("light gray", "dark blue"),
    "focused current breakpoint": ("white", "light green"),
    "focused disabled current breakpoint": ("light gray", "light green"),

    # source
    "breakpoint source": ("light blue", "black"),
    "current breakpoint source": ("black", "light green"),
    "breakpoint focused source": ("dark gray", "dark blue"),
    "current breakpoint focused source": ("black", "light green"),
    "breakpoint marker": ("dark red", "default"),

    "search box": ("default", "default"),

    "source": ("light blue", "default"),
    "current source": ("light gray", "light blue"),
    "current focused source": ("light gray", "light blue"),

    "focused source": ("dark gray", "dark blue"),

    "current highlighted source": ("black", "dark cyan"),
    "highlighted source": ("light blue", "black"),

    "line number": ("light blue", "default"),
    "keyword": ("dark green", "default"),
    "name": ("light blue", "default"),
    "literal": ("dark cyan", "default"),
    "string": ("dark cyan", "default"),
    "doublestring": ("dark cyan", "default"),
    "singlestring": ("light blue", "default"),
    "docstring": ("dark cyan", "default"),
    "backtick": ("light green", "default"),
    "punctuation": ("light blue", "default"),
    "comment": ("light green", "default"),
    "classname": ("dark blue", "default"),
    "funcname": ("dark blue", "default"),

    # shell

    "command line edit": ("light blue", "default"),
    "command line prompt": ("light blue", "default"),

    "command line output": ("light blue", "default"),
    "command line input": ("light blue", "default"),
    "command line error": ("dark red", "default"),

    "focused command line output": ("black", "light green"),
    "focused command line input": ("black", "light green"),
    "focused command line error": ("dark red", "light blue"),

    "command line clear button": ("light blue", "default"),
    "command line focused button": ("black", "light blue"),
})
