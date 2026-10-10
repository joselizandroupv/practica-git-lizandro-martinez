players = ["charly", "juan", "iancarlo", "lizandro"]
print("Lista Original: ", players)

# Slicing
print(players[0:2])  # ["charly", "juan"]

# El slicing me permite trabajar con un grupo
# especifico de una lista: el resultado se le
# conoce como "un slice" de la lista original.

print("1:4: ", players[1:4])  # ["juan", "iancarlo", "lizandro"]
print(":4: ", players[:4])  # ["charly", "juan", "iancarlo", "lizandro"]
print("2:: ", players[2:])  # ["iancarlo", "lizandro"]
print("[-3:]: ", players[-3:])  # ["juan", "iancarlo", "lizandro"]

# CASOS ESPECIALES DEL SLICING
# players = ["charly", "juan", "iancarlo", "lizandro"]

print(players[1:6])  # ["juan", "iancarlo", "lizandro"]
print(players[6:1])  # []
print(players[:0])  # []

# Looping through a slice
students = ["raul", "charly", "juan", "iancarlo", "lizandro"]
# TAREA Slicing [::]
for student in students[2:4]:
    print(f"El estudiante {student}, va a pasar la materia")
print(students)

# ¿Como podemos copiar una lista?
my_food = ["pizza", "tacos", "flautas"]
my_friend_food = my_food  # MANERA ERRONEA DE COPIAR UNA LISTA

# 3 MANERAS DE COPIAR UNA LISTA
# METODO 1.- Usando slicing
my_friend_food_2 = my_food[:]  # MANERA CORRECTA DE COPIAR UNA LISTA

# METODO 2.- Usando el metodo copy()
my_friend_food_3 = my_food.copy()  # MANERA CORRECTA DE COPIAR UNA LISTA

# METODO 3.- Usando el metodo BUILD IN list()
my_friend_food_4 = list(my_food)  # MANERA CORRECTA DE COPIAR UNA LISTA
