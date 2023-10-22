__all__ = ['Stack', 'Queues']

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def print_items(self):
        for item in self.stack:
            print(item)


class Queues():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)         #new items added at the back

    def dequeue(self):
        item = self.queue[0]
        del self.queue[0]
        return item

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)


class Deque():
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        item = self.deque[0]
        del self.deque[0]
        return item

    def remove_rear(self):
        return self.deque.pop()

    def is_empty(self):
        return self.deque == []

    def size(self):
        return len(self.deque)


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None     


class UnorderedLinkedList():
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        node = self.head
        count = 0
        while(node is not None):
            count = count + 1
            node = node.next
        return count

    def search(self, item):
        node =self.head
        found = False
        while(node is not None):
            if node.data == item:
                found = True
                break
            node = node.next
        return found

    def print_all(self):
        node = self.head
        while(node is not None):
            print(node.data)
            node = node.next
                

    def remove(self, item):
        found = self.search(item)
        if found:
            node = self.head
            while(node is not None):            #for rest of the items
                if node.data == item:
                    if node.next is not None:
                        node.data = node.next.data
                        node.next = node.next.next
                    else:
                        node.data = None
                    break
                node = node.next
        else:
            print("The given value was not found in Linked List")
        
        
