# Practical Work

## Description

This program consists of multiple stages to process and analyze data from different datasets related to the "Previaje" program. The goal is to create various classes, functions, and graphs to explore the data and answer specific questions.

## Stages

### Stage 1

- Read the file [coordenadas_provincias.csv](https://drive.google.com/file/d/1WWvf6yn5oS1xarapKnwr3s8l2wKWtd7d/view?usp=drive_link): 
- Create the `listToDict` function that converts the read data into a list of dictionaries.
- Call the above function with the data from the read file and verify that it returns the expected result.
- Create the constructor of the 'Provincia' class.
- Create an object of the 'Provincia' class.

### Stage 2

- Read this [file](https://datos.yvera.gob.ar/dataset/09679fe3-7379-481d-a36a-6b1e3d7374b1/archivo/9d4db872-0a51-4042-9daa-e55bc7a3044c) as 'previaje.csv'.
- Propose data structures to work with each dataset (could be different for each dataset).
- Create the constructor of the 'Viaje' class.
- Create an object of the 'Viaje' class.
- Create a function 'datos_relevantes' that returns data for specific headers passed as parameters.
- Create a function 'mas_viajeros' that calculates the province that received the most travelers in a given month and year as parameters.
- Create a function 'calcular_promedio' that calculates the average number of travelers per trip for a specific origin province.

### Stage 3: New Analysis and Graph

- Use the data from the 'previaje.csv' file to load a data structure with the data relevant to answer the question: How many trips were made in each edition of the PreViaje program?
- Create a pie chart that shows the percentages of trips corresponding to each edition, relative to the total number of trips in the entire program. Use the matplotlib and seaborn modules for the graph.

### Stage 4: Graph

- Create a bar graph that shows the total number of trips per destination province for a chosen edition of the Previaje program.

### Stage 5: Graph

- Write a function that prompts the user to choose an edition of the Previaje program and then shows a bar graph indicating the total number of trips per destination province for that edition.

## How to Run

1. Clone this repository to your local machine.
2. Install the required libraries using:
`pip install -r requirements.txt`
3. Run the program using a Python interpreter:
`python main.py`
4. Follow the instructions in the program to perform different stages of the practical work.

## Requirements

- Python 3.5 or higher.
- Libraries: csv, os, matplotlib, seaborn.

## License

This project is licensed under the [MIT License](LICENSE).


