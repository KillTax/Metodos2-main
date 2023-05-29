import streamlit as st
import pandas as pd
import numpy as np


tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplo","Aplicacion"])
with tab1:
    st.title(":blue[Regla del Trapecio]")
    st.header("Definicion")
    st.markdown("La primera de las formulas de Newton-Cotes esta basada en aproximar $f(x)$ en el intervalo $(x_0,x_1)$ mediante una linea recta, de ahi el nombre de *regla del trapecio*, la cual fue obtenida mediante la integracion de $P_1(x)$; sin embargo, tambien puede considerarse una adaptacion de la definicion de la integral definida como una suma al estimar $\int_a^b f(x)dx$ subdividiendo el intervalo de $a$ a $b$ en $n$ subintervalos. El area bajo la curva en cada subintervalo es aproximada por el trapecio formado por sustituir la curva por su secante. Entonces, la integral es aproximada por la suma de todas las areas trapezoidales. Si se conociera el limite de esta suma cuando el ancho del intervalo tiende a cero, se tendria el valor exacto de la integral, pero en la integracion numerica el numero de intervalos es finito.")
    st.markdown("Para un intervalo $[a,b]$ subdividido en $n$ subintervalos de tamaño $h$, la formula se generaliza de la siguiente forma:")
    st.markdown(r"$\int_a^b f(x)dx = \sum_{i=0}^n \frac{h}{2}(f_i+f_{i+1}) = \frac{h}{2}(f_0 +2f_1 +2f_2 + ... +2f_{n-1} +f_n) =$")
    st.markdown(r"$\int_a^b f(x)dx = \frac{h}{2} (f_0 +f_n + 2 \sum_{i=1}^{n-1} f_i$")
    st.markdown("A la generalizacion de la formula de Newton-Cotes para $n$ subintervalos se le llama *regla del trapecio compuesta* o simplemente *regla del trapecio*. Es obvio que el metodo esta sujeto a errores dependiendo del tamaño del intervalo y de las caracteristicas propias de la funcion.")
    st.markdown("Esta regla puede aplicarse a una funcion que solo se conoce por una tabla de valores o a una funcion conocida, en cuyo caso debera decidirse el valor apropiado de $h$ para obtener una buena aproximacion.")

with tab2:
    st.title(":blue[Regla del Trapecio]")
    st.header("Ejemplo")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
with tab3:
    st.title(":blue[Metodo de Hermite]")
    st.header("Aplicacion")
    