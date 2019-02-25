Total = 10_000
speed = int(input("cycle speed:"))
hours = int(input("daily limt:"))
daily_dist = speed * hours

days = Total / daily_dist
months = days // 30
days = days % 30
years = months // 12
months = months % 12
print(years "Years ", monthds "Months ",  days "days ")

