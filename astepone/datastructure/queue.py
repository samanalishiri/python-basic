import heapq


# Saman Alishiri samanalishiri@gmail.com


class PriorityQueue:
    def __init__(self):
        self.__queue = []
        self.__index = 0

    def push(self, item, priority):
        heapq.heappush(self.__queue, (-priority, self.__index, item))
        self.__index += 1
        return self

    def pop(self):
        return heapq.heappop(self.__queue)[-1]

    def empty(self):
        return len(self.__queue) < 1

    def print(self):
        for n in self.__queue:
            print(n[-1], end=' ')

    def nlargest(self, n):
        return heapq.nlargest(n, self.__queue)

    def nsmallest(self, n):
        return heapq.nsmallest(n, self.__queue)