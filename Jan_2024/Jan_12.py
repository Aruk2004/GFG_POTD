# Reverse First K elements of Queue

class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0


class Solution:
    def modifyQueue(self, q, k):
        stack = []

        # Dequeue the first k elements and push them onto a stack
        for i in range(k):
            stack.append(q.front())
            q.dequeue()

        # Pop the elements from the stack and enqueue them back into the queue
        while stack:
            q.enqueue(stack.pop())

        # Dequeue the remaining elements and enqueue them back into the queue
        size = q.size()
        for i in range(size - k):
            q.enqueue(q.front())
            q.dequeue()

        return q

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    q = SimpleQueue()
    elements = [1, 2, 3, 4, 5]

    for element in elements:
        q.enqueue(element)

    k = 3
    modified_queue = sol.modifyQueue(q, k)

    # Print the modified queue elements
    while not modified_queue.is_empty():
        print(modified_queue.front(), end=" ")
        modified_queue.dequeue()

