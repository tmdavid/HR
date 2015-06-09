__author__ = 'User'

class bucket:
    bucketarray = []
    nitems = 0
    def __init__(self):
        self.bucketarray = []
        self.nitems = len(self.bucketarray)
    def additem(self, value):
        self.bucketarray.append(value)
    def contains(self, value):
        if self.bucketarray.__contains__(value): return True
        else: return False


class hashtable:
    nbuckets = 0
    table = []
    def __init__(self, nbuck):
        self.nbuckets=nbuck
        for i in range (self.nbuckets):
            b = bucket()
            self.table.append(b)
    def hashfunction(self,value):
        return value%self.nbuckets

    def addvalue(self, value):
        key = self.hashfunction(value)
        self.table[key].additem(value)
        return True
    def getvalue(self, value):
        key = self.hashfunction(value)
        if self.table[key].contains(value): return value
        else: return False



hasht = hashtable(9) #here you define 9 buckets

for i in range (96):
    hasht.addvalue(i)

print hasht.getvalue(97)
print hasht.getvalue(2)

for bucket in hasht.table:
    print bucket.bucketarray
