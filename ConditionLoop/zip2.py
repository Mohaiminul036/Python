names = ['Tom', 'Andy', 'Alex', 'Dorothy']
salarys = [1200, 1050, 1600, 2010]
print(list(zip(names,salarys)))
print(list(enumerate(names)))

for idx,name in enumerate(names):
    print(name,idx)
for name, salary in zip(names,salarys):
    print(name+"'s salary/week:",salary)