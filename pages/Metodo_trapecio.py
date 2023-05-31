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
    st.markdown(r"$\int_a^b f(x)dx = \frac{h}{2} (f_0 +f_n + 2 \sum_{i=1}^{n-1} f_i)$")
    st.markdown("A la generalizacion de la formula de Newton-Cotes para $n$ subintervalos se le llama *regla del trapecio compuesta* o simplemente *regla del trapecio*. Es obvio que el metodo esta sujeto a errores dependiendo del tamaño del intervalo y de las caracteristicas propias de la funcion.")
    st.markdown("Esta regla puede aplicarse a una funcion que solo se conoce por una tabla de valores o a una funcion conocida, en cuyo caso debera decidirse el valor apropiado de $h$ para obtener una buena aproximacion.")

with tab2:
    st.title(":blue[Regla del Trapecio]")
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
    st.markdown(r"$\int_{1.4}^{3.8} f(x)dx = \frac{0.2}{2}(4.055 +2(4.953) + 2(6.050) + 2(7.389) + 2(9.025) + 2(11.023) + 2(13.464) + 2(16.445) + 2(20.086) + 2(24.533) + 2(29.964) + 2(36.598) + 44.701) = 40.7816$")
    st.markdown("Los datos de la tabla corresponden a $f(x) = e^x$ asi que el valor exacto de la integral es:")
    st.markdown(r"$e^{3.8} - e^{1.4} = 40.6460$")
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
    st.title(":blue[Regla del Trapecio]")
    st.header("Aplicacion")
    def hermite_interpolation(x, f_x, f_prime_x, x_interp):
        n = len(x)
        m = 2 * n
        
        Q = np.zeros((m, m))
        b = np.zeros(m)
        
        for i in range(n):
            Q[2 * i][0] = x[i]
            Q[2 * i + 1][0] = x[i]
            Q[2 * i + 1][1] = f_prime_x[i]
            
            b[2 * i] = f_x[i]
            b[2 * i + 1] = f_x[i]
        
        for i in range(2, m):
            for j in range(1, i):
                Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (Q[i][0] - Q[i-j][0])
        
        interpolated_values = []
        
        for interp_point in x_interp:
            p = Q[0][0]
            product = 1
            
            for i in range(1, m):
                product *= (interp_point - Q[i-1][0])
                p += Q[i][i] * product
            
            interpolated_values.append(p)
        
        return interpolated_values


    def main():
        st.title("Método de Hermite")
        
        st.header("Ingresar Datos")
        n = st.number_input("Número de puntos:", min_value=2, step=1, value=3)
        
        x_values = []
        f_x_values = []
        f_prime_x_values = []
        
        for i in range(n):
            st.subheader(f"Punto {i+1}")
            x = st.number_input("Valor de x:")
            f_x = st.number_input("Valor de f(x):")
            f_prime_x = st.number_input("Valor de f'(x):")
            
            x_values.append(x)
            f_x_values.append(f_x)
            f_prime_x_values.append(f_prime_x)
        
        st.header("Interpolación")
        x_interp = st.text_input("Valores de x a interpolar (separados por comas):")
        x_interp = [float(x.strip()) for x in x_interp.split(",") if x.strip()]
        
        if st.button("Interpolar"):
            interpolated_values = hermite_interpolation(x_values, f_x_values, f_prime_x_values, x_interp)
            
            st.subheader("Resultados:")
            for i, interp_point in enumerate(x_interp):
                st.write(f"Para x = {interp_point}, el valor interpolado es {interpolated_values[i]}")
        

    if __name__ == "__main__":
        main()