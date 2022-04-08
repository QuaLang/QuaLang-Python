from sys import stdout

# Keywords
KW_print = "log"
KW_print2 = "print"
KW_if = "if"

KW_let = "define"
KW_let2 = "public"
KW_let3 = "assign"
KW_assign = "value"
KW_assign2 = "set"
KW_assign3 = "equals"
KW_import1 = "include"
KW_import2 = "import"
KW_def = "function"
KW_def2 = "static"
KW_return1 = "return"
KW_return2 = "data"
KW_try = "execute"
KW_try2 = "try"
KW_except = "except"
KW_main = "main"
KW_end = "end"
KW_end2 = "exit"

KW_break = "breaker"
KW_break2 = "break"
KW_continue = "constant"
KW_continue2 = "continue"
KW_endless_loop = "forever"
KW_endless_loop2 = "repeat"
KW_while_loop = "while"

KW_less_than_OP = "islessthan"
KW_greater_than_OP = "isgreaterthan"
KW_greater_or_equals_OP = "isgreaterthanorequalto"
KW_less_or_equals_OP = "islessthanorequalto"
KW_is_not_OP = "isNot"
KW_equals_OP = "is"

KW_PY = "python:"

keywords = [
    KW_print,
    KW_if,
    KW_let,
    KW_let2,
    KW_let3,
    KW_assign,
    KW_assign2,
    KW_assign3,
    KW_import1,
    KW_import2,
    KW_def,
    KW_def2,
    KW_return1,
    KW_return2,
    KW_try,
    KW_try2,
    KW_except,
    KW_main,
    KW_end,
    KW_end2,
    KW_break,
    KW_break2,
    KW_continue,
    KW_continue2,
    KW_endless_loop,
    KW_endless_loop2,
    KW_while_loop,
    KW_less_than_OP,
    KW_greater_than_OP,
    KW_greater_or_equals_OP,
    KW_less_or_equals_OP,
    KW_is_not_OP,
    KW_equals_OP,
    KW_PY,
]

INDENT_KW = [
    KW_if,
    KW_def,
    KW_try,
    KW_try2,
    KW_except,
    KW_while_loop,
    KW_endless_loop,
    KW_endless_loop2,
]


# Tokens that the interpreter will totally ignore
ignore_tokens = {"~", "'", "#"}

# Characters in numbers
digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}

# Separators are used in tokenization
separators = {
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    ",",
    "\n",
    " ",
    "+",
    "-",
    "*",
    "/",
    "%",
    "^",
    "=",
}

# Operators
operators = {
    "+",
    "-",
    "*",
    "/",
    "%",
    "^",
    "=",
    "[",
    "]",
    "(",
    ")",
    "{",
    "}",
    ",",
    ">",
    "<",
    "<=",
    ">=",
    "!=",
    "is",
    "isNot",
}
OP_build_in_functions = {"to_string", "to_int", "to_float", "length"}


def join_list(l):
    return "".join(map(str, l))
