from utils.openspace import Openspace
from utils.table import Seat
from utils.table import Table
import csv

def main():
    # A list of people to seat
with open('openspace-organizer/new_colleagues.csv') as csvfile:
            reader = csv.reader(csvfile)
            
# Make an openspace with 6 tables and 4 chars behind each table
openspace = Openspace (numberoftables = 6, numberofseats = 4)

# put the people on the seats
openspace.organize(names)

#Show who is where
openspace.display()
