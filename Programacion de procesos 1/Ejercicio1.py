import tkinter as tk
from tkinter import font

def sumar():
    try:
        ress = int(numero1.get()) + int(numero2.get()) + int(numero3.get())
        resultado.config(text=f"Resultado suma: {ress}")
    except:
        resultado.config(text="Ingrese valores enteros")

def dividir():
    try:
        num3 = int(numero3.get())
        if num3 == 0:
            resultado.config(text="No se puede dividir por cero")
        else:
            ress = (int(numero1.get()) + int(numero2.get())) / num3
            resultado.config(text=f"Resultado división: {ress:.2f}")
    except:
        resultado.config(text="Ingrese valores enteros")

Formulario = tk.Tk()
Formulario.title("Operaciones con tres números")
Formulario.geometry("600x450")
Formulario.configure(bg="#f0f0f0")

titulo_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Arial", size=12)
button_font = font.Font(family="Arial", size=12, weight="bold")
result_font = font.Font(family="Arial", size=14, weight="bold")

numero1 = tk.StringVar()
numero2 = tk.StringVar()
numero3 = tk.StringVar()

main_frame = tk.Frame(Formulario, bg="#f0f0f0", padx=20, pady=20)
main_frame.pack(expand=True, fill="both")

titulo = tk.Label(main_frame, text="Calculadora de Tres Números", font=titulo_font, bg="#f0f0f0", fg="#333333")
titulo.pack(pady=10)

input_frame = tk.Frame(main_frame, bg="#f0f0f0")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Número 1", font=label_font, bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(input_frame, textvariable=numero1, width=30, font=label_font).grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Número 2", font=label_font, bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(input_frame, textvariable=numero2, width=30, font=label_font).grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="Número 3", font=label_font, bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
tk.Entry(input_frame, textvariable=numero3, width=30, font=label_font).grid(row=2, column=1, pady=5)

button_frame = tk.Frame(main_frame, bg="#f0f0f0")
button_frame.pack(pady=20)

suma_button = tk.Button(button_frame, text="Sumar", command=sumar, font=button_font, bg="#4CAF50", fg="white", padx=20, pady=10)
suma_button.grid(row=0, column=0, padx=10)

dividir_button = tk.Button(button_frame, text="Dividir", command=dividir, font=button_font, bg="#2196F3", fg="white", padx=20, pady=10)
dividir_button.grid(row=0, column=1, padx=10)

result_frame = tk.Frame(main_frame, bg="#f0f0f0")
result_frame.pack(pady=20)

resultado = tk.Label(result_frame, text="Resultado", font=result_font, bg="#f0f0f0", fg="#333333")
resultado.pack()

Formulario.mainloop()
