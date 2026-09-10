class MyHashMap:

    def __init__(self):
        self.memo = [None] * (1000000 + 1)

    def put(self, key: int, value: int) -> None:
        self.memo[key] = value

    def get(self, key: int) -> int:
        if self.memo[key] != None:
            return self.memo[key]
        return -1

    def remove(self, key: int) -> None:
        self.memo[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)