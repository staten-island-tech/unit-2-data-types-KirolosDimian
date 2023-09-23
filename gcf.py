def gcf(x,y):
    if x>y:
        less = y
    else:
        less=x
    for i in range(1, less+1):
        if ((x % i==0) and (y % i==0)):
            gcf=i    
        return gcf
num1=54
num2=24
print("The Greates Common Factor is",gcf(num1,num2))