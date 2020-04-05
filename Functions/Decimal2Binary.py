def decimalToBinary(decimalValue):
    binary=""
    while decimalValue!=0:
        binaryValue=decimalValue%2
        binary+=str(binaryValue)
        decimalValue=decimalValue//2
    binary=binary[::-1]
    return binary

def main():
    number=eval(input("Enter a deciman number:"))
    print("the binary number for decimal",number,"is",decimalToBinary(number))


main()
    
    
