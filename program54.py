class Findfactors:
    def CheckFactor(ino):
        iCnt = 1
        iSum = 0
        
        print("Factors of",ino,"are :")

        for iCnt in range (iCnt, int(ino+1/2)):
            if (ino % iCnt == 0):
                print(iCnt)
                iSum = iSum + iCnt
        print("Summation of factors : ",iSum)

        if(iSum == ino):
            print("Perfect Number")
        else:
            print("Not a Perfect Number")

class Main:
    iNo = 0

    print("Enter the frequency")
    iNo = int(input())

    Findfactors.CheckFactor(iNo)
     