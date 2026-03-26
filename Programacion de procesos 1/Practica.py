import tkinter as tk
from tkinter import ttk

def calcular():
    try:
        precio = float(precio_var.get())
        iva = precio * 0.15
        total = precio + iva
        resultado_var.set(f"Total + IVA: C${total:.2f}")
    except:
        resultado_var.set("Error en datos")

ventana = tk.Tk()
ventana.title("Gestión de Dispositivos")
ventana.geometry("350x350")
ventana.configure(bg="#1e1e1e")

frame = tk.Frame(ventana, bg="#2c2c2c", padx=20, pady=20)
frame.pack(expand=True)

# Variables
nombre_var = tk.StringVar()
tipo_var = tk.StringVar()
precio_var = tk.StringVar()
resultado_var = tk.StringVar()

# Estilo
def label(text):
    return tk.Label(frame, text=text, fg="white", bg="#2c2c2c")

def entry(var):
    return tk.Entry(frame, textvariable=var, bg="#3c3c3c", fg="white", insertbackground="white")

# UI
label("Nombre Dispositivo").grid(row=0, column=0, sticky="w")
entry(nombre_var).grid(row=1, column=0, pady=5)

label("Tipo de Dispositivo").grid(row=2, column=0, sticky="w")
ttk.Combobox(frame, textvariable=tipo_var,
             values=["USB", "Teclado", "Auriculares"]).grid(row=3, column=0, pady=5)

label("Precio").grid(row=4, column=0, sticky="w")
entry(precio_var).grid(row=5, column=0, pady=5)

tk.Button(frame, text="Calcular", command=calcular,
          bg="#4CAF50", fg="white").grid(row=6, column=0, pady=10)

tk.Label(frame, textvariable=resultado_var,
         fg="#00ffcc", bg="#2c2c2c").grid(row=7, column=0)

ventana.mainloop()