import tkinter as tk

root = tk.Tk()

Numero_1 = tk.StringVar()
Numero_2 = tk.StringVar()
Resultado = tk.StringVar()
mensaje = tk.StringVar()

Ope_anc_bot = 17
Ope_alt_bot = 2

sw = False

def suma():
    x = int(Numero_1.get())
    y = int(Numero_2.get())
    r = x + y
    print ('Resultado: ',r)
    mensaje.set('Suma Realizada')
    Numero_1.set('')
    Numero_2.set('')
    Resultado.set(str(r))

def resta():
    x = int(Numero_1.get())
    y = int(Numero_2.get())
    r = x - y
    print('Resultado: ', r)
    mensaje.set('Resta Realizada')
    Numero_1.set('')
    Numero_2.set('')
    Resultado.set(str(r))

def multiplica():
    x = int(Numero_1.get())
    y = int(Numero_2.get())
    r = x * y
    print('Resultado: ', r)
    mensaje.set('Multiplicación Realizada')
    Numero_1.set('')
    Numero_2.set('')
    Resultado.set(str(r))

def divide():
    x = int(Numero_1.get())
    y = int(Numero_2.get())
    r = x / y
    print('Resultado: ', r)
    mensaje.set('Division Realizada')
    Numero_1.set('')
    Numero_2.set('')
    Resultado.set(str(r))

root.geometry('300x405')
root.title('Calculadora')

root.configure(bg="#007582")

tk.Label(root, text='Calculadora', bg="#007582", fg='white', font=("arial", 20, "bold")).place(x=75, y=10)
tk.Label(root, text='Primer Numero', bg="#007582", fg='white',).place(x=40, y=45)
tk.Label(root, text='Segundo Numero', bg="#007582", fg='white',).place(x=170, y=45)
tk.Label(root, text='Operaciones', bg="#007582", fg='white', font=("arial", 12, "bold")).place(x=100, y=110)
tk.Label(root, text='Solución', bg="#007582", fg='white', font=("arial", 12, "bold")).place(x=110, y=233)

tk.Entry(root, justify='center', bg="#00FFC8", font=("arial", 10, "bold"), width=15, borderwidth=9, textvariable=Numero_1).place(x=20, y=70)
tk.Entry(root, justify='center', bg="#00FFC8", font=("arial", 10, "bold"), width=15, borderwidth=9, textvariable=Numero_2).place(x=157, y=70)
tk.Entry(root, justify='center', bg="#00FFC8", font=("arial", 10, "bold"), width=34, borderwidth=9, textvariable=Resultado).place(x=20, y=265)

tk.Button(root, text='Sumar', bd=0, width=Ope_anc_bot, height=Ope_alt_bot, command=suma).place(x=20, y=140)
tk.Button(root, text='Restar', bd=0, width=Ope_anc_bot, height=Ope_alt_bot, command=resta).place(x=157, y=140)
tk.Button(root, text='Multiplicar', bd=0, width=Ope_anc_bot, height=Ope_alt_bot, command=multiplica).place(x=20, y=190)
tk.Button(root, text='Dividir', bd=0, width=Ope_anc_bot, height=Ope_alt_bot, command=divide).place(x=157, y=190)

tk.Label(root, textvariable=mensaje, bg="#007582", fg='white', font=('', 15)).place(x=50, y=310)

tk.Button(root, text='Salir', bd=0, width=36, height=2, command=root.destroy).place(x=20, y=350)

root.mainloop()

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