num=int(input("Please enter a number: "))
num2=int(input("Please enter another number: "))
factors = []

def gcf():
    for i in range (num, 0, -1):
        if num%i==0 and num2%i==0:
            factors.append(i)
    print (max(factors))
gcf()