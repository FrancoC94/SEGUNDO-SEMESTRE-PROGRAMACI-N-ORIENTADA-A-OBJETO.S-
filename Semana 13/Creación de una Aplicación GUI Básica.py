import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar():
    dato = entrada_texto.get()  # Obtener el texto ingresado
    if dato:  # Verificar si el campo no está vacío
        lista_datos.insert(tk.END, dato)  # Agregar a la lista
        entrada_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese un dato.")

# Función para limpiar la entrada de texto
def limpiar():
    entrada_texto.delete(0, tk.END)  # Limpiar el campo de texto

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Información")  # Título de la ventana

# Etiqueta de título
titulo = tk.Label(ventana, text="Aplicación de Gestión de Datos", font=("Arial", 14))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Etiqueta para indicar el campo de entrada
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.grid(row=1, column=0, padx=10)

# Campo de texto para ingresar los datos
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.grid(row=1, column=1, padx=10)

# Botón para agregar el dato
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.grid(row=2, column=0, pady=10)

# Botón para limpiar el campo de texto
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=2, column=1, pady=10)

# Lista para mostrar los datos agregados
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el loop de la ventana
ventana.mainloop()
#CRIS FRANCO