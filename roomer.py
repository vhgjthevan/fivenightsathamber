#return the rooms connected to current room
def checkconnections(room):
    connectlist=[]
    for hall in hallwaylist:
        if room in hall:
            for i in hall:
                if i != room:
                    connectlist.append(i)
    return connectlist

#find the room with the lowest distance value
def chooseroom(room):
    dist2rooms = ["room1", "room2", "room4"]
    dist1rooms = ["room3", "room5"]
    dist0rooms = ["room6"]
    if room in dist2rooms:
        startroomval = 2
    elif room in dist1rooms:
        startroomval = 1
    else:
        startroomval = 0
    roomopts = []
    for room in checkconnections(room):
        roomoptval=100
        if room in dist2rooms:
            roomoptval = 2
            if roomoptval < startroomval:
                roomopts.append(room)
        elif room in dist1rooms:
            roomoptval = 1
            if roomoptval < startroomval:
                roomopts.append(room)
        else:
            roomoptval = 0
            if roomoptval < startroomval:
                roomopts.append(room)
    return roomopts




hallwaya = ["room1", "room2", "room3"]
hallwayb = ["room1", "room4"]
hallwayc = ["room3", "room5", "room6"]
hallwayd = ["room3", "room4"]
hallwaylist = [hallwaya, hallwayb, hallwayc, hallwayd]


location=input("room: ")
print(chooseroom(location))
