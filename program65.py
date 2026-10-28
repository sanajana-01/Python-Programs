class GetDigits:
    def EachDigits(iNo):
        iValue1 = iNo
        iDigits = 0
        iSum = 0
        count = 0

        while(iNo != 0):
            if iNo < 0:
                iNo = -iNo

            iDigits = iNo % 10
            count += 1

            if(iDigits%2 == 0):
                print("Even : ",iDigits)
            else:
                print("Odd : ",iDigits)

            iSum = iSum + iDigits

            iNo = int (iNo / 10)
            print(iNo)
            print("----------------")
            
        print("Number of digits in",iValue1,"are : ",count)
        print("Addition of digits",iValue1,"is : ",iSum)

class Main:
    iValue = 0

    print("Enter the Number : ")
    iValue = int(input())

    GetDigits.EachDigits(iValue)


