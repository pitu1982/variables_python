# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

print('Ingrese palabra 3:')
palabra_3 = str(input())

suma= palabra_1 + palabra_2 + palabra_3
print('El resultado sumar', palabra_1, 'y', palabra_2,'y',palabra_3 , 'es', suma )

# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL
# Imprimir el resultado en pantalla
palabra_len = len('suma')
caracter_inicial = suma[0]
print(caracter_inicial)

palabra_len = len('suma')
caracter_inicial = suma[4]
print(caracter_inicial)

palabra_len = len('suma')
caracter_inicial = suma[12]
print(caracter_inicial)

print(suma[0],suma[4],suma[12])