num1 = float(int(input("Enter the 1st value: ")))
num2 = float(int(input("Enter the 2nd value: ")))
opr = input("Enter operator: ")

ch = 0
while True:
    if(opr == "+"):
        result = num1 + num2
        print("Result :", result)
        break
    elif(opr == "-"):
        result = num1 - num2
        print("Result :", result)
        break
    elif(opr == "*"):
        result = num1 * num2
        print("Result :", result)
        break
    elif(opr == "/"):
        if(num2 != 0):
           result = num1 / num2
           print("Result :", result)
           break
        else:
            print("Division by zero is not allowed!")
            break
    else:
        print("Invalid Operator")

