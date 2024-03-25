"""Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation."""


def basic_op(operation, value1, value2):
    if operation == "+":
        return value1 + value2
    elif operation == "-":
        return value1 - value2
    elif operation == "*":
        return value1 * value2
    elif operation == "/":
        if value2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return value1 / value2
    else:
        raise ValueError("Invalid operation. Supported operations are '+', '-', '*', and '/'.")
