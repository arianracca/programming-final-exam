# FINAL PRACTICAL WORK

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

print("""
      ########################################
      ##               STAGE 1               #
      ########################################
      """)

def open_file(file):
    """
    Read data from the input file and return
    a list with the information to be used in the task.
    """
    file_path = os.path.join(os.path.dirname(__file__), file)
    data_list = []
    with open(file_path, 'r') as data:
        reader = csv.reader(data)
        for row in reader:
            data_list.append(row)
        data_list.pop(0)
    return data_list

# Read and parse 'coordenadas_provincias.csv' as a list
province_data_list = open_file('coordenadas_provincias.csv')

# Print the result of 'coordenadas_provincias' being parsed as a list
# print("Result of 'coordenadas_provincias' being parsed as a list:")
# print(province_data_list)


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

# print("Result of processing the list of 'coordenadas_provincias' as a list of dictionaries:")
# print(list_to_dict(province_data_list))

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
print("""
-------------------------------------------------------------
Result of instantiate all the provinces found on the dataset
-------------------------------------------------------------
""")
province_dictionary = list_to_dict(province_data_list)
for name, coordinates in province_dictionary.items():
    province = Province(name, coordinates)  # creates the object as an instance of the class
    print(province)


# **FINAL PRACTICAL WORK**

# Stage 2
"""
*    Read the file located at this address:
https://datos.yvera.gob.ar/dataset/09679fe3-7379-481d-a36a-6b1e3d7374b1/archivo/9d4db872-0a51-4042-9daa-e55bc7a3044c
    as 'previaje.csv'
*    Propose data structures to work with each dataset. (They can be different)
*    Create the constructor of the 'Trip' class.
*    Create an object of the 'Trip' class.
*    Create a function 'relevant_data' that returns only the data of specific headers passed as parameters with the same data structure being used.
*    Create a function 'most_travelers' that calculates the province that received the most travelers in a given month and year as parameters.
*    Create a function 'calculate_average' that calculates the average number of travelers per trip in a specific origin province.
"""

#https://drive.google.com/file/d/1KWnSldEp76LoqMqNGyjLJYhEUlx1jIDJ/view?usp=sharing

import csv

print("""
      ########################################
      ##               STAGE 2               #
      ########################################
      """)
trip_list = open_file('viajes_origen_destino_mes.csv')

# Print the list
# print(trip_list)

## Class Trip
"""
1. Create the constructor of the Trip class. Its attributes will be:
- start_month
- origin_province
- destination_province
- trips
- travelers
- edition
2. Create a __str__ method that returns the trip data in a well-formatted way.
"""

class Trip:
    """
    This class represents a trip,
    containing the relevant data for analysis.
    """
    def __init__(self, start_month, origin_province, destination_province, trips, travelers, edition):
        self.start_month = start_month
        self.origin_province = origin_province
        self.destination_province = destination_province
        self.trips = trips
        self.travelers = travelers
        self.edition = edition

    def __str__(self):
        return f"Trip: start month: {self.start_month}, origin: {self.origin_province}, destination: {self.destination_province}, trips: {self.trips}, number of travelers: {self.travelers}, edition: {self.edition}"

# Examples:
# Create objects for each item in the trip_list
# for item in trip_list:
#     trip = Trip(item[0], item[1], item[2], int(item[3]), int(item[4]), item[5])  # creates the object as an instance of the class
#     print(trip)

## Functions

def trip_list_to_dict(trip_list):
    """
    This function returns a list of dictionaries of trips based on a given list.
    """
    trip_dict_list = []
    for item in trip_list:
        trip_dict = {
            "start_month": item[0],
            "origin_province": item[1],
            "destination_province": item[2],
            "trips": int(item[3]),
            "travelers": int(item[4]),
            "edition": item[5]
        }
        trip_dict_list.append(trip_dict)
    return trip_dict_list

trips = trip_list_to_dict(trip_list)
# print("Result of iteration on trips dataset, parsing them to dictionary")
# print(trips)

def relevant_data(trip_list, *headers):
    relevant_data_list = []
    for item in trip_list:
        relevant_data_dict = {}
        for header in headers:
            if header in ["start_month", "origin_province", "destination_province", "trips", "travelers", "edition"]:
                relevant_data_dict[header] = item[[x.lower() for x in ["start_month", "origin_province", "destination_province", "trips", "travelers", "edition"]].index(header)]
        if relevant_data_dict:
            relevant_data_list.append(relevant_data_dict)
    return relevant_data_list

# Example of use, filter by "trips" and "edition" columns
trips_edition = relevant_data(trip_list, "trips", "edition")
# print("Filter of columns selected by parameter")
# print(trips_edition)

# Calculate the province that received the most travelers in a given month and year.
def most_travelers(trip_list, month, year):
    month_str = str(month).zfill(2)  # Fill the month value with zeros on the left if less than a decade
    travelers_by_province = {}
    for item in trip_list:
        if item[0] == f'{year}-{month_str}':
            destination_province = item[2]
            travelers = int(item[4])
            if destination_province in travelers_by_province:
                travelers_by_province[destination_province] += travelers
            else:
                travelers_by_province[destination_province] = travelers
    if travelers_by_province:
        province_most_travelers = max(travelers_by_province, key=travelers_by_province.get)
        return province_most_travelers
    else:
        return "No data available."

# Example of use, print results for each month in 2022
print("""
--------------------------------------------------------------------------------
Result of selecting the province with the most travelers for each month in 2022
--------------------------------------------------------------------------------
""")
for month in range(1, 13):
    province = most_travelers(trip_list, month, 2022)
    print(f"Province with the most travelers in {month}/2022: {province}")

# Example of use, case when there is no data for a specific month (10-2023)
print("""
-----------------------------------------
Result of selecting a month without data
-----------------------------------------
""")
province = most_travelers(trip_list, 10, 2023)
print(f"Province with the most travelers in 10/2023: {province}")

# Calculate the average number of travelers per trip in a specific origin province.
def calculate_average(trip_list, origin_province):
    total_trips = 0
    total_travelers = 0
    for item in trip_list:
        if item[1] == origin_province:
            trips = int(item[3])
            travelers = int(item[4])
            total_trips += trips
            total_travelers += (trips + travelers)
    if total_trips > 0:
        average = int(total_travelers / total_trips)
        return average
    else:
        return "Not enough trips"

# Create a list of provinces to apply the average calculation
provinces = []
for element in trip_list:
    origin_province = element[1]
    # Add each province only once to the list
    if origin_province not in provinces:
        provinces.append(origin_province)

# Examples iterating through each province
print("""
-----------------------------------------------------------------------------------
Result of iteration for each province calculating the averages (travelers per trip)
-----------------------------------------------------------------------------------
""")
for province in provinces:
    average = calculate_average(trip_list, province)
    print(f"Average travelers per trip in {province}: {average}")

# **FINAL PRACTICAL WORK**

# Stage 3: New Analysis and Graph
"""
In this final stage, you will:
- Use the data from the 'previaje.csv' file to load a data structure that you consider appropriate for the data relevant to answer the following question: How many trips were made in each edition of the PreViaje program?
- Create a pie chart that shows the percentages of trips corresponding to each edition, relative to the total number of trips in the entire program. To do this, you should use the matplotlib and seaborn modules. Use the published examples as a guide.
"""

print("""
      ########################################
      ##               STAGE 3               #
      ########################################
      """)

# Filter relevant headers: trips and edition
trips_edition = relevant_data(trip_list, "trips", "edition")

def calculate_trips_per_edition(data_list):
    """
    Function that receives a list of dictionaries as a parameter
    and returns the number of trips per edition in a dictionary
    (key: edition, value: total trips)
    """
    trips_per_edition = {}

    for trip in data_list:
        edition = trip['edition']
        trips = int(trip['trips'])
        if edition in trips_per_edition:
            trips_per_edition[edition] += trips
        else:
            trips_per_edition[edition] = trips
    return trips_per_edition

trips_per_edition = calculate_trips_per_edition(trips_edition)
print("""
--------------------------------------------------------------------------------------
Result of creating a dictionary with the number of trips for each edition of PreViaje
--------------------------------------------------------------------------------------
""")
print(trips_per_edition)

## Graph

import matplotlib.pyplot as plt

def create_graph(dictionary):
    editions_list = list(dictionary.keys())
    trips_list = list(dictionary.values())

    # Create the graph
    plt.figure(figsize=(8, 8))
    plt.pie(trips_list, labels=editions_list, autopct="%0.1f%%", startangle=35)

    # Set title
    plt.title("Number of Trips per Edition of PreViaje")

    # Show the graph
    plt.show()

print("""
------------------------------------------
| Figure 1 - Created and shown on screen |
------------------------------------------
""")
print("Close the Figure 1 to continue")
create_graph(trips_per_edition)

# DEFENSE OF PRACTICAL WORK

# Write a function that prompts the user to choose an edition of the Previaje program
# and then shows a bar graph indicating the total number of trips per destination province for that edition.

print("""
      ########################################
      ##               STAGE 4               #
      ########################################
      """)

def graph_total_travelers_per_destination_province_for_edition(trip_list):
    """
    Function that takes an input of a Previaje edition and prints a
    graph of travelers per province for that edition.

    Parameters:
    trip_list (list): List of dictionaries containing the trip data.

    Returns:
    None
    """

    # Control structure to handle user input for the Previaje edition
    while True:
        selected_edition = input("""Choose the Previaje edition you want to know
    the total number of travelers per destination province and graph.
    Options:
    previaje 1
    previaje 2
    previaje 3
    """).lower()

        # Validate the user input to ensure a valid edition is chosen
        if selected_edition in ["previaje 1", "previaje 2", "previaje 3"]:
            break
        else:
            print("Invalid edition. Please choose from the available options.")

    # Filter relevant headers: travelers, destination, and edition
    relevant_data_list = relevant_data(trip_list, "destination_province", "travelers", "edition")

    travelers_per_edition_destination = {}
    # Calculate the total number of travelers per destination province for the chosen edition
    for trip in relevant_data_list:
        if trip['edition'] == selected_edition:
            travelers = int(trip['travelers'])
            destination_province = trip['destination_province']
            if destination_province in travelers_per_edition_destination:
                travelers_per_edition_destination[destination_province] += travelers
            else:
                travelers_per_edition_destination[destination_province] = travelers

    # Extract data for the graph
    province_list = list(travelers_per_edition_destination.keys())
    travelers_list = list(travelers_per_edition_destination.values())

    # Create and display the bar graph
    print("""
------------------------------------------
| Figure 2 - Created and shown on screen |
------------------------------------------
""")
    fig, ax = plt.subplots()
    ax.bar(province_list, travelers_list, width=0.7, edgecolor="white", linewidth=0.7)
    plt.xticks(rotation=90)
    plt.title(f"Total Travelers per Destination Province - {selected_edition.capitalize()}")
    plt.xlabel("Destination Province")
    plt.ylabel("Total Travelers")
    plt.tight_layout()
    plt.show()


graph_total_travelers_per_destination_province_for_edition(trip_list)
