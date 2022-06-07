def SquareSum(n):
    f = [1] * (n)
    if (n <= 0):
        return 0
    f[0] = 1
    f[1] = 2
    print("Terms of fibonacci series are: ",f[0], f[1],end=" ")
    sum = ((f[0] * f[0]) +(f[1] * f[1]))

    for i in range(2, n):
        f[i] = (f[i - 1] +f[i - 2])
        print(f[i],end=" ")
        sum += (f[i] * f[i])


    return sum

n = int(input("Enter the numbers of terms:"))
print("\nSum of squares of Fibonacci numbers is :",SquareSum(n))