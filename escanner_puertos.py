import socket 

ip = input("Ingresa la direccion IP a escanear: ")
# Definimos el rango
from puerto in range(1,65535):
# Usamos IPs version 4
# Prorocolo tcp/IP
    sock = socket.socket(socket.AF.INET, socket.SOCK_STREAM)
    sock.settimeout(5)
# Se conecta a la ip que le damos en el puerto especificado
    result = sock.connect_ex((ip, puerto))
# Imprimimos los resultados
    if result == 0:
        print("Puerto abierto: " + str(puerto))
        sock.close()
    else:
        print("Puerto Cerrado: " + str(puerto))