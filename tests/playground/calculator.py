from typing import Union

class Calculator:
    def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x + y

    def subtract(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x - y

    def multiply(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x * y

    def divide(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        if y == 0:
            return None
        return x / y

if __name__ == "__main__":
    calculator = Calculator()