class GetDigits:
    def EachDigits(iNo):
        iDigits = 0
        iRev = 0

        while(iNo != 0):
            if iNo < 0:
                iNo = -iNo

            iDigits = iNo % 10
            iRev = (iRev * 10) + iDigits
            iNo = int (iNo / 10)
        return iRev
    
    def CheckPalindrome(iNo,iRev):
        return (iRev == iNo)

class Main:
    iValue = 0
    iResult = 0
    bRet = False

    print("Enter the Number : ", end="")
    iValue = int(input())

    iResult = GetDigits.EachDigits(iValue)
    bRet = GetDigits.CheckPalindrome(iValue,iResult)

    if(bRet):
        print("Is Palindrome")
    else:
        print("Not Palindrome")



