def find_age(year_of_birth, present_year):
    age = present_year - year_of_birth
    return age
 



def Main():
    year  =  input("Enter your year of born:  ")
    year = int(year)
    user_age = find_age(year, 2019)
    print("Your age is", user_age)

#Main
Main()
    
