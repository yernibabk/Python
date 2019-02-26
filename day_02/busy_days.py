booked = [1,3,9,12,13,18,26,27,28,29]
holidays = [4,5,15,16,21,22]
busydays = booked + holidays
busydays.sort()
#length = len(busyday)
available = list()
for i in range(1, 30):
    if i not in busydays:
        available.append(i)
        print(i)
##        continue
##    else:
##        print(i)
