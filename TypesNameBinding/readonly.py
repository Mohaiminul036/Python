values = (3,2,1)
valuesCopy = values
valuesCopy = (1,2,3)
print(values, "-", valuesCopy)

string = "string"
stringCopy = string
stringCopy = "new string"
print(string, "-", stringCopy)

person1=[1,2,3]
person2=person1
person2[2]=1000
print(person1,person2)

chars=bytearray(b'abcddfsd')
charsCopy=chars.copy()
charsCopy1=chars[:]
print(id(chars),id(charsCopy),id(charsCopy1))