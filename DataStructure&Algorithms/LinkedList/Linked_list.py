# Linked list does not have indexes in memory
# Linked list, all the next are served in different places in memory
# It has a Head and a Tail

## Adding a new node to the end of the linked list = O(1)
## Removing the last node of the linked list = O(n)
## Adding a new node to the front of the list = O(1)
## Removing a node from the front of the list = O(1)
## Adding a node in the middle of the list = O(n)
## Removing a node from the middle of the list = O(n)
## Looked by Value for an exact node in the list = O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    # This is a constructor and gonna create a new node
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    #  This creates a new node and adds it to the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # This creates a new node and adds it to the beginning
    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        pre = self.head
        temp = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        temp = self.head.next
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return temp

    # This creates a new node and adds it to the specified index
    def insert(self, index, data):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(data)
        if index == self.length:
            return self.append(data)
        else:
            new_node = Node(data)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        else:
            prev = self.get(index - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



linked_list = Linkedlist(4)
linked_list.append(5)
linked_list.append(6)
linked_list.print_list()
print(f"This is the head: {linked_list.head.value}")
print(f"This is the tails: {linked_list.tail.value}")

# 3 Items - returns 3 Node
print(linked_list.pop())
# 2 Items - returns 2 Node
print(linked_list.pop())
# 1 Items - returns 1 Node
print(linked_list.pop())
# 0 Items - returns None
print(linked_list.pop())

head= {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value":23,
            "next": {
                "value":7,
                "next": {
                    "value":4,
                    "next": None
                }
            }
        }
    }
}

print(head['next']['next']['value'])
#print(my_linked_list.head.next.next.value)