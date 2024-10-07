firstnum = float(input("enter first number: "))
secondnum = float(input("enter second number: "))
operation = input("operation you want to preform, (+, -, *, /): ")

if operation == '+':
    print(firstnum + secondnum)
elif operation == '-':
    print(firstnum - secondnum)
elif operation == '*':
    print(firstnum * secondnum)
elif operation == '/':
    print(firstnum / secondnum)

