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
