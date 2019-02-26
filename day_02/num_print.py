FH = open("runs.txt")
text = FH.read()
lines = text.split('\n')
lines = lines[:-1]
nums = list()
for item in lines:
    n = int(item)
    nums.append(n)

print(nums)
