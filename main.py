import sys
from utils.openspace import Openspace
from utils.file_utils import read_input_file

def main():
    """ 
    reads an input file with names and organizes an openspace
    writes the output to a csv file
    """
    
    # Read names from a text file by providing an input filename manually

    # input_file = "./data/" + input("Provide a valid filename (within the data folder): ")
    # # # Read names from a text file
    # input_names = read_input_file(input_file)

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "new_colleagues.txt"
    
        
    input_file_path = "./data/" + input_file
    input_names = read_input_file(input_file_path)

    
    # Create the 6 tables with each 4 seats
    openspace = Openspace(number_of_tables=6)

    openspace.organize(input_names)
    openspace.display()

    output_file = "./data/organized_openspace.csv"

    openspace.export_to_csv(output_file)
  
if __name__ == "__main__":
    main()
