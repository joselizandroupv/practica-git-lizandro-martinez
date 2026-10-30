"""
Programa para calcular el indice de
masa corporal de una persona.

weigth: Peso de la Persona
heigth: Altura de la Persona
"""

weigth_txt = input("Peso (KG): ")
heigth_txt = input("Altura (MTS): ")

try:
    weigth = float(weigth_txt)
    heigth = float(heigth_txt)
    imc = weigth / (heigth**2)
    print(f"Tu indice de masa corporal es: {imc}")

except ValueError:
    print("Datos No Validos (Peso: 50.45, Altura: 1.70)")

except ZeroDivisionError:
    print("La Altura debe ser Diferente de Cero")

except Exception:  # noqa: BLE001
    print(Exception)
print("Procesos Posteriores")
