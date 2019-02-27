class Captain:

    def __init__(self, name, won, lost, played):
        self.name = name
        self.no_of_own_match = won
        self.no_of_lost_match = lost
        self.no_of_played_match = played
        

    def display(self):
        print(f"{self.name}-{self.no_of_own_match}-{self.no_of_lost_match}")

    def __str__(self):
        return f"{self.name},{self.no_of_own_match},{self.no_of_lost_match}, {self.no_of_played_match}"

    def __repr__(self):
        return f"Date{self.dd}.{self.mm}.{self.yy}"
#Main
cap1 = Captain('Sachin', 232 ,21 ,29)
cap2 = Captain('Dhoni', 212 ,12 ,22)
print(cap1)
print(cap2)

dictonary = dict()
dictonary['cap1'] = ('Sachin', 232 ,21 ,29)
dictonary['cap2'] = ('Dhoni', 212 ,12 ,22)
print(dictonary)
