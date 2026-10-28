class GetDigits:
    def EachDigits(iNo):
        iValue1 = 0

        while(iNo != 0):
            iValue1 = iNo % 10
            print(iValue1,end = "")
            iNo = int (iNo / 10)


class Main:
    iValue = 0

    print("Enter the Number : ")
    iValue = int(input())

    GetDigits.EachDigits(iValue)


