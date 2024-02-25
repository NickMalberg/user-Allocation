"""
Queue implemntation to use FiFo 
"""

from icecream import ic


class un_Queue:
    """
    Uses for Queue of employees.
    Must prove max_size of the queue.
    """

    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def is_full(self):
        return len(self.queue) == self.max_size

    def push(self, item):
        if not self.is_full():
            self.queue.append(item)
        else:
            print("queue is full")

    def pop(self):
        if not self.is_empty():
            return self.queue.pop()
        else:
            print("queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


def main():
    test = Queue(5)
    for i in range(6):
        ic(test.push(i))


if __name__ == "__main__":
    main()
