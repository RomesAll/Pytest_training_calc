from typing import Union

class Calculator:
    
    def addition(x: Union[float, int], y: Union[float, int]):
        return round(x + y, 3)
    def subtraction(x: Union[float, int], y: Union[float, int]):
        return round(x - y, 3)
    def multiplication(x: Union[float, int], y: Union[float, int]):
        return round(x * y, 3)
    def division(x: Union[float, int], y: Union[float, int]):
        return round(x / y, 3)

if __name__ == '__main__':
    calc = Calculator()
    print(calc)