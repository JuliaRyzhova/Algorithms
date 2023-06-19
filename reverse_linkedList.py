class ListNode:
    def __init__(self, value=0, next=None): # Создание ноды(узла)
        self.val = value
        self.next = next

class Linked_list:
    def __init__(self): # Инициализация списка
        self.head = None

    def add_first(self, value): # Добавление нового эл-та в начало списка
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
    
    def print(self): # Вывод списка в консоль
        current_node = self.head
        result = ""
        while current_node:
            result = result + " " + str(current_node.val)
            current_node = current_node.next
        print(result)

    def reverse_linkedList(self): # Функция разворота связанного списка
        prev = None 
        current = self.head 
        while current: 
            next_node = current.next 
            current.next = prev 
            prev = current
            current = next_node
        self.head = prev



my_list = Linked_list()
my_list.add_first(5)
my_list.add_first(3)
my_list.add_first(12)
my_list.add_first(41)
my_list.add_first(36)

my_list.print()

my_list.reverse_linkedList()
my_list.print()