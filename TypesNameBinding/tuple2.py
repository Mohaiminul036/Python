numbers = tuple([1,2,3])
print(numbers)
chars = tuple('abc')
print(chars)
digits1 = (x for x in range(9))
print("digits1:", digits1)
digits2 = tuple(x for x in range(9))
print(digits2)