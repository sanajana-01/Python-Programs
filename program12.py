import sys

class Sum:
    def addition(self,ino1,ino2):
        iAns = ino1 + ino2
        return iAns

class test:
     def type(self,iNo3):
        try:
            iNo3 = int(iNo3)
            return iNo3
        except :
            print("Invalid input! Please enter \"digits\" only." , file = sys.stderr) # error output
            return 0
     
class main:
    ino1 = 0
    ino2 = 0
    ians = 0

    print("Enter first no : ")
    ino1 = input()
    t = test()
    ino1 = t.type(ino1)
    if ino1 == 0:
        sys.exit()
    
    print("Enter second no : ")
    ino2 = input()
    ino2 = t.type(ino2)
    if ino2 == 0:
        sys.exit()

    sum = Sum()
    ians = sum.addition(ino1,ino2)
    print("Addition is : ",ians)



    

    
