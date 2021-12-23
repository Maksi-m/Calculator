a = int(input("Lead the first number: "))
c = input('Enter a sign: ')
b = int(input("Lead the second number: "))
if c == ("+"):
    def f(x, y):
        return x + y
elif c == ("-"):
    def f(x, y):
        return x - y
elif c == ("*"):
    def f(x, y):
        return x * y
elif c == ("/"):
    def f(x, y):
        return x / y
elif c == ("**"):
    def f(x, y):
        return x ** y