import sys

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

    if ino1 / 2 != 0:
        print("Entered no is " + iNo1 + " is a Even.")



    

    
