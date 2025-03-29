class Calculator:

    def validate_number(self, a, b):
        """Utility method to validate if inputs are numbers."""
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both arguments must be numbers")

    def add(self, a, b):
        self.validate_number(a, b)
        return a + b

    def minus(self, a, b):
        self.validate_number(a, b)
        return a - b

    def multiply(self, a, b):
        self.validate_number(a, b)
        return a * b

    def divide(self, a, b):
        self.validate_number(a, b)
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b
