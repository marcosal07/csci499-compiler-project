class Interpreter:
    def __init__(self):
        self.symbol_table = {}

    def evaluate(self, node):

        # NUMBER
        if node.__class__.__name__ == "Number":
            return node.value

        # VARIABLE
        elif node.__class__.__name__ == "Variable":
            if node.name in self.symbol_table:
                return self.symbol_table[node.name]
            raise NameError(f"Undefined variable '{node.name}'")

        # BINARY OPERATIONS
        elif node.__class__.__name__ == "BinOp":
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            # Arithmetic
            if node.op == "PLUS":
                return left + right
            elif node.op == "MINUS":
                return left - right
            elif node.op == "MULT":
                return left * right
            elif node.op == "DIV":
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                return left // right

            # Comparisons
            elif node.op == "GT":
                return left > right
            elif node.op == "LT":
                return left < right
            elif node.op == "EQ":
                return left == right

        # ASSIGNMENT
        elif node.__class__.__name__ == "Assign":
            value = self.evaluate(node.expr)
            self.symbol_table[node.name] = value

        # PRINT
        elif node.__class__.__name__ == "Print":
            print(self.evaluate(node.expr))

        # IF STATEMENT
        elif node.__class__.__name__ == "If":
            if self.evaluate(node.condition):
                self.evaluate(node.body)

        else:
            raise Exception(f"Unknown node type: {node}")

    def execute(self, statements):
        for stmt in statements:
            self.evaluate(stmt)
