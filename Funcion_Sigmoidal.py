import matplotlib.pylab as plt
import numpy as np

e = 2.71
a = 1.4
b = 2
c = -1

def f(x):
    return a/(1+e**(-b*(x-c)))

x = np.linspace(-5, 5, 400)
print('''
~~~~~~~~~~~~~ Problema A ~~~~~~~~~~~~~''')
print (x)

def f(x2):
    return 1/(1+3.14**(-1*(x2-(-1))))

x2 = np.linspace(-3, 2, 200)
print('''
~~~~~~~~~~~~~ Problema B ~~~~~~~~~~~~~''')
print (x2)

def f(x3):
    return 2/(1+3**(-1*(x3-(-2))))

x3 = np.linspace(-2, 1, 50)
print('''
~~~~~~~~~~~~~ Problema C ~~~~~~~~~~~~~''')
print (x3)

plt.plot(x, f(x), label='Probelma A', linewidth=2, color='blue')
plt.plot(x2, f(x2), label='Probelma B', linewidth=2, color='orange')
plt.plot(x3, f(x3), label='Probelma C', linewidth=2, color='purple')
plt.title('Función Sigmoidal')
plt.xlabel('Eje de las Abscisas')
plt.ylabel('Eje de las Ordenadas')
plt.legend()
plt.grid()
plt.show()