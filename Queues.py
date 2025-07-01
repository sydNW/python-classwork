class CircularQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * CircularQueue.DEFAULT_CAPACITY

        self._size = 0

        self._front = 0

    # def __len__(self):
    #     return self._size

    def is_Empty(self):

        return self._size == 0

    def first(self):

        if self.is_Empty():
            raise Empty("The queue is empty") # call the class that we created to call an exemption
        return self._data[self._front] # the '_data' means it is sensitive and should not be tampered with

    def dequeue(self):

        if self.is_Empty():
            raise Empty("The queue is empty for dequeue operation")

        front = (self._front + 1) % len(self._data)

        dequeued_element = self._data[self._front]

        self._data[self._front] = None #garbage collection

        self._size -= 1

        return dequeued_element

    def enqueue(self, element):

        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        tail = (self._front + self._size) % len(self._data) #getting the position where to insert the element. We only insert at the end/ at the tail

        self._data[tail] = element

        self._size += 1

    def _resize(self, new_capacity):
        ...

class Empty(Exception):
    pass

if __name__ == "__main__":
    object_queue = CircularQueue()

    insert_elements = [11,22,33,44,55]

    for elements in insert_elements:
        object_queue.enqueue(elements)

        print(f"Added Element: {elements}")
        print(f"The new size of the queue: {object_queue._size}")

    # print("\n current queue representation: ")