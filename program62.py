class GetDigits:
    def EachDigits(iNo):
        iValue1 = 0

        while(iNo != 0):
            iValue1 = iNo % 10
            print(iValue1)
            iNo = int (iNo / 10)
            print(iNo)
            print("----------------")


class Main:
    iValue = 0

    print("Enter the Number : ")
    iValue = int(input())

    GetDigits.EachDigits(iValue)


