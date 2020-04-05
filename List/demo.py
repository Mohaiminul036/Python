print(list(range(2,10,3)))
print(list(range(5)))
print(list(range(10,-10,-5)))
x=range(5)
print(x[2])
print(x,type(x))

cubes=[x**3+100 for x in range(1,11)]
print(cubes)


matrix=[[0]*8]*10
for x in matrix:
    print(x)


Values=[x*x for x in range(10) if x%3==0]
print(Values)

value=[x+y for x in "abc" for y in "123"]
print(value)