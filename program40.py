#   Input 4
#   1     2    3     4   

class Display:
    def PrintDigits(iNo):
        iCnt = 1
        for iCnt in range (1,iNo + 1):
            print(iCnt,end = "\t")

class Main:
    iValue = 0
    print("Enter Number : ")
    iValue = int(input())

    Display.PrintDigits(iValue)


