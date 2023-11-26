def main(list_names):
    answer = input("If you want to write all your friends names at once, type W. If you prefer to write one by one type X. If you forgot someone and want to add a name type Y. If you want to remove someone from the list, type Z. ").upper()
    if answer == "W":
        allatonce(list_names)
    elif answer == "X":
        onebyone(list_names)
    elif answer == "Y":
        addname(list_names)
    elif answer == "Z":
        removename(list_names)
    else:
        main(list_names)

def allatonce(list_names):
    names = input("Write your friends' names separated by a comma or Y if you want to go to the menu: ")
    if names.upper() != "Y": 
        for name in names.split(","):
            list_names.append(name.strip())
        secretfriend(list_names)
    else:
        main(list_names)

def onebyone(list_names):
    name = input("Write your friend's name, Y if you want to go to the menu or X if there's no one left: ")
    if name.upper() == "X":
        secretfriend(list_names)
    elif name.upper() == "Y":
        main(list_names)
    else:
        list_names.append(name)
        onebyone(list_names)

def addname(list_names):
    print(f"The list of names looks like this: {list_names}.")
    name = input("Write your friend's name that you want to add, Y if you want to go to the menu or X if there's no one left: ")
    if name.upper() == "X":
        secretfriend(list_names)
    elif name.upper() == "Y":
        main(list_names)
    else:
        list_names.append(name)
        addname(list_names)

def removename(list_names):
    print(f"The list of names looks like this: {list_names}.")
    name = input("Write your friend's name that you want to delete, Y if you want to go to the menu or X if it's done: ")
    if name.upper() == "X":
        secretfriend(list_names)
    elif name.upper() == "Y":
        main(list_names)
    else:
        list_names.remove(name)
        removename(list_names)

def secretfriend(list_names):
    import random
    received = []
    gave = []
    toreceive = []
    togive = []
    for name in list_names:
        toreceive.append(name)
        togive.append(name)
    pairs = {}
    while toreceive != [] or togive !=[]:
        name1 = random.choice(togive)
        name2 = random.choice(toreceive)
        if name1 != name2:
            gave.append(name1)
            togive.remove(name1)
            received.append(name2)
            toreceive.remove(name2)
            pairs[name1] = name2
    report(pairs)
    
def report(pairs):
    for name1 in pairs:
        print(f"{name1.capitalize()} is giving a present to {pairs[name1].capitalize()}")

main([])
