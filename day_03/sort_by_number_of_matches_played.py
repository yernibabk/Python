with open("captains.txt") as FH:
    captains = dict()
    header  = next(FH)
    for line in FH:
        parts = line.split(',')
        name = parts[0]
        games = int(parts[2])
        captains[name] = games

for name in sorted(captains):
    print(f"{name:>19}:{captains[name]:>3}")
else:
    print("-"*25)

#print sorted by number of matches played
    def get_value(x):
        return captains.get(x)
for name in sorted(captains, key= captains.get, reverse=True):
    print(f"{name:>19}:{captains[name]:>3}")
else:
    print("-"*25)
