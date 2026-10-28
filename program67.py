class GetDigits:
    def EachDigits(iNo):
        iDigits = 0
        count = 0

        while(iNo != 0):
            if iNo < 0:
                iNo = -iNo

            iNo = int (iNo / 10)
            count += 1
        return count
    
    def DigitSum(iNo):
        iSum = 0
        while(iNo != 0):
            if iNo < 0:
                iNo = -iNo

            iDigits = iNo % 10
            iSum = iSum + iDigits
            iNo = int (iNo / 10)
        return iSum
    
    def AverageDigit(iNo1, iNo2):
        return iNo1/iNo2
    
class Main:
    iValue = 0
    digit = 0
    sumdigit = 0
    fAvg = 0.0

    print("Enter the Number : ")
    iValue = int(input())

    digit = GetDigits.EachDigits(iValue)
    print("Number of digits in",iValue,"are : ",digit)

    sumdigit = GetDigits.DigitSum(iValue)
    print("Addition of digits",iValue,"is : ",sumdigit)

    fAvg = GetDigits.AverageDigit(sumdigit, digit)
    print("Average of Number is : ",fAvg)


