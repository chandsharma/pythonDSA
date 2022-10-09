# {"key",value} => dict["key"] = value

class HashMap():
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for letter in key:
            hash += ord(letter)
        return hash%self.MAX

    def add(self,key,val):
        hash = self.get_hash(key)
        self.arr[hash] = val

    def get(self,key):
        hash = self.get_hash(key)
        return self.arr[hash]

    def remove(self,key):
        hash  = self.get_hash(key)
        if self.arr[hash]:
            self.arr[hash] = None

    #Overriding operators to use this as we use dict in python
    # a['key'] = value

    def __setitem__(self,key,value):
        self.add(key,value)

    def __getitem__(self,key):
        return self.get(key)

    def __delitem__(self,key):
        self.remove(key)

if __name__ == '__main__':
    hm = HashMap()
    print(hm.get_hash("march 6"))
    hm.add("march 6",306)
    print(hm.get('march 6'))
    print(hm.arr)
    hm.remove('march 6')
    print(hm.get('march 6'))

    hm["march 6"] =3066
    hm["march 7"] =30662
    hm["march 8"] =30
    hm["march 9"] =3
    print(hm.arr)
    print(hm["march 7"])
    del hm['march 8']
    print(hm.arr)