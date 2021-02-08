class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class Linked_list():
    def __init__(self,):
        self.head = None
        self.tail = None
    
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return None
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        self.tail.next = new_head
        self.tail.next.previous = self.tail
        return None
    def remove(self, value):
        if self.head is None:
            return None
        node = self.head
        while node.next:
            if node.value == value:
                node.next = self.head.next.next
        return node


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return None

        self.tail.next = Node(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return None


ll = Linked_list()
ll.append(10)
ll.append(30)
ll.prepend(400)
ll.append(40)
ll.append(100)
ll.remove(30)
node = ll.tail
while node:
    print(node.value)
    node = node.previous
