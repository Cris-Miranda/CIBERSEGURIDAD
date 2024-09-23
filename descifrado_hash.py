import hashlib  # Se importamos la librería 'hashlib' que permite realizar operaciones de hashing, en este caso para calcular el hash SHA-256 de una cadena de texto.

hash_file = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08" 
# Almcenamos en la variable 'hash_file' el valor del hash SHA-256 correspondiente a una cadena previamente calculada.
# El propósito del programa es encontrar la cadena original (contraseña) que produjo este hash usando un ataque de diccionario.

dic_file = input("Ingresa la direccion del archivo de tu diccionario: ")
# Solicitamos al usuario que ingrese la dirección (ruta) de un archivo que contiene un diccionario, es decir, una lista de posibles contraseñas.
# Este archivo será utilizado para comparar los hashes generados con el valor de 'hash_file'.

with open(dic_file, 'r') as file:
    # Intentamos abrir el archivo cuyo nombre o ruta fue ingresado por el usuario.
    # La palabra clave 'with' asegura que el archivo se abra y cierre correctamente.
    
    diccionario = [line.strip() for line in file]
    # Leemos cada línea del archivo y se almacena en una lista llamada 'diccionario'. 
    # Cada línea corresponde a una posible contraseña, eliminando cualquier espacio o salto de línea innecesario con 'strip()'.

    for password in diccionario:
        # Con el ciclo iteramos sobre cada posible contraseña contenida en el diccionario.

        hash_calculado = hashlib.sha256(password.encode()).hexdigest()
        # Calculamos el hash SHA-256 de la contraseña actual (iterada en ese momento).
        # La función 'encode()' convierte la contraseña de una cadena de texto a formato binario (bytes).
        # 'hexdigest()' convierte el hash generado a una cadena de texto hexadecimal, que es el formato común de representación de hashes.

        if hash_calculado == hash_file:
            # Comparamos el hash calculado con el hash que estamos intentando "romper".
            # Si coinciden, se ha encontramos la contraseña original.

            print("La contraseña original es: " + password)
            # Si los hashes coinciden, se imprimimos la contraseña original que generó el hash y se termina la búsqueda.

            break
            # Nos salimos del bucle 'for' ya que no es necesario seguir buscando una vez que se encuentra la contraseña.
        else:
            # Si los hashes no coinciden, seguimos buscando con la siguiente contraseña del diccionario.

            print("La contraseña no se encuentra en el diccionario")
            # Si el hash calculado no coincide con el hash buscado, imprimimos que la contraseña no se encuentra en el diccionario.
