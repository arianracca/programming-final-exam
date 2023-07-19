# **FINAL PRACTICAL WORK**

# Stage 1
"""
- Read the file 'coordenadas_provincias.csv' located at this address: \
  `
  https://drive.google.com/file/d/1WWvf6yn5oS1xarapKnwr3s8l2wKWtd7d/view?usp=drive_link
  `
- Create the listToDict function that converts the read data into a list of dictionaries.
- Call the above function with the data from the read file and verify that it returns the expected result.
- Create the constructor of the 'Province' class.
- Create an object of the 'Province' class.
"""

import os
import csv

print("STAGE 1:")

def open_file(file_path):
    """
    Read data from the input file and return
    a list with the information to be used in the task.
    """
    data_list = []
    with open(file_path, 'r') as data:
        reader = csv.reader(data)
        for row in reader:
            data_list.append(row)
        data_list.pop(0)
    return data_list

# Construct the file path for 'coordenadas_provincias.csv'
file_path = os.path.join(os.path.dirname(__file__), 'coordenadas_provincias.csv')

# Read and parse 'coordenadas_provincias.csv' as a list
province_data_list = open_file(file_path)

# Print the result of 'coordenadas_provincias' being parsed as a list
print("Result of 'coordenadas_provincias' being parsed as a list:")
print(province_data_list)


def list_to_dict(data_list):
    """
    Take the result of reading data as an argument and return a list
    of dictionaries.
    It has a default 'header' argument.
    The key is the value at index 0, and the associated values are a tuple
    with the rest of the elements in the list.
    """
    province_dictionary = {}
    for key, value1, value2 in data_list:
        province_dictionary[key] = (value1, value2)

    return province_dictionary

print("Result of processing the list of 'coordenadas_provincias' as a list of dictionaries:")
print(list_to_dict(province_data_list))

## Class Province

class Province:
    """
    This class represents a province.
    Attributes:
    name: str
    coordinates: tuple
    """
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates

    def __str__(self):
        return f"The province is: {self.name}, coordinates: {self.coordinates}"

# Examples:
print("Result of creating all the provinces found on the dataset")
province_dictionary = list_to_dict(province_data_list)
for name, coordinates in province_dictionary.items():
    province = Province(name, coordinates)  # creates the object as an instance of the class
    print(province)
