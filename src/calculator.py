class Calculator:

    def add(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both arguments must be numbers")
        return a + b

    def minus(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both arguments must be numbers")
        return a - b

    def multiply(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both arguments must be numbers")
        return a * b

    def divide(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both arguments must be numbers")
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b
