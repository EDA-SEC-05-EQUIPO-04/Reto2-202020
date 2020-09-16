"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config
from time import process_time 
"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

#archivo_casting = "Data\MoviesCastingRaw-small.csv"
archivo_casting = "Data\AllMoviesCastingRaw.csv"
archivo_details = "Data\AllMoviesDetailsCleaned.csv"
#archivo_details = "Data\SmallMoviesDetailsCleaned.csv"



# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________
def printProductoraData(productor1):
    """
    Imprime los libros de un autor determinado
    """
    if productor1:
        print('\nSe encontraron {} productoras con el parametro de busqueda. '.format(lt.size(productor1)))
        iterator1 =it.newIterator(productor1)
        while it.hasNext(iterator1):
            productor=it.next(iterator1)
            print('\nProductor encontrado: ' + productor['name'])
            print('Total de peliculas: ' + str(lt.size(productor['movies'])))
            iterator = it.newIterator(productor['movies'])
            promedio=0
            print("")
            print("{0:<50}{1:<20}{2:>8}".format("Titulo: ","Promedio:","Productora:"))

            while it.hasNext(iterator):
                movie = it.next(iterator)
            
                print("{0:<50}{1:<20}{2:>8}".format(movie['original_title'], movie['vote_average'], movie['production_companies']))
                promedio+= float(movie['vote_average'])
            promedio *= 1/lt.size(productor['movies'])
            print("\nCalificación promedio de la productora: {:.2f}/10".format(promedio))
    else:
        print('No se encontro el autor')



# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Descubrir productoras de cine")
    print("3- Conocer a un director")
    print("4- Conocer a un actor ")
    print("5- Entender un género cinematográfico")
    print("6- Encontrar películas por país ")
    print("0- Salir")


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados
    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """

    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs = input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0]) ==1: #opcion 1
                t1=process_time() 
                print("Inicializando Catálogo ....")
                # cont es el controlador que se usará de acá en adelante
                cont = controller.initCatalog()
                print("Cargando información de los archivos ....")
                controller.loadData(cont, (archivo_details),(archivo_casting))
                t2=process_time()
                print ("Tiempo de carga: {}".format(t2-t1))
                print('Numero peliculas cargadas: ' + str(controller.detailSize(cont)))
                print(controller.encontrarElemento(cont,1))
                print(controller.encontrarElemento(cont,2000))
            elif int(inputs[0]) ==2: #opcion 2
                print("Se encontraron {} productoras".format(controller.productorasSize(cont)))
                productorname = input("Nombre de la productora a buscar: ")
                t1=process_time()
                productorinfo = controller.getMoviesByProductora(cont, productorname)
                printProductoraData(productorinfo)
                t2=process_time()
                print ("Tiempo de carga: {}".format(t2-t1))
            elif int(inputs[0])==3: #opcion 3
                pass
            elif int(inputs[0])==4: #opcion 4
                pass
            elif int(inputs[0])==5: #opcion 5
                pass
            elif int(inputs[0])==0:
                sys.exit(0)
                
if __name__ == "__main__":
    main()