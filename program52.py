class Findfactors:
    def CheckFactor(ino):
        iCnt = 1
        print("Factors of",ino,"are :",end="")
        for iCnt in range (iCnt, int(ino+1/2)):
            if (ino % iCnt == 0):
                print(iCnt,",",end="")
class Main:
    iNo = 0

    print("Enter the frequency")
    iNo = int(input())

    Findfactors.CheckFactor(iNo)
     