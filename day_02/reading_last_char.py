friends = ["raj", "sam"]

def get_last(x):
    return x[-1]

sorted(friends, key=get_last)
