# Created by Efrain Noa         May 31, 2017
import io
# Created by Efrain Noa
# Description: This code read lines found into a csv file
# How to use:
# Input: 1) provide a csv file. It should have hree columns of number separated by comma
# 
# Output: 1) It classifies and sortes into variables to plop such as:
#           x_data, and y_data, z_data
# ---------------------------------------------------------------------------

# Import modules
import re
from itertools import islice # import a module to read lines (line by line)
import sort_function as sf

def setup_inputs():
    # Set up file name
    #file_name = "E:\\hidro\\M_J_Python\\python_class\\Mod_1\\database\\txt_files\\two_columns_data.txt"
    file_name = "E:\\Spring 2017\\GEOG-572\\Database_project\\realdata\\odtrial.csv"
    
    print "File name: ",file_name
    line_to_read = 0
    x_data, y_data, z_data = read_lines_from_a_file(file_name) # <---  call function

    print x_data, y_data, z_data

    x,y,z = sf.sort_list (x_data, y_data, z_data) # <---  call function
    
def read_lines_from_a_file(file_name):

    num_lines = sum(1 for line in open(file_name)) # it gets number of rows of a txt file

    x_data = []; y_data = []; z_data = []

    with open(file_name) as lines:
        line_values = lines.read().split("\n") #read all line values as list. Each txt.file line is a value into the list
        #print "### (to verify) All line values: ", all_line_value
        line_values.pop() #remove the last value of the list, which in this case is empty
        print len (line_values)
        
        for line in line_values:
            line_split = re.split(',',line)

            x_value = line_split[0]; y_value = line_split[1]; z_value = line_split[2]
            x_data.append(x_value); y_data.append(y_value); z_data.append(z_value)
        
    x_data = map(float, x_data) # convert a list of strings into list of float
    y_data = map(float, y_data)
    z_data = map(float, z_data)

    print "end read_line function"
    print
    return x_data, y_data, z_data

if __name__ == "__main__":
    setup_inputs()
