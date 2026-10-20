class Loop:
    def display(iNo):
        iCounter = 0
    # INPUT UPDATER
        if iNo <= 0:
            iNo = -iNo
            if iNo == 0:
                print("Enter any value except 0. ")
        iCounter = 1 
        while(iCounter <= iNo ): 
            print("---------------")
            print(iCounter,"Jay Ganesh...")
            print("---------------")
            iCounter-=1            #infinite loop
            

            

class Main:
    iValue = 0
    print("Enter the frequency : ")
    iValue = int(input())

    Loop.display(iValue)