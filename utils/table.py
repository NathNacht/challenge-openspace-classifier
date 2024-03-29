class Seat():
    """
    Represents a seat on a table.    
    """
    def __init__(self, free: bool, occupant: str):
        """ 
        :param free (bool): Indicates whether the seat is currently unoccupied (True) or occupied (False).
        :param occupant (str): The name of the occupant of the seat. Empty string if the seat is unoccupied.
        """
        self.free = free
        self.occupant = occupant
    
    def __str__(self):
        if self.free:
            return "This seat is free"
        else:
            return f"This seat is occupied by {self.occupant}"
        
    def set_occupant(self, name):
        """ 
        set_occupant(name): sets the occupant of the seat to the specified name and
        updates the free status accordingly

        :param name: name of the occupant
        """
        self.occupant = name
        self.free = False

    def remove_occupant(self):
        """ 
        removes the current occupant from the seat and marks the seat as free
        """
        self.occupant = None
        self.free = True

class Table():
    """ 
    Represents a table with a specified capacity.
    """
    def __init__(self, capacity:int):
        """ 
        :param capacity (int): The maximum number of seats the table can accommodate.
        """
        self.capacity = capacity
        # Initialize seats as a list containing Seat objects with specified capacity
        self.seats = [Seat(free=True, occupant=None) for _ in range(capacity)]

    def __str__(self):
        x = "\n".join(str(seat) for seat in self.seats)
        return f"Table with capacity {self.capacity}, {self.left_capacity()} seats left \n" + x
        
    def has_free_spot(self) -> bool:
        """       
        has_free_spot(): Checks if there is at least one free seat on the table.

        :return: True if there is at least one free seat on the table, False otherwise.
        """
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat_name(self, name) -> bool:
        """
        assign_seat_name(name): Assigns the specified name to an available seat on the table.

        :param name: name of the occupant
        :return: True if a seat was assigned, False otherwise.
        """
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self) -> int:
        """
        left_capacity(): Returns the number of free seats remaining on the table.

        :return: The number of free seats remaining on the table.
        """
        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
        return count