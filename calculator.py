class Calculator:
    
    def add(self, a, b):
        if not (isinstance(a,(int, float))) and (isinstance(b,(int, float)))):
            raise Exception()
        return a+b

    def subtract(self, a,b):
        if not (isinstance(a,(int, float))) and (isinstance(b,(int, float)))):
            raise Exception()
        return a-b

    def divide(self, a,b):
        if not (isinstance(a,(int, float))) and (isinstance(b,(int, float)))):
            raise Exception()
        return a/b

    def multiply(self, a,b):
        if not (isinstance(a,(int, float))) and (isinstance(b,(int, float)))):
            raise Exception()
        return a*b




class Calculator User:
    def __init__(self):
        self.cal = Calculator()

    def add(self,a,b):
        try:
            return self.cal.add(a,b)
        except:
            print("Wrong arguments passed to add")
    
    def subtract(self,a,b):
        try:
            return self.cal.subtract(a,b)
        except:
            print("Wrong arguments passed to subtract")

    def divide(self,a,b):
        try:
            return self.cal.divide(a,b)
        except:
            print("Wrong arguments passed to divide")

    def multiply(self,a,b):
        try:
            return self.cal.multiply(a,b)
        except:
            print("Wrong arguments passed to multiply")

    


    