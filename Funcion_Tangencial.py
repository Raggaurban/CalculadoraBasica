import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1/2*(np.tan(x+3.14/4))

x = np.linspace(-2, 4, 150)
print('''
~~~~~~~~~~~~~ Problema A ~~~~~~~~~~~~~''')
print(x)

def f(x2):
    return 30*(np.tan(x2+20))

x2 = np.linspace(-3, 3, 200)
print('''
~~~~~~~~~~~~~ Problema B ~~~~~~~~~~~~~''')
print(x2)

def f(x3):
    return 90*(np.tan(x3+80))

x3 = np.linspace(-6, 8, 50)
print('''
~~~~~~~~~~~~~ Problema C ~~~~~~~~~~~~~''')
print(x3)

plt.plot(x, f(x), label='Problema A', linewidth=2, color='red')
plt.plot(x2, f(x2), label='Probelma B', linewidth=2, color='blue')
plt.plot(x3, f(x3), label='Probelma C', linewidth=2, color='green')
plt.title('Función Tangencial')
plt.xlabel('Eje de las Abscisas')
plt.ylabel('Eje de las Ordenadas')
plt.legend()
plt.grid()
plt.show()
