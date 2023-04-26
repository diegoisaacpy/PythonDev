import matplotlib.pyplot as plt

# Especificar el punto de origen y las componentes x e y de los vectores
x, y = 3, 5
u1, v1 = 1, 2
u2, v2 = 2, 3
u3, v3 = 3, 4

# Graficar los vectores
fig, ax = plt.subplots()
ax.quiver(x, y, u1, v1, angles='xy', scale_units='xy', scale=1, color='blue')
ax.quiver(x, y, u2, v2, angles='xy', scale_units='xy', scale=1, color='green')
ax.quiver(x,y, u3, v3, angles='xy', scale_units='xy',scale=1, color='red')

# Configurar los límites de los ejes
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

# Mostrar la gráfica
plt.show()
