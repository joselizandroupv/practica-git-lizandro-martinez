# DICTIONARO SIMPLE
alien_0 = {"color": "green", "points": 5}

# Diccionario vacio
alien_1 = {}

# El diccionario mas simple
alien_2 = {"color": "verde"}

# Accesar a los elementos de un disccionario
print(f" Tu alien 0 es de color: {alien_0['color'].upper()}")
print(f" Si desvives al alien 0 se te otorga: {alien_0['points']}")

# Agregar elementos a un diccionario
alien_0["x_position"] = 25
alien_0["y_position"] = 0
print(alien_0)

# Modificando un valor en un diccionario
print("\n Modificando elementos del dict")
alien_0["y_position"] = 80
print(alien_0)

# Eliminando un elemento de un diccionario
print("\n Eliminando elementos al dict")
del alien_0["points"]
print(alien_0)

# Diccionario para objetos (elementos) similares
favorite_languajes = {"jen": "python", "sarah": "c", "eduard": "ruby", "pill": "python"}

# LOOPING Though all key-values pairs
# Looping a traves de todos los pares de llave-valor
user_0 = {
    "username": "Carlos",
    "firstname": "Tovar",
    "lastname": "Garcia",
    "age": 34,
    "birthday": "6-Feb",
}

print("\n Looping a traves de los pares llaves, valor \n")
for key, value in user_0.items():
    print("key: ", key)
    print("Value: ", value, "\n")

print("\n Looping a traves de los pares llaves \n")
for key in user_0.keys():
    print("key: ", key)

print("\n Looping a traves de los pares valores \n")
for value in user_0.values():
    print("value: ", value)
