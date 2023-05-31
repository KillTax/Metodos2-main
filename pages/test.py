## Gráfica de ejemplo
import streamlit as st
import matplotlib.pyplot as plt

# Datos de muestra
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1.3, 3.5, 4.2, 5.0, 7.0, 8.8, 10.1, 12.5, 13.0, 15.6]

# Crear la gráfica
plt.plot(x, y, 'b.-')

# Personalizar la gráfica
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de ejemplo')

# Mostrar la gráfica en Streamlit
st.pyplot(plt)
