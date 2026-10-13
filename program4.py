iValue1 = 0 
iValue2 = 0
iResult = 0 

iValue1 = int(input("Enter first number : "))
iValue2 = int(input("Enter second number : "))

def add(iValue1,iValue2):

    iResult = iValue1 + iValue2
    return iResult

iResult = add(iValue1, iValue2)

print("Addition of 2 numbers is : ",iResult)
