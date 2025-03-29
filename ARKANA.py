#Importamos modulos
from rich import print 
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from os import system
from rich.text import Text
from rich.table import Table
from prompt_toolkit.completion import FuzzyWordCompleter
from rich.console import Console
from datetime import datetime

from time import sleep
import random
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

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
        # Libros predefinidos para mostra o prestar
        self.libros = {"El Quijote": Libro(
        nombre="El Quijote",
        editorial="Espasa",
        autor="Miguel de Cervantes",
        fecha_publi="1605",
        isbn="978-84-670-0523-3"
    ),
    "Cien Años de Soledad": Libro(
        nombre="Cien Años de Soledad",
        editorial="Sudamericana",
        autor="Gabriel García Márquez",
        fecha_publi="1967",
        isbn="978-987-566-537-5"
    ),
    "Harry Potter y la Piedra Filosofal": Libro(
        nombre="Harry Potter y la Piedra Filosofal",
        editorial="Bloomsbury",
        autor="J.K. Rowling",
        fecha_publi="1997",
        isbn="978-84-7888-445-2"
    ),
    "El Señor de los Anillos": Libro(
        nombre="El Señor de los Anillos",
        editorial="Minotauro",
        autor="J.R.R. Tolkien",
        fecha_publi="1954",
        isbn="978-84-450-0168-4"),
         "1984": Libro(
        nombre="1984",
        editorial="Secker & Warburg",
        autor="George Orwell",
        fecha_publi="1949",
        isbn="978-0-452-28423-4"
    ),
    "Orgullo y Prejuicio": Libro(
        nombre="Orgullo y Prejuicio",
        editorial="T. Egerton",
        autor="Jane Austen",
        fecha_publi="1813",
        isbn="978-0-19-953556-9"
    ),
    "Crimen y Castigo": Libro(
        nombre="Crimen y Castigo",
        editorial="The Russian Messenger",
        autor="Fiódor Dostoievski",
        fecha_publi="1866",
        isbn="978-84-206-9489-9"
    ),
    "Moby-Dick": Libro(
        nombre="Moby-Dick",
        editorial="Harper & Brothers",
        autor="Herman Melville",
        fecha_publi="1851",
        isbn="978-0-14-243724-7"
    ),
    "Los Juegos del Hambre": Libro(
        nombre="Los Juegos del Hambre",
        editorial="Scholastic",
        autor="Suzanne Collins",
        fecha_publi="2008",
        isbn="978-84-204-2361-0"
    ),
    "Don Juan Tenorio": Libro(
        nombre="Don Juan Tenorio",
        editorial="Juan de la Cuesta",
        autor="José Zorrilla",
        fecha_publi="1844",
        isbn="978-84-376-0492-8"
    ),
    "Drácula": Libro(
        nombre="Drácula",
        editorial="Archibald Constable and Company",
        autor="Bram Stoker",
        fecha_publi="1897",
        isbn="978-84-339-6744-7"
    ),
    "El retrato de Dorian Gray": Libro(
        nombre="El retrato de Dorian Gray",
        editorial="Lippincott's Monthly Magazine",
        autor="Oscar Wilde",
        fecha_publi="1890",
        isbn="978-84-376-0493-5"
    ),
    "Los Miserables": Libro(
        nombre="Los Miserables",
        editorial="A. Lacroix, Verboeckhoven & Cie",
        autor="Victor Hugo",
        fecha_publi="1862",
        isbn="978-84-376-0494-2"
    ),
    "Rayuela": Libro(
        nombre="Rayuela",
        editorial="Sudamericana",
        autor="Julio Cortázar",
        fecha_publi="1963",
        isbn="978-84-376-0495-9"
    )
}
        # Datos de clientes ramdom para ver la informacion
        self.clientes = {"12345678A": Cliente(
        dni="12345678A",
        nombre="Juan Pérez",
        fecha_nac="15/03/1990",
        tlf="600123456",
        correo_electronico="juan.perez@example.com"
    ),
    "87654321B": Cliente(
        dni="87654321B",
        nombre="María López",
        fecha_nac="22/07/1985",
        tlf="610987654",
        correo_electronico="maria.lopez@example.com"
    ),
    "11223344C": Cliente(
        dni="11223344C",
        nombre="Carlos Ramírez",
        fecha_nac="10/12/1995",
        tlf="620123789",
        correo_electronico="carlos.ramirez@example.com"
    ),
    "11223344C": Cliente(
        dni="11223344C",
        nombre="Carlos Ramírez",
        fecha_nac="10/12/1995",
        tlf="620123789",
        correo_electronico="carlos.ramirez@example.com"
    ),

    "22334455D": Cliente(
        dni="22334455D",
        nombre="Ana López",
        fecha_nac="25/07/1988",
        tlf="630456123",
        correo_electronico="ana.lopez@example.com"
    ),
    "33445566E": Cliente(
        dni="33445566E",
        nombre="Javier Morales",
        fecha_nac="15/03/1992",
        tlf="640789321",
        correo_electronico="javier.morales@example.com"
    ),
    "44556677F": Cliente(
        dni="44556677F",
        nombre="Laura García",
        fecha_nac="05/11/1990",
        tlf="650123456",
        correo_electronico="laura.garcia@example.com"
    ),
    "55667788G": Cliente(
        dni="55667788G",
        nombre="Miguel Fernández",
        fecha_nac="18/05/1985",
        tlf="660987654",
        correo_electronico="miguel.fernandez@example.com"
    ),
    "66778899H": Cliente(
        dni="66778899H",
        nombre="Sofía Martínez",
        fecha_nac="02/09/1998",
        tlf="670321654",
        correo_electronico="sofia.martinez@example.com"
    ),
    "77889900J": Cliente(
        dni="77889900J",
        nombre="Diego Torres",
        fecha_nac="12/02/1993",
        tlf="680654321",
        correo_electronico="diego.torres@example.com"
    ),
    "88990011K": Cliente(
        dni="88990011K",
        nombre="Isabel Pérez",
        fecha_nac="30/06/1996",
        tlf="690123987",
        correo_electronico="isabel.perez@example.com"
    ),
    "99001122L": Cliente(
        dni="99001122L",
        nombre="Pablo Sánchez",
        fecha_nac="08/04/1991",
        tlf="610456789",
        correo_electronico="pablo.sanchez@example.com"
    ),
    "00112233M": Cliente(
        dni="00112233M",
        nombre="Elena Vargas",
        fecha_nac="22/08/1994",
        tlf="620789123",
        correo_electronico="elena.vargas@example.com"
    )}
        
        # Datos ramdom para prestados
        self.prestados = {"Cien Años de Soledad": ("12345678A", "Juan Pérez", "Cien Años de Soledad"),
    "Harry Potter y la Piedra Filosofal": ("87654321B", "María López", "Harry Potter y la Piedra Filosofal")}
        
    def animacion_carga(self, mensaje, duracion=3):
        system("cls")
        """
        Animación de carga 
        """
        with Progress(
            SpinnerColumn('aesthetic'),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=None),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        ) as progress:
            tarea = progress.add_task(f"[green]{mensaje}", total=100)
            
            # Efectos de animación
            for _ in range(20):
                sleep(duracion / 20)
                progress.update(tarea, advance=random.uniform(3, 7))
        
    #Funcion para añadir libro -------------------------------------------------------------------------------------------------
    def añadir_libro(self,nombre,editorial,autor,fecha_publi,isbn):
        # Comprobamos que el libro no se duplique
        if nombre not in self.libros:
            #Creamos una insancia del libro y la guardamos con la clave del nombre del libro
            self.libros[nombre] = Libro(nombre,editorial,autor,fecha_publi,isbn)
            system('cls')
            console.print(f'Libro añadido {nombre} correctamente')
            prompt("Pulsa enter para continuar",style=style)
            system('cls')
        else:
            console.input(Panel('El libro ya esta añadido en la lista',border_style ='yellow',width=40))
    
    # Funcion para mostrar libros -----------------------------------------------------------------------------------------------------
    def mostrar_libros(self):
        self.animacion_carga('Desenfundando el catálogo de libros 📚✨')

        # Comprobamos que haya libros
        if self.libros:
            tabla = Table(
                title="🌟 CATÁLOGO MAESTRO DE LIBROS 🌟", 
                expand=True, 
                style="bold")
            # Añadimos columnas
            tabla.add_column("🔖 Título", style="cyan bold")
            tabla.add_column("🏛️ Editorial", style="magenta")
            tabla.add_column("✍️ Autor", style="green bold")
            tabla.add_column("📅 Publicación", style="yellow")
            tabla.add_column("🔢 ISBN", style="red")
            
            # Creamos unas opciones de colores ramdom
            opciones_colores = [
                "bold red", "bold green", "bold blue", 
                "bold magenta", "bold cyan"
            ]
            color = random.choice(opciones_colores)
            for libro in self.libros.values():
                if libro.disponible:
                    tabla.add_row(
                    f"[{color}]{libro.nombre}[/{color}]",  
                    libro.editorial,
                    libro.autor,
                    libro.fecha_publi,
                    libro.isbn
                )
            console.print(tabla)
            prompt()
        else:
            prompt("No hay libros registrados\n\nPulsa enter para continuar",style=style)

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
                console.print(Panel(f'[#27ff58]Libro "{nombre_libro}" prestado correctamente a {nombre_cliente}[/]',border_style='#27ff58',width=40))
                prompt("Pulsa enter para continuar",style=style)
                system('cls')
            else:
                console.input(Panel('El libro ya está prestado',border_style='yellow',width=40))
        else:
            console.input(Panel('El libro o el usuario no existen',border_style='red',width=40))
        
        
    # Mostramos los libros prestado ----------------------------------------------------------------
    def mostrar_libros_prestados(self):
        self.animacion_carga('Desempolvando libros prestados... 📚⏰')
        if self.prestados:
            tabla = Table(title = "Libros prestados",expand=True,)
            tabla.add_column("Dni")
            tabla.add_column("Nombre")
            tabla.add_column("Nombre libro")
            for nombre_libro, (dni, nombre_cliente, _) in self.prestados.items():
                tabla.add_row(dni,nombre_cliente,nombre_libro)
            console.print(tabla)
            prompt("Pulsa enter para continuar",style=style)
        else:
            prompt("No hay libros prestados\n\nPulsa enter para continuar",style=style)

    # Funcion para devolver libro ---------------------------------------------------------------------------------------------------+++++++++++++++++++
    def devolver_libro(self,nombre_libro):
        if self.prestados and nombre_libro in self.prestados:
            del self.prestados[nombre_libro]
            self.libros[nombre_libro].disponible = True
            prompt('Libro devuelto correctamente',style=style)
        else:
            prompt('No hay libros prestados',style=style)

    # Funcion para agregar clientes ----------------------------------------------------------------------------------------------
    def agregar_cliente(self,dni,nombre,fecha_nac,tlf,correo_electronico):
        if dni not in self.clientes:
            self.clientes[dni] = Cliente(dni,nombre,fecha_nac,tlf,correo_electronico)
            system("cls")
            console.print(f"Usuario {nombre} registrado correctamente")
            prompt("Pulsa enter para continuar",style=style)
            system("cls")
        else:
            console.input(Panel('El dni ya esta regitrado',border_style='red',width=40))

    # Funcion para mostar clientes ------------------------------------------------------------------------------------------------
    def mostrar_clientes(self):
        self.animacion_carga('Revisando el listado de clientes... 👥📚')
        
        tabla = Table(title = "Clientes",expand=True,)
        tabla.add_column("DNI")
        tabla.add_column("Nombre")
        tabla.add_column("Fecha nacimiento")
        tabla.add_column("Telefono")
        tabla.add_column("Correo electronico")
        for cliente in self.clientes.values():
            tabla.add_row(cliente.dni,cliente.nombre,cliente.fecha_nac,str(cliente.tlf),cliente.correo_electronico)
        console.print(tabla)
        prompt()
    # Funcion para eliminar usuario --------------------------------------------------------------------------------------------------+++++++++++++++++++++
    def eliminar_usuario(self,dni):
        if self.clientes :
            if dni in self.clientes:
                del self.clientes[dni]
                prompt("Usuario eliminado correctamente",style=style)
            else:
                prompt("No hay usuarios registrados con ese dni",style=style)

        else:
            prompt("No hay usuarios registrados",style=style)
    
console = Console()


style = Style.from_dict({
    'prompt': 'bold fg:#ffb027',
    '': 'fg:#ffffff'
})
prompt('Poner en pantalla completa para visualizar correctamete',style=style)
system("cls")



menu="""
[#7df4f3]

                          
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
arkana = Biblioteca()

# Bucle principal
def main():
    
    while True:
        system("cls")
        while True:
            try:
                system("cls")
                console.print(titulo)
                console.print(menu_principal)
                # Pregutamos que quiere hacer
                opcion = int(prompt('Seleciona una opcion: ',style=style))
                break
            except:
                console.input(Panel('[red]Opcion no valida pulsa enter para coninuar[/]',border_style="red",width=40))
                continue

        if opcion == 1: # Opcion de añadir libro --------------------------------------------------------------------------------------------
            while True:
                system('cls') # Borramos pantalla
                try:
                    panel1 = Panel(Align.center('[#90CAF9]\nAñadir libro[/]'),border_style='#90CAF9',width=50,title='Menu para añadir libros')
                    console.print(panel1)# Le mostramos en que menu estamos
                    
                    while True:
                        # Le pedimos los datos
                        nombre_libro = prompt('Introduce el nombre del libro: ', style=style).strip().capitalize()
                        editorial = prompt('Introduce la editorial del libro: ', style=style).strip().capitalize()
                        autor = prompt('Introduce el autor del libro: ', style=style).strip().capitalize()

                        # Validar que ningún campo esté vacío
                        if not nombre_libro:
                            console.print(Panel('[bold red]El nombre del libro no puede estar vacío[/]', border_style='red', width=40))
                            continue
                        if not editorial:
                            console.print(Panel('[bold red]La editorial no puede estar vacía[/]', border_style='red', width=40))
                            continue
                        if not autor:
                            console.print(Panel('[bold red]El autor no puede estar vacío[/]', border_style='red', width=40))
                            continue
                        else:
                            break

                    while True:
                        try:
                            fecha_publi = prompt('Introduce la fecha de publicacion [dia/mes/año]: ',style=style)
                            datetime.strptime(fecha_publi, '%d/%m/%Y')
                            break
                        except:
                            console.print(Panel("[red]\nFecha inválida[/]",border_style="red"))
                            continue

                    isbn = prompt('Introduce el ISBN: ',style=style)
                    while True:
                        if len(isbn) != 10:
                            console.print(Panel("[bold red]ISBN-tiene que tener 10 numeros[/]", border_style="red", width=50))
                            continue
                        else:
                            break
                    arkana.añadir_libro(nombre_libro,editorial,autor,fecha_publi,isbn)
                    
                except :
                    console.input(Panel('Has introducido algun dato erroneo\n\nPulsa enter para continuar',border_style='red',width=40))
                    system('cls')
                    continue
                

        elif opcion == 2: # Opcion de prestar libro -----------------------------------------------------------------------------------------
            system('cls')
            panel1 = Panel(Align.center('[#90CAF9]\nPrestar libro[/]'),border_style='#90CAF9',width=50,title='Menu para añadir libros')
            console.print(panel1) 

            # Auto completar con el dni de los clientes
            clientes = FuzzyWordCompleter(arkana.clientes)
            while True:
                dni = prompt('Introduce el dni del cliente para prestar: ',completer=clientes,style=style).upper()
                if len(dni) != 9 or not dni[0:8].isdigit() or not dni[8].isalpha():
                    console.print(Panel("[bold red]DNI inválido. Formato correcto: 12345678A[/]", border_style="red", width=50))
                    continue
                else:
                    break
            
            libros_disponibles = FuzzyWordCompleter(arkana.libros)
            nombre_libro = prompt('Introduce el nombre del libro a prestar: ',completer = libros_disponibles,style=style)
            
            arkana.prestar_libro(dni,nombre_libro)


        elif opcion == 3: # Opcion de devolver libro  ---------------------------------------------------------------------------------------
            panel1 = Panel(Align.center('[#90CAF9]\nDevolver libro[/]'),border_style='#90CAF9',width=50,title='Menu para devolver libros')
            console.print(panel1)
            libros_devolver = FuzzyWordCompleter(arkana.prestados)
            nombre_libro = prompt('Introduce el nombre del libro a devolver',completer = libros_devolver,style=style).capitalize()
            arkana.devolver_libro(nombre_libro)

        elif opcion == 4: # Mostrar libros disponibles ---------------------------------------------------------------------------------------
            panel1 = Panel(Align.center('[#90CAF9]\nMostrar libros[/]'),border_style='#90CAF9',width=50,title='Libros disponibles')
            console.print(panel1)
            arkana.mostrar_libros()

        elif opcion == 5: # Mostrar libros prestado  -----------------------------------------------------------------------------------------
            console.print('Libros prestados')
            arkana.mostrar_libros_prestados()

        elif opcion == 6: # Registro de usuarios  -----------------------------------------------------------------------------------------
            panel1 = Panel(Align.center('[#90CAF9]\nRegistrar usuarios[/]'),border_style='#90CAF9',width=50,title='Registro de usuarios')
            console.print(panel1)

            # Bucle para pedir datos
            while True:
                
                while True:
                    dni = prompt('Introduce el dni del cliente a registrar: ',style=style).upper()
                    if len(dni) != 9 or not dni[0:8].isdigit() or not dni[8].isalpha():
                        console.print(Panel("[bold red]DNI inválido. Formato correcto: 12345678A[/]", border_style="red", width=50))
                        continue
                    else:
                        break
                nombre = prompt('Introduce el nombre del cliente a registrar: ',style=style).capitalize()
                
                # Bucele para validar la fecha en el formato correcto
                while True:
                    try:
                        fecha_nac = prompt('Introduce la fecha de nacimiento del cliente [dia/mes/año]: ',style=style)
                        datetime.strptime(fecha_nac, '%d/%m/%Y')
                        
                        break
                    except:
                        console.print("[bold red]Fecha inválida[/]")
                        continue
                while True:
                    tlf = prompt('Introduce el numero de telefono del cliente: ',style=style)
                    if len(tlf) != 9 or not tlf.isdigit():
                        console.print(Panel("[bold red]Teléfono inválido. Debe tener 9 dígitos[/]", border_style="red", width=50))
                        continue
                    else:
                        break
                correo_electronico = prompt('Introduce el correo electronico del cliente: ',style=style)
                break
                
            arkana.agregar_cliente(dni,nombre,fecha_nac,tlf,correo_electronico)

        elif opcion == 7: # Mostrar usuarios registrados  ------------------------------------------------------------------------------------
            # Mostrar clientes
            arkana.mostrar_clientes()
            
        elif opcion == 8: # Eliminar usuario  -----------------------------------------------------------------------------------------
            if arkana.clientes:
                panel1 = Panel(Align.center('[#90CAF9]\nMenu para eliminar usuarios[/]'),border_style='#90CAF9',width=50,title='Eliminar usuario')
                console.print(panel1)
                arkana.mostrar_clientes()
                eliminar_usuario = FuzzyWordCompleter(arkana.clientes)
                while True:
                    dni = prompt("Introduce el DNI del usuario a eliminar: ",completer=eliminar_usuario,style=style)
                    #Validar dni
                    if len(dni) != 9 or not dni[0:8].isdigit() or not dni[8].isalpha():
                        console.print(Panel("[bold red]DNI inválido. Formato correcto: 12345678A[/]", border_style="red", width=50))
                        continue
                    else:
                        break
                arkana.eliminar_usuario(dni)
            else:
                console.input(Panel("No hay clientes registrados",border_style="fffc27",width=40))
            
        elif opcion == 9: # Salida del programa  -----------------------------------------------------------------------------------------
            prompt('Muchas gracias por usar el programa',style=style)
            break

        

if __name__ == "__main__":
    main()
