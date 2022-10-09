#often is the chance of getting same hash for two diffrent keys
#from our hash function

#here is approach to eliminate the risk of unwanted overiding of old data 
#we will use list which stores key,value pairs 

class HashMap():
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for letter in key:
            hash += ord(letter)
        return hash%self.MAX

    def __setitem__(self,key,value):
        hash = self.get_hash(key)
        for index,element in enumerate(self.arr[hash]):
            if element[0] == key:
                self.arr[hash][index] = (key,value)
                return
        self.arr[hash].append((key,value))

    def __getitem__(self,key):
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]
        return None

    def __delitem__(self,key):
        hash = self.get_hash(key)
        for index,element in enumerate(self.arr[hash]):
            if element[0] == key:
                del self.arr[hash][index]
                return

if __name__ == '__main__':
    hm = HashMap()
    hm['march 6']  = 12
    hm['march 17']  = 123
    hm['march 8']  = 124
    hm['march 9']  = 125
    print(hm.arr)
    # print(hm['march 6'])
    # print(hm['march 17'])
    # print(hm['march 8'])
    # print(hm['march 9'])
    del hm['march 6']
    del hm['march 17']
    del hm['march 6']
    print(hm.arr)