import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Datos de muestra
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1.3, 3.5, 4.2, 5.0, 7.0, 8.8, 10.1, 12.5, 13.0, 15.6])

# Polinomio
p = np.poly1d([1.538, -0.36])

# Valores de x para el polinomio
x_p = np.linspace(1, 10, 100)
y_p = p(x_p)

# Crear la gráfica
plt.plot(x, y, 'bo', label='Datos')
plt.plot(x_p, y_p, 'r-', label='P(x) = 1.538x - 0.36')

# Personalizar la gráfica
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica con polinomio')
plt.legend()

# Guardar la gráfica en un archivo de imagen
plt.savefig('grafica.png')

# Mostrar la gráfica en Streamlit
st.image('grafica.png')