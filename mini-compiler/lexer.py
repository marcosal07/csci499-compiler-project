import re

# Token definitions
TOKEN_SPEC = [
    ("NUMBER", r"\d+"),
    ("ID", r"[A-Za-z_]\w*"),
    ("EQ", r"=="),
    ("ASSIGN", r"="),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MULT", r"\*"),
    ("DIV", r"/"),
    ("GT", r">"),
    ("LT", r"<"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("NEWLINE", r"\r?\n"),   # handles Windows and Unix line endings
    ("SKIP", r"[ \t]+"),
   
]

# Build combined regex
TOKEN_REGEX = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)

def tokenize(code):
    tokens = []

    for match in re.finditer(TOKEN_REGEX, code):
        kind = match.lastgroup
        value = match.group()

        # Convert numbers
        if kind == "NUMBER":
            value = int(value)

        # Ignore whitespace and newline tokens completely
        if kind not in ("SKIP", "NEWLINE"):
            tokens.append((kind, value))

    return tokens
