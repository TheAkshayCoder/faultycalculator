value1=int(input('enter your first number'))
value2=int(input('enter your second number'))
operation=input('enter the operation')
if (value1 or value2==45) and (value1 or value2==3) and operation=='*':
    print('555')
elif (value1 or value2==56) and (value1 or value2==9) and operation=='+':
    print('77')
elif (value1 or value2==56) and (value1 or value2==6) and operation=='/':
    print('4')
else:
    if operation=='+':
        c=sum(value1+value2)
        print(c)
    elif operation=='-':
        c=value1-value2
        print(c)
    elif operation=='/':
        c=value1/value2
        print(c)
    elif operation=='-':
        c=value1*value2
        print(c)