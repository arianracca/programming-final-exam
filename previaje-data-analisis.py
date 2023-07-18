# **TRABAJO PRÁCTICO FINAL**


# Etapa 1
"""
- Leer el archivo 'coordenadas_provincias.csv' que se encuentra en esta dirección: \
  `
  https://drive.google.com/file/d/1WWvf6yn5oS1xarapKnwr3s8l2wKWtd7d/view?usp=drive_link
  `
- Crear la función listToDict que se encarga de convertir los datos leídos a una lista de diccionarios.
- Llamar a la función anterior con los datos del archivo leído y verificar que devuelva lo pedido.
- Crear el constructor de la clase 'Provincia'
- Crear un objeto de la clase 'Provincia'
"""
import os
import csv

print("STAGE 1:")
def openFile(file_path):
  """
    Lee datos del archivo de entrada y retorna
    una lista con la información que se va a usar en el trabajo.
  """
  lista = []
  with open(file_path, 'r') as datos:
    lectura = csv.reader(datos)
    for fila in lectura:
      lista.append(fila)
    lista.pop(0)

    return lista
  
file_path = os.path.join(os.path.dirname(__file__), 'coordenadas_provincias.csv')
lista_provincias_coordenadas = openFile(file_path)
print("Result of coordenadas_provincias being parsed as a list:")
print(lista_provincias_coordenadas)


