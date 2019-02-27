def remove_vowels():
    names = ['Anil','Babu','Laxman','Eswar']
    vowels = ['A','E','I','O','U']
    counter = 1;
    newname = list()
    for name in names:
        print("Name: ", name)
        for i in range(1, len(name)):
            for v in vowels:
                if name[i] == v.lower():
                    print(name.replace(name[i],""))
                    newname.append(name.replace(name[i],""))

    print(newname)


#Main
remove_vowels()
