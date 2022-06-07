def sum(n):
    sum = 0
    for i in range (1,n+1):
        sum += i
    return sum

x = int(input("Enter number of integers: "))
print("The sum of entered integers is:",sum(x))