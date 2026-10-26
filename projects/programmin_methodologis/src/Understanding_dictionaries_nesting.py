# NESTINO

# Listas de Diccionarios
covenant_elite = {"name": "elite", "color": "azul", "points": 10, "shield": True}
covenant_jackal = {"name": "jackal", "color": "gray", "points": 6, "shield": True}
covenant_grunts = {"name": "grunt", "color": "orange", "points": 3, "shield": False}

covenants = []
covenants.append(covenant_elite)
covenants.append(covenant_jackal)
covenants.append(covenant_grunts)
print(covenants)

print("Looping")
# LOOPING though the list
for covenant in covenants:
    print(covenant)

# Vamos a crear una flotilla de enmigos (COVENANTS)
covenants_float = []
for _ in range(2):
    covenants_float.append(covenant_elite)

for _ in range(5):
    covenants_float.append(covenant_jackal)

for _ in range(20):
    covenants_float.append(covenant_grunts)

print("\n FLOTILLA")
print(covenants_float)

# NESTING: Una lista en un diccionario
# MENU
tacos = {"tortillas": ["maiz", "harina"], "guisos": ["bistek", "tripa", "pastor"]}

print(f"Tu has ordenado unos tacos de {tacos['guisos'][0]} ")
print(f"En tortillas de {tacos['tortillas'][1]}")

# Nesting: DICCIONARIOS EN DICCIONARIOS
# Menu de Usuarios

users = {
    "charly": {
        "firstname": "Carlos",
        "middlename": "Antonio",
        "lastname": "Tovar Garcia",
        "location": "Mexico",
        "age": 34,
    },
    "mrred": {
        "firstname": "Jose",
        "middlename": "Lizandro",
        "lastname": "Villarreal Martinez",
        "location": "Mexico",
        "age": 18,
    },
}

# LOOPING DE DICCIONARIOS EN DICCIONARIOS
for user, user_info in users.items():
    fullname = (
        f"{user_info['firstname']} {user_info['middlename']} {user_info['lastname']}"
    )
    location = user_info["location"]
    age = user_info["age"]
    print(f"\n\n El nombre completo de {user} es: ")
    print(fullname)
    print(f"\n La ubicacion de {user} es: ")
    print(location)
    print(f"\n La edad de {user}: ")
    print(age)
