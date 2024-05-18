from random import randint

def binary_search(arr, item):
    '''
    Busqueda binaria
    @arr: lista ordenada de elementos
    @item: elemento a buscar
    '''
    l = -1
    r = len(arr)
    while r - l > 1:
        mid = (r + l)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            l = mid
        else:
            r = mid
    return l


def find_range(arr, index):
    '''
    retorna el menor y mayor indice de los elementos contiguos iguales a `arr[index]`
    '''
    min_index = index
    max_index = index

    while min_index - 1 >= 0 and arr[index] == arr[min_index - 1]:
        min_index -= 1
    
    while max_index + 1 < len(arr) and arr[index] == arr[max_index + 1]:
        max_index += 1

    return min_index, max_index
    

def test(number_cases, arr_len, min_val, max_val):
    '''
    test para el metodo `binary_search`
    @number_cases: numero de casos a generar
    @arr_len: cantidad de elementos de los casos a probar
    @min_val: menor valor de los casos a probar
    @max_val: mayor valor de los casos a probar
    '''

    # Generar una lista de numeros aleatorios
    # con una probabilidad de 1/10 buscar un elemento aleatorio que sea menor que todos los de la lista
    # con una probabilidad de 1/10 buscar un elemento aleatorio que sea mayor que todos los de la lista
    # con una probabilidad de 4/5 buscar un elemento aleatorio dentro de la lista
    for _ in range(number_cases):
        a = [randint(min_val,max_val) for _ in range(arr_len)]
        a.sort()
        if randint(0,5) == 0:
            # 1/5 de prob de que el elemento no esté en el array
            if randint(0,1) == 0:
                # 1/10 de prob de que el elemento sea menor que todos
                value = min_val - randint(1,5)
                found = binary_search(a,value)
                if found != -1:
                    print('error buscando menor que todos')
                    print('arr: ' + str(a))
                    print('found: ' + str(found))
                    print('-------------------------')
            else:
                # 1/10 de que el elemento sea mayor que todos
                value = max_val + randint(1,5)
                found = binary_search(a,value)
                if found != arr_len - 1:
                    print('error buscando mayor que todos')
                    print('arr: ' + str(a))
                    print('found: ' + str(found))
                    print('-------------------------')
        else:
            # buscando adentro
            index = randint(0,arr_len - 1)
            found = binary_search(a,a[index])
            min_index, max_index = find_range(a,index)
            if found < min_index or found > max_index:
                print('error buscando dentro')
                print('index: ' + str(index))
                print('arr: ' + str(a))
                print('found: ' + str(found))
                print('min_index: ' + str(min_index))
                print('max_index: ' + str(max_index))
                print('-------------------------')
            
test(100000, 100, 0, 70)