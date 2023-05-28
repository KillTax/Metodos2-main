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
    st.subheader("Defincion 2")
    st.markdown("Sean $x_0, x_1, x_2, ..., x_n, n+1$ numeros distintos en $[a,b]$ y $m_i$ un entero no-negativo asociado a $x_i$ para $i = 0, 1, ..., n$. Supongase que $f \in C^m[a, b]$ y que $m = max_{0 \leq i \leq n} m_i$. El plinomio osculante que aproxima a $f(x)$ es el polinomio $P(x)$ de menor grado tal que")
    st.markdown("$\frac{d^k P(x_i)}{dx^k} = \frac{d^k f(x_i)}{dx^k}$     Para $i = 0, 1, ..., n$ y $k = 0, 1, 2, ..., m$.")
    st.markdown("Notese que se cuando $n = 0$ el polinomio osculante que aproxima a $f(x)$ es el polinomio de Taylor de grado $m_0$ para $f(x)$ en $x_0$. Cuando $m_i = 1$ para cada $i = 0, 1, ..., n$ da una clase de polinomios llamados polinomios de Hermite. Para una funcion dada $f$, estos polinomios no solo coinciden con $f$ en $x_0, x_1, x_2, ..., x_n$, sino que, como sus primeras derivadas coinciden tambien con las de $f$, tienen la misma apariencia que la funcion en $(x_i, f(x_i))$ en el sentido que las lineas tangentes al polinomio y a la funcion coinciden.")
    st.subheader("Teorema 1")
    st.markdown("Si $f \in C^1[a, b]$ y $x_0, x_1, x_2, ..., x_n \in [a,b]$ son distintos, el unico polinomio de menor grado que coincide con $f$ y $f'$ en $x_0, x_1, x_2, ..., x_n$ es un polinomio de grado a lo mas $2n + 1$ dado por")
    st.markdown("$H_{2n+1}(x) = \sum_{i=0}^n f(x_j)H_{n,j}(x) + \sum_{i=0}^n f'(x_j)\widehat(H_{n,j})(x)$")
    st.markdown("Donde:")
    st.markdown("$H_{n,j}(x) = [1-2(x-x_j)L'_{n,j}(x_j)]L_{n,j}^2 (x)$")
    st.markdown("$\widehat(H_{n,j})(x) = (x-x_j)L_{n,j}^2 (x)$")
    st.markdown("En este contexto, $L_{n,j}$ denota al j-esimo coeficiente polinomial de Lagrange de grado $n$, definido en la ecuacion")
    st.markdown("$L_{n,j} (x) = $\prod_{i=1}_{i \neq j}^n \fraq{x-x_i}{x_j - x_i}$ para cada $j = 0, 1, ..., n$")
    st.markdown("Ademas, si $f \in C^{(2n+2)}[a, b]$, entonces")
    st.markdown("$f(x)-H_{2n+1}(x) = \fraq{(x-x_0)^2 ... (x-x_n)^2}{(2n+2)!}f^{(2n+2)}(\xi)$")