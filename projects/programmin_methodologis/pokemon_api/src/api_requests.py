"""
    Vamos a revisar nuestra primmera peticion a una API.
"""
import requests

# La API corresponde a la informacion de Pikachu
api_url = https://pokeapi.co/api/v2//pokemon/25

# Peticion 
response = request.get(api_url, timeout = 10)

# Para revisar si hubo errores en la Peticion
response.raise_for_status() 

print(response.status_code)
pokemon = response.json()

# Tipo de variables de Pokemon
print(type(pokemon))

# Imprimir el contenido de Pokemon
# print(pokemon)

# Vamos a imprimir Id
print("Id: ", pokemon["id"])
print("Nombre: ", pokemon["name"])
print("No Recuerdo: ", pokemon[""])
print("Altura: ", pokemon["height"]/10)
print("Peso: ", pokemon["weight"]/10)

# Imprimir los datos
for element in pokemon["types"]:
    print("Pokemon Tipo: ", element["type"]["name"])