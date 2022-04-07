from time import time

start = time()  # Set and start a timer

from sys import stdout
from traceback import format_exc
from argparse import ArgumentParser


def main():

    arg_parser = ArgumentParser()
    arg_parser.add_argument("file", nargs="?", default="store.qua")
    arg_parser.add_argument("-intpr", action="store_true")
    arg_parser.add_argument("--time", action="store_true")
    args = arg_parser.parse_args()

    if args.file:
        from os.path import exists

        if args.intpr:
            from interpreter import run_in_interpreter

            run_in_interpreter(args.file)

        else:
            try:
                from QuaPy import run_in_py

                exec(run_in_py(args.file), globals(), globals())
            except Exception:
                error_msg = format_exc().split('File "<string>",')[-1]
                stdout.write(f"Exception in{error_msg}")

    if args.time:
        stdout.write(f"\nExecution Time: [{time() - start}] sec.\n")


if __name__ == "__main__":
    main()
