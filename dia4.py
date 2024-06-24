# Solicitar al usuario que ingrese una lista de números separados por comas
numeros = input("Introduce una lista de números separados por comas: ")

# Convertir la cadena de entrada en una lista de números
lista_numeros = [int(numero) for numero in numeros.split(',')]

# Ordenar la lista en orden ascendente
lista_numeros.sort()

# Mostrar la lista ordenada
print("La lista de números ordenada en orden ascendente es:")
print(lista_numeros)
