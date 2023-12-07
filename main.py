import tkinter as tk
import socket
import requests
# Codigo creado con ChatGPT4
# Función para obtener la dirección IP local
def get_local_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        local_ip_label.config(text=f"Tu dirección IP local es: {ip_address}")
    except Exception as e:
        local_ip_label.config(text="No se pudo obtener la dirección IP local")

# Función para obtener la dirección IP pública
def get_public_ip_address():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        public_ip = response.json()["ip"]
        public_ip_label.config(text=f"Tu dirección IP pública es: {public_ip}")
    except Exception as e:
        public_ip_label.config(text="No se pudo obtener la dirección IP pública")

# Crear la ventana
window = tk.Tk()
window.title("Direcciones IP")

# Etiqueta para la dirección IP local
local_ip_label = tk.Label(window, text="", font=("Arial", 12))
local_ip_label.pack(pady=10)

# Etiqueta para la dirección IP pública
public_ip_label = tk.Label(window, text="", font=("Arial", 12))
public_ip_label.pack(pady=10)

# Botón para obtener la dirección IP local
local_ip_button = tk.Button(window, text="Obtener IP Local", command=get_local_ip_address)
local_ip_button.pack()

# Botón para obtener la dirección IP públic a
public_ip_button = tk.Button(window, text="Obtener IP Pública", command=get_public_ip_address)
public_ip_button.pack()

# Ejecutar la aplicación de  ChatGPT
window.mainloop()
