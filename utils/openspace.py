from utils.table import Table

class Openspace():
    def __init__(self, tables, number_of_tables: int):
        self.tables = Table()
        self.number_of_tables = number_of_tables

    def organize(self, names):
        for name in names:
            self.tables.assign_seat_name(name)

    def display(self):
        ...

    def store(filename):
        ...
    