import calc
import sys

astr1 = int(sys.argv[1])
astr2 = int(sys.argv[2])
ind1 = int(sys.argv[3])
astria_score = calc.add(astr1, astr2)
win_score = calc.sub(astria_score, ind1)
print("From epc:", __name__)
print("Indian has to socre ", win_score+1 , " to win")
