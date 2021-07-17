import cal_module

c=cal_module.calculator()

def fun(i):
    if(i==1):
        c.add(a,b)
    elif(i==2):
        c.sub(a,b)
    elif (i == 3):
        c.mul(a, b)
    elif (i == 4):
        c.div(a, b)
    elif (i == 5):
        c.expo(a, b)
    elif ( i == 6):
        c.swap(a,b)
    else:
        return 0
    return 1

ret=0
while(ret!=1):
    x = int(input("Enter an option "))
    if(x<=5):
        a = int(input("enter num1 "))
        b = int(input("enter num2 "))
    ret = fun(x)