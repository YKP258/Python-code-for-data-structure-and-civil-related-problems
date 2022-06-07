print("The numbers are:",end=" ")
def sum():
    sum = 0

    for i in range (1,101):
        if(i%4==0 and i%7!=0):
            print(i,end=",")
            sum +=i
    return sum

print("\n\nSum of above numbers is:",sum())
