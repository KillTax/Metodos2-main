import streamlit as st
import pandas as pd
import numpy as np


tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplo","Aplicacion"])
with tab1:
    st.title(":blue[Regla de Simpson 3/8]")
    st.header("Definicion")
    st.markdown("La siguiente formula de Newton-Cotes, basada en un polinomio de cuatro puntos o cubico")
    st.markdown(r"$\int_{x_0}^{x_3}f(x)dx \approx \frac{3}{8}h[f_0+3f_1+3f_2+f_3]-\frac{3}{80}h^5f^{iv}(\xi)$")
    st.markdown("Tambien debe de generalizarse para aplicarse a un conjunto de $n$ subintervalos, donde $n$ debe de ser multiplo de tres. La regla resultante se conoce como *Regla de Simpson 3/8*:")
    st.markdown(r"$\int_a^bf(x)dx \approx \frac{3}{8}[f_0+3f_1+3f_2+2f_3+3f_4+...+2f_{n-3}+3f_{n-2}+3f_{n-1}+f_n]$")
    st.markdown("Con un termino del error:")
    st.markdown(r"$E_{global} = -\frac{3h^5}{180}\frac{(b-a)}{3h}f^{iv}(\xi) = -\frac{(b-a)}{180}h^4f^{iv}(\xi)$")
    st.markdown("Se aplica igual que la regla de Simpson 1/3. Si la funcion es conocida se divide el intervalo de integracion en $n$ paneles, donde $n$ debe ser divisible entre tres.")

with tab2:
    st.title(":blue[Regla de Simpson 3/8]")
    st.header("Ejemplo")
    st.markdown(r"Continuando con la funcion empleada en la Regla del Trapecio y Regla de Simpson 1/3, aplicar la regla de Simpson 3/8 a $f(x) = e^{-x^2}$ para integrar de $x = 0.2$ a $x = 1.5$. Comparar el resultado con 3, 6, 9, 12 paneles.")
    st.markdown("Para ejemplificar el proceso se presentan las tablas y calculos de las 2 primeras aproximaciones")
    st.markdown(r"""
    |       h =  0.43333     |
    |------------------------|
    | $n$ |   $x$  |  $f(x)$ |
    |-----|--------|---------|
    |  0  |   0.2  | 0.96079 |
    |  1  | 0.63333| 0.66958 |
    |  2  | 1.16666| 0.32053 |
    |  3  |   1.5  | 0.10540 |
    |     |        |         |
    |     |        |         |
    |     |        |         |
    """)
    st.markdown(r"""
    |      h =  0.216667     |
    |------------------------|
    | $i$ |   $x$  |  $f(x)$ |
    |-----|--------|---------|
    |  0  |   0.2  | 0.96079 |
    |  1  | 0.41667| 0.91360 |
    |  2  | 0.63333| 0.66958 |
    |  3  |  0.85  | 0.48554 |
    |  4  | 1.16666| 0.32053 |
    |  5  | 1.28333| 0.19264 |
    |  6  |   1.5  | 0.10540 |
    """)
    st.markdown(r"$\int_{0.2}^{1.5} e^{-x^2}dx \cong \frac{3}{8}(0.43333)(0.96079 +3(0.66958) + 3(0.32053) + 0.10540) = 0.65593$")
    st.markdown(r"$\int_{0.2}^{1.5} e^{-x^2}dx \cong \frac{3}{8}(0.216667)(0.96079 +3(0.91360) + 3(0.66958) + 2(0.48554) + 3(0.32053) + 3(0.19264) + 0.10540) = 0.65872$")
    st.markdown("Los resultados para las aproximaciones restantes se concentran en la siguiente tabla")
    st.markdown(r"""
    | $n$ |   $h$  | Integral|
    |-----|--------|---------|
    |  3  | 0.43333| 0.65593 |
    |  6  | 0.21667| 0.65872 |
    |  9  | 0.14444| 0.65881 |
    | 12  | 0.10833| 0.65882 |
    """)
    st.markdown("Esta regla es menos eficiente que Simpson 1/3. Sin embargo, se emplea cuando se tiene una tabla de valores con $n$ multiplo de tres. Si se combinan las dos reglas, de Simpson 1/3 y Simpson 3/8, las aproximaciones obtenidas seran mucho mejores que las obtenidas con la regla del trapecio")
with tab3:
    st.title(":blue[Regla de Simpson 3/8]")
    st.header("Aplicacion")