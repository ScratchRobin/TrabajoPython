print("\n****SISTEMA DE MENU****\n")

print("\nCONDICIONAL IF\n")

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('INGRESO DE DOS NUMEROS', accion1),
        '2': ('INGRESO DE TRES NUMEROS', accion2),
        '3': ('MULTIPLO DE 7', accion3),
        '4': ('PAR E IMPAR', accion4),
        '5': ('TELEFONÍA', accion5),
        '6': ('Salir', salir)
    }

    generar_menu(opciones, '6')


def accion1():
    print('*****INGRESO DE DOS NUMEROS****')

    '''Determinar el mayor en 3 numeros ingresados'''
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    n3 = int(input("Ingrese el tercer numero: "))

    if n1 > n2 and n1 > n3:
        print("El numero mayor es: ", n1)
    elif n2>n1 and n2 > n3:
        print("El numero mayor es: ", n2)
    elif n3 > n1 and n3 > n2:
        print("El numero mayor es: ", n3)
    else:
        print("No se pudo establecer el numero mayor.")

    if n1 < n2 and n1 < n3:
        print("El numero menor es: ", n1)
    elif n2<n1 and n2 < n3:
        print("El numero menor es: ", n2)
    elif n3 > n1 and n3 > n2:
        print("El numero menor es: ", n3)
    else:
        print("No se pudo establecer el numero menor.")


def accion2():
    print('***INGRESO DE TRES VALORES*****')
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    n3=int(input("Ingrese el tercer numero:"))

    if n1 > n2 and n1 > n3:
        print("El numero mayor es: ", n1)
    elif n2>n1 and n2 > n3:
        print("El numero mayor es: ", n2)
    elif n3 > n1 and n3 > n2 :
        print("El numero mayor es: ",n3)
    else:
        print("No se pudo establecer el numero mayor.")

    if n1 < n2 and n1 < n3:
        print("El numero menor es: ", n1)
    elif n2<n1 and n2 < n3:
        print("El numero menor es: ", n2)
    elif n3 < n1 and n3 < n2 :
        print("El numero menor es: ", n3)
    else:
        print("No se pudo establecer el numero menor.")

def accion3():
    print('****MULTIPLO DE 7')

    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    num3=int(input("Ingrese el tercer numero: "))
    suma=int(num1+num2+num3)

    print("La suma es: ", suma)

    if suma%7==0:
        print("Es multiplo de 7.")
    else:
        print("No es numltiplo de 7.")
def accion4():
    print('****PAR E IMPAR******')

    num1=int(input("Ingrese un numero entero: "))
    num2=int(input("Ingrese otro numero: "))
    num3=int(input("Ingrese otro numero: "))
    sum=int(num1+num2+num3)
    prom=float(sum/3)
    print("\n")

    print("La suma es: ", sum)
    print("El promedio es: ", prom)

    if prom % 2 ==0 :
        print("El numero es par.")
    else:
        print(" El numero es impar ")

def accion5():
    print('****TELEFONÍA******')

    name = str(input("Ingrese su nombre: "))
    time1 = int(input("Ingrese el minuto consumidos: "))
    time2 = int(input("Ingrese el minutos consumidos intercionalmente: "))

    total = 0
    sumaTime=int(time1+time2)

    print("El tiempo es: ", sumaTime)

    if sumaTime <=25:
        print("Minutos gratis.")
    elif time1 <=25:
        Acumulador = time1-25
        time2 += Acumulador
        total=time2 * 2.5

        print("Los totales en los minutos nacionales es", time1 , "en Q")
        print("Los total de internacional es ", time2, "en Q")

        print("El total es: ", total, "en Q")
    else:
        print("\n\n")
        time2-=25
        total=(time1 + 0.5) + (time2+2.5)
        print("El total es: ", total, "en Q")
def salir():
    print('Saliendo')

if __name__ == '__main__':
    menu_principal()