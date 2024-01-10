def choice():
    d = ("+", "-", "*", "/")
    while True:
        try:
            c = input("Enter an operation (+, -, *, /): ")
            if c not in d:
                raise Exception
        except Exception:
            print("Invalid operation! Please enter one of +, -, *, /")
        else:
            return c
def get_numbers():
    while True:
        try:
            y = float(input("Enter the number: "))
            return y
        except ValueError:
            print("Please enter valid numbers (integer or float)")
def calculate():
    c = choice()
    x = get_numbers()
    y = get_numbers()
    if c == "+":
        print(x + y)
    elif c == "-":
        print(x - y)
    elif c == "*":
        print(x * y)
    elif c == "/":
        try:
            if y == 0:
                raise ZeroDivisionError
            return x / y
        except ZeroDivisionError:
            print("Tivy chi karox bajanvel 0-i")

calculate()