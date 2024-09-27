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
        return "f{self.occupant},{self.free}"
    
    # create a list of seats and give them a name
names = ["Basma","Dhrisya", "Ihor", "Izabella", "Kelli", "Wouter"]
list_seats =[]
for name in names:
    seat = Seat()
    seat.set_occupant(name)
    list_seats.append(seat)

print(list_seats) # Show the list of oblects

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
        for i in self.seats: #i is seat
            if i.free:
                return True
            
            else :
                return False
    
    def assign_seat(self, name):
        for i in self.seats: # i is seat
           if i.free == True:
                i.set_occupant(name)
                break

        

    def left_capacity(self):
        free_seats = 0
        for seat in self.seats:
            if seat.free:
                free_seats +=1
        return free_seats
    

table_1 = Table()


print(f"If there are free seats? {table_1.has_free_spot()}")
table_1.assign_seat("Ihor")
print(f"If there are free seats after assign? {table_1.left_capacity()}")