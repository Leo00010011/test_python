from sys import path
path.append(".")

from Solucion_8.sol import binary_search
from concurrent.futures import ThreadPoolExecutor
from itertools import chain
from random import randint

def paralell_search(queries, dom, workers = 1):
    '''
    Metodo para procesar en paralelo las queries
    @queries: lista de valores a buscar en el dominio
    @dom: dominio de búsqueda
    @workers: números de hilos en los que dividir el trabajo
    '''

    # * que cada worker procese una parte de las quieries y lo guarde en la variable result_acum
    # * cada worker puede ir guardando en result_acum sus resultados, pq los threads comparten memoria   
    # y se pasa por referencia a cada hilo
    slice_size = len(queries)//workers
    result_acum = [[] for _ in range(workers)]
    args = [(queries[i*slice_size:(i + 1)*slice_size], dom, result_acum, i) for i in range(workers)]

    with ThreadPoolExecutor(max_workers= workers) as executor:
        executor.map(search_thread, args)

    return list(chain(*result_acum))

def search_thread(args):
    '''
    Método auxiliar a search para recibir todo en una tupla de argumentos
    @args: (queries, dominio, result_acum, indice_para_el_resultado)
    '''
    queries,dom,results, index = args[0], args[1], args[2], args[3]
    results[index] = search(queries, dom)

def search(queries, dom):
    '''
    Método para búscar sincronamente cada query en el dominio
    @queries: lista de elementos a buscar en el dominio
    @dom: dominio de búsqueda
    '''
    return [binary_search(dom, query) for query in queries]

def test(case_number, queries_len, dom_len, min_value, max_value, workers = 2):
    '''
    Generador de test aleatorios para `parallel_search`:
    @case_number: numero de casos a probar
    @queries_len: cantidad de queries de cada caso
    @dom_len: cantidad de elementos del dominio
    @min_value: menor valor de los elementos del dominio y las queries
    @max_value: mayor valor de los elementos del dominio y las queries
    @workers: cantidad de hilos a utilizar en los tests
    '''

    # El test se basa en que la busqueda sincrona es correcta por lo que deben devolver los mismos valores

    for _ in range(case_number):
        queries = [randint(min_value, max_value) for _ in range(queries_len)]
        dom = [randint(min_value, max_value) for _ in range(dom_len)]
        dom.sort()
        index_list = paralell_search(queries,dom,workers)
        index_list_true = search(queries, dom)
        if index_list != index_list_true:
            print('queries ' + str(queries))
            print('dom ' + str(dom))
            print('\n')
            print('mine: ' + str(index_list))
            print('true: ' + str(index_list_true))

if __name__ == "__main__":
    test(5,10,20,0,5,5)    
