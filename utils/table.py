# This file defines a table with how many seats it encompasses

class Seat():
    """
    Represents a seat on a table.

    Attributes:
        free (bool): Indicates whether the seat is currently unoccupied (True) or occupied (False).
        occupant (str): The name of the occupant of the seat. Empty string if the seat is unoccupied.
    
    Methods:
        set_occupant(name): Sets the occupant of the seat to the specified name and updates the free status accordingly.
        remove_occupant(): Removes the current occupant from the seat and marks the seat as free.
    """
    def __init__(self, free: bool, occupant: str):
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name):
        self.occupant = name
        self.free = False

    def remove_occupant(self):
        self.occupant = ""
        self.free = True
    

class Table():
    """
    Represents a table with a specified capacity.

    Attributes:
        capacity (int): The maximum number of seats the table can accommodate.
        seats (list): A list containing Seat objects representing the seats of the table.

    Methods:
        has_free_spot(): Checks if there is at least one free seat on the table.
        assign_seat_name(name): Assigns the specified name to an available seat on the table.
        left_capacity(): Returns the number of free seats remaining on the table.
    """
    def __init__(self, capacity:int):
        self.capacity = capacity
        # Initialize seats as a list containing Seat objects with specified capacity
        self.seats = [Seat(free=True, occupant="") for _ in range(capacity)]
    
    def has_free_spot(self) -> bool:
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat_name(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self) -> int:
        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
        return count

# Example usage:
table = Table(4)
print(table.has_free_spot())  # Output: True
table.assign_seat_name("John")
table.assign_seat_name("Alice")
print(table.left_capacity())  # Output: 2

