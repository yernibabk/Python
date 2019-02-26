def add(x, y):
    val = x+ y
    return val

def sub(x, y):
    val = x - y;
    return val

#Main
print("calc :", __name__)
if __name__ == "__main__":
    
    a = 10
    b = 20;
    c = add(a, b)
    d = sub(a, b)

    print("Sum:", c)
    print("diff:", d)
