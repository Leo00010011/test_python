from random import randint
from statistics import median

def find_median(arr:list):
    '''
    Metodo para encontrar la mediana en un array
    @arr: array al que hay que buscarle la mediana
    '''
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2
    else:
        return arr[len(arr)//2]
    

def test(number_cases, arr_len, min_val, max_val):
    '''
    Metodo para probar el metodo `find_median`
    @number_cases: cantidad de casos a probar
    @arr_len: cantidad de elementos de los casos a probar
    @min_val: menor valor de los casos a probar
    @max_val: mayor valor de los casos a probar
    '''

    for _ in range(number_cases):
        a = [randint(min_val,max_val) for _ in range(arr_len)]
        if find_median(a) != median(a):
            print(a)
            print(find_median(a))
            print(median(a))
            print('---------------------')

test(100, 15, 0, 10)

