from tkinter import *

v = Tk()
v.title("Calculadora")
v.geometry("400x410")
v.resizable(False, False)
v.configure(background="#024C4C")

col_bot = "#F5F5F5"
anc_bot = 10
alt_bot = 3
oper = ""
tp = StringVar()

def clear():
    global oper
    oper = ""
    tp.set("0")

def click(b):
    global oper
    oper += str(b)
    tp.set(oper)

def resultado():
    global oper
    try:
        r = str(eval(oper))
    except:
        r = "ERROR"
    tp.set(r)

clear()
# fila uno
BUno = Button(v, text="1", bg=col_bot, width=anc_bot, height=alt_bot, command=lambda: click(1)).grid(row=1, column=0, pady=10)
BDos = Button(v, text="2", bg=col_bot, width=anc_bot, height=alt_bot, command=lambda: click(2)).grid(row=1, column=1, pady=10)
BTres = Button(v, text="3", bg=col_bot, width=anc_bot, height=alt_bot, command=lambda: click(3)).grid(row=1, column=2, pady=10)
BSum = Button(v, text="+", bg="#616161", width=anc_bot, fg='white', height=alt_bot, command=lambda: click("+")).grid(row=1, column=3, pady=10)
# fila dos
BCuat = Button(v, text="4", bg=col_bot, width=anc_bot, height=alt_bot, command=lambda: click(4)).grid(row=2, column=0, pady=10)
BCinco = Button(v, text="5", bg=col_bot, width=anc_bot, height=alt_bot, command=lambda: click(5)).grid(row=2, column=1, pady=10)
BSeis = Button(v, text="6", bg=col_bot, width=anc_bot, height=alt_bot, command=lambda: click(6)).grid(row=2, column=2, pady=10)
BRest = Button(v, text="-", bg="#616161", width=anc_bot, fg='white', height=alt_bot, command=lambda: click("-")).grid(row=2, column=3, pady=10)
# fila tres
BSiete = Button(v, text="7", bg=col_bot, width=anc_bot, height=alt_bot, command=lambda: click(7)).grid(row=3, column=0, pady=10)
BOcho = Button(v, text="8", bg=col_bot, width=anc_bot, height=alt_bot, command=lambda: click(8)).grid(row=3, column=1, pady=10)
BNueve = Button(v, text="9", bg=col_bot, width=anc_bot, height=alt_bot, command=lambda: click(9)).grid(row=3, column=2, pady=10)
BMult = Button(v, text="*", bg="#616161", width=anc_bot, fg='white', height=alt_bot, command=lambda: click("*")).grid(row=3, column=3, pady=10)
# fila cuatro
BC = Button(v, text="C", bg="#F44336", width=anc_bot, fg='white', height=alt_bot, command=clear).grid(row=4, column=0, pady=10)
BCero = Button(v, text="0", bg=col_bot, width=anc_bot, height=alt_bot, command=lambda: click("0")).grid(row=4, column=1, pady=10)
BIgu = Button(v, text="=", bg="#F44336", width=anc_bot, fg='white', height=alt_bot, command=resultado).grid(row=4, column=2, pady=10)
BDiv = Button(v, text="/", bg="#616161", width=anc_bot, fg='white', height=alt_bot, command=lambda: click("/")).grid(row=4, column=3, pady=10)

P = Entry(v, font=("arial", 20, "bold"), width=22, borderwidth=10, background="#D5DB08", textvariable=tp)
P.grid(row=0, column=0, columnspan=4, padx=25, pady=25)

v.mainloop()