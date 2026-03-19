from lexer import tokenize
from parser import Parser
from interpreter import Interpreter

def run_file(filename):
    with open(filename, "r") as f:
        source_code = f.read()

    tokens = tokenize(source_code)

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter()
    interpreter.execute(ast)


if __name__ == "__main__":
    run_file("program.txt")
