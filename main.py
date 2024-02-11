import sys
from utils.openspace import Openspace
from utils.file_utils import read_input_file

def main():
    """ 
    reads an input file with names and organizes an openspace
    writes the output to a csv file
    """
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        print("The input file that you have provided is: " + input_file)
    else:
        input_file = "new_colleagues.txt"
        print("As you did not specify any input file, the default one will be used: " + input_file)
        print("In case you want to use your own inputfile, place it under the data folder and provide the filename as an argument")
    
        
    input_file_path = "./data/" + input_file
    input_names = read_input_file(input_file_path)
    
    # Create the 6 tables with each 4 seats
    openspace = Openspace(number_of_tables=6)

    openspace.organize(input_names)
    openspace.display()

    output_file = "./data/organized_openspace.csv"

    openspace.store(output_file)

    print("The organized openspace has been saved to: " + output_file)
  
if __name__ == "__main__":
    main()
