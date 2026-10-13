iNo1 = 0
iNo2 = 0 
iAns = 0

print ("Enter the first value : ")
iNo1 = int(input())

print("Enter the second value : ")
iNo2 = int(input())


def Addition(iNo1,iNo2):
    iAns = iNo1 + iNo2
    return iAns

iAns = Addition(iNo1, iNo2)
print("addition is : ", iAns ,end="")