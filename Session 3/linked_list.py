class Node:
    def __init__(self, data=None):
        self.element = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.__counter = 0

    def append(self, data):
        if self.head.element is None:
            self.head.element = data
        else:
            n = Node(data)
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = n
        self.__counter = self.__counter + 1

    def appendleft(self, data):
        if self.head.element is None:
            self.head.element = data
        else:
            n = Node(data)
            current = self.head
            self.head = n
            n.next = current
        self.__counter = self.__counter + 1

    def len(self):
        return self.__counter

    def insert(self, data, index):
        if index < self.len():
            if index == 0:
                self.appendleft(data)
            else:
                current = self.head
                for i in range(0, index - 1):
                    current = current.next
                n = Node(data)
                n.next = current.next
                current.next = n
                self.__counter = self.__counter + 1

        elif index == self.len():
            self.append(data)

        else:
            print("Index doesn't exist")

    def pop(self):
        if self.head.element is None:
            r = "Linked List is Empty!"
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            r = current.next.element
            current.next.element = None
            current.next = None
            self.__counter = self.__counter - 1
        return r

    def popleft(self):
        if self.head.element is None:
            r = "Linked List is Empty!"
        else:
            current = self.head
            r = current.element
            self.head = current.next
            current.element = None
            current.next = None
            self.__counter = self.__counter - 1
        return r

    def display(self):
        current = self.head
        r = [current.element]
        while current.next is not None:
            current = current.next
            r.append(current.element)
        return f"LinkedList({r})"


if __name__ == "__main__":
    linked_list = LinkedList()  # initializing LinkedList class object
    linked_list.append(2)  # Adding data on the end of the linked list
    linked_list.append(3)
    linked_list.append(8)
    linked_list.append(9)
    print(f"Data added on the end: {linked_list.display()}\n")  # LinkedList([2, 3, 8, 9])

    linked_list.appendleft(10)
    linked_list.appendleft(12)
    print(f"Data added on the front: {linked_list.display()}\n")  # LinkedList([12, 10, 2, 3, 8, 9])

    print(linked_list.pop())  # 9
    print(linked_list.pop())  # 8
    print(linked_list.popleft())  # 12

    print(f"\nData after popping: {linked_list.display()}\n")  # LinkedList([10, 2, 3])

    linked_list.insert(10, 4)  # Error: Index doesn't exist
    linked_list.insert(14, 3)  # perform functionality of appendleft() function as 3 is the last index
    linked_list.insert(16, 2)  # Value will be added at index = 2

    print(f"\nData after insertion: {linked_list.display()}\n")  # LinkedList([10, 2, 16, 3, 14])

    print(f"Length of Linked List: {linked_list.len()}")  # 5
