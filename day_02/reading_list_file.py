with open("runs.txt") as FH:
    empty = list()
    for num in FH:
        empty.append(int(num))

    empty.sort()
    print(empty)
