from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.python import PythonLexer
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML

# Definir un estilo personalizado
style = Style.from_dict({
    # Estilo general
    '': 'bg:#1e1e1e fg:#ffffff',  # Fondo oscuro y texto blanco
    'prompt': 'bold fg:#00ff00',  # Texto del prompt en verde neón y negrita
    'cursor': 'fg:#ff00ff',       # Cursor en magenta
    'hint': 'italic fg:#00ffff',  # Pista en azul eléctrico y cursiva
    'error': 'bold fg:#ff0000',   # Mensajes de error en rojo brillante
})

# Atajos de teclado personalizados
bindings = KeyBindings()

@bindings.add('c-c')  # Ctrl+C para salir
def _(event):
    event.app.exit(result="Salir")

@bindings.add('c-t')  # Ctrl+T para mostrar un mensaje especial
def _(event):
    event.app.exit(result="🎉 ¡Atajo presionado!")

# Función principal
def main():
    # Mensaje de bienvenida
    print(HTML('<prompt>🌟 Bienvenido al Prompt Chulo 🌟</prompt>'))
    
    # Prompt con estilo chulo
    respuesta = prompt(
        HTML('<prompt>⚡ Escribe algo:</prompt> '),  # Prompt personalizado
        style=style,
        lexer=PygmentsLexer(PythonLexer),          # Resaltado de sintaxis (opcional)
        key_bindings=bindings,                     # Atajos de teclado
        multiline=True,                            # Permitir múltiples líneas
        enable_open_in_editor=True,                # Abrir en editor externo si es necesario
        mouse_support=True,                        # Soporte para ratón
    )
    
    # Mostrar la respuesta
    if respuesta.strip():  # Si no está vacío
        print(HTML(f'<hint>✨ Ingresaste:</hint> <b>{respuesta}</b>'))
    else:
        print(HTML('<error>⚠️ No ingresaste nada.</error>'))

if __name__ == "__main__":
    main()