import random

# Функция генерирующая рандомный список
def generate_list():
    result = random.sample(range(1, 50), 10)
    print("Random number list is :")
    print(result)
    return result


# Функция обмена значениями
# i и j - индексы соседних элементов списка
# arr - список
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Функция просеивания (перемещение верхнего элемента вниз)
# arr - список
# i - индекс родительского элемента
# upper - верхняя граница списка
def sift_down(arr, i, upper):
    while(True):
        left = i * 2 + 1 # Задаем левый дочерний элемент
        right = i * 2 + 2 # Задаем правый дочерний элемент
        if max(left, right) < upper: # Проверяем есть ли у родителя дочерний элемент
            if arr[i] >= max(arr[left], arr[right]): # Проверяем больше ли родитель чем его больший дочерний элемент. Если нет, то отсается на месте
                break
            elif arr[left] > arr[right]: 
                swap(arr, i, left) # Если левый дочерний больше правого, то меняем левый и родитель местами
                i = left # обновим индекс родительского элемента
            else:
                swap(arr, i, right) # Если правый дочерний больше левого, то меняем правый и родитель местами
                i = right # обновим индекс родительского элемента
        elif left < upper: # Проверяем на то если имеется только левый дочерний элемент
            if arr[left] > arr[i]:
                swap(arr, i, left)
                i = left 
            else:
                break
        elif right < upper: # Проверяем на то если имеется только правый дочерний элемент
            if arr[right] > arr[right]:
                swap(arr, i, right)
                i = right
            else:
                break
        else:
            break

#  Реализация сортировки
def heap_sort(arr):
    for i in range ((len(arr) -2) // 2, -1, -1): # (len(arr) -2) // 2 - это нижний правый элемент
        sift_down(arr, i, len(arr))

    for last_el in range(len(arr) -1, 0, -1): # Не затрагиваем правую(отсортированную) часть списка
        swap(arr, 0, last_el)
        sift_down(arr, 0, last_el)
    
    print("List after heap sort :")
    print(arr)



lst = generate_list()
heap_sort(lst)

#  O (n log(n))
