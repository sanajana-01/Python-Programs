class Loop:
    def display(iNo):
        iCounter = 0
    # INPUT UPDATER
        if iNo <= 0:
            iNo = -iNo
            if iNo == 0:
                print("Enter any value except 0. ")

        for iCounter in range(1, iNo + 1):  #start = 0, end = 5
            print("----------------")
            print(iCounter,"Jay Ganesh...")
            print("----------------")

            

class Main:
    iValue = 0
    print("Enter the frequency : ")
    iValue = int(input())

    Loop.display(iValue)