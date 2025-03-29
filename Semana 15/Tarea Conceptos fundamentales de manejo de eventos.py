import tkinter as tk
from tkinter import messagebox


class TareaApp:
    def __init__(self, root):
        # Inicializamos la ventana principal de la aplicación
        self.root = root
        self.root.title("Lista de Tareas")  # Título que aparece en la ventana
        self.root.geometry("400x400")  # Tamaño de la ventana (ancho x alto)

        # Lista para almacenar las tareas y su estado (completada o no)
        self.tareas = []

        # Campo de entrada para que el usuario escriba nuevas tareas
        self.entry_tarea = tk.Entry(self.root, font=("Arial", 14), width=30)
        self.entry_tarea.pack(pady=20)  # Se agrega con un poco de espacio arriba y abajo

        # Botón para añadir una nueva tarea a la lista
        self.boton_agregar = tk.Button(self.root, text="Añadir Tarea", font=("Arial", 12), command=self.agregar_tarea)
        self.boton_agregar.pack(pady=5)  # Un espacio pequeño entre botones

        # La lista donde se mostrarán las tareas. Aquí el usuario puede verlas y seleccionarlas.
        self.lista_tareas = tk.Listbox(self.root, height=10, width=40, font=("Arial", 12), selectmode=tk.SINGLE)
        self.lista_tareas.pack(pady=20)  # Espacio alrededor de la lista

        # Botón para marcar la tarea seleccionada como completada
        self.boton_completar = tk.Button(self.root, text="Marcar como Completada", font=("Arial", 12),
                                         command=self.marcar_completada)
        self.boton_completar.pack(pady=5)

        # Botón para eliminar la tarea seleccionada de la lista
        self.boton_eliminar = tk.Button(self.root, text="Eliminar Tarea", font=("Arial", 12),
                                        command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        # Asociamos la tecla Enter con la acción de agregar tarea (más fácil para el usuario)
        self.entry_tarea.bind("<Return>", self.agregar_tarea_tecla)

    # Función para agregar una nueva tarea cuando el usuario hace clic en "Añadir Tarea"
    def agregar_tarea(self, event=None):
        tarea = self.entry_tarea.get()  # Obtenemos el texto que el usuario escribió
        if tarea != "":
            self.tareas.append({"tarea": tarea, "completada": False})  # Añadimos la tarea a la lista
            self.actualizar_lista()  # Actualizamos la vista de la lista de tareas
            self.entry_tarea.delete(0, tk.END)  # Limpiamos el campo de entrada para la siguiente tarea
        else:
            # Si el campo está vacío, mostramos un mensaje de advertencia
            messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

    # Esta función se llama cuando el usuario presiona Enter después de escribir una tarea
    def agregar_tarea_tecla(self, event):
        self.agregar_tarea()  # Llamamos a la misma función de agregar tarea

    # Función para actualizar la lista de tareas, mostrando todas las tareas actuales
    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)  # Limpiamos la lista actual de la interfaz

        for idx, tarea in enumerate(self.tareas):  # Iteramos sobre todas las tareas
            # Si la tarea está completada, cambiaremos el color de fondo para que se vea
            color_fondo = "lightgreen" if tarea["completada"] else "white"
            self.lista_tareas.insert(tk.END, tarea["tarea"])  # Insertamos la tarea en la lista
            self.lista_tareas.itemconfig(idx, {'bg': color_fondo})  # Aplicamos el color de fondo según el estado

    # Función para marcar una tarea como completada
    def marcar_completada(self):
        try:
            tarea_seleccionada = self.lista_tareas.curselection()[0]  # Obtenemos la tarea seleccionada
            self.tareas[tarea_seleccionada]["completada"] = True  # Marcamos la tarea como completada
            self.actualizar_lista()  # Actualizamos la lista de tareas para reflejar el cambio
        except IndexError:
            # Si no se ha seleccionado ninguna tarea, mostramos un mensaje de advertencia
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    # Función para eliminar una tarea de la lista
    def eliminar_tarea(self):
        try:
            tarea_seleccionada = self.lista_tareas.curselection()[0]  # Obtenemos la tarea seleccionada
            del self.tareas[tarea_seleccionada]  # Eliminamos la tarea de la lista
            self.actualizar_lista()  # Actualizamos la lista de tareas después de eliminarla
        except IndexError:
            # Si no se ha seleccionado ninguna tarea, mostramos un mensaje de advertencia
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")


# Esta parte es lo que inicia la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Creamos la ventana principal
    app = TareaApp(root)  # Inicializamos la aplicación
    root.mainloop()  # Ejecutamos el bucle principal para que la aplicación funcione


