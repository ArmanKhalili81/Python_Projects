from calculate import *


class Getnumber:
    def __init__(self):
        num1 = int(input("Enter Number 1 : "))
        self.operator = input("Enter Operator : ")
        num2 = int(input("Enter Number 2 : "))
        self.ob = Calculate(num1, num2)
        self.call_operation

    @property
    def call_operation(self):
        if self.operator == '+':
            print(self.ob.sum())
        elif self.operator == '-':
            print(self.ob.sub())
        elif self.operator == '*':
            print(self.ob.mul())
        elif self.operator == '/':
            print(self.ob.div())
        else:
            print("Operator Invalid ...")
