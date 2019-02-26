with open("C:/Users/Administrator/Desktop/python_learing/day_02/PyPractice-master/data/captains.txt") as FH:
    counter = 0
    for line in FH:
        counter += 1
        print (line, end="")
        if counter == 5:
            break
