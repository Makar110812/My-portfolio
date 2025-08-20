# Idents
def indent(n):
    print("\n" * (n - 1))

# Error list
def error(n):
    if n == 1:
        print(f"Error: the first value is not a number.")
    elif n == 2:
        print(f"Error: the second value is not a number.")
    elif n == 3:
        print(f"Error: An incorrect character has been entered.")
    elif n == 4:
        print(f"Error: you cannot divide by zero.")
    elif n == 5:
        print(f"Error: The symbol is not recognized.")
    elif n == 6:
        print(f"Error: Invalid expression. Available options: Yes/No.")
    elif n == 7:
        print(f"Error: Numbers must be integers for integer division.")
    else:
        print(f"Error: Internal code error. Please contact the developer.")

# Help
def help():
    print("\nHELP\n----\nTo use the calculator, enter an expression in the following format:\n",
          "<Number_1> <Symbol (+; -; *; /; ^; **; //; %)> <Number_2>", sep="")

# Checking for a request for help
print(f"Do you need any help?")
match input():
    case "True" | "t" | "T" | "y" | "Y" | "yes" | "Yes" | "YES":
        help()
        indent(1)
    case "False" | "f" | "F" | "n" | "N" | "no" | "No" | "NO":
        indent(1)
    case _:
        error(6)

while True:
    # Data entry
    i_1, s, i_2 = input().split()
    indent(1)

    # Checking the entered data
    if "." in  i_1:
        try:
            a = float(i_1)
        except ValueError:
            error(1)
        else:
            i_1 = float(i_1)
    else:
        try:
            a = int(i_1)
        except ValueError:
            error(1)
        else:
            i_1 = int(i_1)

    if "." in  i_2:
        try:
            a = float(i_2)
        except ValueError:
            error(2)
        else:
            i_2 = float(i_2)
    else:
        try:
            a = int(i_2)
        except ValueError:
            error(2)
        else:
            i_2 = int(i_2)

    if s not in ["+", "-", "*", "/", "^", "**", "//", "%"]:
        error(3)

    # Amount
    if s == "+":
        print(f"{i_1} + {i_2} = {i_1 + i_2}")

    # Subtraction
    elif s == "-":
        print(f"{i_1} - {i_2} = {i_1 - i_2}")

    # Multiplication
    elif s == "*":
        print(f"{i_1} * {i_2} = {i_1 * i_2}")

    # Division
    elif s == "/":
        if i_2 == 0:
            error(4)
        if i_1 / i_2 == float(i_1 // i_2):
            print(f"{i_1} / {i_2} = {i_1 // i_2}")
        else:
            print(f"{i_1} / {i_2} = {i_1 / i_2}")

    # Exponentiation
    elif s in ["^", "**"]:
        print(f"{i_1} ^ {i_2} = {i_1 ** i_2}")

    # Integer division
    elif s == "//":
        if float(int(float(i_1))) == float(i_1) and float(int(float(i_2))) == float(i_2):
            print(f"{i_1} // {i_2} = {i_1 // i_2}")
        else:
            error(7)

    # Finding the remainder of the division
    elif s == "%":
        print(f"{i_1} % {i_2} = {i_1 % i_2}")

    else:
        error(5)
    indent(2)
