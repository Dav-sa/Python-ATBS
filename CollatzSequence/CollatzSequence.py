def collatz(n):
    if n % 2 == 0:
        print(n // 2)
        return n // 2
    else:
        print(3 * n + 1)
        return 3 * n + 1


try:
    num = int(input("enter a number"))
    result = collatz(num)
    while result != 1:
        result = collatz(result)
except ValueError:
    print("You must enter an integer")
