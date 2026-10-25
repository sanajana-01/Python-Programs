# Input 8 --> 1     *     3     *     5     *    7      *

class Pattern:
    def NumStar(ino):
        iCnt = 1
        for iCnt in range (iCnt,ino,+2):
            print(iCnt,"\t * \t",end = "")
class Main:
    iValue = 0

    print("Enter Number")
    iValue = int(input())
    Pattern.NumStar(iValue)

