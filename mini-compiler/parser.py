from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, token_type):
        token = self.current()
        if token and token[0] == token_type:
            self.pos += 1
            return token
        raise SyntaxError(
            f"Syntax Error: Expected {token_type}, got {token}"
        )

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self.statement())
        return statements

    def statement(self):
        token = self.current()

        # IF statement
        if token[0] == "ID" and token[1] == "if":
            self.eat("ID")
            condition = self.expr()
            body = self.statement()
            return If(condition, body)

        # PRINT statement
        if token[0] == "ID" and token[1] == "print":
            self.eat("ID")
            self.eat("LPAREN")
            expr = self.expr()
            self.eat("RPAREN")
            return Print(expr)

        # ASSIGNMENT
        name = self.eat("ID")[1]
        self.eat("ASSIGN")
        expr = self.expr()
        return Assign(name, expr)

    def expr(self):
        node = self.term()

        # Arithmetic + -
        while self.current() and self.current()[0] in ("PLUS", "MINUS"):
            op = self.eat(self.current()[0])[0]
            node = BinOp(node, op, self.term())

        # Comparison operators
        if self.current() and self.current()[0] in ("GT", "LT", "EQ"):
            op = self.eat(self.current()[0])[0]
            node = BinOp(node, op, self.term())

        return node

    def term(self):
        node = self.factor()

        while self.current() and self.current()[0] in ("MULT", "DIV"):
            op = self.eat(self.current()[0])[0]
            node = BinOp(node, op, self.factor())

        return node

    def factor(self):
        token = self.current()

        if token[0] == "NUMBER":
            return Number(self.eat("NUMBER")[1])

        elif token[0] == "ID":
            return Variable(self.eat("ID")[1])

        elif token[0] == "LPAREN":
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node

        raise SyntaxError("Invalid expression")
