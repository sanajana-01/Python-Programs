class SimplePattern:
    def StarPattern(iNo):
        iCnt = 0
        for iCnt in range (iCnt, iNo):
            print("* \t",end = "")

class Main:
    iNum = 0
  
    print("Enter frequency :")
    iNum = int(input())
    
    SimplePattern.StarPattern(iNum)

   