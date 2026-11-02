articulos  = ['Portatil', 'Mouse inalambrico', 'Base refrigerante', 
                'Licencia antivirus', 'Memoria USB 64GB', 'Impresora'] 
precios    = [2350000, 65000, 89000, 120000, 38000, 780000] 
cantidades = [2, 5, 3, 4, 10, 1] 

IVA = 1.19
DESCUENTO = 0.95
MINIMO = 5000000

# Calculamos subtotales y total desde el inicio
subtotales = []
suma_subtotal = 0
for i in range(len(precios)):
        subtotal = precios[i] * cantidades[i]
        subtotales.append(subtotal)
        suma_subtotal += subtotal

if suma_subtotal > MINIMO:
        total_pagar = suma_subtotal * DESCUENTO * IVA
else:
        total_pagar = suma_subtotal * IVA

# Mostramos al usuario el menu disponible 
print('''MENU
1. Ver el carrito
2. Ver la lista de subtotales
3. Ver la factura oredenada
4. Ver el descuento toal
5. Devolver un articulo
6. Salir''')


while True:
        # Damos la entrada para que el usuario escoja opcion 
        opcion = input('Ingrese una opcion del menu: ')
        # Validamos que la entrada sea valida 
        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 6:
                print('Error. Ingrese una opcion valida')
                continue
        else:
             opcion = int(opcion)
        # desarrollamos las condiocionales respecto a cada opcion del menu 
        if opcion == 1:
                print('\n===CARRITO DE ARTICULOS===')
                for i in range(len(articulos)):
                        print(f'{i+1} ---> {articulos[i]}')
        elif opcion == 2:
                print('\n===LISTA DE SUBTOTALES===')
                for i in range(len(precios)):
                        print(f'{i+1} --> {subtotales[i]}')
        elif opcion == 3:
                print('\n===FACTURA ORDENADA===')
                # Mostramos la factura en formato ordenada con un for 
                for n in range(len(articulos)):
                        print(f'Articulo: {articulos[n]:>20} \tCantidad: {cantidades[n]:>7} \tPrecio por unidad: {precios[n]:>7} \tSubtotal: {subtotales[n]:>7}')
        elif opcion == 4: 
                print('\n===DESCUENTOS APLICADOS===')  
                # verificamos los descuentos por montos de compra             
                if suma_subtotal > 5000000:
                        descuento = suma_subtotal * 0.95
                        total_pagar = descuento * 1.19
                        print(f'OBTUVISTE UN DESCUENTO POR MONTO DE COMPRA DEL 5%. El total es ---> {total_pagar:,.2f}')
                else:
                        print('NO APLICA AL DESCEUNTO')
                        total_pagar = suma_subtotal * 1.19
                        print(f'El total pagar con el IVA es ---> {total_pagar:,.2f}')
        elif opcion == 5:
                print('\n===DEVOLUCION DE ARTICULO===')
                devolver = input('Ingrese el articulo a devolver: ')
                posicion = -1

                # El for solo busca la posicion
                for i in range(len(articulos)):
                        if articulos[i].lower() == devolver.lower():
                                posicion = i

                # borrar y recalcular
                if posicion == -1:
                        print('El producto ingresado no existe')
                else:
                        articulos.pop(posicion)
                        precios.pop(posicion)
                        cantidades.pop(posicion)
                        subtotales.pop(posicion) 

                        # Recalculamos la suma y el total
                        suma_subtotal = 0
                        for i in range(len(subtotales)):
                                suma_subtotal += subtotales[i]

                        if suma_subtotal > MINIMO:
                                total_pagar = suma_subtotal * DESCUENTO * IVA
                        else:
                                total_pagar = suma_subtotal * IVA
                        
                        print(f'Nueva lista de productos ---> {articulos}')
                        print(f'Lista de precios actualizada ---> {precios}')
                        print(f'Lista de nuevas cantidades ---> {cantidades}')
        elif opcion == 6:
                print('Saliendo del programa.... Gracias por la compra!!')
                break

print('\n---RESUMEN DE LA COMPRA---')
for n in range(len(articulos)):
        print(f'Articulo: {articulos[n]:>20} \tCantidad: {cantidades[n]:>7} \tPrecio por unidad: {precios[n]:>7} \tSubtotal: {subtotales[n]:>7}')
print(f'El total a pagar es ---> {total_pagar:,.2f}')
