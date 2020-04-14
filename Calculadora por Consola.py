sw = True

def sumar():
    num1 = int(input('Ingrese un numero: '))
    num2 = int(input('Ingrese un numero: '))
    print('La suma es: ', num1+num2)

def restar():
    num1 = int(input('Ingrese un numero: '))
    num2 = int(input('Ingrese un numero: '))
    print('La resta es: ', num1 - num2)

def multiplicar():
    num1 = int(input('Ingrese un numero: '))
    num2 = int(input('Ingrese un numero: '))
    print('La multiplicacion es: ', num1 * num2)

def dividir():
    num1 = int(input('Ingrese un numero: '))
    num2 = int(input('Ingrese un numero: '))
    print('La division es: ', num1 / num2)


def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False


def opcion_no_disponible():
    print('Opcion no disponible')

menu = '''
======= Calculadora ======
1. Sumar dos numeros
2. Restar dos numeros 
3. Multiplicar 2 numeros
4. Dividir dos numeros
5. Salir
'''

while sw:
    print(menu)
    opcion = int(input('Ingrese la opcion: '))
    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 3:
        multiplicar()
    elif opcion == 4:
        dividir()
    elif opcion == 5:
        terminar_programa()
    else:
        opcion_no_disponible()
