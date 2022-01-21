#Assignment 2-3 by Diego Suarez


#Three is a crowd
names = ["Diego", "Joe", "Jack", "John"]

print(names)

def crowd_test(crowd):
    if len(crowd) > 3:
        while len(crowd) > 2:
            crowd.pop(len(crowd)-1)

crowd_test(names)

print(names)

#Three is a crowd - part 2
def crowd_testP2(crowd):
    if len(crowd) > 3:
        while len(crowd) > 2:
            crowd.pop(len(crowd)-1)
    else:
        print("The room is not very crowded")

crowd_testP2(names)

#Six is a mob
namesP3 = ["Diego", "Joe", "Jack", "John", "Jill", "Jenny"]
print(namesP3)

def crowd_testP3(crowd):
    if len(crowd) > 3:
        if len(crowd) > 5:
            print("There's a mob in the room")

        while len(crowd) > 2:
            crowd.pop(len(crowd)-1)
    elif len(crowd) == 0:
        print("There are no people in the room")
    elif len(crowd) > 2 and len(crowd) < 6:
        print("The room is crowded")
    else:
        print("The room is not very crowded")
    print(crowd)

crowd_testP3(namesP3)

namesP3.append("Jim")
#crowd
crowd_testP3(namesP3)
#empty room
crowd_testP3([])

