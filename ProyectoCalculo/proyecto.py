import numpy as np
import matplotlib.pyplot as plt

# Definimos la función
def f(x, y):
    return 1/(x**2 + y**2)

# Creamos una malla de puntos en el plano (x, y)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Evaluamos la función en los puntos de la malla
Z = f(X, Y)

# Graficamos las curvas de nivel
plt.contour(X, Y, Z)
plt.show()
