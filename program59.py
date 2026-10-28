class Check:
    def CheckPrimeNo(iNo):
        iCnt = 2
        flag = True

        for iCnt in range(iCnt ,int(iNo/2)+1):
            if (iNo % iCnt == 0) :
                flag = False
                break
            else:
                return flag


class Main:
    iValue = 0
    bRet = False

    print("Enter a Number : ")
    iValue = int(input())
    bRet = Check.CheckPrimeNo(iValue)

    if(bRet == True):
        print(iValue,"is PRIME NUMBER")
    else:
        print(iValue,"is NOT PRIME NUMBER")