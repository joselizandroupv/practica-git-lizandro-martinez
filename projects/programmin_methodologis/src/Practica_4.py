"""
Realizar un programa que calcule
el total de un ticket, tomando
en cuenta el IVA y la propina
"""

subtotal_txt = input("Subtotal (MX): ")
iva_txt = input("IVA (%) Ejemplo: 16: ")
tip_txt = input("Propina (%) Ejemplo: 10 (Negativo para Doña Tota)")

try:
    subtotal = float(subtotal_txt)
    iva = float(iva_txt) / 100
    tip = float(tip_txt) / 100

except:  # noqa: E722
    print("Entrada no Valida NMMS")
    raise SystemExit(1)

iva_account = subtotal * iva
tip_account = subtotal * tip
total = subtotal + iva_account + tip_account

print("Subtotal: ", subtotal)
print("Propina: ", tip_account)
print("Iva: ", iva_account)
print("Total: ", total)
