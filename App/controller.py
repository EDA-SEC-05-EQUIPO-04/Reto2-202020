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

import config as cf
from App import model
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from time import process_time 
"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(catalog, Moviesfile,Castingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadDetails(catalog, Moviesfile)
    loadCastings(catalog, Castingfile)

def loadDetails(catalog, Moviesfile):
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open( Moviesfile, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                model.addDetails(catalog, row)
                authors = row['production_companies']  # Se obtienen los autores
                model.addProductoraMovie(catalog, authors, row)   
                name_id=row['id']
                model.addIdMovie(catalog,name_id,row)
                genres=row['genres']
                genres=genres.split("|")
                for genre in genres:
                    model.addGenreMovie(catalog, genre, row)
                countries=row['production_countries']     
                countries=countries.split("|")
                for country in countries:
                    model.addCountryMovie(catalog, country, row)          
    except:
        print("Hubo un error con la carga del archivo")
    
    return 0

def loadCastings(catalog, Moviesfile):
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open( Moviesfile, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                model.addCasting(catalog, row)   
                authors = row['director_name']  # Se obtienen los autores
                model.addDirectorMovie(catalog, authors, row)
                for i in range (1,6):
                    author_name="actor{}_name".format(i)
                    model.addActorMovie(catalog, row[author_name], row)    
                name_id=row['id']
                model.addIdCastingMovie(catalog,name_id,row)              
    except:
        print("Hubo un error con la carga del archivo")
    
    return 0

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def productorasSize(catalog):
    return model.productorasSize(catalog)

def directoresSize(catalog):
    return model.directoresSize(catalog)

def genresSize(catalog):
    return model.genresSize(catalog)

def actoresSize(catalog):
    return model.actoresSize(catalog)

def countriesSize(catalog):
    return model.countriesSize(catalog)

def getMovieById(id,lista):
    return model.getMovieById(lista,id)

def getMovieByIdCasting(id,lista):
    return model.getMovieByIdCasting(lista,id)

def getMoviesByProductora(catalog, productoraname):
    productorainfo = model.getMoviesByProductora(catalog, productoraname)
    return productorainfo

def getMoviesByDirector(catalog, directorname):
    directorinfo = model.getMoviesByDirector(catalog, directorname)
    return directorinfo

def getMoviesByActor(catalog, directorname):
    directorinfo = model.getMoviesByActor(catalog, directorname)
    return directorinfo

def getMoviesByGenre(catalog, directorname):
    genreinfo = model.getMoviesByGenre(catalog, directorname)
    return genreinfo

def getMoviesByCountry(catalog, directorname):
    directorinfo = model.getMoviesByCountry(catalog, directorname)
    return directorinfo

def detailSize(catalog):
    return model.detailSize(catalog)

def castingSize(catalog):
    return model.castingSize(catalog)

def encontrarElemento(camino,posicion):
    return model.encontrarElemento(camino,posicion)

