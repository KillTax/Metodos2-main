import streamlit as st
import pandas as pd
import numpy as np


tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplo","Aplicacion"])
with tab1:
    st.title(":blue[Regla de Simpson 1/3]")
    st.header("Definicion")
    st.markdown("Las siguientes formulas compuestas de Newton-Cotes, basadas en polinomios de interpolacion de $2^o$ y $3^{er}$ grado, son conocidas como las reglas de simpson. La primera, basada en uno cuadratico, es conocida como la regla de Simpson 1/3, y la que esta basada en un polinoio cubico se conoce como la regla de Simpson 3/8, estos nombres se deben a los coeficientes de las formulas.")
    st.markdown("La formula de $2^o$ grado de Newton-Cotes integra un polinomio cuadratico sobre dos intervalos del mismo ancho, a continuacion se construira la regla compuesta de la ecuacion")
    st.markdown(r"$\int_{x_0}^{x_1}f(x)dx = \frac{h}{3}[f_0+4f_1+2f_2]$")
    st.markdown("La formula compuesta que se aplica a una subdivision del intervalo de integracion en $n$ subintervalos (con $n$ par) es:")
    st.markdown(r"$\int_a^bf(x)dx = \frac{h}{3}[f_0+4f_1+2f_2+4f_3+2f_4+...+2f_{n-2}+4f_{n-1}+f_n]$")
    st.markdown("Esta formula se reconoce como la regla de Simpson 1/3")
    st.markdown("Cuyo termino del error global esta dado por")
    st.markdown(r"$E_{global} = -\frac{h^5}{90}\frac{(b-a)}{2h}f^{iv}(\xi) = -\frac{(b-a)}{180}h^4f^{iv}(\xi)$")
    st.markdown("Como puede verse el orden del error global cambia a $O(h^4)$. El denominador en el termino del error cambia a 180 porque se esta integrando sobre un numero de subintervalos par (significa que la regla global se aplica $h/2$ veces). El hecho que el error es $O(h^4)$, es de especial importancia")

with tab2:
    st.title(":blue[Regla de Simpson 1/3]")
    st.header("Ejemplo")
    st.markdown("Supongase que se desea integrar la funcion tabulada a continuacion sobre el intervalo (1.4, 3.8).")
    st.markdown(r"""
    | $x$ | $f(x)$ |
    |-----|--------|
    | 1.4 |  4.055 |
    | 1.6 |  4.953 |
    | 1.8 |  6.050 |
    | 2.0 |  7.389 |
    | 2.2 |  9.025 |
    | 2.4 | 11.023 |
    | 2.6 | 13.464 |
    | 2.8 | 16.445 |
    | 3.0 | 20.086 |
    | 3.2 | 24.533 |
    | 3.4 | 29.964 |
    | 3.6 | 36.598 |
    | 3.8 | 44.701 |
    """)
    st.markdown("Entonces empleando la regla del trapecio compuesta:")
    st.markdown(r"$\int_1.4^3.8 f(x)dx = \frac{0.2}{2}(4.055 +2(4.953) + 2(6.050) + 2(7.389) + 2(9.025) + 2(11.023) + 2(13.464) + 2(16.445) + 2(20.086) + 2(24.533) + 2(29.964) + 2(36.598) + 44.701) = 40.7816$")
    st.markdown("Los datos de la tabla corresponden a $f(x) = e^x$ asi que el valor exacto de la integral es:")
    st.markdown(r"$e^3.8 - e^1.4 = 40.6460$")
    st.markdown("Con Newton-Cotes se vio que el error de la regla del trapecio es ")
    st.markdown(r"*error* $= -\frac{1}{12}h^3f''(\xi)$")
    st.markdown("Vale enfatizar que este error es el error en un solo paso, por eso se llama error local. Dado que, generalmente, esta regla se aplica a una serie de subintervalos para obtener la integral de $x = a$ a $x = b$, el interes radica en el error global.")
    st.markdown("El desarrollo de la formula para el error global de la regla del trapecio consiste en la suma de los errores locales:")
    st.markdown(r"$E_{global} = -\frac{1}{12}h^3(f''(\xi_1)+f''(\xi_2)+...+f''(\xi_n))$")
    st.markdown(r"Cada uno de los valores $\xi_i$ se encuentra en los $n$ subintervalos sucesivos.")
    st.markdown("El hecho de que el error global sea $O(h^2)$ es razonable.")
    st.markdown("Cuando la funcion $f(x)$ es conocida, esta ultima expresion permite estimar el error de la integracion numerica por la regla del trapecio. Aplicando esta ecuacion, el valor se encierra al calcular los valores maximos y minimos de $f'(x)$ en el intervalo $[a,b]$.")
    st.markdown("La expresion del error esta dada por:")
    st.markdown(r"*error* $= -\frac{1}{12}h^3nf''(\xi) 1.4 \leq \xi \leq 3.8$")
    st.markdown(r"""*error* $$= -\frac{1}{12}(0.2)^2(3.4-1.8) \left\{\begin{array}{l}e^{1.4}\\e^{3.8}\end{array}\right\} = \left\{\begin{array}{l}-0.0324 (\min)\\-0.3573 (\max)\end{array}\right\}$$""")
    st.markdown("En el ejemplo el error fue: $-0.1356$, como puede observarse, queda dentro de la cota obtenida.")
with tab3:
    st.title(":blue[Regla de Simpson 1/3]")
    st.header("Aplicacion")
    