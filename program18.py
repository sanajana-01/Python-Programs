import sys

class test:
     def type(self,iNo3):
        try:
            iNo3 = int(iNo3)
            return iNo3
        except :
            print("Invalid input! Please enter \"digits\" only." , file = sys.stderr) # error output
            return 0
        
class Check:
    def maximum(self,iNo1,iNo2):
        if iNo1 > iNo2:
            print("Maximum Number is : ",iNo1)
        else:
            print("Maximum Number is : ",iNo2)
     
class main:
    ino1 = 0
    ino2 = 0

    print("Enter first no : ")
    ino1 = input()

    t = test()
    ino1 = t.type(ino1)

    if ino1 == 0:
        sys.exit()

    print("Enter second no : ")
    ino2 = input()

    t = test()
    ino2 = t.type(ino2)

    if ino2 == 0:
        sys.exit()

    check = Check()
    check.maximum(ino1,ino2)

    



    

    
