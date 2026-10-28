articulos  = ['Portatil', 'Mouse inalambrico', 'Base refrigerante', 
                'Licencia antivirus', 'Memoria USB 64GB', 'Impresora'] 
precios    = [2350000, 65000, 89000, 120000, 38000, 780000] 
cantidades = [2, 5, 3, 4, 10, 1] 
subtotales = []
suma_subtotal = 0

for i in range(len(precios)):
        precio_elemento = precios[i] * cantidades[i]
        subtotales.append(precio_elemento)
print(subtotales)

for n in range(len(articulos)):
        print(f'Artiulo: {articulos[n]} Cantidad: {cantidades[n]} Precio por unidad: {precios[n]}  Subtotal: {subtotales[n]}')

for a in range(len(subtotales)):
        suma_subtotal += subtotales[a]
if suma_subtotal > 5000000:
    descuento = suma_subtotal * 0.95
    total_pagar = descuento * 1.19
    print(f'OBTUVISTE UN DESCUENTO POR MONTO DE COMPRA DEL 5%. El total es ---> {total_pagar:,.2f}')
else:
    print(f'El total pagar con el IVA es ---> {suma_subtotal:,.2f}')

# damos la entrada de datos para el articulo a devolver
articulos_nuevo = []
precios_nuevos = []
cantidades_nuevas = []
encontrado = False

devolver = input('Ingrese el articulo a devolver: ').capitalize()

for i in range(len(articulos)):
        if articulos[i] == devolver:
            encontrado = True 
            total_pagar -= subtotales[i]
            print(f'Nuevo total descontando la devolucion. El total es ---> {total_pagar:,.2f}')
        else:
             articulos_nuevo.append(articulos[i])
             precios_nuevos.append(precios[i])
             cantidades_nuevas.append(cantidades[i])
if not encontrado:
      print('El producto ingresado no existe')
print(f'Nueva lista de productos ---> {articulos_nuevo}')
print(f'Lista de precios actualizada ---> {precios_nuevos}')
print(f'Lista de nuevas cantidades ---> {cantidades_nuevas}')

