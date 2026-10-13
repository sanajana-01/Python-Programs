iNo1 = 0
iNo2 = 0 
iAns = 0

iNo1 = int(input("Enter the first value : \n"))
iNo2 = int(input("Enter the second value : \n"))

def Addition(iNo1,iNo2):
    iAns = iNo1 + iNo2
    return iAns

iAns = Addition(iNo1, iNo2)
print("addition is : ", iAns)