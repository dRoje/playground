from dataclasses import dataclass
from typing import List


@dataclass
class Element:
    key: str
    value: int

    def __repr__(self):
        return f"{self.key} -> {self.value}"


class HashTable:
    def __init__(self, size: int):
        self.table: List[List[Element]] = [[] for _ in range(size)]
        self.size = size

    def __repr__(self):
        retval = ""
        for i, row in enumerate(self.table):
            retval += f"[{i}]: {row}\n"

        return retval

    def _hash(self, element: str) -> int:
        """Hashing algorithm."""
        sum_ = 0
        for char in element:
            sum_ += ord(char)  # ascii value

        return sum_ % self.size

    def update(self, key, value):
        index = self._hash(key)

        # update existing
        for el in self.table[index]:
            if el.key == key:
                el.value = value
                return

        # add new
        self.table[index].append(Element(key=key, value=value))

    def get(self, key):
        index = self._hash(key)
        for el in self.table[index]:
            if el.key == key:
                return el.value

    def delete(self, key):
        index = self._hash(key)
        for i, el in enumerate(self.table[index]):
            if el.key == key:
                self.table[index].pop(i)
