from Tokenizer import Tokenizer
from Parser import Parser
from Interpreter import Interpreter
from Compiler import Compiler
import sys

if __name__ == "__main__":
    code = input("Enter code: ")

    if not code or not code[0].isdigit() and code[0] not in "+-":
        print("Invalid code string.")
        sys.exit()

    tokens = list(Tokenizer(code))
    tree = Parser(tokens).parse()
    bytecode = list(Compiler(tree).compile())
    Interpreter(bytecode).interpret()
