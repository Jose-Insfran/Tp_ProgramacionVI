import flet as ft

def main(page: ft.Page):
    page.window_width = 600
    page.window_height = 500
    page.title = "Lista de compras"

    # Crear un campo de texto para la entrada
    new_task = ft.TextField(hint_text="¿Qué necesitas comprar?", width=300)

    def add_clicked(e):
        # Agregar una casilla de verificación con la etiqueta de la tarea
        if new_task.value:  # Asegúrate de que no esté vacío
            page.add(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            new_task.focus()
            new_task.update()

    # Logo y texto del encabezado
    logo = ft.Image(src="C:\\Users\\CPE-LABORATORIO-03\\Documents\\pg6\\logo.png", width=150, height=150)
    header_text = ft.Text("Bienvenidos a la App de Lista de Compras", size=20, weight=ft.FontWeight.BOLD)

    # Organizar el encabezado en una columna
    header = ft.Column([
        logo,
        header_text
    ], alignment="center")

    # Agregar elementos a la aplicación
    page.add(
        header,
        ft.Divider(height=20),  # Agrega un divisor
        ft.Row([new_task, ft.ElevatedButton("Agregar", on_click=add_clicked)])
    )

# Ejecutar la aplicación
ft.app(target=main)