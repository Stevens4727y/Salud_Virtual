import tkinter as tk

def registrar():
    resultado_text = "Registro:\n\n"
    resultado_text += f"Nombre: {nombre_var.get()}\n"
    resultado_text += f"Apellido: {apellido_var.get()}\n"
    resultado_text += f"Edad: {edad_var.get()}\n"
    resultado_text += f"Fecha de Nacimiento: {fecha_var.get()}\n"

    resultado.config(text=resultado_text)


def calcular():
    if salario_var.get() == "" or antiguedad_var.get() == "" or deduccion_var.get() == "":
        resultado.config(text="Faltan datos")
        return

    try:
        salario = float(salario_var.get())
    except:
        resultado.config(text="Salario inválido")
        return

    try:
        antiguedad = int(antiguedad_var.get())
    except:
        resultado.config(text="Antigüedad inválida")
        return

    try:
        deduccion = float(deduccion_var.get())
    except:
        resultado.config(text="Deducción inválida")
        return

    total = salario + antiguedad - deduccion
    resultado.config(text=f"Resultado: {total:.2f}")


root = tk.Tk()
root.title("Formulario")
root.geometry("400x400")

# Variables
nombre_var = tk.StringVar()
apellido_var = tk.StringVar()
edad_var = tk.StringVar()
fecha_var = tk.StringVar()
salario_var = tk.StringVar()
antiguedad_var = tk.StringVar()
deduccion_var = tk.StringVar()

tk.Label(root, text="Nombre").grid(row=0, column=0)
tk.Entry(root, textvariable=nombre_var).grid(row=0, column=1)

tk.Label(root, text="Apellido").grid(row=1, column=0)
tk.Entry(root, textvariable=apellido_var).grid(row=1, column=1)

tk.Label(root, text="Edad").grid(row=2, column=0)
tk.Entry(root, textvariable=edad_var).grid(row=2, column=1)

tk.Label(root, text="Fecha Nac").grid(row=3, column=0)
tk.Entry(root, textvariable=fecha_var).grid(row=3, column=1)

tk.Label(root, text="Salario").grid(row=4, column=0)
tk.Label(root, text="Antigüedad").grid(row=4, column=1)
tk.Label(root, text="Deducción").grid(row=4, column=2)

tk.Entry(root, textvariable=salario_var, width=10).grid(row=5, column=0)
tk.Entry(root, textvariable=antiguedad_var, width=10).grid(row=5, column=1)
tk.Entry(root, textvariable=deduccion_var, width=10).grid(row=5, column=2)

# Botones
tk.Button(root, text="Registrar", bg="red", command=registrar).grid(row=6, column=0, pady=10)
tk.Button(root, text="Calcular", bg="lightblue", command=calcular).grid(row=6, column=1)

# Resultado
resultado = tk.Label(root, text="Resultado")
resultado.grid(row=7, column=0, columnspan=3)

root.mainloop()