with open("captains.txt") as FH:
    #captains = dict()
    header  = next(FH)
    captains = list()

    for line in FH:
            cap = dict()
            parts = line.split(',')
            name = parts[0]
            mat, won, lost = [int(x) for x in parts[2:5]]
            cap['name'] = name
            cap['mat'] = mat
            cap['won'] = won
            cap['lost'] = lost
            captains.append(cap)
    for cap in captains:
        print(f"{cap['name']:>19} {cap['mat']} {cap['won']} {cap['lost']}")

    
##    capt1 = next(FH)
##    parts = capt1.split(',')
##    name = parts[0]
##    parts[2:5]
##    played, won, lost = parts[2:5]
##    played, won, lost = [int(x) for x in parts[2:5]]
##    capt_d1 = dict()
##    capt_d1['name'] = name
##    capt_d1['mat'] = played
##    capt_d1['lost'] = lost
##
##    capt2 = next(FH)
##    parts = capt2.split(',')
##    capt2['name'] = name
##    capt2['mat'] = played
##    capt2['lost'] = lost

    
