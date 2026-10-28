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

class Main:
    iValue = 0
    iResult = 0

    print("Enter the Number : ", end="")
    iValue = int(input())

    iResult = GetDigits.EachDigits(iValue)
    print("Reverse : ",iResult)


