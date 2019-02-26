def print_lines(FH):
    while True:
        line = FH.readline()

        if line == "":
            break
        print(line, end="")

with open("C:/Users/Administrator/Desktop/python_learing/day_02/PyPractice-master/data/captains.txt") as MYFH:
    print_lines(MYFH)
