"""
Vamos a realizar un programa que pregunte
el nombre de una persona y su edad
"""

name = input("¿Como te llamas? ")
age_txt = input("¿Cual es tu edad?")

try:
    age = int(age_txt)
    print(f"Hola {name}, Tienes {age_txt} años.")
    print("En Corea tendrias", age + 1)

except:  # noqa: E722
    print("El numero tecleado no es Entero.")

print("Procesos Posteriores")
