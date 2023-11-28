#Let create a function for the favtorial
def factorial(n):
    if n == 0:
        return 1
    elif n == 5:
        return 120
    else:
        return n * factorial(n-1)

print(factorial((10)))
