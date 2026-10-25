# Input 5
# 1+2+3+4+5 = 15

class Calculation:
    def Summation(ino):
        iSum = 0
        iCnt = 1
        for iCnt in range (iCnt, ino):
            iSum = iSum + iCnt
        return iSum

class Main:
    iValue = 0
    iResult = 0

    print("Enter Frequency : ")
    iValue = int(input())

    iResult = Calculation.Summation(iValue)

    print("Summation of numbers : ",iResult)
