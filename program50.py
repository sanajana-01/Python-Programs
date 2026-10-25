class Calculation:
    def Divisible(ino):
       
        if(ino % 3 == 0 and ino % 5 == 0):
            print(ino," Is Divisible by 3 and 5 both")
        elif (ino % 3 == 0):
            print(ino," Is Divisible by 3")
        elif (ino % 5 == 0):
            print(ino," Is Divisible by 5")
        else:
            print(ino," Is Not Divisible by 3 and 5")

class Main:
    iValue = 0
    iResult = 0

    print("Enter Frequency : ")
    iValue = int(input())

    Calculation.Divisible(iValue)

