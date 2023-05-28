import streamlit as st
import pandas as pd
import numpy as np

tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplos","Aplicaciones"])
with tab1:
    st.title(":blue[Metodo de Hermite]")
    st.header("Teorema")
    st.markdown("Un polinomio se puede ajustar no solo a los valores de la función sino también a las derivadas en los puntos. Los polinomios ajustados a los valores de la función y de su derivada se llaman *polinomios de interpolación de Hermite* o *polinomios osculantes*.")
    st.markdown("El conjunto de los polinomios osculantes es una generalización de los polinomios de Taylor y los polinomios de Lagrange. Estos polinomios tienen la propiedad de que dados $n + 1$ números distintos $x_0, x_1, x_2, ..., x_n$ y los enteros no negativos $m_0, m_1, m_2, ..., m_n$, el polinomio osculante que aproxima a una función $f \in C^m[a, b]$, donde $m = max(m_0, m_1, m_2, ..., m_n)$ y $x_i \in [a, b]$ para cada $i = 0, 1, ..., n$, es el polinomio de menor grado con la propiedad de que coincide con la función f y todas sus derivadas de orden menor o igual a $m_i$ en $x_i$ para cada $i = 0, 1, ..., n$. El grado de este polinomio osculante será a lo más")
    st.latex(r"""\[
    \sum_{i=}^{n}m_{i}+n
    \]""")
    """
    
    Mientras que por otro lado, la tasa de aprendizaje del descenso del gradiente se representa como $alpha$
    """
    st.latex(r"""\alpha""")
    """La tasa de aprendizaje es el tamaño del paso dado por cada gradiente. Si bien una tasa de aprendizaje grande puede darnos valores mal optimizados para
    """
    st.latex(r"""\beta y \theta""") 
    """, la tasa de aprendizaje también puede ser demasiado pequeña, lo que requiere un incremento sustancial en el número de iteraciones necesarias para obtener el punto de convergencia (el punto de valor óptimo para beta y theta) . Este algoritmo nos da el valor de alpha , beta y theta como salida.
    . Para implementar un algoritmo de descenso de gradiente necesitamos seguir 4 pasos:
    
    +Inicializar aleatoriamente el sesgo y el peso theta
    +Calcular el valor predicho de y que es Y dado el sesgo y el peso
    +Calcular la función de costo a partir de los valores pronosticados y reales de Y
    +Calcular pendiente y los pesos.
    
    Se inicia tomando un valor aleatorio para el sesgo y las ponderaciones, que en realidad podría estar cerca del sesgo y las ponderaciones óptimos o puede estar lejos.
    """
  