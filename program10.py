class Sum:
    def addition(self,ino1,ino2):
        return ino1 + ino2

class main:
    ino1 = 0
    ino2 = 0
    ians = 0

    print("Enter first no : ")
    ino1 = int(input())

    print("Enter second no : ")
    ino2 = int(input())

    sum = Sum()
    ians = sum.addition(ino1,ino2)
    print("Addition is : ", ians)

