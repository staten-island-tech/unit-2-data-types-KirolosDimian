number=input("Please put a number you would like to know the factors to here: ")

def factors(x):
    print("The factors of" ,x, "are:")
    for i in range(x,0,-1):
        if x % i ==0:
            print(i)


factors(number)