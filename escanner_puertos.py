import socket 

ip = input("Ingresa la direccion IP a escanear: ")
# Definimos el rango
from puerto in range(1,65535):

    sock = socket.socket(socket.AF.INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    
    result = sock.connect_ex((ip, puerto))