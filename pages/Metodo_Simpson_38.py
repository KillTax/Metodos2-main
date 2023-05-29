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
    st.markdown("Aplicar la regla de Simpson 1/3 a los datos de la siguiente tabla:")
    st.markdown(r"""
    | $i$ |   $x$  |  $f(x)$ |
    |-----|--------|---------|
    |  0  |   0.7  | 0.64835 |
    |  1  |   0.9  | 0.91360 |
    |  2  |   1.1  | 1.16092 |
    |  3  |   1.3  | 1.36178 |
    |  4  |   1.5  | 1.48500 |
    |  5  |   1.7  | 1.55007 |
    |  6  |   1.9  | 1.52882 |
    |  7  |   2.1  | 1.44513 |
    """)
    st.markdown("Dado que el numero de subintervalos es siete y no se ajusta a la regla de Simpson 1/3, existen dos posibilidades: el primero o el ultimo subintervalo se integran usando la regla del trapecio y el resto con la regla de Simpson 1/3")
    st.markdown("Primera opcion, iniciando con la regla de Simpson 1/3:")
    st.markdown(r"$\int_{0.7}^{1.9} f(x)dx \cong \frac{0.2}{3}(0.64835 +4(0.91360) + 2(1.16092) + 4(1.36178) + 2(1.48500) + 4(1.55007) + 1.52882 = 1.5193873$")
    st.markdown("Regla del trapecio:")
    st.markdown(r"$\int_{1.9}^{2.1} f(x)dx = \frac{0.2}{2}(1.52882 + 1.44513) = 0.297395$")
    st.markdown("Total:")
    st.markdown(r"$\int_{0.7}^{2.1} f(x)dx \cong 1.5193873 + 0.29739 = 1.8167823")
    st.markdown("Segunda opcion, primer intervalo por la regla del trapecio:")
    st.markdown(r"$\int_{0.7}^{0.9} f(x)dx \cong \frac{0.2}{2}(0.64835 + 0.91360) = 0.156195$")
    st.markdown("Regla de Simpson 1/3")
    st.markdown(r"$\int_{0.9}^{2.1} f(x)dx \cong \frac{0.2}{3}(0.91360 +4(1.16092) + 2(1.36178) + 4(1.48500) + 2(1.55007) + 4(1.52882) + 1.44513 = 1.661426$")
    st.markdown("Total:")
    st.markdown(r"$\int_{0.7}^{2.1} f(x)dx \cong 0.156195 + 1.661426 = 1.817621$")
    st.markdown("Normalmente no se sabe en que extremo aplicar la regla del Trapecio, por lo que graficar los puntos e identificar la forma general de la curva puede ser util.")
with tab3:
    st.title(":blue[Regla de Simpson 3/8]")
    st.header("Aplicacion")