def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))
