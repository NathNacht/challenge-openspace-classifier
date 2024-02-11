import random
from .table import Table
from .file_utils import write_to_csv

class Openspace():
    def __init__(self, number_of_tables: int):
        self.tables = [Table(capacity=4) for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables

    def __str__(self) -> str:
        return "\n".join(str(table) for table in self.tables)

    def organize(self, names):
        """ 
        For each random name in names a check is done if there is a free spot on a table.
        If there is a free spot, a name is assigned to a seat

        :param names: list of names
        """
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat_name(name)
                    break  # Move to the next name once assigned
        
    def display(self):
        """
        Displays the current state of the tables.
        """
        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i}:")
            for j, seat in enumerate(table.seats, start=1):
                print(f"Seat {j}: {'Occupied by: ' + seat.occupant if not seat.free else 'Empty'}")
            print()  # Empty line between tables
        print(f"Number of seats left: {sum(table.left_capacity() for table in self.tables)}")

    def store(self, output_path):
        """
        Generates a list_of_tuples (tableid, seatid, name)
        call file_utils.write_csv(list_of_tuples, headernames, path)

        :param output_path: path to the csv file
        """
        tuple_for_csv = [("TableID", "SeatID", "Name")]
        for i, table in enumerate(self.tables, start=1):
            for j, seat in enumerate(table.seats, start=1):
                tuple_for_csv.append((i,j, seat.occupant))
        write_to_csv(tuple_for_csv, output_path)