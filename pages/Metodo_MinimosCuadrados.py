import streamlit as st
import matplotlib.pyplot as plt
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
    st.markdown("Para minimizar $e_i$ se emplea el concepto de norma vectorial, las mas comunes son las que se analizan a continuacion.")

    st.subheader("Error maximo o norma espectral")
    st.markdown("La norma espectral consiste en hacer minima la magnitud del error maximo. Sea $P_n(x_i)$ el i-esimo valor de la recta de aproximacion y $y_i$ el i-esimo valor dado para $y$. El problema de determinar la ecuacion de la mejor aproximacion polinomial, en el sentido absoluto, consiste en encontrar los valores de los coeficientes $a_0, a_1, ..., a_n$ que minimicen")
    st.markdown(r"$E_{\infty}(a_0, a_1, ..., a_n) = \max_{1 \leq i \leq m} \mid y_i-P_n(x_i) \mid$")
    st.markdown("Este problema se conoce como *minimax* y su solucion no es tan simple, ya que la funcion de valor absoluto no tiene derivada en el origen y da una importancia indebida a un simple error grande.")

    st.subheader("Error medio o desviacion absoluta")
    st.markdown("Esta otra alternativa implica hallar los valores de $a_0, a_1, ..., a_n$ que minimicen")
    st.markdown(r"$E_1(a_0, a_1, ..., a_n) = \sum_{i=1}^m \mid y_1-P_n(x_i) \mid$")
    st.markdown("Esta cantidad se llama *desviacion absoluta*. Para minimizar una funcion de varias variables se deben igualar a cero sus derivadas parciales y resolver en forma simultanea las ecuaciones restantes.")
    st.markdown(r"$\frac{\partial E_1}{\partial a_i} = 0$ para $i = 1, 2, ..., n$")
    st.markdown("La dificultad de este procedimiento radica en que el valor absoluto no es derivable en cero, y no necesariamente se puede obtener la solucion de este sistema de ecuaciones. Por otro lado, este criterio solo promedia el error en varios puntos sin dar suficiente valor relativo a un punto que esta muy alejado de la aproximacion.")

    st.subheader("Error cuadratico")
    st.markdown("Esta tercera opcion, conocida como minimos cuadrados, requiere determinar el mejor polinomio de aproximacion cuando el error es la suma de los cuadrados de las diferencias entre los valores de $y_i$ y los valores de $P_n(x_i)$. Por lo tanto, hay que encontrar las constantes $a_0, a_1, ..., a_n$ que reduzcan al minimo la suma de los errores al cuadrado")
    st.markdown(r"$E_2(a_0, a_1, ..., a_n) = \sum_{i=1}^m (y_1-P_n(x_i))^2$")
    st.markdown("Este criterio proporciona un resultado unico para un conjunto de datos, ademas coincide con el principio de *maxima probabilidad* estadistica. Si los errores de medicion poseen una distribucion normal y si la desviacion estandar es constante para todos los datos, entonces puede demostrarse que la recta determinada al minimizar la suma de los cuadrados tiene valores de pendiente y ordenada con maxima probabilidad de ocurrencia(Curtis y Wheatley, 2000).")
    st.markdown("El metodo de minimos cuadrados, en comparacion con los dos criterios anteriores, concede mayor valor relativo al punto que esta alejado del resto de los datos, pero no permite que ese punto domine la aproximacion.")

    st.subheader("Regresion lineal")
    st.markdown("Cuando un polinomio de ajuste es de grado uno, es decir, es una linea recta, el ajuste se conoce como regresion lineal y la recta de ajuste optimo se conoce como *recta de regresion*, esta recta esta dada por")
    st.markdown(r"$P(x) = a_1x + a_0$")
    st.markdown("El problema de ajustar la mejor recta con minimos cuadrados a una coleccion de datos $[(x_i,y_i)] \}_{i=1}^m$ implica minimizar el error dado por la ecuacion donde el polinomio es lineal:")
    st.markdown(r"$E_2(a_0, a_1) = \sum_{i=1}^m (y_1-a_0-a_1x_i)^2$")
    st.markdown("Con respecto a los parametros $a_0$ y $a_1$. Para que haya un minimo, se calculan las derivadas parciales y se igualan a cero")
    st.markdown(r"$\frac{\partial}{\partial a_0}\sum_{i=1}^m(y_1-a_0-a_1x_i)^2=2 \sum_{i=1}^m(y_1-a_0-a_1x_i)^2(-1) = 0$")
    st.markdown(r"$\frac{\partial}{\partial a_1}\sum_{i=1}^m(y_1-a_0-a_1x_i)^2=2 \sum_{i=1}^m(y_1-a_0-a_1x_i)^2(-x_i) = 0$")
    st.markdown("Estas ecuaciones se simplifican en lo que se conoce como ecuaciones normales:")
    st.markdown(r"$a_0m + a_1 \sum_{i=1}^m x_i = \sum_{i=1}^m y_i$")
    st.markdown(r"$a_0 \sum_{i=1}^m x_i + a_1 \sum_{i=1}^m x_i^2 = \sum_{i=1}^m x_iy_i$")
    st.markdown("La solucion de este sistema de ecuaciones es:")
    st.markdown(r"$a_0 = \frac{\sum x_i^2 \sum y_i - \sum x_iy_i \sum x_i}{m \sum x_i^2 - (\sum x_i)^2}$, $a_1 = \frac{m \sum x_iy_i - \sum x_i \sum y_i}{m \sum x_i^2 - (\sum x_i)^2}$")
    st.markdown("Todas las sumas son para $i = 1, ..., m$")

with tab2:
    st.title(":blue[Metodo de Minimos Cuadrados]")
    st.header("Ejemplo")
    st.markdown("Supongase que se desea ajustar una curva al siguiente conjunto de datos, los cuales al graficarlos sugieren una relacion lineal.")
    st.markdown("""
    | $x_i$ | $y_i$ |
    |-------|-------|
    |   1   |  1.3  |
    |   2   |  3.5  |
    |   3   |  4.2  |
    |   4   |  5.0  |
    |   5   |  7.0  |
    |   6   |  8.8  |
    |   7   | 10.1  |
    |   8   | 12.5  |
    |   9   | 13.0  |
    |  10   | 15.6  |    
    """)

    #Grafica

    # Datos de muestra
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [1.3, 3.5, 4.2, 5.0, 7.0, 8.8, 10.1, 12.5, 13.0, 15.6]

    # Crear la gráfica
    plt.plot(x, y, 'b.-')

    # Personalizar la gráfica
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Puntos sobre los que se realiza el ajuste')
    # Mostrar la gráfica en Streamlit
    st.pyplot(plt)

    st.markdown("La razon probable de que no se ajuste una recta a estos datos es que, al ser datos experimentales, tienen errores.")
    st.markdown("Para obtener los coeficientes del sistema de ecuaciones se construye la siguiente tabla")
    st. markdown("""
    |   $x_i$   |   $y_i$   |  $x_i^2$   |   $x_iy_i$   |
    |-----------|-----------|------------|--------------|
    |     1     |    1.3    |      1     |      1.3     |
    |     2     |    3.5    |      4     |       7      |
    |     3     |    4.2    |      9     |     12.6     |
    |     4     |     5     |     16     |      20      |
    |     5     |     7     |     25     |      35      |
    |     6     |    8.8    |     36     |     52.8     |
    |     7     |   10.1    |     49     |     70.7     |
    |     8     |   12.5    |     64     |     100      |
    |     9     |    13     |     81     |     117      |
    |    10     |   15.6    |    100     |     156      |
    |$\sum = 55$|$\sum = 81$|$\sum = 385$|$\sum = 572.4$|
    """)
    st.markdown("El sistema de ecuaciones a resolver es")
    st.latex(r"""\begin{bmatrix} 10 & 55 \\ 55 & 38 \\ \end{bmatrix} \begin{bmatrix} a_0 \\ a_1 \\ \end{bmatrix} = \begin{bmatrix} 81 \\ 572.4 \\ \end{bmatrix}""")
    st.markdown("La solucion para los coeficientes es")
    st.markdown(r"$\frac{385(81) - 55(572.4)}{10(385)-(55)^2} = -0.36$")
    st.markdown(r"$\frac{10(572.4) - 55(81)}{10(385)-(55)^2} = 1.538$")
    st.markdown("El polinomio lineal resultante es $P(x) = 1.538x - 0.36$. en la siguiente figura se muestran los puntos de la tabla y la linea de regresion que los ajusta por medio de este polinomio")

    #Grafica ajustada

    # Datos de muestra
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([1.3, 3.5, 4.2, 5.0, 7.0, 8.8, 10.1, 12.5, 13.0, 15.6])

    # Polinomio
    p = np.poly1d([1.538, -0.36])

    # Valores de x para el polinomio
    x_p = np.linspace(1, 10, 100)
    y_p = p(x_p)

    # Crear la gráfica
    plt.plot(x, y, 'bo', label='Datos')
    plt.plot(x_p, y_p, 'r-', label='P(x) = 1.538x - 0.36')

    # Personalizar la gráfica
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica con polinomio')
    plt.legend()

    # Guardar la gráfica en un archivo de imagen
    plt.savefig('grafica.png')

    # Mostrar la gráfica en Streamlit
    st.image('grafica.png')

    st.markdown("Para analizar el error numericamente se evalua el polinomio en cada uno de los valores de $x_i$ y se obtiene el error, lo que puede verse en la siguiente tabla")
    st. markdown("""
    |   $x_i$   |   $y_i$   |  $P(x_i)$   |$(y_i-P(x_i))^2$|
    |-----------|-----------|-------------|----------------|
    |     1     |    1.3    |       1     |    0.014884    |
    |     2     |    3.5    |       4     |    0.614656    |
    |     3     |    4.2    |       9     |    0.002916    |
    |     4     |     5     |      16     |    0.627264    |
    |     5     |     7     |      25     |     0.1089     |
    |     6     |    8.8    |      36     |    0.004624    |
    |     7     |   10.1    |      49     |    0.093636    |
    |     8     |   12.5    |      64     |    0.309136    |
    |     9     |    13     |      81     |    0.232324    |
    |    10     |   15.6    |     100     |     0.3364     |
    |$\sum = 55$|$\sum = 81$| $\sum = 385$|    2.34474     |
    """)