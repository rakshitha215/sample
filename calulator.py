num1=int(input("Enter the first number"))
num2=int(input("Enter the seconf Number"))
operation=input("Enter the operation such as +,-,/,%,*,etc")
if operation=='+':
    sum=num1+num2
    print(sum)
elif operation=='-':
    sub=num1-num2
    print(sub)
elif operation=='*':
    mul=num1*num2
    print(mul)
elif operation=='/':
    div=num1/num2
    print(div)
elif operation=='%':
    rem=num1%num2
    print(rem)
else:
    print("Invalid symbol")

