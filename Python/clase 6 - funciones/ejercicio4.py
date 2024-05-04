def factorial(a):
    total = 1
    for n in range(1, a+1, 1):
        total = total * n
    return total


print(factorial(3))
