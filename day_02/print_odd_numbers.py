
def findOdd(x, y):
    for x in range(x, y):
        if (x % 2) == 1:
            print(x)


def findTwoThreeDigit(x, y):
    for x in range(x, y):
        if (x < 100):
            print(x/2)
        else:
            print(x*x)

def printFebi():
    firstVal = 0
    secondVal = 1
    print(firstVal)
    print(secondVal)
    thirdVal = firstVal + secondVal
    print(thirdVal)
    for x in range(4, 11):
        firstVal =secondVal
        secondVal = thirdVal
        thirdVal = firstVal + secondVal
        print(thirdVal)

#:main
findOdd(120, 151)
findTwoThreeDigit(94, 108)
printFebi()
