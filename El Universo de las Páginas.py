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
from rich_pixels import Pixels
from rich.console import Console




console = Console()

system("cls")


menu="""
[#C0C0C0]
███████╗██╗         ██╗   ██╗███╗   ██╗██╗██╗   ██╗███████╗██████╗ ███████╗ ██████╗     ██████╗ ███████╗    ██╗      █████╗ ███████╗    ██████╗  █████╗  ██████╗ ██╗███╗   ██╗ █████╗ ███████╗
██╔════╝██║         ██║   ██║████╗  ██║██║██║   ██║██╔════╝██╔══██╗██╔════╝██╔═══██╗    ██╔══██╗██╔════╝    ██║     ██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██╔════╝ ██║████╗  ██║██╔══██╗██╔════╝
█████╗  ██║         ██║   ██║██╔██╗ ██║██║██║   ██║█████╗  ██████╔╝███████╗██║   ██║    ██║  ██║█████╗      ██║     ███████║███████╗    ██████╔╝███████║██║  ███╗██║██╔██╗ ██║███████║███████╗
██╔══╝  ██║         ██║   ██║██║╚██╗██║██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║   ██║    ██║  ██║██╔══╝      ██║     ██╔══██║╚════██║    ██╔═══╝ ██╔══██║██║   ██║██║██║╚██╗██║██╔══██║╚════██║
███████╗███████╗    ╚██████╔╝██║ ╚████║██║ ╚████╔╝ ███████╗██║  ██║███████║╚██████╔╝    ██████╔╝███████╗    ███████╗██║  ██║███████║    ██║     ██║  ██║╚██████╔╝██║██║ ╚████║██║  ██║███████║
╚══════╝╚══════╝     ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝     ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
[/]                                                                                                                                                                            
"""
menu2 = """
[#14effd ]
╔════════════════════════════════════════════════════════╗
║   [bold #ccf2ec]                ░▒▓ BIBLIOTECA ▓▒░ [/]                  ║
║   [#ccf2ec]          █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█[/]            ║
║   [#ccf2ec]          █[blink]  UNIVERSO DE LAS PAGINAS[/]    █[/]            ║  
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

while True:
    system("cls")
    console.print(titulo)
    console.print(menu_principal)
    input()


