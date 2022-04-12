#classes are user defined blueprint or prototype
#sum, multiplication, addition , constant
#methods, class variables, instance variable, constructor etc
#objects for your classes

#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num = 100 #class variable
    #default constructor
    def __init__(self, a, b):
        self.firstNumber= a
        self.secondNumber= b
        print("i am called automatically when object is created")

    def getData(self):
        print("i am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj=Calculator(2, 3) #sintax to create objects in python
obj.getData()
print(obj.Summation())

obj=Calculator(4, 5) #sintax to create objects in python
obj.getData()
print(obj.Summation())