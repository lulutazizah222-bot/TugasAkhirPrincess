# Definisi class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Membuat node
node1 = Node('Andi')
node2 = Node('Budi')
node3 = Node('Citra')

# Menghubungkan node (linked list)
node1.next = node2
node2.next = node3

# Head menunjuk ke node pertama
head = node1

# Traversal / menampilkan isi linked list
while head:
    print(head.data)
    head = head.next