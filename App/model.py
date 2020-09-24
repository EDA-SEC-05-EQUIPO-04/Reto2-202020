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
import config
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator as li
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def newCatalog():
    catalog = {'details': None,
               'casting': None, 'productoras': None, 'directores':None, 'id':None,'actores':None,'genres':None,'country':None
                }

    catalog['details'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    catalog['casting'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    catalog['productoras'] = mp.newMap(36000,
                                   loadfactor=0.4,
                                   comparefunction=compareMapName)
    catalog['directores'] = mp.newMap(85950,
                                   loadfactor=0.4,
                                   comparefunction=compareMapName)
    catalog['actores'] = mp.newMap(260900,
                                   loadfactor=0.4,
                                   comparefunction=compareMapName)                               
    catalog['id'] = mp.newMap(329050,
                                   loadfactor=0.4,
                                   comparefunction=compareMapId)
    catalog['id_casting'] = mp.newMap(329050,
                                   loadfactor=0.4,
                                   comparefunction=compareMapId)
    catalog['genres'] = mp.newMap(25,
                                   loadfactor=0.4,
                                   comparefunction=compareMapId)
    catalog['country'] = mp.newMap(240,
                                   loadfactor=0.4,
                                   comparefunction=compareMapId)

    return catalog

def newProductora(name):
    author = {'name': "", "movies": None,  "average_rating": 0}
    author['name'] = name
    author['movies'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    return author

def newDirector(name):
    author = {'name': "", "movies": None,  "average_rating": 0}
    author['name'] = name
    author['movies'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    author['details'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    return author

def newActor(name):
    author = {'name': "", "movies": None,  "average_rating": 0}
    author['name'] = name
    author['movies'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    author['details'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    return author

def newId(name):
    author = {'id': "", "movies": None}
    author['id'] = name
    author['movies'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    return author

def newIdCasting(name):
    author = {'id': "", "movies": None}
    author['id'] = name
    author['movies'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    return author

def newGenre(name):
    author = {'name': "", "movies": None,  "average_rating": 0}
    author['name'] = name
    author['movies'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    return author

def newCountry(name):
    author = {'name': "", "movies": None,  "average_rating": 0}
    author['name'] = name
    author['movies'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    return author

# Funciones para agregar informacion al catalogo
def addDetails(catalog, movie):
    lt.addLast(catalog['details'], movie)
    
def addCasting(catalog, movie):
   lt.addLast(catalog['casting'], movie)

def addProductoraMovie(catalog, authorname, movie):
    authors = catalog['productoras']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        entry = mp.get(authors, authorname)
        author = me.getValue(entry)
    else:
        author = newProductora(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(author['movies'], movie)

def addDirectorMovie(catalog, authorname, movie):
    authors = catalog['directores']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        entry = mp.get(authors, authorname)
        author = me.getValue(entry)
    else:
        author = newDirector(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(author['movies'], movie)

def addGenreMovie(catalog, authorname, movie):
    authors = catalog['genres']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        entry = mp.get(authors, authorname)
        author = me.getValue(entry)
    else:
        author = newGenre(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(author['movies'], movie)

def addCountryMovie(catalog, authorname, movie):
    authors = catalog['country']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        entry = mp.get(authors, authorname)
        author = me.getValue(entry)
    else:
        author = newCountry(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(author['movies'], movie)

def addActorMovie(catalog, authorname, movie):
    authors = catalog['actores']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        entry = mp.get(authors, authorname)
        author = me.getValue(entry)
    else:
        author = newActor(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(author['movies'], movie)

def addIdMovie(catalog, authorname, movie):
    authors = catalog['id']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        return "Hay dos peliculas con mismo id, compruebe sus datos."
    else:
        author = movie
        mp.put(authors, authorname, author)

def addIdCastingMovie(catalog, authorname, movie):
    authors = catalog['id_casting']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        return "Hay dos peliculas con mismo id, compruebe sus datos."
    else:
        author = movie
        mp.put(authors, authorname, author)   
    
def addId(catalog, authorname, movie):
    authors = catalog['id']
    mp.put(authors, authorname, movie)

def addIdCasting(catalog, authorname, movie):
    authors = catalog['id']
    mp.put(authors, authorname, movie)    

def addGenre(catalog,authorname,movie):
    authors = catalog['genres']
    mp.put(authors, authorname, movie)

def addCountry(catalog,authorname,movie):
    authors = catalog['country']
    mp.put(authors, authorname, movie)

# ==============================
# Funciones de consulta
# ==============================
#Funciones de tamaño
def productorasSize(catalog):
    return mp.size(catalog['productoras'])

def directoresSize(catalog):
    return mp.size(catalog['directores'])

def actoresSize(catalog):
    return mp.size(catalog['actores'])

def genresSize(catalog):
    return mp.size(catalog['genres'])

def countriesSize(catalog):
    return mp.size(catalog['country'])

def detailSize(catalog):
    return lt.size(catalog['details'])

def castingSize(catalog):
    return mp.size(catalog['casting'])

#Funcion inicial
def encontrarElemento(catalog, posicion):
    primero = lt.getElement(catalog['details'],posicion)
    respuesta = "El título de la película: " + primero["original_title"] + ", " + "La fecha de estreno: " + primero["release_date"] + ", " + "El promedio de la votación: " + primero["vote_average"]+ ", " +"Número de votos: " + primero["vote_count"]+ ", " + "Idioma de la película: " + primero["original_language"]
    return respuesta

#Funciones get

def getMovieById(id_lista,lista):
    entry = mp.get(lista, id_lista)
    author = me.getValue(entry)
    return author

def getMovieByIdCasting(id_lista,lista):
    entry = mp.get(lista, id_lista)
    author = me.getValue(entry)
    return author

def getMovieByGenres1(id_lista,lista):
    return mp.get(lista, id_lista)

def getMoviesByProductora(catalog, producername):
    
    lst=mp.keySet(catalog['productoras'])
    n=4
    iterator=li.newIterator(lst)
    lista_producers=lt.newList()
    while li.hasNext(iterator):
        element=li.next(iterator)
        if  producername.lower() in element.lower():
            producer = mp.get(catalog['productoras'], element)
            if producer:
                #return me.getValue(producer)
                lt.addLast(lista_producers,me.getValue(producer))
    if lt.isEmpty(lista_producers):
        return None
    return lista_producers
    #return None

def getMoviesByGenre(catalog, producername):  
    lst=mp.keySet(catalog['genres'])
    iterator=li.newIterator(lst)
    lista_producers=lt.newList()
    while li.hasNext(iterator):
        element=li.next(iterator)
        if  producername.lower() in element.lower():
            producer = mp.get(catalog['genres'], element)
            if producer:
                #return me.getValue(producer)
                lt.addLast(lista_producers,me.getValue(producer))
    if lt.isEmpty(lista_producers):
        return None
    return lista_producers
    #return None    

def getMoviesByDirector(catalog, producername):
    
    lst=mp.keySet(catalog['directores'])
    iterator=li.newIterator(lst)
    lista_producers=lt.newList()
    while li.hasNext(iterator):
        element=li.next(iterator)
        if  producername.lower() in element.lower():
            producer = mp.get(catalog['directores'], element)
            if producer:
                #return me.getValue(producer)
                lt.addLast(lista_producers,me.getValue(producer))
    if lt.isEmpty(lista_producers):
        return None
    return lista_producers
    #return None    

def getMoviesByCountry(catalog, producername):
    
    lst=mp.keySet(catalog['country'])
    iterator=li.newIterator(lst)
    lista_producers=lt.newList()
    while li.hasNext(iterator):
        element=li.next(iterator)
        if  producername.lower() in element.lower():
            producer = mp.get(catalog['country'], element)
            if producer:
                #return me.getValue(producer)
                lt.addLast(lista_producers,me.getValue(producer))
    if lt.isEmpty(lista_producers):
        return None
    return lista_producers
    #return None    

def getMoviesByActor(catalog, producername):
    
    lst=mp.keySet(catalog['actores'])
    iterator=li.newIterator(lst)
    lista_producers=lt.newList()
    while li.hasNext(iterator):
        element=li.next(iterator)
        if  producername.lower() in element.lower():
            producer = mp.get(catalog['actores'], element)
            if producer:
                #return me.getValue(producer)
                lt.addLast(lista_producers,me.getValue(producer))
    if lt.isEmpty(lista_producers):
        return None
    return lista_producers

# ==============================
# Funciones de Comparacion
# ==============================

def compareMovieIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapName(keyname, name):
    nameentry = me.getKey(name)
    if (keyname == nameentry):
        return 0
    elif (keyname > nameentry):
        return 1
    else:
        return -1

def compareMapId(keyname, name):
    nameentry = me.getKey(name)
    if (keyname == nameentry):
        return 0
    elif (keyname > nameentry):
        return 1
    else:
        return -1