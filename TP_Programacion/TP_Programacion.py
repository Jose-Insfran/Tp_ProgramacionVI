import flet as ft

def main(page: ft.Page):
    # Configuración inicial de la ventana de la aplicación
    page.window_width = 600
    page.window_height = 400
    page.title = "Lista de compras"

    # Lista para almacenar las tareas que el usuario agregue
    tasks = []

    # Función que se ejecuta al agregar una nueva tarea
    def add_task(e):
        # Verifica que el campo de texto no esté vacío
        if new_task.value:
            # Agrega la tarea a la lista como un diccionario, donde "label" es el nombre de la tarea
            # y "editing" indica si está en modo de edición
            tasks.append({"label": new_task.value, "editing": False})
            # Actualiza la interfaz para mostrar la tarea nueva
            update_task_list()
            # Limpia el campo de texto y lo enfoca nuevamente
            new_task.value = ""
            new_task.focus()
            # Refresca la página para reflejar los cambios
            page.update()

    # Función para eliminar una tarea de la lista
    def remove_task(e, index):
        # Elimina la tarea en la posición 'index'
        tasks.pop(index)
        # Vuelve a mostrar la lista actualizada
        update_task_list()
        # Refresca la página para que el usuario vea los cambios
        page.update()

    # Función para poner una tarea en modo de edición
    def modify_task(e, index):
        # Cambia el estado de la tarea a "editing", permitiendo su modificación
        tasks[index]["editing"] = True
        # Actualiza la lista para que el usuario pueda editar la tarea
        update_task_list()

    # Función para guardar los cambios realizados a una tarea
    def save_task(e, index, new_value):
        # Actualiza el nombre de la tarea con el nuevo valor introducido por el usuario
        tasks[index]["label"] = new_value.value
        # Cambia el estado de "editing" a False para salir del modo de edición
        tasks[index]["editing"] = False
        # Actualiza la lista para que la tarea modificada se muestre de nuevo
        update_task_list()

    # Función para actualizar y mostrar la lista de tareas en la pantalla
    def update_task_list():
        task_widgets = []
        # Itera sobre las tareas y las organiza visualmente
        for i, task in enumerate(tasks):
            if task["editing"]:
                # Si la tarea está en modo de edición, muestra un campo de texto y un botón para guardar
                new_value = ft.TextField(value=task["label"], width=200)
                save_button = ft.ElevatedButton("Guardar", on_click=lambda e, idx=i, field=new_value: save_task(e, idx, field))
                task_widgets.append(ft.Row([new_value, save_button]))
            else:
                # Si la tarea no está en modo de edición, muestra un checkbox con su nombre, y los botones de modificar y eliminar
                checkbox = ft.Checkbox(label=task["label"])
                modify_button = ft.ElevatedButton("Modificar", on_click=lambda e, idx=i: modify_task(e, idx))
                delete_button = ft.ElevatedButton("Eliminar", on_click=lambda e, idx=i: remove_task(e, idx))
                task_widgets.append(ft.Row([checkbox, modify_button, delete_button]))

        # Actualiza la interfaz visual con los elementos de la lista
        task_list.controls = task_widgets
        page.update()

    # Campo de texto donde el usuario ingresa nuevas tareas
    new_task = ft.TextField(hint_text="¿Qué necesitas comprar?", width=300)

    # Imagen del logo de la aplicación
    logo = ft.Image(src="C:\\Users\\enriq\\TP_Programacion\\logos.PNG", width=150, height=150)

    # Texto del encabezado con el título de la aplicación
    header_text = ft.Text("Bienvenidos a la App de Lista de Compras", size=20, weight=ft.FontWeight.BOLD)
    
    # Organizar la imagen y el texto del encabezado para que se centren
    header = ft.Column([
        logo,
        header_text
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # Contenedor que almacenará y mostrará la lista de tareas
    task_list = ft.Column([], alignment="center")

    # Agregar todos los elementos de la interfaz (encabezado, campo de texto, botones, lista de tareas) a la página
    page.add(
        header,
        ft.Divider(height=20),  # Espacio entre el encabezado y el resto
        ft.Row([new_task, ft.ElevatedButton("Agregar", on_click=add_task)]),  # Campo para agregar tareas y botón
        ft.Divider(height=10),  # Espacio antes de la lista de tareas
        task_list  # La lista de tareas se muestra aquí
    )

# Ejecutar la aplicación
ft.app(target=main)
