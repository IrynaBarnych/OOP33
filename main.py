#Синтаксис Однозв'язковий список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}] -> {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return f"{self.head}"

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node #новий елемент стає початком
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next #переміщуємося до наступного елементу
        last_node.next = new_node

    def replace(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                print(f"Значення {old_data} замінено на {new_data}")
                return
            current = current.next
        print(f"Значення {old_data} не знайдено у списку")

my_lst = LinkedList()
nums = input("Введіть усі числа через пробіл ").split()
for num in nums:
    my_lst.append(int(num))
print(my_lst)
#сюди пункти меню
#Замінити значення у списку
old_value = int(input("Введіть значення, яке треба замінити: "))
new_value = int(input("Введіть значення, на яке замінити: "))
my_lst.replace(old_value, new_value)
print(my_lst)
