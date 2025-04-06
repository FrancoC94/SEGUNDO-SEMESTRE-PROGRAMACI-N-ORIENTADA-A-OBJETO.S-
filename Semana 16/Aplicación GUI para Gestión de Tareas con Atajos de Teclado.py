import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.tasks = []

        # Configuramos la interfaz
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Añadir tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_list = tk.Listbox(root, width=40, height=10)
        self.task_list.pack(pady=10)

        self.complete_button = tk.Button(root, text="Marcar como completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Atajos de teclado para hacerlo más fácil
        self.root.bind('<Return>', self.add_task)
        self.root.bind('<c>', self.complete_task)
        self.root.bind('<Delete>', self.delete_task)
        self.root.bind('<Escape>', self.close)

    def add_task(self, event=None):
        task = self.entry.get()
        if task:  # Si hay algo escrito, lo añadimos
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()
            self.entry.delete(0, tk.END)  # Limpiamos el campo de texto
        else:
            messagebox.showwarning("¡Ups!", "No olvides escribir una tarea antes de añadirla.")

    def complete_task(self, event=None):
        try:
            idx = self.task_list.curselection()[0]
            self.tasks[idx]["completed"] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("¡Ups!", "Selecciona una tarea para marcar como completada.")

    def delete_task(self, event=None):
        try:
            idx = self.task_list.curselection()[0]
            del self.tasks[idx]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("¡Ups!", "Selecciona una tarea para eliminar.")

    def update_task_list(self):
        self.task_list.delete(0, tk.END)  # Limpiamos la lista de tareas actual
        for task in self.tasks:
            task_text = f"{task['task']} (Completada)" if task["completed"] else task['task']
            self.task_list.insert(tk.END, task_text)  # Insertamos las tareas

    def close(self, event=None):
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
