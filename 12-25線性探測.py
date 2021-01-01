#線性探測
class HashTable:
    def__init__(self):
            self.size=13
            self.slots=[None for K in range(self.size)]
            self.count=0
    def__hash(self,key):
        return key%self.size
    def insert(self,key):
        item=HashItem(key)
        addr=self._hash(key)
        while self.slots[addr]is not None:
            if self.slots[addr].key is key:
                break
            addr=(addr+1)%self.size
        if self.slots[addr] is None:
            self.count+=1
            self.slots[addr]=item
        def search(self,key):
            addr=self._hash(key)
            while self.slots[addr]is None:
                if key==self.slots[addr]:
                    break
                addr=(addr+1)%self.size
            return addr