

class Calculate:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def sum(self): return self.__num1 + self.__num2
    def sub(self): return self.__num1 - self.__num2
    def mul(self): return self.__num1 * self.__num2

    def div(self): return self.__num1 / \
        self.__num2 if self.__num2 > 0 else "Divide By Zero!"
