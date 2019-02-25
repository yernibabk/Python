def add(x, y):
    val = x+ y
    return val

def sub(x, y):
    val = x - y;
    return val

#Main
a = 10
b = 20;
c = add(a, b)
d = sub(a, b)
print("Sum:", c)
print("diff:", d)

#Austria scored 250 runs in first innings
#india score 220 run in their 1st innings
#Australia then score 150 run their 2nd innings
#how many runs shoud india socre to win 
astria_score = add(250, 150)
win_score = sub(astria_score, 220)
print("Indian has to socre ", win_score+1 , " to win")

# i bought vegetable for 120
#i bought fruits for 55
#i gave the cashier 200
#how much money cashier should return?
total_cost = add(120, 55)
return_money = sub(200, total_cost)
print("return money: ", return_money)




