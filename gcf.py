num=int(input("Please enter a number:"))
num2=int(input("Please enter another number:"))

def gcf():
    for i in range (num, 0, -1):
        if num%i==0 and num2%i==0:
            print(i)
            max(i)
gcf()