#   Input 4
#   1     2    3     4   

class Display:
    def PrintDigits(iNo):
        iCnt = 1
        while(iCnt <= iNo):         
            print(iCnt,end = "\t")
            iCnt += 1                

class Main:
    iValue = 0
    print("Enter Number : ")
    iValue = int(input())

    Display.PrintDigits(iValue)


