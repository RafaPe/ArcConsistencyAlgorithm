# Consistencia de Arco

Este repositorio tiene como objetivo implementar el algoritmo de arco-consistencia AC-3, una técnica crucial en la resolución de Problemas de Satisfacción de Restricciones. Además de la implementación, se incluirá documentación detallada que explique el funcionamiento del algoritmo, por qué es importante en el contexto de los Problemas de Satisfacción de Restricciones y cómo puede aplicarse. Además se incluiran ejemplos concretos de problemas de satisfacción de restricciones donde la implementación de AC-3 será aplicada. Estos ejemplos servirán como guía práctica para entender cómo integrar y utilizar el algoritmo.

## Introducción

Los Problemas de Satisfacción de Restricciones (PSR o CSP por sus siglas en inglés) son un paradigma común en la inteligencia artificial y la optimización. En un PSR, el objetivo es encontrar una asignación de valores a un conjunto de variables, sujeta a un conjunto de restricciones que deben cumplirse. Estas restricciones expresan relaciones entre las variables y definen el espacio de soluciones válidas para el problema. Los PSR tienen aplicaciones en una variedad de campos, incluyendo la planificación, la programación y la resolución de problemas combinatorios.

El algoritmo de **arco-consistencia** es una técnica fundamental para mejorar la eficiencia en la resolución de PSR. El término "arco" se refiere a pares de variables relacionadas en el problema. La arco-consistencia trabaja propagando restricciones a través de estos arcos para reducir el dominio de las variables. En otras palabras, busca eliminar valores del dominio de una variable que no son consistentes con los valores de las variables relacionadas, lo que resulta en una reducción del espacio de búsqueda.


## Algoritmo

### Modelado de restricciones

En la representación de un PSR, las variables y las restricciones se modelan como vértices en una gráfica bipartita. Las variables constituyen un conjunto de vértices, y las restricciones forman el otro conjunto de vértices. Las aristas de la gráfica conectan variables con restricciones, reflejando así las dependencias entre ellas.

La estructura bipartita permite visualizar de manera clara las relaciones entre las variables y las restricciones, sirviendo como base para la aplicación efectiva de la arco-consistencia.

El algoritmo AC-3 actúa sobre esta gráfica bipartita, realizando un proceso iterativo de propagación de consistencia a través de los arcos. La arco-consistencia se logra eliminando valores inconsistentes de los dominios de las variables
<p align="center">
 <img src="docs/imgs/bipartite_example.png" alt="Texto Alternativo" width="400" height="200">
</p>

### Pseudocódigo de AC-3

```
AristasPorProcesar = Todas las aristas.
while AristasPorProcesar != ∅:
    (X, C) = Escoge una arista de AristasPorProcesar y quítala.
    for x in dom(X):
        if no existe y tal que C(x, y) se satisface:
            Quita a x de dom(X) y agrega todas las aristas (Z, D) donde D es una condición que involucra a X y Z ≠ X.
```
---

1. **Inicialización**

Se comienza definiendo el conjunto de _AristasPorProcesar_, que contiene todas las aristas de la gráfica bipartita que representa las relaciones entre variables y restricciones del PSR.

2. **Iteración Principal**

El algoritmo entra en un bucle que se ejecuta mientras haya aristas por procesar en _AristasPorProcesar_. Cada iteración del bucle se centra en una arista específica.

3. **Selección de Arista**

Se elige una arista $(X, C)$ del conjunto _AristasPorProcesar_ y se elimina del conjunto. Esta arista conecta una variable $X$ con una restricción $C$ en la gráfica bipartita.

4. **Consistencia de Arco**

Se realiza un bucle sobre el dominio $dom(X)$ de la variable $X$. Para cada valor $x$ en el dominio, se verifica si existe algún conjunto de valores $\vec{y}$ para el resto de variables, tal que la restricción $C(x, \vec{y})$ se satisface. Si no existe tales valores, significa que el valor $x$ no cumple la arco-consistencia con la restricción $C$.

>_En este punto evaluamos cada valor del dominio de la variable y analizamos si es posible que ese valor pueda cumplir con la restricción con la que está relacionada_


5. **Actualización del Dominio**

En caso de que no exista $\vec{y}$ que satisfaga la restricción para un valor $x$, se elimina $x$ del dominio $dom(X)$. Además, se agregan nuevas aristas al conjunto _AristasPorProcesar_, las cuales son todas aquellas $(Z, D)$ donde la condición $D$ de estas nuevas aristas implica a $X$ y $Z$ sea diferente de $X$.

>_Si no hay forma de que el valor analizado cumpla con la restricción, se quita del dominio de la variable respectiva pues ninguna propuesta de solución que contenga ese valor en esa variable será solución al problema. Esto pudo afectar a otros valores que necesitaban de este para ser consistentes, por lo tanto es necesario volver a revisar ciertas aristas_

6. **Fin de Iteración**

El bucle continúa hasta que no haya más aristas en _AristasPorProcesar_. En este punto se logra la arco-consistencia y garantizamos que todos los valores de las variables son consistentes con las restricciones.

> _Esto no garantiza que cualquier combinación de los valores restantes sea una solución al problema. Para obtener la solución o soluciones finales se necesita realizar una búsqueda sobre los dominios reducidos obtenidos por el algoritmo_ 


## Ejemplo
Vamos a abordar un problema pequeño y directo para simplificar la explicación del funcionamiento del algoritmo la resolución de PSRs. La comprensión de estos conceptos y pasos será fundamental, ya que la solución de problemas más complejos se realiza siguiendo el mismo procedimiento como veremos después.

En la siguiente figura, se deben colocar seis números entre el 1 y el 5 en los cuadrados, de manera que se cumplan las siguientes condiciones:

- La suma de los números en cada renglón debe ser la misma.
- La suma de los números en cada columna debe ser la misma.

Se han proporcionado algunos números en los cuadrados. **¿Puedes determinar qué número debe colocarse en el cuadro sombreado?**


<p align="center">
 <img src="docs/imgs/example_problem.png" alt="Texto Alternativo" width="500" height="150">
</p>

### Solución
Se observa que este problema puede ser modelado como un PSR, pues hay restricciones muy claras dentro de las instrucciones. Por lo tanto, como primer paso, identificaremos y modelaremos las restricciones del problema. Para esto será util asignar nombres a las las casillas en blanco, ya que estas serán nuestras variables.

<p align="center">
 <img src="docs/imgs/example_problem2.png" alt="Texto Alternativo" width="500" height="150">
</p>

Ahora sí podemos modelar las restricciones en función de las variables. En primer lugar se menciona que la suma de los renglones debe ser la misma, esto puede expresarse de la siguente forma:

$$1 + A + 4 = B + 2+ C$$

Lo cual representa que la suma del primer renglón debe ser igual a la del segundo. Posteriormente también se nos indica que la suma por columnas también debe ser equivalente. Y su expresión quedaría de la siguiente forma:
$$1 +B = A+2 = 4+C$$

Con estas expresiones hemos modelado las restricciones del problema. Ahora la pregunta es si existen valores para $A,B,C \in$ { $1,2,3,4,5$ } tal que se cumplan ambas restricciones. Resolviendo este PSR podremos responder a la pregunta del problema.

<!-- > Notemos que es necesario hacer asignaciones a todas las variables para poder responder la pregunta sobre el valor de la casilla sombreada. Es por esto que es necesario resolver todo el sistema para encontrar la respuesta. -->

Ya que tenemos la modelación de restricciones, variables y sus dominios, podemos obtener la gráfica de restricciones. Recordemos que debe ser una gráfica bipartita donde las restricciones serán un tipo de nodo y las variables otro. Cada nodo de restricción irá unido a las variables que están involucradas en esta.

<p align="center">
 <img src="docs/imgs/constraints_example_problem.png" alt="Texto Alternativo" width="450" height="240">
</p>

> Notemos que la modelación de esta gráfica puede variar (no es única) y esto afectaría directamente al desempeño del algoritmo de arco-consistencia.

Con esta gráfica ya podemos aplicar el algoritmo de arco-consistencia **AC-3** para reducir los dominios de las variables (si es que hay valores que no presentan consistencia de arco). Si se quiere revisar el paso a paso de la aplicación del algoritmo a este problema se puede revisar el siguiente documento: [AC-3 aplicado (paso a paso)](docs/arco_consistencia_aplicada.pdf)

Después de aplicar el algoritmo de arco-consistencia, nos damos cuenta que el dominio de las variables cambió. Esto pasó porque sí existian valores inconsistentes con los arcos de restricciones, por lo tanto se eliminaron. Los nuevos dominios ahora son: $A  \in$ { $3, 4$ } &nbsp;&nbsp; $B \in$ { $4, 5$ } &nbsp;&nbsp; $C \in$ { $1, 2$ }

Esto ya nos deja con un espacio de búsqueda mucho más manejable. Antes teniamos $5^3$ combinaciones de donde buscar, ahora sólo tenemos $2^3$. Por lo tanto pasamos de 125 combinaciones a tan solo 8 (esta es la ventaja de la arco-consistencia). Estás 8 posibles soluciones incluso se pueden escribir aquí mismo:

1. $A = 3$ &nbsp;&nbsp;&nbsp; $B = 4$ &nbsp;&nbsp;&nbsp; $C = 1$
2. $A = 4$ &nbsp;&nbsp;&nbsp; $B = 4$ &nbsp;&nbsp;&nbsp; $C = 1$
3. $A = 3$ &nbsp;&nbsp;&nbsp; $B = 5$ &nbsp;&nbsp;&nbsp; $C = 1$
4. $A = 4$ &nbsp;&nbsp;&nbsp; $B = 5$ &nbsp;&nbsp;&nbsp; $C = 1$
5. $A = 3$ &nbsp;&nbsp;&nbsp; $B = 4$ &nbsp;&nbsp;&nbsp; $C = 2$
6. $A = 4$ &nbsp;&nbsp;&nbsp; $B = 4$ &nbsp;&nbsp;&nbsp; $C = 2$
7. $A = 3$ &nbsp;&nbsp;&nbsp; $B = 5$ &nbsp;&nbsp;&nbsp; $C = 2$
8. $A = 4$ &nbsp;&nbsp;&nbsp; $B = 5$ &nbsp;&nbsp;&nbsp; $C = 2$

Ahora, para responder a la pregunta del problema, tenemos que buscar la solución dentro de nuestro espacio de búsqueda reducido. La estrategia de búsqueda puede variar, y aunque existen algoritmos especializados, en este caso, dada la simplificación del problema, no es necesario recurrir a ellos. Abordaremos la búsqueda de la siguiente manera:

**Observación:** La variable $C$ solo puede tener dos valores posibles: 1 o 2.

**Caso 1:**&nbsp;&nbsp;$C = 1$

En este escenario, la restricción de la suma por columnas ( $1 + B = A + 2 = 4 + C$ ) implica:

$$1 + B = A + 2 = 5$$

Esto conduce a $A = 3$ y $B = 4$. Sin embargo, al verificar estas asignaciones en la restricción de suma por fila ( $1 + A + 4 = B + 2 + C$ ), obtenemos:

$$1 + 3 + 4 = 4 + 2 + 1$$

Lo cual resulta en $8 \neq 7$, contradiciendo la restricción. Por lo tanto, $C$ no puede ser 1.

**Caso 2:** &nbsp;&nbsp;$C = 2$

En este caso, la restricción de la suma por columnas implica:

$$1 + B = A + 2 = 6$$

Lo que lleva a $A = 4$ y $B = 5$. Verificando estas asignaciones en la restricción de suma por fila ( $1 + A + 4 = B + 2 + C$ ), obtenemos:

$$1 + 4 + 4 = 5 + 2 + 2$$

Esto resulta en $9 = 9$, confirmando que esta asignación cumple con las restricciones. Por lo tanto, concluimos que **el número 2 es el valor que debe ir en la casilla sombreada**.


## Conclusiones
El algoritmo AC-3 se presentó como una técnica fundamental para mejorar la eficiencia en la resolución de PSR. Se describió detalladamente el funcionamiento del algoritmo, desde la modelación de restricciones y la representación gráfica bipartita hasta el pseudocódigo y los pasos concretos de la aplicación del algoritmo.

La reducción del dominio de las variables tras la aplicación de AC-3 resultó ser una ventaja crucial. Pasamos de un espacio de búsqueda inicial de $5^3$ combinaciones a tan solo $2^3$ combinaciones. Esta disminución drástica en las posibles combinaciones simplificó significativamente la búsqueda de soluciones al problema. La arco-consistencia demostró su eficacia al eliminar valores inconsistentes, permitiéndonos enfocarnos en un conjunto más manejable de soluciones potenciales.

Es importante destacar que, aunque el ejemplo presentado puede parecer relativamente sencillo, la aplicabilidad de AC-3 se extiende a problemas mucho más complejos. Este algoritmo ha demostrado ser eficaz en la resolución de rompecabezas como el Sudoku, donde las restricciones son más numerosas y las soluciones más intricadas. Al enfrentarse a problemas de mayor envergadura, AC-3 se convierte en una herramienta valiosa para reducir el espacio de búsqueda y acelerar el proceso de encontrar soluciones viables.

Además, es fundamental destacar que algoritmo no se limita a problemas de rompecabezas; su aplicabilidad se extiende a diversos escenarios del mundo real. Por ejemplo, en la asignación de recursos en proyectos de construcción, donde se deben cumplir restricciones de tiempo, presupuesto y disponibilidad de materiales. Además, en la programación de horarios escolares, donde las limitaciones de aulas, profesores y preferencias de asignaturas deben ser consideradas.

## Recuros Adicionales
Para aquellos interesados en explorar la implementación práctica del algoritmo de arco-consistencia AC-3, hemos proporcionado el código correspondiente al ejemplo presentado anteriormente. Además del código para el problema de las sumas constantes en la matriz, también hemos incluido implementaciones para otros dos problemas adicionales que ilustran la versatilidad de AC-3. Estos ejemplos adicionales no solo amplían la comprensión del algoritmo, sino que también ofrecen la oportunidad de ver cómo se aplica a situaciones más complejas y diversas.



### Matriz de sumas constantes 

En la siguiente figura, se deben colocar seis números entre el 1 y el 5 en los cuadrados, de manera que se cumplan las siguientes condiciones:

- La suma de los números en cada renglón debe ser la misma.
- La suma de los números en cada columna debe ser la misma.

Se han proporcionado algunos números en los cuadrados. **¿Puedes determinar qué número debe colocarse en el cuadro sombreado?**


<p align="center">
 <img src="docs/imgs/example_problem.png" alt="Texto Alternativo" width="500" height="150">
</p>

- [Jupyter Notebook](notebooks/MatrizSumasConstantes.ipynb)
- [Código en script](scripts/constant_sum_matrix.py)

### Problema del Cubo

Los vértices de un cubo se numeran del 1 al 8 de manera que el resultado de sumar los cuatro números de cada cara es el mismo para todas las caras. Se han colocado ya los números 1, 4 y 6 como se muestra en la figura. **¿Qué número va en el vértice marcado con x?**

<center>
<img src="docs/imgs/cube_problem.png">
</center>

- [Jupyter Notebook](notebooks/ProblemaCubo.ipynb)
- [Código en script](scripts/cube_problem.py)

### Criptoaritmética

Cada letra representa un dígito del sistema de numeración decimal.

Encuentra los valores, tales que:

- Una letra y un dígito estén asociados de manera biunívoca.
- Los "números" *TWO* y *FOUR* no tengan ceros a la izquierda.
- El sistema sea consistente al realizar la operación suma.

<center>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALYAAACXCAYAAAC4AKGXAAAFOHRFWHRteGZpbGUAJTNDbXhmaWxlJTIwaG9zdCUzRCUyMmFwcC5kaWFncmFtcy5uZXQlMjIlMjBtb2RpZmllZCUzRCUyMjIwMjEtMDEtMjJUMDElM0EzNyUzQTI3LjEzMlolMjIlMjBhZ2VudCUzRCUyMjUuMCUyMChYMTEpJTIyJTIwZXRhZyUzRCUyMm9sc1RVZXVlOFdyaTFQTDJBQWVlJTIyJTIwdmVyc2lvbiUzRCUyMjE0LjIuNiUyMiUzRSUzQ2RpYWdyYW0lMjBpZCUzRCUyMmJuNmZtRm80Nk5sNUJaNDRYcWJ2JTIyJTIwbmFtZSUzRCUyMlBhZ2UtMSUyMiUzRTdWbGRiNXN3RlAwMWVZd0VnZEQwTVIlMkZ0cGtuVHBtVmIycjY1NElJMWc2bmpKTEJmUHp2WWZKT1NxVW1JeWt0ckg5dlh2dmVjJTJCRjdoZ1RIM28wOFVoTjVYNGtBOEdHbE9OREFXZzlGb1lrMzRYd0hFQ1dDYVZnSzRGRGtKcEdmQUV2MkZFdFFrdWtFT1hCY21Na0l3UTJFUnRFa1FRSnNWTUVBcDJSV252UkJjM0RVRUxxd0FTeHZnS3JwQ0R2T2tXMk10d3o5RDVIcHFaMTJUSXo1UWt5V3c5b0JEZGpuSXVCc1ljMG9JUzFwJTJCTklkWXhFN0ZKVmwzM3pDYUhvekNnTFZac0RLJTJCdklMaGt6NGMzdnJiQU45TTV0UGZRek94c2dWNEl4MldoMld4aW9CTHlTYVUweUJsTUtxTE8zaFcwN1hxdWZUVVc2NFNTSHpJYU15bktJbklGWEd4dTh1aXJTdWpYaTdTaWdFZ0NYWlR3MWtNZUVPRzRZaVE2RFVoc1REZmRlYWdiU0UwMXV0R2tEZDdJUUVicnZmU25mSUpoaFpHMlNCdnVmTCUyRjNzaHpHUkNyJTJGOSUyRnNUMldHJTJCNXBZS2xybmNHVkhqdTFkVVdpSmNFNnh3RDNtODdndGRONWNNMHIlMkJ3RG5CaEhJa0lBRVV4ME1ZbHlDQWtSdndyczJwaHh5ZkNjRWclMkZtT2F5Z0VmT1k3WVpyYnpFSVBMRU5oaXp4MiUyRk9UakdkUlk0VUZDanBjZXFVVnhlV2MyYXJzb3RKeWp6bkhvYVhaV2VWcjJlV3VvcEttcnBVdkl5R3VYMXpzcjRkcFF5UHBRR2FuTFdXVFV3N2x3V1QxUDJ4ZEs0ZFZYWGJwJTJGRzYwWGRuVFIlMkJjMVY2NnRONFd6MTFKSTFQJTJCalIlMkJjUTFjT28zcmRYbjhPTTVINCUyRnBMWnRiSSUyQnZVeWZMZ2dNZDh1U09ySU5VOUc3dTNsaTdSeVRLeWFJczA2cSUyQksxYzExNzl4JTJGNTJrdTAxNTFhU20lMkYlMkJ4dFpudTlQVDNwR1NSMiUyRiUyQk12Yk9LdmpWcTZDN1JjJTJGWlBtRDk2RlhRcUlLMjVkSHBaTkRpSlFvR3psUTg2V1d4emRFQkk4UWVaSmhFJTJCekhYWGtUNVRxdzZBVCUyRjRnMW91T28lMkY1a1d6UnZoY1hLSUJPNWRtd0ZRSGNIN0toTm14UkV6RkFYWGpRb3ZGbVZoOGZvSkJDREJqYUZ0Mm80MVh1OEoyZyUyRmE4dnpSN0ZZcklpamNSUnVTcFRSOVhRdUdSSUt4bEtBbEV4dEpkWjZuYWQ4bmczZTE1TnBtZHYxTWJkUHclM0QlM0QlM0MlMkZkaWFncmFtJTNFJTNDJTJGbXhmaWxlJTNFh8P4PQAAC5RJREFUeJztnWdoFFsYhjfdmHjtxoImKwFLIrbYYkWNoiLYu2JBxYoNDBpUUGzBiMEWFLEGRH8oNkQRVKLYwAJ2RCyQiJhIEhJNsu/9ce8Oc/bMps5kZ8++Dxxwd74z583kMczO7s7nACEK4vB1AEKsgGITJaHYREkoNlESik2UhGITJaHYREkoNlESik2UhGITJaHYREkoNlESik2UhGITJaHYREkoNlESik2UhGITJaHYREkCUuzOnTvD4XDUaUyYMMGULCNGjBD2GxYWhtLSUsPaQ4cOSTlycnIMa1+/fi3VrlmzxpTMnnz58gUZGRlISUmB0+lEw4YNER0dDafTidGjR2P//v349u2bJWt7g2L7WOz09HRp348ePTKsnT9/vlSbkZFhWHvmzBmp9vr166ZkdlNcXIwNGzYgIiKiyuMVGRmJ1NRUr/9pzYZi+1jsV69eSfs+dOiQYW1iYqJUO336dMPaNWvWCHUREREoLi42JTMA5ObmIikpqcbHbfDgwfj165dpObwRkGLPmzcPw4YNk0bv3r2lX0S3bt0Ma9PS0kzL065dO2HN+fPnSzVFRUUICQmR8jmdTsN9Dh48WKgbMWKEaXmLi4vRrVs3Q3FDQkLQrl07tG3bFsHBwYY1/fv3x58/f0zLY0RAiu2Np0+fSr+Eq1evWr7uokWLhDUTEhKkmnv37mnbg4KChPq8vDyhtqKiAo0aNRJq9u7da1reuXPnSsepUaNGyMrKwu/fv7W6X79+4cCBA2jQoIFUv2rVKtPyGEGxdfhK7AsXLghrBgcHo6ioSKjJyMjQtvfq1QstWrTQHl+5ckWoffPmjfRzPH/+3JSsT548kfbdpUsXvH371uuc58+fIy4uTvrL/v79e1MyGUGxdfhK7Pz8fOk04969e0LNzJkztW3Lli3D2LFjtceep0Vnz54V9hUTEwOXy2VK1gkTJkjH6PHjx1XOu3nzpjRv4cKFpmQygmLr8JXYADBw4EBh3X379gnb4+PjtW0nTpzAtm3btMejRo0SatetWyfsa+7cuaZkLC4ulq6ATJs2rdrzhw0bJsxt3rw5KioqTMnmCcXW4Uuxt2/fLqw7c+ZMbVt+fr5wXv3q1SvcuHFDe9ykSRPhL/LQoUOFfZ09e9aUjPo1vZ0GVcbJkyel+U+ePDElmycUW4cvxfY8d42Pj9e23bp1S3s+KioK5eXl+Pnzp1DvPsd1uVz4559/hBeaubm5pmTMzMyUjk9l59ae5OTkSPOzs7NNyeYJxdbhS7FdLhdatmwprO2+3rtz507tuSFDhmhz9Kcnp06dAgC8e/dO2EfPnj1Ny7h582bpBWBNLtvl5eVJx3f//v2m5dNDsXX4UmwAmD17trD2rVu3AACTJk3SntuwYYNWP2vWLO35FStWAACys7OFfaSmppqWb9OmTZLYf//+rfb8goIC6fju2bPHtHx6KLYOX4vt+Tb4zp07AQDt27fXnjt//rxWf+DAAe35pKQkAMD69euFfdy5c8e0fPr13OPdu3fVnv/48WNp/unTp03Lp4di6/C12Hl5ecKLxIkTJyI3N1fI8+nTJ63+4cOH2vNhYWEoKSkRrjxERUWZ+g7ftWvX6nR8jD6/8uDBA9Py6aHYOnwtNgDhbf327dvj6tWr2uMWLVoItaWlpQgPD9e25+TkoHHjxtrjcePGmZqtqKhIWM/hEK/eVIX+2rvD4UDTpk1RXl5uakY3FFuHHcT2fIG2dOlS7d9jxoyR6vv06SOcZ+vnZmZmmp5v/PjxwhpBQUF49uxZlfNu374tHdsFCxaYns8NxdZhB7Hv378vrB8dHa39e+vWrVK9Xmb9ZT6Ho2aX4qqL/vTHPRISEvDx40evc16+fImOHTtKLzxrcn5eUyi2DjuIXVZWJpxOVJXl9OnThrUdOnSwLOOMGTOk9Ro3bowTJ04In3EpKChAZmYmIiMjpfqVK1dalg+g2AJ2EBsAJk+ebCir56f4AODt27eGtYsXL7YsX2FhIbp27Wq4bnh4OOLi4hAbG4vQ0FDDmr59+/Jjq/WJXcQ+duyYlCM2Ntaw1uVyoUmTJlL9xYsXLc34/ft39OzZ01DcysbAgQPx8+dPS7MBFFvALmJ//fpVyjFlyhSv9SkpKdL5a318S6WwsBCrV6+WrpQYjcjISGzcuBElJSWW5wIotoBdxAaAhIQEIUdl79ClpaUJtQMGDKjHpMDnz5+xZ88eDB8+HB06dEBkZCQaNmyIuLg4jBo1ChkZGfj+/Xu9ZqLYREkoNlESik2UhGITJaHYREkoNlESik2UhGITJaHYREkoNlESik2UhGITJaHYREkoNlESik2UhGITJaHYREkoNlGSgBTbTl3D2OfRGii2j8Vmn0droNg+Fpt9Hq0hIMVmn8e6wT6PXvjw4QPevHnji6UrhX0eqwf7PHohMTFRuiWuHWCfx6phn8dKoNgi7PNoPhRbB/s8Vg77PFYBxZZhn0dzodg62Oexctjn8X/Ky8ulH6SqYdYvoTawz2PlsM/j/1RUVBheA46KikJYWJjhtvq4eO8NX99tlX0ezYOnIjp8LTb7PJoHxdbha7HZ59E8KLYOX4sNsM+jWVBsHXYQm30ezYFi67CD2OzzaA4B+ek+b9hBbPZ5NAeKrcMOYgPs82gGFFuHXcRmn8e6Q7F12EVs9nmsOxRbh13EBtjnsa5QbKIkFJsoCcUmSkKxiZJQbKIkFJsoCcUmSkKxiZJUW2z91/05OOp7bNu2zRqxCfEnKDZREopNlIRiEyWh2ERJKDZREopNlIRiEyWh2ERJLBO7tLS0Tu80Wf1lVD1261O4Y8cO6XhUdcekOXPmCPX62xCbjWfHhKpGREQEEhMTMXXqVMvuh+1JQItt1z6FqomtHyEhIdi+fbtl2dwErNh27lOostgOx3+3RfPWUdgs6lXsjh07Gt4T22jcvXvXqmi271Poj2L369dP+h0OGTIEiYmJCAsLM6y3knoVe/fu3VYtVyPs3qfQH8Wu7N59nz9/RmxsrFAfGhpq6R+HgBPbH/oUqiY2ABw+fFiaY1bvSSMCTmx/6FOoothGN423sjtzQIntL30KVRT74MGDQn1ERISltzsLKLH9pU+hamJ//fpVOpVbsmSJZfkAm17us+pasb/0KfRHsZOTkzFy5EhhDB8+HD169JBuWpmQkIAfP35Ylg8IMLH9pU+hP4pdnREcHIwFCxZYLjUQYGL7S59CVcWOiYnB8ePHUVZWZlk2N7Z8g6YmstUEf+lTqKrY7rF8+XLLsrkJqBeP/tKn0B/FNnrxWFJSgmfPnmHQoEFSvRWNn/QElNj+0qdw165d0rHTNy0yYsqUKUJ9p06dTM/lpjbvPHrWnzt3zrJ8QICJDfhHn8KsrCxprRcvXlQ6p3v37kJ9cnKyJdmA2l3H9uyElp6eblk+IADF9oc+hZ69Hh0OB9auXeu1/unTpwgJCRHqFy1aZEk2oHZix8TECPVbtmyxLB8QgGID9u9TWFZWJokQHByMtLQ05Ofna3UVFRW4dOkSnE6nlO/y5cuW5auN2M2aNRPq169fb1k+IEDF9oc+hUeOHDFc2+FwoFWrVnA6nYYfB3U4/vtIqMvlsixbbcRu2rSpUG/lpyOBABUbsH+fQgBYtmxZjfM5nU7Lv8ZWG7HbtGkj1M+ZM8fSjAErNmDvPoVusrKyDBuUeo6goCDMmDGjXvo71kbs5ORkoT4uLg4FBQWWZQxosd3YsU+hnsLCQhw9ehSTJ0+G0+lEdHQ0wsPD0bp1awwaNAibNm2y/LqwntqInZ6eLs1JTU21LCNvv0CUhGITJaHYREkoNlESik2UhGITJaHYREkoNlESik2UhGITJaHYREkoNlESik2UhGITJaHYREkoNlESik2UhGITJaHYREkoNlESik2UhGITJaHYREkoNlESik2UhGITJaHYREkoNlESik2U5F+PsJam9Xan+wAAAABJRU5ErkJggg==" alt="Texto alternativo">
</center>

- [Jupyter Notebook](notebooks/CriptoAritmetica.ipynb)
- [Código en script](scripts/cryptarithmetic.py)




