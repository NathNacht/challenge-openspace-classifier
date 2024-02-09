# read data from a .txt file

def read_input_file(filename):

    names = []

    with open(filename, "r") as file:
        names = [line.strip() for line in file.readlines()]

    return names        

def write_output_file(outputfile):
    ...

# testing the function
# output = read_input_file("./data/new_colleages.txt")
# print(output)
