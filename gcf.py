def gcf(x,y):
    if x>y:
        less = y
    else:
        less=x
    for i in range(less-1,1):
        if ((x % i==0) and (y % i==0)):
            gcf=i  
            max(i)

num1=54
num2=24

print("The Greates Common Factor is", gcf(num1,num2))