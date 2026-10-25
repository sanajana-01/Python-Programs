# Input 4 --> 1     *     2     *     3     *    4      *

class Pattern:
    def NumStar(ino):
        iCnt = 0
        for iCnt in range (ino, iCnt,-1):
            print(iCnt,"\t * \t",end = "")
class Main:
    iValue = 0

    print("Enter Number")
    iValue = int(input())
    Pattern.NumStar(iValue)

