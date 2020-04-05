def greeting(n,gender='male'):
    n = n.title()
    s = "Mr" if gender=='male' else 'Miss'
    print("Hi,",s,n)
    return

sName = "alan turing"
greeting(sName)
print("sName after function call:",sName)