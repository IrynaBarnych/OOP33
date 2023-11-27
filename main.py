#Синтаксис Однозв'язковий список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}] -> {self.next}"
node1 = Node(1)
print(node1)
node2 = Node(2)
print(node2)
node3 = Node(3)
node1.next = node2
print(node1)
node1.next = node2
node2.next = node3
print(node1)

#

#Синтаксис Однозв'язковий список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}] -> {self.next}"

node = Node(1)
current_node = node

for i in range(2, 330):
    new_node = Node(i)
    current_node.next = new_node
    current_node = new_node

print(node)

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
my_lst = LinkedList()
my_lst.append(1)
my_lst.append(2)
my_lst.append(3)
my_lst.append(4)
print(my_lst)

#Синтаксис Двозв'язаний список
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.prev} <- [{self.data}] -> {self.next} "

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

my_list = DoublyLinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(10)
#додавання елементу на початок списку
new_node = Node(0)
new_node.next = my_list.head
if my_list.head is not None:
    my_list.head.prev = new_node
my_list.head = new_node
#додавання елементу на другу позицію списку
new_node = Node(4)
current = my_list.head
while current.data != 5:
    current = current.next
if current.next is not None:
    current.next.prev = new_node
current.next = new_node
new_node.prev = current
#виведення списку
current = my_list.head
elements = []
while current:
    elements.append(str(current.data))
    current = current.next
print(" <-> ".join(elements))



