with open("captains.txt") as FH:
    captains = dict()
    header  = next(FH)
    for line in FH:
        parts = line.split(',')
        name = parts[0]
        games = int(parts[2])
        won = int(parts[3])
        lst = int(parts[4])
        captains[name] = [games, won, lst]

for name in sorted(captains):
    print(f"{name:>19}:{captains[name]}")
else:
    print("-"*25)

#print sorted by number of matches played
    def get_value(x):
        cap_info = captains.get(x)
        return cap_info[-1]
    
for name in sorted(captains, key= captains.get, reverse=True):
    print(f"{name:>19}:{captains[name]}")
else:
    print("-"*25)
