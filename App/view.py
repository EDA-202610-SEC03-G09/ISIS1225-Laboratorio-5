"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 * Lina Ojeda
 """

import sys
import App.logic as logic
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as lt

data_structure = None

"""
La vista se encarga de la interacción con el usuario
Presenta el menú de opciones y por cada selección
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_logic(data_structure):
    """
    Se crea una instancia del controlador
    """
    control = logic.new_logic(data_structure)
    return control


def print_menu():
    """
    Menu de usuario
    """
    print("Bienvenido")
    print("0- Escoger tipo de estructura de datos (Array_list o Single_linked_list)")
    print("1- Cargar información en el catálogo")
    print("2- Consultar la información de un libro")
    print("3- Consultar los libros de un autor")
    print("4- Libros por género")
    print("5- Seleccionar algoritmo de ordenamiento")
    print("6- Seleccionar muestra de libros")
    print("7- Ordenar los libros por rating")
    print("8- Salir")

def select_data_structure():
    """
    Vista: Captura la selección del usuario y retorna
    la estructura de datos elegida.
    """
    print("\nEscoge la estructura de datos a usar:")
    print("1 - Array_list")
    print("2 - Single_linked_list")
    
    sub_input = ""
    
    while sub_input == "":
        sub_input = input("\nSeleccione una opción: ")
        global data_structure
        # Encapsulamos la estructura de datos seleccionada en la variable `data_structure`
        if sub_input == "1":
            data_structure = al
            print("Has elegido Array_list")
            return al
        elif sub_input == "2":
            data_structure = lt
            print("Has elegido Single_linked_list")
            return lt
        else:
            print("Opción no válida, intenta de nuevo.")
            sub_input = ""

def load_data(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    books, authors, tags, book_tags= logic.load_data(control)
    return books, authors, tags, book_tags

def print_author_data(author):
    """
    Recorre la lista de libros de un autor, imprimiendo
    la información solicitada.
    """
    if author:
        print("Autor encontrado: " + author["name"])
        print("Promedio: " + str(author["average_rating"]))
        print("Total de libros: " + str(data_structure.size(author["books"])))
        for book_pos in range(0, data_structure.size(author['books'])):
            book = data_structure.get_element(author['books'], book_pos)
            print("Titulo: " + book["title"] + "  ISBN: " + book["isbn"])
    else:
        print("No se encontró el autor")
        
        
def print_book_info(book):
    """
    Imprime los mejores libros solicitados
    """
    if book:
        print("Titulo: " + book['title'] + 
              "ISBN: " + book['isbn'] + 
              "Rating: " + str(book['average_rating']) +
              "Work text reviews count: " + str(book['work_text_reviews_count']))
    else:
        print('No se encontraron libros')



def print_sort_results(sort_books, sample=3):
    """
    Imprime la información de una muestra de libros ordenados.

    Args:
    sort_books (data_structure): La estructura de datos que contiene los libros ordenados.
    sample (int): El número de libros a imprimir. Por defecto, 3.
    
    Se espera que la función imprima la información de 'sample' libros usando la función
    print_book_info(). 
    """
    current = sort_books["first"] if "first" in sort_books else None
    pos = 0

    while current is not None and sample > 0:
        book = current["info"]
        print(f"Título: {book['title']}")
        print(f"Autor(es): {book['authors']}")
        print(f"Rating: {book['average_rating']}")
        print(f"Año: {book['original_publication_year']}")
        print("-" * 40)
        sample -= 1
        current = current["next"]
        pos += 1

    if "elements" in sort_books:  # caso array_list
        for pos in range(min(sample, sort_books["size"])):
            book = sort_books["elements"][pos]
            print(f"Título: {book['title']}")
            print(f"Autor(es): {book['authors']}")
            print(f"Rating: {book['average_rating']}")
            print(f"Año: {book['original_publication_year']}")
            print("-" * 40)

# variables utiles para el programa

data_str="""Seleccione el algoritmo de estructura de datos:
1. Array_list
2. Linked_list
"""

algo_str = """Seleccione el algoritmo de ordenamiento recursivo:
1. Selection Sort
2. insertion Sort
3. shell Sort
4. Merge Sort
5. Quick Sort
"""
                 
exit_opt_lt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")


# main del ejercicio
def main():
    """
    Menú principal
    """
    # bandera para controlar el ciclo del menu
    working = True
    control = None
    # tamaño de la muestra para pruebas
    size = 0.0

    # ciclo del menu
    while working:
        print_menu()
        inputs = input("Seleccione una opción para continuar\n")
        
        if int(inputs[0]) == 0:
            # Capturamos la estructura de datos seleccionada
            user_data_structure = select_data_structure()
        
            # Se crea el controlador asociado a la vista
            control = new_logic(user_data_structure)
            
        elif int(inputs[0]) == 1:
            print("Cargando información de los archivos ....")
            
            bk, at, tg, bktg = load_data(control)
            print("Libros cargados: " + str(bk))
            print("Autores cargados:" + str(at))
            print("Géneros cargados: " + str(tg))
            print("Asociaciones libro-género cargadas: " + str(bktg))


        elif int(inputs[0]) == 2:
            number = input("Ingrese el id del libro que desea buscar: ")
            book = logic.get_book_info_by_book_id(control, int(number))
            print_book_info(book)

        elif int(inputs[0]) == 3:
            authorname = input("Nombre del autor a buscar: ")
            author = logic.get_books_by_author(control, authorname)
            print_author_data(author)

        elif int(inputs[0]) == 4:
            label = input("Etiqueta a buscar: ")
            book_count = logic.count_books_by_tag(control, label)
            print('Se encontraron: ', book_count, ' Libros')
                 
        elif int(inputs[0]) == 5:
            algo_opt = input(algo_str)
            algo_opt = int(algo_opt)
            algo_msg = logic.select_sort_algorithm(algo_opt)
            print(algo_msg[1])
            
        elif int(inputs[0]) == 6:
            size = input("Indique tamaño de la muestra: ")
            size = int(size)
            logic.set_book_sublist(control, size)

        elif int(inputs[0]) == 7:
            print("Ordenando los libros por rating ...")
            result = logic.sort_books(control)
    
            print_sort_results(result[0])
            print("Tiempo de ejecucion:", f"{result[1]:.3f}", "ms")
            


        elif int(inputs[0]) == 8:
            # confirmar salida del programa
            end_str = "¿Desea salir del programa? (s/n): "
            opt_usr = input(end_str)
            # diferentes opciones de salida
            if opt_usr in exit_opt_lt:
                working = False
                print("\nGracias por utilizar el programa.")

        else:
            continue
    sys.exit(0)