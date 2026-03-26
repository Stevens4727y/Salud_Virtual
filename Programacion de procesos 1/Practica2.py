import tkinter as tk

def calcular_salario():
    try:
        base = float(salario_base_var.get())
        extras = float(horas_extra_var.get())
        total = base + extras
        resultado_var.set(f"Salario Total: C${total:.2f}")
    except:
        resultado_var.set("Error en datos")

ventana = tk.Tk()
ventana.title("Gestión de Empleado")
ventana.geometry("350x420")
ventana.configure(bg="#1e1e1e")

frame = tk.Frame(ventana, bg="#2c2c2c", padx=20, pady=20)
frame.pack(expand=True)

# Variables
nombre_var = tk.StringVar()
apellido1_var = tk.StringVar()
apellido2_var = tk.StringVar()
salario_base_var = tk.StringVar()
horas_extra_var = tk.StringVar()
resultado_var = tk.StringVar()

# Estilo
def label(text):
    return tk.Label(frame, text=text, fg="white", bg="#2c2c2c")

def entry(var):
    return tk.Entry(frame, textvariable=var, bg="#3c3c3c", fg="white", insertbackground="white")

# UI
label("Nombre de empleado").grid(row=0, column=0, sticky="w")
entry(nombre_var).grid(row=1, column=0, pady=5)

label("Apellido 1").grid(row=2, column=0, sticky="w")
entry(apellido1_var).grid(row=3, column=0, pady=5)

label("Apellido 2").grid(row=4, column=0, sticky="w")
entry(apellido2_var).grid(row=5, column=0, pady=5)

label("Salario Base").grid(row=6, column=0, sticky="w")
entry(salario_base_var).grid(row=7, column=0, pady=5)

label("Horas Extra").grid(row=8, column=0, sticky="w")
entry(horas_extra_var).grid(row=9, column=0, pady=5)

tk.Button(frame, text="Calcular", command=calcular_salario,
          bg="#2196F3", fg="white").grid(row=10, column=0, pady=10)

tk.Label(frame, textvariable=resultado_var,
         fg="#00ffcc", bg="#2c2c2c").grid(row=11, column=0)

ventana.mainloop()