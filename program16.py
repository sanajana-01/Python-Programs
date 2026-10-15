import sys

class test:
     def type(self,iNo3):
        try:
            iNo3 = int(iNo3)
            return iNo3
        except :
            print("Invalid input! Please enter \"digits\" only." , file = sys.stderr) # error output
            return 0
        
class EvenOdd:
    def type(self,iNo1):
        if iNo1 % 2 == 0:
            return True
        else:
            return False
class main:
    ino1 = 0
    bool = False

    print("Enter first no : ")
    ino1 = input()

    t = test()
    ino1 = t.type(ino1)

    if ino1 == 0:
        sys.exit()

    eo = EvenOdd()
    bool = eo.type(ino1)

    if bool == True:
        print("Entered number" , ino1 , "is a Even Number.")
    else:
        print("Entered number" , ino1 , "is a Odd Number.")

    



    

    
