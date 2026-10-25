# Input 5
# 1+2+3+4+5 = 120

class Calculation:
    def Factorial(ino):
        iFact = 1
        iCnt = 1
        for iCnt in range (iCnt, ino+1):
            iFact = iFact * iCnt 
        return iFact

class Main:
    iValue = 0
    iResult = 0

    print("Enter Frequency : ")
    iValue = int(input())

    iResult = Calculation.Factorial(iValue)

    print("Factorial of ",iValue,"is :",iResult)
