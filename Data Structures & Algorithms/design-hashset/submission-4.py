class MyHashSet:

    def __init__(self):
        self.memo = 0

    def add(self, key: int) -> None:
        self.memo = self.memo | (1 << key)

    def remove(self, key: int) -> None:
        if (self.memo >> key & 1) != 0:
            temp = (1 << key)
            self.memo = self.memo ^ temp

    def contains(self, key: int) -> bool:
        return (self.memo & (1 << key)) != 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)