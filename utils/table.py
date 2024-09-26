class Seat:
    """Class defining a seat characterized by :
        - free
        - occupant"""
    def __init__(self):
        self.free = True
        self.occupant = ""
    def set_occupant(self,name):
        self.free =False
        self.occupant = name
    def remove_occupant(self):
        self.free = True
        self.occupant = ""
    def __str__(self):
        return "{self.occupant},{self.free}"
names = ["Basma","Dhrisya", "Ihor", "Izabella", "Kelli"]
list_seats =[]
for name in names:
    seat = Seat()
    seat.set_occupant(name)
    list_seats.append(seat)
print(list_seats)

class Table: 
    """Class defining a table characterized by :
        - capacity
        - seats"""
    def __init__(self):
        self.capacity = 4
        self.seats = []
        for i in range(self.capacity):
            self.seats.append(Seat())
        
    def has_free_spot(self):
        for i in self.seats:
            if i.free == True:
                return True
                break
    
    def assign_seat(self, name):
        for i in self.seats:
            i.set_occupant(name)

    def left_capacity():
        for i in seat.set_occupant(name):
            return 
