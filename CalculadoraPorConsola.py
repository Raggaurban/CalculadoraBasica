sw = True

def suma():
    x = int(input("Ingrese Numero: "))
    y = int(input("Ingrese Otro Numero: "))
    r = x + y
    print ('Resultado: ',r)

def resta():
    x = int(input("Ingrese Numero: "))
    y = int(input("Ingrese Otro Numero: "))
    r = x - y
    print('Resultado: ', r)

def multiplica():
    x = int(input("Ingrese Numero: "))
    y = int(input("Ingrese Otro Numero: "))
    r = x * y
    print('Resultado: ', r)

def divide():
    x = int(input("Ingrese Numero: "))
    y = int(input("Ingrese Otro Numero: "))
    r = x / y
    print('Resultado: ', r)

def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False

def opcion_no_disponible():
    print('Opcion no disponible')

menu = '''
======= Calculadora ======
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
'''

while sw:
    print(menu)
    opcion = int(input('Ingrese la opcion: '))
    if opcion is 1:
        suma()
    elif opcion is 2:
        resta()
    elif opcion is 3:
        multiplica()
    elif opcion is 4:
        divide()
    elif opcion is 5:
        terminar_programa()
    else:
        opcion_no_disponible()

