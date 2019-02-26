##print("Print first 5 lines")
##with open("C:/Users/Administrator/Desktop/python_learing/day_02/PyPractice-master/data/captains.txt") as FH:
##    counter = 0
##    for line in FH:
##        counter += 1
##        print (line, end="")
##        if counter == 5:
##            break
##
##print("Last 5 lines")
##with open("captains.txt") as FH:
##    all_text = FH.read()
##    all_lines = all_text.split('\n')
##    num_lines = len(all_lines)
##    counter = 0
##    for line in all_lines:
##        counter += 1
##        if counter > num_lines - 6:
##            print(line)


print("Print captain names:")
with open("C:/Users/Administrator/Desktop/python_learing/day_02/PyPractice-master/data/captains.txt") as FH:
    headers = next(FH)
    counter = 0
    dictonary = dict()
    for line in FH:
        counter += 1
        #print (line.split(',')[0])
        #print (line.split(',')[2])
        key = line.split(',')[0]
        val = line.split(',')[2]
        dictonary.update({key : val})
        if counter == 5:
            break
print(dictonary)
dictonary_list = sorted(dictonary)
print("after sort:")
print(dictonary_list)


