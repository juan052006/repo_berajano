monto_compra = float(input("Inegresa el monto de la compra:"))
miembro_tienda = input("Es miembro de la tienda?:").lower()
MONTO = 1000
if monto_compra >= MONTO  and miembro_tienda == "si":
    print(f"El costo de la compra es {monto_compra * 0.9:,.2f}")
elif monto_compra >= MONTO and miembro_tienda == "no":
    print(f"El costo de la compra es de {monto_compra * 0.95:,.2f}")
else:
    print(f"el costo de la compra es de: {monto_compra:,.2f}")
