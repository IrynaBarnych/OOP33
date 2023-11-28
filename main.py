# Завдання 2
# Користувач вводить з клавіатури набір рядків. Збережіть отримані рядки до двозв’язного списку. Після чого
# покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.
# Дія виконується залежно від вибору користувача,
# після чого меню з’являється знову.


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f"[{self.data}] <->"

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += f" {current.data} <->"
            current = current.next
        return result + " None"

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            new_node.prev = last_node
            last_node.next = new_node

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                print(f"Значення {data} видалено")
                return
            current = current.next
        print(f"Значення {data} не знайдено у списку")

    def contains(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

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
nums = input("Введіть усі числа через пробіл: ").split()
for num in nums:
    my_lst.append(int(num))
print(my_lst)

while True:
    print("\nМеню:")
    print("1. Додати елемент до списку.")
    print("2. Видалити елемент зі списку.")
    print("3. Показати вміст списку.")
    print("4. Перевірити, чи є значення у списку.")
    print("5. Замінити значення у списку.")
    print("6. Вийти")

    choice = int(input("Оберіть опцію: "))

    if choice == 1:
        element = int(input("Додайте елемент до списку: "))
        my_lst.append(element)
    elif choice == 2:
        element = int(input("Видаліть елемент зі списку: "))
        my_lst.remove(element)
    elif choice == 3:
        print("Показати вміст списку:")
        print(my_lst)
    elif choice == 4:
        number = int(input("Чи є значення у списку: "))
        if my_lst.contains(number):
            print(f"Значення {number} знаходиться у списку.")
        else:
            print(f"Значення {number} не знайдено у списку.")
    elif choice == 5:
        old_value = int(input("Введіть значення, яке треба замінити: "))
        new_value = int(input("Введіть значення, на яке замінити: "))
        my_lst.replace(old_value, new_value)
    elif choice == 6:
        print("До побачення!")
        break
    else:
        print("Неправильний вибір. Оберіть опцію від 1 до 6.")
