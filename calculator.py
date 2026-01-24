def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

math_functions = {}
math_functions["+"] = add
math_functions["-"] = subtract
math_functions["*"] = multiply
math_functions["/"] = divide


end = False

while end == False:

    first_number = float(input("What is your first number? "))
    should_continue = True
    while should_continue == True:
        operator = input("+\n-\n*\n/\nPick an operation: ")

        second_number = float(input("What is your second number? "))
        def calculate():

            if operator == "+":
                return math_functions["+"](first_number, second_number)
            elif operator == "-":
                return math_functions["-"](first_number, second_number)
            elif operator == "*":
                return math_functions["*"](first_number, second_number)
            elif operator == "/":
                return math_functions["/"](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {calculate()}")
        again = input(f"Type 'y' to continue calculating with {calculate()}, or type 'n' to start a new calculation: ")
        if again == 'y':
            first_number = calculate()
            continue
        if again == 'n':
            should_continue = False
