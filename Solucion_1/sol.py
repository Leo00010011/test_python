from random import randint
def merge_arrays(a:list, b:list) -> list:
    '''
    Método para mezclar dos listas ordenadas
    @a: una lista ordenada
    @b: una lista ordenada
    '''

    index_a = 0
    index_b = 0
    result = []
    # mezclar hasta que se acabe uno de los dos arrays
    while index_a < len(a) and index_b < len(b):
        if a[index_a] < b[index_b]:
            result.append(a[index_a])
            index_a += 1
        else:
            result.append(b[index_b])
            index_b += 1

    # copiar el resto del que no se acabó
    if index_a == len(a):
        result += b[index_b:]
    else:
        result += a[index_a:]
    
    return result

def test(case_number, len_a, len_b, min_val, max_val):
    '''
    Test para probar el método `merge_arrays`
    @case_number: cantidad de casos a probar
    @len_a: cantidad de elementos del array a
    @len_b: cantidad de elementos del array b
    @min_val: menor valor de los array
    @max_val: mayor valor de los array 
    '''

    for _ in range(case_number):
        a = [randint(min_val,max_val) for _ in range(len_a)]
        b = [randint(min_val,max_val) for _ in range(len_b)]
        a.sort()
        b.sort()
        merged_mine = merge_arrays(a,b)
        merged_true = (a + b)
        merged_true.sort()
        if not merged_mine == merged_true:
            print(merged_mine)
            print(merged_true)
            print('------------------------------------')

test(100, 20, 20, 0, 10)