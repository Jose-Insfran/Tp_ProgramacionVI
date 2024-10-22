import flet as ft

def main(page: ft.Page):
    page.window_width = 600
    page.window_height = 800
    page.title = "Lista de compras"

    tasks = []  # Lista para almacenar las tareas agregadas dinámicamente

    # Función para agregar una tarea
    def add_task(e):
        if new_task.value:  # Asegúrate de que no esté vacío
            tasks.append({"label": new_task.value, "editing": False})  # Agregar como diccionario
            update_task_list()
            new_task.value = ""
            new_task.focus()
            page.update()  # Actualiza la página después de agregar la tarea

    # Función para eliminar una tarea
    def remove_task(e, index):
        tasks.pop(index)
        update_task_list()
        page.update()  # Actualiza la página después de eliminar la tarea

    # Función para modificar una tarea
    def modify_task(e, index):
        tasks[index]["editing"] = True
        update_task_list()

    # Función para guardar la tarea modificada
    def save_task(e, index, new_value):
        tasks[index]["label"] = new_value.value  
        tasks[index]["editing"] = False  # Salir del modo edición
        update_task_list()

    # Función para limpiar toda la lista
    def clear_list(e):
        tasks.clear()  # Vacía la lista de tareas
        update_task_list()

    # Función para actualizar la lista de tareas en la interfaz
    def update_task_list():
        task_widgets = []
        for i, task in enumerate(tasks):
            if task["editing"]:
                # Modo edición: Mostrar TextField y botón Guardar
                new_value = ft.TextField(value=task["label"], width=200)
                save_button = ft.ElevatedButton("Guardar", on_click=lambda e, idx=i, field=new_value: save_task(e, idx, field))
                task_widgets.append(ft.Row([new_value, save_button]))
            else:
                # Modo normal: Mostrar Checkbox y botones Modificar (con ícono de lápiz) y Eliminar (con ícono de basurero)
                checkbox = ft.Checkbox(label=task["label"])
                modify_button = ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, idx=i: modify_task(e, idx))
                delete_button = ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, idx=i: remove_task(e, idx))
                task_widgets.append(ft.Row([checkbox, modify_button, delete_button]))

        task_list.controls = task_widgets
        page.update()  # Actualiza la lista visualmente

    # Crear un campo de texto para la entrada
    new_task = ft.TextField(hint_text="¿Qué necesitas comprar?", width=300)

    # Logo y texto del encabezado
    logo = ft.Image(src="C:\\Users\\enriq\\TP_Programacion\\logos.PNG", width=150, height=150)

    # Centrar la imagen y el texto
    header_text = ft.Text("Bienvenidos a la App de Lista de Compras", size=20, weight=ft.FontWeight.BOLD)
    
    # Organizar el encabezado en una columna centrada
    header = ft.Column([
        logo,
        header_text
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)  

    # Contenedor para la lista de tareas
    task_list = ft.Column([], alignment="center")

    # Botón para limpiar toda la lista con ícono de basurero
    clear_button = ft.IconButton(icon=ft.icons.DELETE_SWEEP, on_click=clear_list, icon_size=30, tooltip="Limpiar lista")

    # Agregar elementos a la aplicación
    page.add(
        header,
        ft.Divider(height=20),  
        ft.Row([new_task, ft.ElevatedButton("Agregar", on_click=add_task)]),  
        ft.Divider(height=10),
        task_list,  
        ft.Divider(height=20),
        clear_button  # Botón de ícono para limpiar la lista
    )

# Ejecutar la aplicación
ft.app(target=main)

