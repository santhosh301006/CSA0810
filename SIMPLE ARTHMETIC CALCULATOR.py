def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", add(x, y))
elif op == '-':
    print("Result:", subtract(x, y))
elif op == '*':
    print("Result:", multiply(x, y))
elif op == '/':
    print("Result:", divide(x, y))
else:
    print("Invalid operator")
