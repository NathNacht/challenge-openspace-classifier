import csv

def read_input_file(filename):
    """
    read data from a .txt file into a list
    """
    names = []

    with open(filename, "r") as file:
        names = [line.strip() for line in file.readlines()]

    return names        
    
def write_to_csv(tuple_for_csv, filename):
    """
    Writes the table information to a CSV file.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tuple_for_csv)

