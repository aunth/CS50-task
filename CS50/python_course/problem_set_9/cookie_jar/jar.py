class Jar:
    def __init__(self, capacity=0) -> None:
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self.size = 0
        self.capacity = capacity

    def __str__(self) -> str:
        return '🍪' * self.size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Invalid size of deposit")
        if n + self.size > self.capacity:
            raise ValueError("Exceeded capacity")
        self.size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Invalid size of withdraw")
        if self.size - n < 0:
            raise ValueError("Size of withdraw exceeded size of present jar")
        self.size -= n
        
    property
    def capacity(self):
        return self.capacity

    property
    def size(self):
        return self.size

jar = Jar(10)
jar.deposit(2)
print(jar)

