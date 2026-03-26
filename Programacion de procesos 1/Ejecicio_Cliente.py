import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

ventana = tk.Tk()
ventana.title("Servidor Socket")
ventana.geometry("550x300")
ventana.configure(bg="#eeeaff")

marco_principal = tk.Frame(ventana, bg="Black", bd=2, highlightbackground="Black", highlightthickness=2)
marco_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

titulo = tk.Label(marco_principal, text="Conexion cliente servidor", font=("Arial", 14, "bold"), bg="white", fg="blue")
titulo.pack(pady=8)

marco_izquierdo = tk.Frame(marco_principal, bg="white")
marco_izquierdo.pack(fill=tk.BOTH, expand=True)

etiqueta_servidor = tk.Label(marco_izquierdo, text="Servidor activo puerto", bg="Black", fg="blue", font=("Times New Roman", 10, "bold"))
etiqueta_servidor.pack(anchor=tk.W)

resultado_servidor = scrolledtext.ScrolledText(marco_izquierdo, height=2)
resultado_servidor.pack(fill=tk.BOTH, pady=3)
resultado_servidor.insert(tk.END, "En espera\n")

etiqueta_conectado = tk.Label(marco_izquierdo, text="Cliente conectado", bg="white", fg="blue", font=("Times New Roman", 10, "bold"))
etiqueta_conectado.pack(anchor=tk.W)

resultado_conectado = scrolledtext.ScrolledText(marco_izquierdo, height=2)
resultado_conectado.pack(fill=tk.BOTH, pady=3)
resultado_conectado.insert(tk.END, "En espera...\n")

etiqueta_cliente = tk.Label(marco_izquierdo, text="Cliente (CMD)", bg="white", fg="blue", font=("Times New Roman", 10, "bold"))
etiqueta_cliente.pack(anchor=tk.W)

resultado_cliente = scrolledtext.ScrolledText(marco_izquierdo, height=8)
resultado_cliente.pack(fill=tk.BOTH, pady=3)
resultado_cliente.insert(tk.END, "En espera de mensajes\n")

def iniciar_servidor():
    boton_iniciar.config(state=tk.DISABLED)
    resultado_servidor.delete(1.0, tk.END)
    resultado_servidor.insert(tk.END, "Servidor en 6000...\n")

    def servidor_thread():
        host = "0.0.0.0"
        puerto = 6000

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, puerto))
        s.listen(1)

        conn, addr = s.accept()

        resultado_conectado.delete(1.0, tk.END)
        resultado_conectado.insert(tk.END, f"{addr}\n")

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            resultado_cliente.insert(tk.END, f"{data.strip()}\n")
            resultado_cliente.see(tk.END)

            if data.strip().lower() == "salir":
                break

            conn.send("Mensaje recibido\n".encode())

        conn.close()
        s.close()
        resultado_cliente.insert(tk.END, "Conexion cerrada\n")

    threading.Thread(target=servidor_thread, daemon=True).start()

def limpiar():
    resultado_servidor.delete(1.0, tk.END)
    resultado_servidor.insert(tk.END, "Esperando...\n")
    resultado_conectado.delete(1.0, tk.END)
    resultado_conectado.insert(tk.END, "Esperando...\n")
    resultado_cliente.delete(1.0, tk.END)
    resultado_cliente.insert(tk.END, "Esperando mensajes...\n")
    boton_iniciar.config(state=tk.NORMAL)

frame_botones = tk.Frame(marco_principal, bg="white")
frame_botones.pack(pady=5)

boton_iniciar = tk.Button(frame_botones, text="Iniciar", command=iniciar_servidor, bg="green", fg="white", width=10, height=1)
boton_iniciar.pack(side=tk.LEFT, padx=5)

boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar, bg="green", fg="white", width=10, height=1)
boton_limpiar.pack(side=tk.LEFT, padx=5)

ventana.mainloop()