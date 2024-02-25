class Room:
    def __init__(self, name, n_desks):
        self.name = name
        self.desks = Queue(n_desks)
        self.attendingUnits = []

    def isFull(self):
        return self.desks == self.desks.size()

    def isEmpty(self):
        return self.desks.size() == 0

    def placeAttendee(self, attendee):
        if not self.isFull():
            self.desks.push(attendee)
            if attendee.unit not in self.attendingUnits:
                self.attendingUnits.append(attendee.unit)
        else:
            print("Room is full")

    def removeAttendee(self, attendee):
        if attendee in self.desks.stack:
            self.desks.stack.remove(attendee)
            print(f"{attendee.name} has been removed from {self.name}")
            self.attendingUnits.remove(attendee.unit)
        else:
            print(f"{attendee.name} is not in {self.name}")

    def getAttendingUnits(self):
        return self.attendingUnits
