from utils.openspace import Openspace
from utils.table import Seat
from utils.table import Table
import csv


with open('utils/new_colleagues.csv') as csvfile:
        reader = csv.reader(csvfile)
        names = list(reader)    
        # Make an openspace with 6 tables and 4 chars behind each table
        openspace = Openspace (number_of_tables = 6, table_capacity = 4)

        # put the people on the seats
        openspace.organize(names)

        #Show who is where
        openspace.display()
