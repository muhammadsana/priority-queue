import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        if self._queue:
            return heapq.heappop(self._queue)[-1]
        raise IndexError("pop from an empty priority queue")

    def peek(self):
        if self._queue:
            return self._queue[0][-1]
        raise IndexError("peek from an empty priority queue")

    def is_empty(self):
        return not bool(self._queue)

    def size(self):
        return len(self._queue)
