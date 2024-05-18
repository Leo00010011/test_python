# Explicaciones de beneficios de utilizar la busqueda binaria

La complejidad temporal de una búsqueda binaria en un lista ordenada de tamaño **n** es de **O(logn)**, mientras que lo búsqueda secuencial es **O(n)**. 

En el ejercicio se nos pide realizar una cantidad de búsquedas igual a la cantidad de elementos de la segunda lista (digamos que es **m**) por lo que si **T(n)** es la complejidad temporal del algoritmo de búsqueda utilizado entonces la complejidad del algoritmo completo será **O(mT(n))**. Si se usa búsqueda secuencial la complejidad sería **O(mn)** y si se usa búsqueda binaria la complejidad sería de **O(mlogn)**.

Teniendo en cuenta que el tamaño del dominio de búsqueda es potencialmente grande el uso de la búsqueda binaria puede reducir los costos considerablemente.
