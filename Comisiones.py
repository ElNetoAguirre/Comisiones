nombre = input("Por favor, dime tu nombre: ")
ventas = int(input("Por favor, dime la cantidad de tus ventas totales en el mes: "))

comision = round((ventas * 0.13),2)

print(f"Hola {nombre}. Tu comsión por las ventas de éste mes es de: ${comision}")