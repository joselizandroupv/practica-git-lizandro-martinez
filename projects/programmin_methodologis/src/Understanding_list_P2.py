# Agregando elementos a una lista
motorcycles = ["honda", "mortalica", 'yamaha']
print(motorcycles) # ["honda", "mortalica", 'yamaha']

# Metodo APPEND agregar elememtos a la lista
print("\n Aprendi a usar el Metodo APPEND \n")

motorcycles.append("kawasaki")
print(motorcycles) # ["honda", "mortalica", 'yamaha', "kawasaki"]

"""
    El metodo APPEND ayuda a crear listas
    facilmente de manera dinamica
"""

motorcycles_2 = [] # Lista vacia
print(motorcycles_2)

motorcycle = "ducati"
motorcycles_2.append(motorcycle) # 1 elemento
motorcycles_2.append("yamaha") # 2 elemento
motorcycles_2.append("suzuki") # 3 elemento
print(motorcycles_2)
motorcycle = "charly"
print(motorcycles_2)
motorcycles_2.append(motorcycle)
print(motorcycles_2)

# Metodo INSERT agregar elememtos a la lista
print("\n Aprendi a usar el Metodo INSERT \n")

"""
    El metodo INSERT nos ayuda agregar elementos   
    a una lista en un indice especifico
"""

motorcycles_3 = ["honda", 'yamaha', "suziki"]
print("\n Lista ORIGINAL")
print(motorcycles_3)
motorcycles_3.insert(0 , "ducati")
print("Lista depues del metodo insert")
print(motorcycles_3) 

# Metodo POP
print("\n Aprendi a usar el Metodo POP \n")

"""
    Elimina el ultimom  elemento de una lista
    pero nos permite utilizar el elementyo depues
    de eliminarlo
"""
motorcycle_4 = ['honda', 'susuki', 'hd', 'mortalica']
print(motorcycle_4)
deleted_motorcycle = motorcycle_4.pop()
print(f"Tu motocicleta es {deleted_motorcycle}")
print(motorcycle_4)

# se puede utilizar tamnbien para eliminar un elemento especifico.
motorcycle_5 = ['honda', 'susuki', 'hd', 'mortalica']
print(motorcycle_5)
motorcycle_5.pop(0)
print(motorcycle_5) # Lista sin honda

# Metodo REMOVE
print("\n Aprendi a usar el Metodo REMOVE \n")

"""
    Permite eliminar elementos por su valor.
"""
motorcycle_6 = ['honda', 'yamaha', 'susuki', 'ducati']
print(motorcycle_6)
motorcycle_6.remove("yamaha")
print(motorcycle_6)

# Ordenar listas
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # Ordemnar la lista de manera permanente
# Argumento opcional de sort(reverse=True)
print(cars)

# Estudiar el metodo de la listas reverse
# estudiar metodos build-in, sorted(), len()

several_items = [["charly", "arnoldo"], ["subaru", "tsuru"]]
print(several_items[1][1])