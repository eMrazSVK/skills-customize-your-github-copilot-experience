def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def safe_divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
