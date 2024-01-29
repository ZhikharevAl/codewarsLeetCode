class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.queue.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
