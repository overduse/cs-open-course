"""
File: jar.py
Description:
    Defining a class `Jar` that simulates a jar or container which can hold items.

"""


class Jar:
    def __init__(self, capacity=12):
        self.size = 0
        self.capacity = capacity

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError


    def withdraw(self, n):
        if n<= self.size:
            self.size -= n
        else:
            raise ValueError


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity>=0:
            self._capacity = capacity
        else:
            raise ValueError

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


    def __str__(self):
        return self.size * '🍪'

def main():
    jar = Jar(3)
    jar.deposit(2)
    print(jar.size)
    print(jar)


if __name__ == '__main__':
    main()
