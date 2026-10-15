class Sum:
    def addition(self,ino1,ino2):
        return ino1 + ino2

class test:
     def type(self,ino1,ino2):
        try:
            ino1 = int(ino1)
            ino2 = int(ino2)
        except :
            print("Invalid input! Please enter \"digits\" only.")
            return

        sum = Sum()
        ians = sum.addition(ino1,ino2)
        print("Addition is : ",ians)
        
class main:
    ino1 = 0
    ino2 = 0
    ians = 0

    print("Enter first no : ")
    ino1 = input()
    
    print("Enter second no : ")
    ino2 = input()

    t = test()
    t.type(ino1,ino2)

    
