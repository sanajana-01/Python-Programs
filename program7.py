iNo1 = 0
iNo2 = 0 
iAns = 0


class arithematic :
    def Addition(self,iNo1,iNo2): # here in python we nees to add self as it receives an A object with 2 parameters so we added self
#  self refers to the current object. = A
        iAns = iNo1 + iNo2
        return iAns

print ("Enter the first value : ")
iNo1 = int(input())

print("Enter the second value : ")
iNo2 = int(input())

A = arithematic()               # A = object
iAns = A.Addition(iNo1, iNo2)

print("addition is : ", iAns)