def factorial(n):
    print("factorial(%d) is called." % (n))
    if n==1:
        return 1
    r = n*factorial(n-1)
    return r

print("6!=",factorial(6))