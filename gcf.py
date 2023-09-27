def gcf(x,y):
    if x>y:
        less = y
    else:
        less=x
    for i in range(less-1,1):
        if ((x % i==0) and (y % i==0)):
            gcf=i    
        thislist = [i]

        thislist.append(gcf)

        print(thislist)

num1=54
num2=24

print("The Greates Common Factor is", gcf(num1,num2))

If x<5 and x>0:
    Eastbound traffic

if x>5 and x<10:
    Westbound Traffic