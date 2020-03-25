class Calculator:
    num1 = int(input("What is your first number you would like me to calculate?(not a decimal)"))
    num2 = int(input("What is your second number you would like me to calculate?(not a decimal)"))
    calculation = input("How would you like me to calculate this?")

    def add():
        if calculation in ["+", "add", "addition"]:
        answer = num1 + num2
        print(answer)
    def subtraction():
        if calculation in ["-", "subtract", "subtraction"]:
        answer = num1 - num2
    
    def divide():
        if calculation in ["/", "divide", "division"]:
            answer = num1 * num2
            print(answer)
    
    


    



    add()