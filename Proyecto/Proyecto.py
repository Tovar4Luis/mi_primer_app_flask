import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Función para añadir tarea
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar una tarea.")

# Función para eliminar tarea
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

# Función para marcar tarea como completada
def mark_task_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, f"{task} - Completado")
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

# Crear widgets
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)

btn_add_task = tk.Button(root, text="Añadir Tarea", width=20, command=add_task)
btn_add_task.pack(pady=5)

btn_delete_task = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
btn_delete_task.pack(pady=5)

btn_mark_task_completed = tk.Button(root, text="Marcar como Completada", width=20, command=mark_task_completed)
btn_mark_task_completed.pack(pady=5)

listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
