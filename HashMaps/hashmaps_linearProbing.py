#hashMap implementation and collision handeling using Linear Probing

class HashMap():
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for letter in key:
            hash += ord(letter)
        return hash%self.MAX

    def __setitem__ (self,key,data):
        hash = self.get_hash(key)
        print(hash)
        if not self.arr[hash] or self.arr[hash][0] == key:
            self.arr[hash] = (key,data)
            return
        for index in list(range(hash+1,self.MAX-1))+list(range(0,hash)):
            if not self.arr[index]:
                self.arr[index] = (key,data)
                return
        raise Exception("Overflow")

    def __getitem__ (self,key):
        hash = self.get_hash(key)
        print(hash)
        if self.arr[hash] and self.arr[hash][0] == key:
            return self.arr[hash][1]
        for index in list(range(hash+1,self.MAX-1))+list(range(0,hash)):
            if self.arr[index] and self.arr[index][0] == key:
                return self.arr[index][1]
        raise Exception("Key Not Found")

    def __delitem__ (self,key):
        hash = self.get_hash(key)
        print(hash)
        if self.arr[hash] and self.arr[hash][0] == key:
            self.arr[hash] = None
            return
        for index in list(range(hash+1,self.MAX-1))+list(range(0,hash)):
            if self.arr[index] and self.arr[index][0] == key:
                self.arr[index] = None
                return
        raise Exception("Key Not Found")

    def size (self):
        return len(self.arr)

hash_map = HashMap()
hash_map['chandan'] = 121
hash_map['sunandan'] = 122
hash_map['ansu'] = 123
hash_map['ritesh'] = 124
print(hash_map.arr)