class Room:
    def __init__(self, description):
        self.description = description
        self.exits = {}

    def connect(self, direction, other_room):
        self.exits[direction] = other_room
 
    def __repr__(self):
        exits_str = ", ".join(self.exits.keys())
        return f"Room('{self.description}') Exits: {exits_str}"
 
 
class Player:
    def __init__(self, start_room):
        self.location = start_room


    def move(self, direction):
        if direction in self.location.exits:
            self.location = self.location.exits[direction]
            return True
        return False
    

hall = Room("You are in a grand hall.")
kitchen = Room("You are in a kitchen. It smells of garlic.")
garden = Room("You stand in a sunny garden.")
 
hall.connect("north", kitchen)
kitchen.connect("south", hall)
hall.connect("east", garden)
garden.connect("west", hall)
 
player = Player(hall)
 
print(player.location.description)
while True:
    cmd = input("Enter direction (or quit): ").strip().lower()
    if cmd == "quit":
        print("Goodbye!")
        break
    if player.move(cmd):
        print(player.location.description)
    else:
        print("You can't go that way.")