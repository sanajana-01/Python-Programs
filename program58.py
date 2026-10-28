class Findfactors:
    def CheckFactor(ino):
        iCnt = 0
        iCnt = 2
        
        for iCnt in range (iCnt, int(ino/2)+1):
            if (ino % iCnt == 0):
                break
        
        iCheck = int((ino/2))
        if(iCnt == iCheck):
            return True
        else:
            return False
    
class Main:
    iNo = 0
    bRet = False

    print("Enter the frequency")
    iNo = int(input())

    bRet = Findfactors.CheckFactor(iNo)

    if(bRet == True):
        print(iNo ,"is a Prime Number")
    else:
        print(iNo,"is Not a Prime Number")


