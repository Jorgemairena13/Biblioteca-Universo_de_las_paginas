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


# Clase libro con todos los atributos que le vamos a pasar
class Libro():
    def __init__(self,nombre,editorial,autor,fecha_publi,isbn):
        self.nombre = nombre
        self.editorial = editorial
        self.autor = autor
        self.fecha_publi = fecha_publi
        self.isbn = isbn
        self.disponible = True
        
# Clase cliente con los atributos principales
class Cliente():
    def __init__(self,dni,nombre,fecha_nac,tlf,correo_electronico):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.tlf = tlf
        self.correo_electronico = correo_electronico

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
    
    # Funcion para mostrar libros -----------------------------------------------------------------------------------------------------
    def mostrar_libros(self): 
        if self.libros:
            for libro in self.libros.values():
                if libro.disponible:
                    print(f"Nombre {libro.nombre}\tEditorial {libro.editorial}\tAutor {libro.autor}\tFecha publicacion {libro.fecha_publi}\tISBN {libro.isbn}")
                    input()
        else:
            input("No hay libros registrados\n\nPulsa enter para continuar")

    #Funcion para prestar libro ---------------------------------------------------------------------------------------------------
    def prestar_libro(self, dni, nombre_libro):
        if nombre_libro in self.libros and dni in self.clientes:
            if nombre_libro not in self.prestados and self.libros[nombre_libro].disponible:
                # Obtenemos el nombre del cliente
                nombre_cliente = self.clientes[dni].nombre
                
                # Guardamos DNI, nombre del cliente y nombre del libro
                self.prestados[nombre_libro] = (dni, nombre_cliente, nombre_libro)
                self.libros[nombre_libro].disponible = False
                
                system('cls')
                console.print(f'Libro "{nombre_libro}" prestado correctamente a {nombre_cliente}')
                input("Pulsa enter para continuar")
                system('cls')
            else:
                console.input('El libro ya está prestado')
        else:
            console.input('El libro o el usuario no existen')
        
        
    # Mostramos los libros prestado ----------------------------------------------------------------
    def mostrar_libros_prestados(self):
        if self.prestados:
            for nombre_libro, (dni, nombre_cliente, _) in self.prestados.items():
                print(f"Libro: {nombre_libro} - Prestado a: {nombre_cliente} (DNI: {dni})")
            input("Pulsa enter para continuar")
        else:
            input("No hay libros prestados\n\nPulsa enter para continuar")

    # Funcion para devolver libro ---------------------------------------------------------------------------------------------------+++++++++++++++++++
    def devolver_libro(self,nombre_libro):
        if self.prestados:
            del self.prestados[nombre_libro]
            self.libros[nombre_libro].disponible = True
            prompt('Libro devuelto correctamente')
        else:
            prompt('No hay libros prestados')

    # Funcion para agregar clientes ----------------------------------------------------------------------------------------------
    def agregar_cliente(self,dni,nombre,fecha_nac,tlf,correo_electronico):
        if dni not in self.clientes:
            self.clientes[dni] = Cliente(dni,nombre,fecha_nac,tlf,correo_electronico)
            system("cls")
            console.print(f"Usuario {nombre} registrado correctamente")
            input("Pulsa enter para continuar")
            system("cls")
        else:
            console.input('El dni ya esta regitrado')

    # Funcion para mostar clientes ------------------------------------------------------------------------------------------------
    def mostrar_clientes(self):
        for cliente in self.clientes.values():
            console.print(f"Dni {cliente.dni}\t Nombre {cliente.nombre}")
        
    
    # Funcion para eliminar usuario --------------------------------------------------------------------------------------------------+++++++++++++++++++++
    def eliminar_usuario(self,dni):
        if self.clientes:
            del self.clientes[dni]
            prompt("Usuario eliminado correctamente")
        else:
            prompt("No hay usuarios registrados")
    
console = Console()
console.input('Poner en pantalla completa para visualizar correctamete')
system("cls")

menu="""
[#5d6d7e]

                          
            ▄████████         ▄████████         ▄█   ▄█▄         ▄████████      ███▄▄▄▄           ▄████████ 
           ███    ███        ███    ███        ███ ▄███▀        ███    ███      ███▀▀▀██▄        ███    ███ 
           ███    ███        ███    ███        ███▐██▀          ███    ███      ███   ███        ███    ███ 
           ███    ███       ▄███▄▄▄▄██▀       ▄█████▀           ███    ███      ███   ███        ███    ███ 
         ▀███████████      ▀▀███▀▀▀▀▀        ▀▀█████▄         ▀███████████      ███   ███      ▀███████████ 
           ███    ███      ▀███████████        ███▐██▄          ███    ███      ███   ███        ███    ███ 
           ███    ███        ███    ███        ███ ▀███▄        ███    ███      ███   ███        ███    ███ 
           ███    █▀         ███    ███        ███   ▀█▀        ███    █▀        ▀█   █▀         ███    █▀  
                             ███    ███        ▀                                                                                                    
[/]                                                                                                                                                                            
"""
menu2 = """
[#90CAF9 ]
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
║   [bold #E3608C]            👥 MENU USUARIOS    [/]                     ║
║[#EF94B3]  ➤ 6. Registrar Usuario  [/]                              ║
║[#EF94B3]  ➤ 7. Usuarios Registrados [/]                            ║
║[#EF94B3]  ➤ 8. Eliminar Usuario [/]                                ║
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
        
        
        # Pregutamos que quiere hacer
        while True:
            system("cls")
            try:
                console.print(menu_principal)
                opcion = int(input('Seleciona una opcion: '))
                break
            except:
                console.input("Introduce una opcion correcta")
                continue

        if opcion == 1: # Opcion de añadir libro --------------------------------------------------------------------------------------------
            while True:
                system('cls') # Borramos pantalla
                try:
                    console.print('Añadir libro')# Le mostramos en que menu estamos
                    # Le pedimos todos los datos necesarios
                    nombre_libro = input('Introduce el nombre del libro: ').capitalize()
                    editorial = input('Introduce la editorial del libro: ').capitalize()
                    autor = input('Introduce el autor del libro: ').capitalize()
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
            dni = prompt('Introduce el dni del cliente para prestar: ')
            
            nombre_libro = prompt('Introduce el nombre del libro a prestar').capitalize()
            
            arcana.prestar_libro(dni,nombre_libro)

        elif opcion == 3: # Opcion de devolver libro  ---------------------------------------------------------------------------------------
            console.print('Devolver libro')
            nombre_libro = prompt('Introduce el nombre del libro a devolver').capitalize()
            arcana.devolver_libro(nombre_libro)

        elif opcion == 4: # Mostrar libros disponibles ---------------------------------------------------------------------------------------
            console.print('Mostar libros disponibles') 
            arcana.mostrar_libros()

        elif opcion == 5: # Mostrar libros prestado  -----------------------------------------------------------------------------------------
            console.print('Libros prestados')
            arcana.mostrar_libros_prestados()

        elif opcion == 6: # Registro de usuarios  -----------------------------------------------------------------------------------------
            console.print('Registrar usuarios')

            # Bucle para pedir datos
            while True:
                try:
                    dni = input('Introduce el dni del cliente a registrar: ')
                    nombre = input('Introduce el nombre del cliente a registrar: ').capitalize()
                    
                    # Bucele para validar la fecha en el formato correcto
                    while True:
                        try:
                            fecha_nac = input('Introduce la fecha de nacimiento del cliente [dia/mes/año]: ')
                            datetime.strptime(fecha_nac, '%d/%m/%Y')
                            
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
            if arcana.clientes:
                console.print('Eliminar usuario')
                console.print("Clientes a eliminar")
                arcana.mostrar_clientes()
                dni = prompt("Introduce el DNI del usuario a eliminar")
                arcana.eliminar_usuario(dni)
            else:
                prompt("No hay usuarios registrados")
            
        elif opcion == 9: # Salida del programa  -----------------------------------------------------------------------------------------
            console.input('Muchas gracias por usar el programa')
            break

        else:
            console.input('Opcion no valida pulsa enter para coninuar')
        system("cls")

if __name__ == "__main__":
    main()
