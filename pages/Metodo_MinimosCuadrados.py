import streamlit as st
import pandas as pd
import numpy as np


tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplo","Aplicacion"])
with tab1:
    st.title(":blue[Metodo de Minimos Cuadrados]")
    st.header("Definicion")
    st.markdown("El estudio de la teoría de la aproximación comprende dos tipos generales de problemas. Uno se presenta cuando una función se da de manera explícita, pero se desea encontrar un tipo más simple de ella, un polinomio, por ejemplo, que sirva para determinar los valores aproximados de una función dada. El otro tipo se refiere a la adaptación de una función otpima a ciertos datos que se pueda emplear para representarlos. El primer tipo de problema puede abordarse empleando cualquiera de las alternativas presentadas en la sección de Interpolación polinomial o por splines cúbi- cos; en esta sección se tratará el segundo caso, que en general consiste en la aplicación de técnicas numéricas a la ciencia y a la ingeniería para ajustar una curva a datos experimentales, de los que, por supuesto, no se conoce la función.")
    st.markdown("Al tratarse de datos experimentales es logico suponer que tienen algun factor de error, por lo qu la funcion de ajuste no necesariamente pasa por los puntos, pero si deberia minimizar los errores,tambien llamados desviaciones o residuos.")
    st.markdown("Sean los valores $(x_i,y_i)$ para $i = 1, 2, ..., m$, los puntos que se desean ajustar por una curva. En este caso un polinomio de grado $n, P_n(x) = a_0 + a_1x + a_2x + ... + a_nx^n$. Entonces los errores a minimizar estan dados por")
    st.markdown(r"$e_i = P_n(x_i)-y_i para i = 1, 2, ..., m$")
    st.markdown("Para minimizar $e_i$ se emplea el concepto de norma vectorial, las mas comunes son las que se analizan a continuacion")

    st.subtitle("Error maximo o norma espectral")
    st.markdown("La norma espectral consiste en hacer minima la magnitud del error maximo. Sea $P_n(x_i)$ el i-esimo valor de la recta de aproximacion y $y_i$ el i-esimo valor dado para $y$. El problema de determinar la ecuacion de la mejor aproximacion polinomial, en el sentido absoluto, consiste en encontrar los valores de los coeficientes $a_0, a_1, ..., a_n$ que minimicen")
    st.markdown(r"E_{\infty}(a_0, a_1, ..., a_n) = \max_{1 \leq i \leq m} \mid y_i-P_n(x_i) \mid")