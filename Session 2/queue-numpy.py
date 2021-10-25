# Queue Implementation using Numpy
import numpy as np

class queue:
    def __init__(self, size):
        self.size = size
        self.elements = np.zeros([self.size], dtype='int8')
        self.clear()

    def enqueue(self, data):
        if self.isFull():
            print("Queue Overflow!")
        else:
            self.rear = self.rear + 1
            if self.front == -1:
                self.front = 0;
            self.elements[self.rear] = data

    def dequeue(self):
        if self.isEmpty():
            return "Queue Underflow!"
        else:
            val = self.elements[self.front]
            self.front = self.front + 1
            return val

    def isEmpty(self):
        return ((self.front == -1 or self.rear == -1) or (self.front > self.rear))

    def isFull(self):
        return (self.rear == self.size - 1)

    def frontV(self):
        return self.elements[self.front]

    def rearV(self):
        return self.elements[self.rear]

    def clear(self):
        self.rear = -1
        self.front = -1


q = queue(3)
q.enqueue(5)
q.enqueue(6)
q.enqueue(8)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())