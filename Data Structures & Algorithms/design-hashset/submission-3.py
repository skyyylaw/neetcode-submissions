class MyHashSet:

    def __init__(self):
        self.memo = [False] * (1000000 + 1)

    def add(self, key: int) -> None:
        self.memo[key] = True

    def remove(self, key: int) -> None:
        self.memo[key] = False

    def contains(self, key: int) -> bool:
        return self.memo[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)