# https://www.codewars.com/kata/5aec1ed7de4c7f3517000079/train/python
#Primera solucion
def first_n_smallest(arr, n):
    lista = arr[:]
    minimo = []
    ordered =[]
    for i in range(n):
        minimo.append(min(lista))
        lista.remove(min(lista))
    for numero in arr:
        if numero in minimo:
            ordered.append(numero)
            minimo.remove(numero)
    return ordered
# Segunda solucion
#     lista = sorted(arr)[:n]
#     return [lista.pop(lista.index(numero)) for numero in arr if numero in lista] 

#casos test
if __name__ == '__main__':
    assert(first_n_smallest([1,2,3,4,5],3), [1,2,3])
    assert(first_n_smallest([5,4,3,2,1],3), [3,2,1])
    assert(first_n_smallest([1,2,3,1,2],3), [1,2,1])
    assert(first_n_smallest([1,2,3,-4,0],3), [1,-4,0])
    assert(first_n_smallest([1,2,3,4,5],0), [])
    assert(first_n_smallest([1,2,3,4,5],5), [1,2,3,4,5])
    assert(first_n_smallest([1,2,3,4,2],4), [1,2,3,2])
    assert(first_n_smallest([2,1,2,3,4,2],2), [2,1])
    assert(first_n_smallest([2,1,2,3,4,2],3), [2,1,2])
    assert(first_n_smallest([2,1,2,3,4,2],4), [2,1,2,2])