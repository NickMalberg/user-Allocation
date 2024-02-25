import random


def chooseRandomPeople(employees):
    """Choose a random number of people from the employees list"""
    num_people = random.randint(1, len(employees))
    attendees = random.sample(employees, num_people)

    return attendees


def createDayExample(employees):
    """Create a day example"""
    attendees = chooseRandomPeople(employees)

    return attendees


employees = [
    Employee("Nick", "Dev", True),
    Employee("Florian", "Dev", False),
    Employee("Oli", "Dev", False),
    Employee("Dominik", "Dev", False),
    Employee("Rick", "Dev", True),
    Employee("Sönke", "Dev", False),
    Employee("Timo", "Dev", True),
    Employee("Alno", "PO", True),
    Employee("Erkan", "PO", False),
    Employee("Till", "Marketing", False),
    Employee("Lukas", "Marketing", False),
    Employee("Marie", "Marketing", False),
    Employee("Marieke", "Marketing", False),
    Employee("Lilly", "Marketing", False),
    Employee("Birte", "Marketing", False),
    Employee("Johannes", "UX", False),
    Employee("Julia", "UX", False),
    Employee("Elena", "UX", True),
    Employee("Artur", "CS", False),
    Employee("Phillip", "CS", False),
    Employee("Tony", "CS", False),
    Employee("Monana", "CS", False),
    Employee("Karim", "Sales", False),
    Employee("Marei", "Sales", False),
    Employee("Angelika", "Sales", False),
    Employee("Else", "Sales", False),
    Employee("Jannik", "Sales", False),
]

# unitMatches shows which units can sit in the same room, sorted by best match
unitMatches = {
    "Dev": ["PO", "UX", "Marketing"],
    "PO": ["Dev", "UX", "Marketing"],
    "Marketing": ["PO", "UX", "Dev", "CS"],
    "UX": ["PO", "Dev", "Marketing"],
    "CS": ["Sales"],
    "Sales": ["CS"],
}

attendees = createDayExample(employees=employees)
rooms = [Room("Aquarium", 4), Room("BigMamba", 10), Room("Loge", 6), Room("Cave", 6)]

for attendee in attendees:
    print(attendee.name, attendee.unit)

# recursive function to place all attendees


def placeAttendees(rooms, attendees):
    # start from first attendee
    if not attendees:
        return True
    person = attendees.pop(0)
    print(f"Placing {person.name} in a room")
    # check if there is a room with an attendee from the same unit
    sameUnitRooms = [
        room
        for room in rooms
        if person.unit in room.attendingUnits and not room.isFull()
    ]
    sameUnitRoomsNames = [room.name for room in sameUnitRooms]
    print(f"Rooms with same unit: {sameUnitRoomsNames} as {person.name}s unit")
    while sameUnitRooms:
        # as long as there are rooms with attendees from the same unit, place the person in the first room
        print(f"Placing {person.name} in the room {sameUnitRooms[0].name}")
        sameUnitRooms[0].placeAttendee(person)
        if placeAttendees(rooms, attendees):
            break

        else:
            print(f"Removing {person.name} from the room {sameUnitRooms[0].name}")
            removedRoom = sameUnitRooms.pop(0)
            removedRoom.removeAttendee(person)

    else:
        # check if there is an empty room available
        print(f"Trying to place {person.name} in an empty room")
        emptyRooms = [room for room in rooms if room.isEmpty()]
        print(f"There are {len(emptyRooms)} for {person.name}")
        if emptyRooms:
            while emptyRooms:
                print(f"Placing {person.name} in the room {emptyRooms[0].name}")
                emptyRooms[0].placeAttendee(person)
                if placeAttendees(rooms, attendees):
                    break
                else:
                    print(f"Removing {person.name} from the room {emptyRooms[0].name}")
                    removedRoom = emptyRooms.pop(0)
                    removedRoom.removeAttendee(person)

        else:  # no empty rooms available. Now we look for rooms with matching units
            # 1. get all rooms with the best matching units
            matchingUnits = unitMatches[person.unit]
            print(matchingUnits)
            matchingUnitRooms = []
            for unit in matchingUnits:
                matchingUnitRooms += [
                    room
                    for room in rooms
                    if unit in room.attendingUnits and not room.isFull()
                ]

            while matchingUnitRooms:
                print(
                    f"There is a room with matching units. Placing {person.name} in the room {matchingUnitRooms[0].name}"
                )
                matchingUnitRooms[0].placeAttendee(person)
                if placeAttendees(rooms, attendees):
                    break
                else:
                    print(
                        f"Removing {person.name} from the room {matchingUnitRooms[0].name}"
                    )
                    removedRoom = matchingUnitRooms.pop(0)
                    removedRoom.removeAttendee(person)
            else:
                print("No suitable room found for the person")
                # move the last person to another room
                return False


placeAttendees(rooms, attendees)

for room in rooms:
    print(f"Room {room.name} has the following units: {room.getAttendingUnits()}")
    print(f"And the follwoing attendees")
    for desk in room.desks.stack:
        print(desk.name)


def main():
    test = Stack(5)
    print(test)


if __name__ == "__main__":
    main()
