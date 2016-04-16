from room import Room

school_map = []

rooms = [
    ['Library','Cafeteria','Gym','English','Algebra'],
    ['Stem Lab','Kitchen','Closet','Principal\'s Office','Study Hall'],
    ['Auditorium','Spanish','Art','Attendance Office','Shop'],
    ['French','Chemistry','Physics','Biology','Health'],
    ['PE Gym','Closet','Annex','Economics','Detention']
]

def build_map():
    global school_map
    for x, row in enumerate(rooms):
        school_map.append([])
        for y, room in enumerate(rooms[x]):
            print(x,y)
            school_map[x].append(Room(room))

build_map()
    