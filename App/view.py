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
from DISClib.DataStructures import listiterator as li
from DISClib.ADT import map as mp
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

archivo_casting = "Data\MoviesCastingRaw-small.csv"
archivo_details = "Data\SmallMoviesDetailsCleaned.csv"



# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________
def printProductoraData(productor1):
    """
    Imprime las peliculas de nombre determinado
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

def printDirectorData(director1,cont):
    """
    Imprime los libros de un autor determinado
    """
    if director1:
        
        print('\nSe encontraron {} directores con el parametro de busqueda. '.format(lt.size(director1)))
        iterator1 =it.newIterator(director1)
        while it.hasNext(iterator1):
            director=it.next(iterator1)
            print('\nProductor encontrado: ' + director['name'])
            print('Total de peliculas: ' + str(lt.size(director['movies'])))
            iterator = it.newIterator(director['movies'])
            promedio=0
            print("")
            print("{0:<50}{1:<20}{2:>8}".format("Titulo: ","Promedio:","Actor principal:"))

            while it.hasNext(iterator):
                movie = it.next(iterator)
                mov=movie['id']
                detail=controller.getMovieById(cont['id'], mov)
                print("{0:<50}{1:<20}{2:>8}".format(detail['title'],detail['vote_average'],movie['actor1_name']))
                promedio+= float(detail['vote_average'])
                promedio+=0            
            promedio *= 1/lt.size(director['movies'])
            print("\nCalificación promedio del director: {:.2f}/10".format(promedio))
            
    else:
        print('No se encontro el autor')

def printActorData(actor1,cont):
    """
    Imprime los libros de un autor determinado
    """
    if actor1:
        print('\nSe encontraron {} actores con el parametro de busqueda. '.format(lt.size(actor1)))
        iterator1 =it.newIterator(actor1)
        while it.hasNext(iterator1):
            actor=it.next(iterator1)
            print('\nActor encontrado: ' + actor['name'])
            print('Total de peliculas: ' + str(lt.size(actor['movies'])))
            iterator = it.newIterator(actor['movies'])
            promedio=0
            print("")
            print("{0:<50}{1:<20}{2:>8}".format("Titulo: ","Promedio:","Director:"))

            while it.hasNext(iterator):
                movie = it.next(iterator)
                mov=movie['id']
                detail=controller.getMovieById(cont['id'], mov)
                print("{0:<50}{1:<20}{2:>8}".format(detail['title'],detail['vote_average'],movie['director_name']))
                promedio+= float(detail['vote_average'])
            promedio *= 1/lt.size(actor['movies'])
            print("\nCalificación promedio del actor: {:.2f}/10".format(promedio))
    else:
        print('No se encontro el autor')

def printGenreData(genero1,cont):
    if genero1:
        print('\nSe encontraron {} generos con el parametro de busqueda. '.format(lt.size(genero1)))
        iterator1 =it.newIterator(genero1)
        while it.hasNext(iterator1):
            genero=it.next(iterator1)
            print('\nGenero encontrado: ' + genero['name'])
            print('Total de peliculas: ' + str(lt.size(genero['movies'])))
            iterator = it.newIterator(genero['movies'])
            promedio=0
            print("")
            print("{0:<50}{1:<20}{2:>8}".format("Titulo: ","Promedio:","Actor principal:"))
            while it.hasNext(iterator):
                movie = it.next(iterator)
                mov=movie['id']
                detail=controller.getMovieById(cont['id'], mov)
                print("{0:<50}{1:<20}{2:>8}".format(detail['title'],detail['vote_average'],detail['genres']))
                promedio+= float(detail['vote_average'])
                promedio+=0            
            promedio *= 1/lt.size(genero['movies'])
            print("\nCalificación promedio del genero: {:.2f}/10".format(promedio))
            
    else:
        print('No se encontro el genero')

def printCountryData(country1,cont):
    if country1:
        
        print('\nSe encontraron {} paises con el parametro de busqueda. '.format(lt.size(country1)))
        iterator1 =it.newIterator(country1)
        while it.hasNext(iterator1):
            country=it.next(iterator1)
            print('\nPaíz encontrado: ' + country['name'])
            print('Total de peliculas: ' + str(lt.size(country['movies'])))
            iterator = it.newIterator(country['movies'])
            promedio=0
            print("")
            print("{0:<50}{1:<20}{2:>8}".format("Titulo: ","Promedio:","Actor principal:"))

            while it.hasNext(iterator):
                movie = it.next(iterator)
                mov=movie['id']
                detail=controller.getMovieByIdCasting(cont['id_casting'], mov)
                print("{0:<50}{1:<20}{2:>8}".format(movie['title'],movie['release_date'],detail['director_name']))
                promedio+= float(movie['vote_average'])
                promedio+=0            
            promedio *= 1/lt.size(country['movies'])
            print("\nCalificación promedio del paíz: {:.2f}/10".format(promedio))
            
    else:
        print('No se encontro el paíz')

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
                tamano_catalogo = input('Que tamaño de catalogo desea cargar: \n1- 2000 peliculas\n2- 300000+ peliculas\n') #leer opción ingresada
                if tamano_catalogo== "1":
                    archivo_casting = "Data\MoviesCastingRaw-small.csv"
                    archivo_details = "Data\SmallMoviesDetailsCleaned.csv"
                elif tamano_catalogo=="2":
                    archivo_casting = "Data\AllMoviesCastingRaw.csv"
                    archivo_details = "Data\AllMoviesDetailsCleaned.csv"
                else:
                    print("Opción invalida. Se cargará la versión 1.")
                    archivo_casting = "Data\MoviesCastingRaw-small.csv"
                    archivo_details = "Data\SmallMoviesDetailsCleaned.csv"

                t1=process_time() 
                print("Inicializando Catálogo ....")
                # cont es el controlador que se usará de acá en adelante
                cont = controller.initCatalog()
                print("Cargando información de los archivos ....")
                controller.loadData(cont, (archivo_details),(archivo_casting))
                t2=process_time()
                print ("Tiempo de carga: {}".format(t2-t1))
                print('Numero peliculas cargadas: ' + str(controller.detailSize(cont)))
                #print(controller.encontrarElemento(cont,1))
                #print(controller.encontrarElemento(cont,2000))
            
            elif int(inputs[0]) ==2: #opcion 2
                print("Se encontraron {} productoras".format(controller.productorasSize(cont)))
                productorname = input("Nombre de la productora a buscar: ")
                t1=process_time()
                productorinfo = controller.getMoviesByProductora(cont, productorname)
                printProductoraData(productorinfo)
                t2=process_time()
                print ("Tiempo de carga: {}".format(t2-t1))
            
            elif int(inputs[0])==3: #opcion 3
                print("Se encontraron {} directores".format(controller.directoresSize(cont)))
                directorname = input("Nombre de la productora a buscar: ")
                t1=process_time()
                directorinfo = controller.getMoviesByDirector(cont, directorname)
                printDirectorData(directorinfo,cont)
                t2=process_time()
                print ("Tiempo de carga: {}".format(t2-t1))
            
            elif int(inputs[0])==4: #opcion 4
                print("Se encontraron {} actores".format(controller.actoresSize(cont)))
                actorname = input("Nombre del actor a buscar: ")
                t1=process_time()
                actorinfo = controller.getMoviesByActor(cont, actorname)
                printActorData(actorinfo,cont)
                t2=process_time()
                print ("Tiempo de carga: {}".format(t2-t1))
            
            elif int(inputs[0])==5: #opcion 5
                print("Se encontraron {} generos".format(controller.genresSize(cont)))
                genrename = input("Nombre del genero a buscar: ")
                t1=process_time()
                genreinfo = controller.getMoviesByGenre(cont, genrename)
                printGenreData(genreinfo,cont)
                t2=process_time()
                print ("Tiempo de carga: {}".format(t2-t1))

            elif int(inputs[0])==6: #opcion 6
                print("Se encontraron {} paises".format(controller.countriesSize(cont)))
                countryname = input("Nombre de la productora a buscar (El nombre del paíz está en ingles) : ")
                t1=process_time()
                countryinfo = controller.getMoviesByCountry(cont, countryname)
                printCountryData(countryinfo,cont)
                t2=process_time()
                print ("Tiempo de carga: {}".format(t2-t1))
            
            elif int(inputs[0])==0:
                sys.exit(0)
                
if __name__ == "__main__":
    main()