import streamlit as st
import pandas as pd
import numpy as np

tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplos","Aplicaciones"])
with tab1:
    st.title(":blue[Metodo de Hermite]")
    st.header("Definicion")
    st.markdown("Un polinomio se puede ajustar no solo a los valores de la función sino también a las derivadas en los puntos. Los polinomios ajustados a los valores de la función y de su derivada se llaman *polinomios de interpolación de Hermite* o *polinomios osculantes*.")
    st.markdown("El conjunto de los polinomios osculantes es una generalización de los polinomios de Taylor y los polinomios de Lagrange. Estos polinomios tienen la propiedad de que dados $n + 1$ números distintos $x_0, x_1, x_2, ..., x_n$ y los enteros no negativos $m_0, m_1, m_2, ..., m_n$, el polinomio osculante que aproxima a una función $f \in C^m[a, b]$, donde $m = max(m_0, m_1, m_2, ..., m_n)$ y $x_i \in [a, b]$ para cada $i = 0, 1, ..., n$, es el polinomio de menor grado con la propiedad de que coincide con la función f y todas sus derivadas de orden menor o igual a $m_i$ en $x_i$ para cada $i = 0, 1, ..., n$. El grado de este polinomio osculante será a lo más")
    st.markdown(r"M = $$\sum_{i=0}^n m_i + n$$")
    st.markdown("Ya que el numero de condiciones que se tiene que satisfacer es $$\sum_{i=0}^n m_i + (n + 1)$$ y un polinomio de grado $M$ tiene $M + 1$ coeficientes que pueden usarse para satisfacer estas condiciones.")
    st.subheader("Defincion")
    st.markdown("Sean $x_0, x_1, x_2, ..., x_n, n+1$ numeros distintos en $[a,b]$ y $m_i$ un entero no-negativo asociado a $x_i$ para $i = 0, 1, ..., n$. Supongase que $f \in C^m[a, b]$ y que $m = max_{0 \leq i \leq n} m_i$. El plinomio osculante que aproxima a $f(x)$ es el polinomio $P(x)$ de menor grado tal que")
    st.markdown(r"$\frac{d^k P(x_i)}{dx^k} = \frac{d^k f(x_i)}{dx^k}$     Para $i = 0, 1, ..., n$ y $k = 0, 1, 2, ..., m$.")
    st.subheader("Teorema")