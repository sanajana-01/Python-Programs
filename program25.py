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
    def Minimum(self,iNo1,iNo2,iNo3,iNo4):
        if iNo1 < iNo2 and iNo1 < iNo3 and iNo1 < iNo4:
            return iNo1
        elif iNo2 < iNo1 and iNo2 < iNo3 and iNo2 < iNo4:
            return iNo2
        elif iNo3 < iNo1 and iNo3 < iNo2 and iNo3 < iNo4:
            return iNo3
        else:
            return iNo4
     
class main:
    ino1 = 0
    ino2 = 0
    ino3 = 0
    ino4 = 0
    bool = 0

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

    print("Enter third no : ")
    ino3 = input()

    t = test()
    ino3 = t.type(ino3)

    if ino3 == 0:
        sys.exit()

    print("Enter fourth no : ")
    ino4 = input()

    t = test()
    ino4 = t.type(ino4)

    if ino4 == 0:
        sys.exit()

    check = Check()
    bool = check.Minimum(ino1,ino2,ino3,ino4) 
    print("Minimum Number is : ",bool)

    



    

    
