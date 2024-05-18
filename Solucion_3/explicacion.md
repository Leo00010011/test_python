# Complejidad temporal de cada Operación

## get_node

En el peor caso el método `get_node` ejecuta tantos llamados recursivos como la altura del árbol donde se ejecuta.

Si el árbol está degenerado (todos sus nodos tienen un solo hijo) la altura es igual a la cantidad de elementos de la lista. En este caso  la complejidad de este algoritmo sería **O(n)** donde n es la cantidad de elementos de la lista.

Si el árbol está balanceado, ocurriría el mejor caso en el cual la altura del árbol es mínima siendo esta $log_2(n - 1)$, por lo que la complejidad temporal del algoritmo sería **O(log(n))**.

## insert

La complejidad temporal `insert` es igual a la complejidad temporal de `get_node` más una constante por lo que, se mantiene con la misma complejidad temporal de `get_node`.

## remove(Me leí mal la orden e implementé el remove)

La complejidad temporal de `remove` es igual a la complejidad temporal de `get_node`, más la complejidad temporal de buscar el menor nodo que es mayor que el nodo a remover, más una constante

Buscar el menor nodo que es mayor que el nodo a remover es buscar el descendiente del su hijo derecho que está más a la izquierda. En el peor caso la cantidad de pasos a dar es igual a la altura del árbol, por lo que su complijidad es similar a la de buscar el nodo.

Por lo tanto la complejidad temporal de remove es **O(h)** donde h es la altura del árbol.

## AVL

Los tiempos de ejecución pueden ser mejorados utilizando estrategias de balanceo como en el caso del AVL