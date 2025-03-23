import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime


# Función para agregar un evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    # Verificar que todos los campos están completos
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")
        return

    # Añadir el evento a la lista
    eventos_tree.insert("", "end", values=(fecha, hora, descripcion))
    entry_fecha.delete(0, "end")
    entry_hora.delete(0, "end")
    entry_descripcion.delete(0, "end")


# Función para eliminar el evento seleccionado
def eliminar_evento():
    selected_item = eventos_tree.selection()
    if selected_item:
        eventos_tree.delete(selected_item)
    else:
        messagebox.showwarning("Seleccionar Evento", "Por favor, selecciona un evento para eliminar.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# Treeview para mostrar eventos
eventos_tree = ttk.Treeview(ventana, columns=("Fecha", "Hora", "Descripción"), show="headings")
eventos_tree.heading("Fecha", text="Fecha")
eventos_tree.heading("Hora", text="Hora")
eventos_tree.heading("Descripción", text="Descripción")
eventos_tree.pack(padx=10, pady=10, fill="both", expand=True)

# Campos de entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(padx=10, pady=10)

tk.Label(frame_entrada, text="Fecha (DD/MM/AAAA):").grid(row=0, column=0)
entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1)

tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1)

# Botones para agregar y eliminar eventos
btn_agregar = tk.Button(ventana, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(padx=10, pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.pack(padx=10, pady=5)

# Botón de salir
btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
btn_salir.pack(padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
