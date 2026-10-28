codigos = [101, 102, 103, 104, 105, 106, 107, 108] 
nombres = ['Mouse óptico', 'Teclado mecánico', 'Pad mouse XL', 'Diadema gamer', 
           'Hub USB 4 puertos', 'Cámara web HD', 'Soporte portátil', 'Cable USB-C'] 
precios = [35000, 189000, 42000, 155000, 58000, 129000, 76000, 22000] 

# declaaramos las listas y las listas auxiliares que utilizaremos 
carrito_codigos = [] 
carrito_cantidades = [] 
carrito_codigos_nueva = []
carrito_cantidades_nueva = []

# declaramos la variable de envio 
envio = 0

# Definimos la variable total
total = 0

# iniciamos el bucle while para que el usuario vea el menu 

while True:
    print('''Menu
    1. Ver catalogo
    2. Agregar producto
    3. Quitar producto
    4. Ver el carrito 
    5. Pagar''')
    opcion = input('Ingrese una opcion que desea realizar: ')

    # Evaluamos la entrada del usuario sea de tipo int() y este en el rango de las opciones
    if opcion.isdigit():
        opcion = int(opcion)
        if  1 <= opcion <= 5:
            print('Opcion valida')
        else:
            print('Opcion invalida. Esta fuera de rango')
    else:
        print('Error. Ingrese un numero')

    # aca damos las otras condicionales

    if opcion == 1:
        print(f'El catalogo de productos es ---> {nombres}')
    elif opcion == 2:
        codigo_nuevo = int(input('Ingrese el codigo del producto que desea agregar: '))
        cantidad = int(input('Ingrese la cantidad de productos que desea: '))
        if codigo_nuevo in codigos:
            carrito_codigos.append(codigo_nuevo)
            carrito_cantidades.append(cantidad)
            print('Codigo agregado exitosamente!!!')
        else:
            print('El producto ya existe ')
    elif opcion == 3:
        codigo_aquitar = int(input('Ingrese el codigo que desea eliminar: '))
        for i in range(len(carrito_codigos)):
            if carrito_codigos[i] != codigo_aquitar:
                carrito_codigos_nueva.append(carrito_codigos[i])
                carrito_cantidades_nueva.append(carrito_cantidades[i])
        carrito_codigos = carrito_codigos_nueva
        carrito_cantidades = carrito_cantidades_nueva
    elif opcion == 4:
        if len(carrito_codigos) == 0:
            print('El carrito esta vacio!! ')
        else:
            for i in range(len(carrito_codigos)):
                codigo = carrito_codigos[i]
                for j in range(len(codigos)):
                    if codigos[j] == codigo:
                        print(f'{codigo} - {nombres[j]} - {carrito_cantidades[i]} - {precios[j]:,.2f}')
    elif opcion == 5:
        for i in range(len(carrito_cantidades)):
            codigo = carrito_codigos[i]
            for j in range(len(codigos)):
                if codigos[j] == codigo:
                    subtotal = precios[j] * carrito_cantidades[i]                  
                    total += subtotal
        if total < 300000:
            envio += 12000
            print(f'El subtotal es ---> ${total:,.2f}')  
            print(f'El total es ---> ${total + envio:,.2f}')   
        else:      
            print(f'El total es ---> ${total:,.2f}')
        break
