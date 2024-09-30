import random  # shuffle the names randomly
from table import Table

class Openspace:
    def __init__(self, number_of_tables, table_capacity):
        self.tables = [Table(table_capacity) for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables

    def organize(self, names):
        """Randomly assign people to seats in different tables."""
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
            else:
                print(f"No seats available for {name}")
    def display(self):
        """Display the seating arrangement in a readable way."""
        for i, table in enumerate(self.tables):
            print(f"Table {i + 1}:")
        for m, seat in enumerate(table.seats):
                if seat.free:
                    print(f"  Seat {m + 1}: Free")
                else:
                    print(f"  Seat {m + 1}: {seat.occupant}")
    def store(self, filename):
        """Store the seat arrangement in exelfile"""
        for i, table in enumerate(self.tables):
                f.write(f"Table {i + 1}:\n")
        
    def store(self, filename):
        """Store seating arrangement in a exel file."""
        for i, table in enumerate(self.tables):
                f.write(f"Table {i + 1}:\n")
        for m, seat in enumerate(table.seats):
                if seat.free:
                        f.write(f"  Seat {m + 1}: Free\n")
                else:
                        f.write(f"  Seat {m + 1}: {seat.occupant}\n")
        print(f"Seating arrangement saved to {filename}")
                         
                        



