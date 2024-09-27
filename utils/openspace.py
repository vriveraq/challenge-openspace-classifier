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
        



