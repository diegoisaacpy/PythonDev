import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.sqrt(x**2 + y**2)

def Funcion(f, c):
    # Generar valores de x y y
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)

    # Evaluar la función en cada punto de la malla
    Z = f(X, Y)

    # Crear una gráfica de contorno con una sola curva de nivel en c
    fig, ax = plt.subplots()
    ax.contour(X, Y, Z, levels=[c])

    # Etiquetar los ejes y agregar un título
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Conjunto de nivel de f(x,y) = ' + str(c))

    # Mostrar la gráfica
    plt.show()

# Generar el conjunto de nivel de f(x,y) = sqrt(x^2 + y^2) para c = 3
Funcion(f, 3)

