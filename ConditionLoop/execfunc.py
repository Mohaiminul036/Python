scopeTemp = {}
scopeTemp['x'] = 30
scopeTemp['y'] = 20
exec("sum = x + y",scopeTemp)
print(sum)
print("sum =", scopeTemp['sum'])