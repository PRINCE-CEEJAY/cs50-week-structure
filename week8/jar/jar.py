class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if self.capacity < 0:
            raise ValueError("capacity must be a non-negative value")

    def __str__(self):
        return self.capacity * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Too much for the jar")
        self.capacity += n

    def withdraw(self, n):
        if n > self.capacity:
            raise ValueError("remaining cookies not up to that amount")
        self.capacity -= n


    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        self.size = 0        
        return self.size + self.capacity
