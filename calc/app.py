from flask import Flask, request

app = Flask(__name__)

# Part 1
@app.route('/add')
def add():
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{a + b}"

@app.route('/sub')
def sub():
    """Substract b from a."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{b - a}"

@app.route('/mult')
def mult():
    """Multiply a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{a * b}"

@app.route('/div')
def div():
    """Divide a by b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{a / b}"

# Further Study
"""Basic math operations."""
def add(a, b):
    """Add a and b."""
    return a + b

def sub(a, b):
    """Substract b from a."""
    return a - b

def mult(a, b):
    """Multiply a and b."""
    return a * b

def div(a, b):
    """Divide a by b."""
    return a / b


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def do_math(operation):
    """Do a math operation"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = OPERATIONS[operation](a, b)
    return str(result)


