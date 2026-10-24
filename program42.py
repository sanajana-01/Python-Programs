#   Input 4
#   4   *   3   *   2   *   1   *   

class Display:
    def PrintDigits(iNo):
        iCnt = 1
        for iCnt in range (iNo ,0,-1):          #5 to 1
            print("\t",iCnt,"\t *",end = "")    

class Main:
    iValue = 0
    print("Enter Number : ")                    #5
    iValue = int(input())

    Display.PrintDigits(iValue)


