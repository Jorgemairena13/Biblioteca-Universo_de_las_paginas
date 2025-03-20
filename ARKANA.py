#Importamos modulos
from rich import print 
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from os import system
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
#from rich_pixels import Pixels
from rich.console import Console
from datetime import datetime



class Libro():
    def __init__(self,nombre,editorial,autor,fecha_publi,isbn):
        self.nombre = nombre
        self.editorial = editorial
        self.autor = autor
        self.fecha_publi = fecha_publi
        self.isbn = isbn
        self.disponible = True
        
    
class Cliente():
    def __init__(self,dni,nombre,fecha_nac,tlf,correo_electronico):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.tlf = tlf
        self.correo_electronico = correo_electronico


class Prestamo():

    def __init__(self,dni , nombre,nombre_libro, fecha_prestamo, fecha_devolucion):
        self.dni = dni
        self.usuario = nombre
        self.libro = nombre_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion


class Biblioteca():

    def __init__(self):
        # Diccionarios donde se va a ir guardando todo
        self.libros = {}
        self.clientes = {}
        self.prestados = {}
        
    #Funcion para añadir libro -------------------------------------------------------------------------------------------------
    def añadir_libro(self,nombre,editorial,autor,fecha_publi,isbn):
        
        # Comprobamos que el libro no se duplique
        if nombre not in self.libros:
            #Creamos una insancia del libro y la guardamos con la clave del nombre del libro
            self.libros[nombre] = Libro(nombre,editorial,autor,fecha_publi,isbn)
            system('cls')
            console.print(f'Libro añadido {nombre} correctamente')
            input("Pulsa enter para continuar")
            system('cls')
        else:
            console.input('El libro ya esta añadido en la lista')

    #Funcion para prestar libro ---------------------------------------------------------------------------------------------------
    def prestar_libro(self,dni,nombre,nombre_libro, fecha_prestamo, fecha_devolucion):

        self.prestados[dni] = Prestamo(dni,nombre,nombre_libro,fecha_prestamo,fecha_devolucion)
        print(self.prestados)
        input()
        # del self.libros[nombre]

    # Funcion para agregar clientes ----------------------------------------------------------------------------------------------
    def agregar_cliente(self,dni,nombre,fecha_nac,tlf,correo_electronico):
        if dni not in self.clientes:
            self.clientes[dni] = Cliente(dni,nombre,fecha_nac,tlf,correo_electronico)
            system("cls")
            console.print(f"Usuario {nombre} registrado correctamente")
            input("Pulsa enter para continuar")
            system("cls")

    # Funcion para mostar clientes ------------------------------------------------------------------------------------------------
    def mostrar_clientes(self):
        for cliente in self.clientes.values():
            console.print(f"Dni {cliente.dni}\t Nombre{cliente.nombre}")
        input()
    
console = Console()
console.input('Poner en pantalla completa para visualizar correctamete')
system("cls")


menu="""
[#5d6d7e]

                           ▄████████         ▄████████       ▄████████         ▄████████      ███▄▄▄▄           ▄████████ 
                          ███    ███        ███    ███      ███    ███        ███    ███      ███▀▀▀██▄        ███    ███ 
                          ███    ███        ███    ███      ███    █▀         ███    ███      ███   ███        ███    ███ 
                          ███    ███       ▄███▄▄▄▄██▀      ███               ███    ███      ███   ███        ███    ███ 
                        ▀███████████      ▀▀███▀▀▀▀▀        ███             ▀███████████      ███   ███      ▀███████████   
                          ███    ███      ▀███████████      ███    █▄         ███    ███      ███   ███        ███    ███ 
                          ███    ███        ███    ███      ███    ███        ███    ███      ███   ███        ███    ███ 
                          ███    █▀         ███    ███      ████████▀         ███    █▀        ▀█   █▀         ███    █▀  
                                            ███    ███                                                                    

                                             
                                                                                                                                                                                              

[/]                                                                                                                                                                            
"""
menu2 = """
[#14effd ]
╔════════════════════════════════════════════════════════╗
║   [bold #ccf2ec]                 ░▒▓ BIBLIOTECA ▓▒░ [/]                 ║
║   [#ccf2ec]          █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█[/]            ║
║   [#ccf2ec]          █[blink]            ARKANA       [/]    █[/]            ║  
║   [#ccf2ec]          █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█[/]            ║
╠════════════════════════════════════════════════════════╣
║  [bold #1b8dff]             📚 MENU LIBROS  [/]                         ║
║[#5aaafa]  ➤ 1. Añadir Libro  [/]                                   ║
║[#5aaafa]  ➤ 2. Prestar Libro [/]                                   ║
║[#5aaafa]  ➤ 3. Devolver Libro [/]                                  ║
╠════════════════════════════════════════════════════════╣
║           [bold #e65700]    🏛️ MENU BIBLIOTECA  [/]                     ║
║[#fda114]  ➤ 4. Libros Disponibles [/]                              ║
║[#fda114]  ➤ 5. Libros Prestados   [/]                              ║
╠════════════════════════════════════════════════════════╣
║   [bold #fe00e7]            👥 MENU USUARIOS    [/]                     ║
║[#fd1477]  ➤ 6. Registrar Usuario  [/]                              ║
║[#fd1477]  ➤ 7. Usuarios Registrados [/]                            ║
║[#fd1477]  ➤ 8. Eliminar Usuario [/]                                ║
╠════════════════════════════════════════════════════════╣
║[#af14fd]               ❯ 9. SALIR    [/]                           ║
╚════════════════════════════════════════════════════════╝

[/]






"""
titulo = Panel(
    Align.center(menu),
    border_style="#000000",
    expand= True
)

menu_principal = Panel(
    Align.center(menu2),
    border_style="#000000",
    expand=True
)
#Instanciamos la clase bibloteca
arcana = Biblioteca()

# Bucle principal
def main():
    console.print(titulo)
    while True:
        # Cada vuelta mostramos el menu principal
        console.print(menu_principal)
        
        # Pregutamos que quiere hacer
        opcion = int(input('Seleciona una opcion: '))

        if opcion == 1: # Opcion de añadir libro --------------------------------------------------------------------------------------------
            while True:
                system('cls') # Borramos pantalla
                try:
                    console.print('Añadir libro')# Le mostramos en que menu estamos
                    # Le pedimos todos los datos necesarios
                    nombre_libro = input('Introduce el nombre del libro: ')
                    editorial = input('Introduce la editorial del libro: ')
                    autor = input('Introduce el autor del libro: ')
                    fecha_publi = input('Introduce la fecha de salida del libro: ')
                    isbn = input('Introduce el ISBN: ')
                    arcana.añadir_libro(nombre_libro,editorial,autor,fecha_publi,isbn)
                    break
                except:
                    console.input('Has introducido algun dato erroneo\n\nPulsa enter para continuar')
                    system('cls')
                    continue
                

        elif opcion == 2: # Opcion de prestar libro -----------------------------------------------------------------------------------------
            console.print('Prestar libro') 
            dni = prompt('Introduce el dni del clienre para prestar: ')
            nombre = prompt('Introduce el nombre del cliente')
            nombre_libro = prompt('Introduce el nombre del libro a prestar')
            fecha_prestamo = prompt('Introduce la fecha del prestamo')
            fecha_devolucion = prompt('Introduce la fecha de devolucion')
            arcana.prestar_libro(dni,nombre,nombre_libro, fecha_prestamo, fecha_devolucion)

        elif opcion == 3: # Opcion de devolver libro  ---------------------------------------------------------------------------------------
            console.print('Devolver libro') 

        elif opcion == 4: # Mostrar libros disponibles ---------------------------------------------------------------------------------------
            console.print('Mostar libros disponibles') 

        elif opcion == 5: # Mostrar libros prestado  -----------------------------------------------------------------------------------------
            console.print('Libros prestados')

        elif opcion == 6: # Registro de usuarios  -----------------------------------------------------------------------------------------
            console.print('Registrar usuarios')
            # dni,nombre,fecha_nac,tlf,correo_electronico
            while True:
                try:
                    dni = input('Introduce el dni del cliente a registrar: ')
                    nombre = input('Introduce el nombre del cliente a registrar: ')
                    while True:
                        try:
                            fecha_nac = input('Introduce la fecha de nacimiento del cliente: ')
                            datetime.strptime(fecha_nac, '%d-%m-%Y')
                            print("Fecha válida")
                            break
                        except:
                            print("Fecha inválida")
                            continue
                    tlf = int(input('Introduce el numero de telefono del cliente: '))
                    correo_electronico = input('Introduce el correo electronico del cliente: ')
                    break
                except:
                    console.input("Las datos introducidos no son correctos")
                    continue
            arcana.agregar_cliente(dni,nombre,fecha_nac,tlf,correo_electronico)
        elif opcion == 7: # Mostrar usuarios registrados  ------------------------------------------------------------------------------------
            console.print('Mostar usuarios registrados')
            arcana.mostrar_clientes()
            input()
        elif opcion == 8: # Eliminar usuario  -----------------------------------------------------------------------------------------
            console.print('Eliminar usuario')

        elif opcion == 9: # Salida del programa  -----------------------------------------------------------------------------------------
            console.input('Muchas gracias por usar el programa')
        else:
            console.input('Opcion no valida pulsa enter para coninuar')
        system("cls")

if __name__ == "__main__":
    main()
