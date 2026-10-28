class Findfactors:
    def CheckFactor(ino):
        iCnt = 1
        iSum = 0
        
        for iCnt in range (iCnt, int(ino+1/2)):
            if (ino % iCnt == 0):
                iSum = iSum + iCnt
        return iSum
    
    def CheckPrime(ino):
        return(ino == 1)
        
class Main:
    iNo = 0
    iRet = 0
    bResult = False

    print("Enter the frequency")
    iNo = int(input())

    iRet = Findfactors.CheckFactor(iNo)
    bResult = Findfactors.CheckPrime(iRet)
    if(bResult == True):
        print(iNo ,"is a Prime Number")
    else:
        print(iNo,"is Not a Prime Number")


