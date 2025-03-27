#Importamos modulos
from rich import print 
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from os import system
from rich.text import Text
from rich.table import Table
from prompt_toolkit.completion import WordCompleter
from rich.console import Console
from datetime import datetime
import threading
from time import sleep
import random
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.box import Box
from rich.box import SIMPLE

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

    def animacion_carga_epica(self, mensaje, duracion=3):
        """
        Animación de carga épica con efectos visuales
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
    
    def mostrar_libros_epic_mode(self):
        """
        Muestra libros con una presentación épica y dinámica
        """
        console = Console()
        
        # Animación inicial de carga
        self.animacion_carga_epica("Desenfundando el catálogo de libros 📚✨")
        
        def generar_tabla_epica():
            # Tabla con efectos visuales
            tabla = Table(
                title="🌟 CATÁLOGO MAESTRO DE LIBROS 🌟", 
                expand=True, 
                style="bold"
                
            )
            tabla.add_column("🔖 Título", style="cyan bold")
            tabla.add_column("🏛️ Editorial", style="magenta")
            tabla.add_column("✍️ Autor", style="green bold")
            tabla.add_column("📅 Publicación", style="yellow")
            tabla.add_column("🔢 ISBN", style="red")
            
            return tabla, [libro for libro in self.libros.values() if libro.disponible]

        def animacion_entrada_libros(tabla, libros):
            # Colores de transición
            colores_transicion = [
                "bold red", "bold green", "bold blue", 
                "bold magenta", "bold cyan", "bold yellow"
            ]
            
            for libro in libros:
                # Efecto de entrada con color aleatorio
                color_actual = random.choice(colores_transicion)
                
                tabla.add_row(
                    Text(libro.nombre, style=color_actual), 
                    Text(libro.editorial, style="dim"),
                    Text(libro.autor, style="italic"),
                    Text(libro.fecha_publi, style="dim"),
                    Text(libro.isbn, style="underline")
                )
                
                # Animación de entrada
                console.print(
                    Panel(
                        tabla, 
                        title="📚 Actualizando Catálogo", 
                        border_style=color_actual
                    )
                )
                sleep(0.5)  # Tiempo entre entradas
            
            return tabla

        def efectos_finales(tabla):
            # Efectos visuales finales
            estilos_finales = [
                Panel(tabla, 
                      title="🎉 CATÁLOGO COMPLETO", 
                      border_style="bold green"),
                Panel(tabla, 
                      title="✨ LIBROS LISTOS", 
                      border_style="bold blue"),
                Panel(tabla, 
                      title="🚀 DESPEGUE LITERARIO", 
                      border_style="bold magenta")
            ]
            
            for estilo in estilos_finales:
                console.print(estilo)
                sleep(0.5)

        # Generación de la tabla
        tabla, libros = generar_tabla_epica()
        
        if not libros:
            console.print(
                Panel(
                    "[bold red]¡Biblioteca Vacía! 📭",
                    border_style="red",
                    expand=False
                )
            )
            return
        
        # Tabla final con animación
        tabla_final = animacion_entrada_libros(tabla, libros)
        
        # Efectos de cierre
        efectos_finales(tabla_final)

    def mostrar_clientes_epic_mode(self):
        """
        Muestra clientes con una presentación ultra dinámica
        """
        console = Console()
        
        # Animación inicial de carga
        self.animacion_carga_epica("Invocando el registro de clientes 👥🔮")
        
        def generar_tabla_epica():
            tabla = Table(
            title="🌈 REGISTRO MAESTRO DE CLIENTES 🌈", 
            expand=True, 
            style="bold",
            box=SIMPLE
        )
                
            tabla.add_column("🆔 DNI", style="cyan bold")
            tabla.add_column("👤 Nombre", style="magenta bold")
            tabla.add_column("🎂 Nacimiento", style="green")
            tabla.add_column("📱 Teléfono", style="yellow bold")
            tabla.add_column("📧 Correo", style="red")
                
            return tabla, list(self.clientes.values())

        def animacion_entrada_clientes(tabla, clientes):
            efectos_visuales = [
                "bold red", "bold green", "bold blue", 
                "bold magenta", "bold cyan"
            ]
            
            for cliente in clientes:
                color = random.choice(efectos_visuales)
                
                tabla.add_row(
                    Text(cliente.dni, style=color), 
                    Text(cliente.nombre, style="italic " + color),
                    Text(cliente.fecha_nac, style="dim"),
                    Text(str(cliente.tlf), style="bold"),
                    Text(cliente.correo_electronico, style="underline")
                )
                
                console.print(
                    Panel(
                        tabla, 
                        title="👥 Actualizando Registro", 
                        border_style=color
                    )
                )
                sleep(0.5)
            
            return tabla

        def efectos_finales(tabla):
            transiciones = [
                ("🎉 REGISTRO COMPLETO", "green"),
                ("✨ CLIENTES ACTIVADOS", "blue"),
                ("🚀 SISTEMA ACTUALIZADO", "magenta")
            ]
            
            for titulo, color in transiciones:
                console.print(
                    Panel(
                        tabla, 
                        title=titulo, 
                        border_style="bold " + color
                    )
                )
                sleep(0.5)

        # Generación de la tabla
        tabla, clientes = generar_tabla_epica()
        
        if not clientes:
            console.print(
                Panel(
                    "[bold red]¡Registro Vacío! 🕳️",
                    border_style="red",
                    expand=False
                )
            )
            return
        
        # Tabla final con animación
        tabla_final = animacion_entrada_clientes(tabla, clientes)
        
        # Efectos de cierre
        efectos_finales(tabla_final)

    def mostrar_prestamos_epic_mode(self):
        """
        Muestra préstamos con una presentación ultra dinámica
        """
        console = Console()
        
        # Animación inicial de carga
        self.animacion_carga_epica("Desvelando los secretos de los préstamos 📖🔍")
        
        def generar_tabla_epica():
            tabla = Table(
                title="⚡ REGISTRO DE PRÉSTAMOS ACTIVOS ⚡", 
                expand=True, 
                style="bold",
                box=Box.DOUBLE_EDGE
            )
            tabla.add_column("🆔 DNI", style="cyan bold")
            tabla.add_column("👤 Cliente", style="magenta bold")
            tabla.add_column("📖 Libro", style="green bold")
            
            return tabla, list(self.prestados.values())

        def animacion_entrada_prestamos(tabla, prestamos):
            efectos_visuales = [
                "bold red", "bold green", "bold blue", 
                "bold magenta", "bold yellow"
            ]
            
            for prestamo in prestamos:
                color = random.choice(efectos_visuales)
                
                tabla.add_row(
                    Text(prestamo[0], style=color), 
                    Text(prestamo[1], style="italic " + color),
                    Text(prestamo[2], style="underline bold")
                )
                
                console.print(
                    Panel(
                        tabla, 
                        title="📚 Rastreando Préstamos", 
                        border_style=color
                    )
                )
                sleep(0.5)
            
            return tabla

        def efectos_finales(tabla):
            transiciones = [
                ("🎉 PRÉSTAMOS REVELADOS", "green"),
                ("✨ LIBROS EN MOVIMIENTO", "blue"),
                ("🚀 SISTEMA ACTUALIZADO", "magenta")
            ]
            
            for titulo, color in transiciones:
                console.print(
                    Panel(
                        tabla, 
                        title=titulo, 
                        border_style="bold " + color
                    )
                )
                sleep(0.5)

        # Generación de la tabla
        tabla, prestamos = generar_tabla_epica()
        
        if not prestamos:
            console.print(
                Panel(
                    "[bold red]¡Ningún Préstamo Activo! 📭",
                    border_style="red",
                    expand=False
                )
            )
            return
        
        # Tabla final con animación
        tabla_final = animacion_entrada_prestamos(tabla, prestamos)
        
        # Efectos de cierre
        efectos_finales(tabla_final)
        
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
            console.input(Panel('El libro ya esta añadido en la lista',border_style ='yellow'))
    
    # Funcion para mostrar libros -----------------------------------------------------------------------------------------------------
    def mostrar_libros(self): 
        if self.libros:
            tabla = Table(title = "Libros disponibles",expand=True,)
            tabla.add_column("Nombre libro")
            tabla.add_column("Editorial")
            tabla.add_column("Autor")
            tabla.add_column("Fecha publicacion")
            tabla.add_column("ISBN")
            for libro in self.libros.values():
                if libro.disponible:
                    tabla.add_row(libro.nombre,libro.editorial,libro.autor,libro.fecha_publi,libro.isbn)
                    console.print(tabla)
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
            tabla = Table(title = "Libros prestados",expand=True,)
            tabla.add_column("Dni")
            tabla.add_column("Nombre")
            tabla.add_column("Nombre libro")
            for nombre_libro, (dni, nombre_cliente, _) in self.prestados.items():
                tabla.add_row(dni,nombre_cliente,nombre_libro)
            console.print(tabla)
            input("Pulsa enter para continuar")
        else:
            input("No hay libros prestados\n\nPulsa enter para continuar")

    # Funcion para devolver libro ---------------------------------------------------------------------------------------------------+++++++++++++++++++
    def devolver_libro(self,nombre_libro):
        if self.prestados and nombre_libro in self.prestados:
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
        
        tabla = Table(title = "Clientes",expand=True,)
        tabla.add_column("DNI")
        tabla.add_column("Nombre")
        tabla.add_column("Fecha nacimiento")
        tabla.add_column("Telefono")
        tabla.add_column("Correo electronico")
        for cliente in self.clientes.values():
            tabla.add_row(cliente.dni,cliente.nombre,cliente.fecha_nac,str(cliente.tlf),cliente.correo_electronico)
        console.print(tabla)
        input()
    # Funcion para eliminar usuario --------------------------------------------------------------------------------------------------+++++++++++++++++++++
    def eliminar_usuario(self,dni):
        if self.clientes :
            if dni in self.clientes:
                del self.clientes[dni]
                prompt("Usuario eliminado correctamente")
            else:
                prompt("No hay usuarios registrados con ese dni")

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
        
        # Pregutamos que quiere hacer
        while True:
            system("cls")
            try:
                console.print(menu_principal)
                opcion = int(input('Seleciona una opcion: '))
                break
            except:
                console.input(Panel('Opcion no valida pulsa enter para coninuar',border_style="red"))
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
            libros_devolver = WordCompleter(arcana.prestados)
            nombre_libro = prompt('Introduce el nombre del libro a devolver',completer = libros_devolver).capitalize()
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

                    tlf = input('Introduce el numero de telefono del cliente: ')
                    correo_electronico = input('Introduce el correo electronico del cliente: ')
                    break
                except:
                    console.input("Las datos introducidos no son correctos")
                    continue
            arcana.agregar_cliente(dni,nombre,fecha_nac,tlf,correo_electronico)

        elif opcion == 7: # Mostrar usuarios registrados  ------------------------------------------------------------------------------------
            console.print('👥 Modo Épico: Registro de Clientes')
            arcana.mostrar_clientes_epic_mode()
            input()

        elif opcion == 8: # Eliminar usuario  -----------------------------------------------------------------------------------------
            if arcana.clientes:
                console.print('Eliminar usuario')
                console.print("Clientes a eliminar")
                arcana.mostrar_clientes()
                eliminar_usuario = WordCompleter(arcana.clientes)
                dni = prompt("Introduce el DNI del usuario a eliminar: ",completer=eliminar_usuario)
                arcana.eliminar_usuario(dni)
            else:
                console.input(Panel("No hay clientes registrados",border_style="yellow",width=30))
            
        elif opcion == 9: # Salida del programa  -----------------------------------------------------------------------------------------
            console.input('Muchas gracias por usar el programa')
            break

        

if __name__ == "__main__":
    main()
