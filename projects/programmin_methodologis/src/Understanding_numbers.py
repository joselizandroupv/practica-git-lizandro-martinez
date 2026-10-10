# Numeros
# Enteros - Integers
"""
Los Numeros enteros los podemos
Sumar (+), Restar (-), Multiplicar (*)
y Dividir (/), Division Entera (//),
Potencias (**n) y Modulo (10%2).
"""

print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
number_1 = 5
number_2 = 10
print(number_1, number_2)
age = 34
print(age)
name = "Charlie Mercury"
print(name, age)

# Floats
"""
    Python llama Float a cualquier numero 
    con punto decimal
"""

print(0.1 + 0.1)
print(0.2 - 0.2)
print(2 * 0.1)
print(2 * 0.2)

# Imprmirn la edad de alguien
age = 34  # Variable Int
# message = "Charly tiene" + age + "años." (ERROR)
message = "Charly tiene " + str(age) + " años."
message_f = f"Charly tiene {age} años."
print(message)
print(message_f)

"""
    TypeError: Python no puede reconocer el tipo de 
    informacion q se esta utilizando.

    En este caso no se puden concatenar
    Ints con String
"""

print(type(age))
print(type(0.1))
print(type(message_f))
print(type(message_f), type(1 + 5), type(2 + 0.5))
