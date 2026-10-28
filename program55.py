class Findfactors:
    def CheckFactor(ino):
        iCnt = 1
        tvalues = ()
    
        for iCnt in range (iCnt, int(ino+1/2)):
            if (ino % iCnt == 0):
                tvalues = tvalues + (iCnt,)
        return tvalues
    
    def FactorsSum(ino):
        iCnt = 1
        iSum = 0
        for iCnt in range (iCnt, int(ino+1/2)):
            if (ino % iCnt == 0):
                iSum = iSum + iCnt
        return iSum
    
    def CheckPerfect(iNo1, iNo2):
        return (iNo1 == iNo2)

class Main:
    iNo = 0
    tRet = ()
    iResult = 0
    bRet = False 

    print("Enter the frequency")
    iNo = int(input())

    tRet = Findfactors.CheckFactor(iNo)
    print("Factors of",iNo,"are :",tRet)

    iResult = Findfactors.FactorsSum(iNo)
    print("Summation of factors :",iResult)

    bRet = Findfactors.CheckPerfect(iNo, iResult)
    if(bRet == True):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


