fecha = input("Ingrese la fecha de nacimiento (dd mm aaaa): ")

fecha = fecha.split()

while len(fecha) > 1:
    numvida = 0

    for num in fecha:
        numvida += int(num)
    print(fecha)
    fecha = str(numvida)
print(fecha)