class SimplePattern:
    def StarPattern(iNo):
        iCnt = 1
        
        for iCnt in range (iCnt, iNo+1):
            print(iCnt," \t",end = "")

class Main:
    iNum = 0
  
    print("Enter frequency :")
    iNum = int(input())
    
    SimplePattern.StarPattern(iNum)