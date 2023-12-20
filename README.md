# Consistencia de Arco

Este repositorio tiene como objetivo implementar el algoritmo de arco-consistencia AC-3, una técnica crucial en la resolución de Problemas de Satisfacción de Restricciones. Además de la implementación, se incluirá documentación detallada que explique el funcionamiento del algoritmo, por qué es importante en el contexto de los Problemas de Satisfacción de Restricciones y cómo puede aplicarse. Además se incluiran ejemplos concretos de problemas de satisfacción de restricciones donde la implementación de AC-3 será aplicada. Estos ejemplos servirán como guía práctica para entender cómo integrar y utilizar el algoritmo.

## Introducción

Los Problemas de Satisfacción de Restricciones (PSR o CSP por sus siglas en inglés) son un paradigma común en la inteligencia artificial y la optimización. En un PSR, el objetivo es encontrar una asignación de valores a un conjunto de variables, sujeta a un conjunto de restricciones que deben cumplirse. Estas restricciones expresan relaciones entre las variables y definen el espacio de soluciones válidas para el problema. Los PSR tienen aplicaciones en una variedad de campos, incluyendo la planificación, la programación y la resolución de problemas combinatorios.

El algoritmo de **arco-consistencia** es una técnica fundamental para mejorar la eficiencia en la resolución de PSR. El término "arco" se refiere a pares de variables relacionadas en el problema. La arco-consistencia trabaja propagando restricciones a través de estos arcos para reducir el dominio de las variables. En otras palabras, busca eliminar valores del dominio de una variable que no son consistentes con los valores de las variables relacionadas, lo que resulta en una reducción del espacio de búsqueda.


## Algoritmo


```
AristasPorProcesar = Todas las aristas.
while AristasPorProcesar != ∅:
    (X, C) = Escoge una arista de AristasPorProcesar y quítala.
    for x in dom(X):
        if no existe y tal que C(x, y) se satisface:
            Quita a x de dom(X) y agrega todas las aristas (Z, D) donde D es una condición que involucra a X y Z ≠ X.
```

