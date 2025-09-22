class MyHashMap:

    def __init__(self):
        self.map_dict = []
        self.keys = set()

        

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.map_dict.append([key,value])
            self.keys.add(key)
        else:
            item = self.findItem(key)
            item[1] = value

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        item = self.findItem(key)
        return item[1]

    def remove(self, key: int) -> None:
        if key in self.keys:
            item = self.findItem(key)
            self.map_dict.remove(item)
            self.keys.remove(key)

    def findItem(self,key):
        for item in self.map_dict:
            if item[0] == key:
                return item

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
