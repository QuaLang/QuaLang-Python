from Lexer import *

# Keywords can execute outside main function
kw_exe_outside_main = {KW_main, KW_def, KW_import1}

variables = []
functions = []

current_line = 0


class Token:
    def __init__(self, tokens):
        self.t_values = []
        self.last_kw = ""

        for tok in tokens:
            if tok:
                self.__make_token(tok)

    def __make_token(self, tok):
        global variables, functions

        if tok in keywords:
            if tok == "is":
                self.t_values.append("==")
            elif tok == "isnot":
                self.t_values.append("!=")
            elif tok == "isgreaterthan":
                self.t_values.append(">")
            elif tok == "islessthan":
                self.t_values.append("<")
            elif tok == "isgreaterthanorequalto":
                self.t_values.append(">=")
            elif tok == "islessthanorequalto":
                self.t_values.append("<=")
            else:
                self.t_values.append(tok)

            self.last_kw = tok

        elif tok in OP_build_in_functions:
            if tok == "length":
                self.t_values.append("len")
            if tok == "to_string":
                self.t_values.append("str")
            if tok == "to_int":
                self.t_values.append("int")
            if tok == "to_float":
                self.t_values.append("float")

        # Variables
        elif self.last_kw == KW_let:
            variables.append(tok)
            self.t_values.append(tok)
        # Functions
        elif self.last_kw == KW_def:
            functions.append(tok)
            self.t_values.append(tok)
        elif self.last_kw == KW_let2:
            variables.append(tok)
            self.t_values.append(tok)
        else:
            self.t_values.append(tok)


class TranslateToPython:
    def __init__(self):
        # tokens
        self.values = []
        self.is_main = False
        self.is_function = False
        self.indent_count = 0
        self.py_code = ""  # Python source code, translated from RickRoll source code

    def translate(self, values):
        self.values = values
        # if there is no code in the current line of code
        if not self.values:
            self.write("")
            return
        if not (self.values[0] in keywords or self.values[0] in functions):
            stdout.write(
                f"Exception in line {current_line}: [{self.values[0]}] is neither a keyword nor function\n"
            )
            return

        if (
            self.is_main
            or (self.is_main == False and self.values[0] in kw_exe_outside_main)
            or self.is_function
        ):
            # Convert Rickroll code to Python
            self.convert(kw=self.values[0])

        else:
            stdout.write(
                f"Exception in line {current_line}: [{self.values[0]}] can not be executed outside the main method\n"
            )

    def convert(self, kw):

        if kw in functions:
            self.write(join_list(self.values))

        elif kw == KW_main:
            self.write('if __name__ == "__main__":')

            self.is_main = True
            self.indent_count += 1

        elif self.indent_count == 0:
            self.is_main = False
            self.is_function = False

        elif kw == KW_print:
            """
            print EXPR
            """

            EXPR = join_list(self.values[1:])
            self.write(f'print({EXPR}, end="")')

        elif kw == KW_print2:
            """
            print EXPR
            """

            EXPR = join_list(self.values[1:])
            self.write(f'print({EXPR}, end="")')

        elif kw == KW_let:
            #print(self.values)
            ID = 0
            EXPR = 0
            if self.values[2] == "value":
              ID = join_list(
                self.values[
                  self.values.index(KW_let) + 1 : self.values.index(KW_assign)
                ]
              )
              EXPR = join_list(self.values[self.values.index(KW_assign) + 1 :])

            
            elif self.values[2] == "set": 
              ID = join_list(
                self.values[
                  self.values.index(KW_let) + 1 : self.values.index(KW_assign2)
                ]
              )
              EXPR = join_list(self.values[self.values.index(KW_assign2) + 1 :])
            elif self.values[2] == "assign": 
              ID = join_list(
                self.values[
                  self.values.index(KW_let) + 1 : self.values.index(KW_assign3)
                  ]
                )
              EXPR = join_list(self.values[self.values.index(KW_assign3) + 1 :])
            #print(ID)
            #print(EXPR)
            #print(self.values)
            self.write(f"{ID} = {EXPR}")
        elif kw == KW_let3:
            #print(self.values)
            ID = 0
            EXPR = 0
            if self.values[2] == "value":
              ID = join_list(
                self.values[
                  self.values.index(KW_let3) + 1 : self.values.index(KW_assign)
                ]
              )
              EXPR = join_list(self.values[self.values.index(KW_assign) + 1 :])

            
            elif self.values[2] == "set": 
              ID = join_list(
                self.values[
                  self.values.index(KW_let3) + 1 : self.values.index(KW_assign2)
                ]
              )
              EXPR = join_list(self.values[self.values.index(KW_assign2) + 1 :])
            elif self.values[2] == "assign": 
              ID = join_list(
                self.values[
                  self.values.index(KW_let3) + 1 : self.values.index(KW_assign3)
                  ]
                )
              EXPR = join_list(self.values[self.values.index(KW_assign3) + 1 :])
            print(ID)
            print(EXPR)
            print(self.values)
            self.write(f"{ID} = {EXPR}")
          
        elif kw == KW_let2:
            #print(self.values[2])
            ID = 0
            EXPR = 0
            if self.values[2] == "value":
              ID = join_list(
                self.values[
                  self.values.index(KW_let2) + 1 : self.values.index(KW_assign)
                ]
              )
              EXPR = join_list(self.values[self.values.index(KW_assign) + 1 :])

            
            elif self.values[2] == "set": 
              ID = join_list(
                self.values[
                  self.values.index(KW_let2) + 1 : self.values.index(KW_assign2)
                ]
              )
              EXPR = join_list(self.values[self.values.index(KW_assign2) + 1 :])
            elif self.values[2] == "assign": 
              ID = join_list(
                self.values[
                  self.values.index(KW_let2) + 1 : self.values.index(KW_assign3)
                ]
              )
              EXPR = join_list(self.values[self.values.index(KW_assign3) + 1 :])
            print(ID)
            print(EXPR)
            self.write(f"{ID} = {EXPR}")

        elif kw == KW_if:
            """
            if CONDI
            """

            CONDI = join_list(self.values[1:])
            self.write(f"if {CONDI}:")
            self.indent_count += 1

        elif kw == KW_try:
            self.write("try:")
            self.indent_count += 1

        elif kw == KW_try2:
            self.write("try:")
            self.indent_count += 1

        elif kw == KW_except:
            self.write("except:")
            self.indent_count += 1

        elif kw == KW_endless_loop:
            self.write("while True:")
            self.indent_count += 1

        elif kw == KW_endless_loop2:
            self.write("while True:")
            self.indent_count += 1

        elif kw == KW_while_loop:
            """
            while1 CONDI
            """

            CONDI = join_list(self.values[1:])
            self.write(f"while {CONDI}:")
            self.indent_count += 1

        elif kw == KW_break:
            self.write("break")

        elif kw == KW_break2:
            self.write("break")

        elif kw == KW_continue:
            self.write("continue")

        elif kw == KW_continue2:
            self.write("continue")

        elif kw == KW_def:
            """
            def ID ARGS
            """
            ID = self.values[1]
            if self.values[2] == "(":
              ARGS = join_list(self.values[3:-1])
              ID = self.values[1]
              self.write(f"def {ID} ({ARGS}):")

            else:
              ARGS = join_list(self.values[2:])
              ID = self.values[1]
              self.write(f"def {ID} ({ARGS}):")
            self.is_function = True
            self.indent_count += 1

        elif kw == KW_def2:
            """
            def ID ARGS
            """
            ID = self.values[1]
            if self.values[2] == "(":
              ARGS = join_list(self.values[3:-1])
              ID = self.values[1]
              self.write(f"def {ID} ({ARGS}):")

            else:
              ARGS = join_list(self.values[2:])
              ID = self.values[1]
              self.write(f"def {ID} ({ARGS}):")
              
        elif kw == KW_return1:
            """
            return1 EXPR return2
            """
            EXPR = join_list(self.values[1:])
            self.write(f"return {EXPR}")

        elif kw == KW_end or KW_end2:
            self.write("pass")
            self.indent_count -= 1

        elif kw == KW_import1:
            """
            import1 lib_name import2
            """
            self.write(f"import {self.values[1]}")

        elif kw == KW_import2:
            """
            import1 lib_name import2
            """
            self.write(f"import {self.values[1]}")

        elif kw == KW_PY:
            self.write(join_list(self.values[1:]))

    def write(self, stmt):
        self.py_code += f"{'  ' * self.indent_count + stmt}\n"


def run_in_py(src_file_name):
    global current_line

    transpiler = TranslateToPython()

    with open(src_file_name, mode="r", encoding="utf-8") as src:

        content = src.readlines()
        content[-1] += "\n"

        for statement in content:  # "statement" is a line of code the in source code
            current_line += 1

            token = Token(lexicalize(statement))
            transpiler.translate(values=token.t_values)

    return transpiler.py_code
