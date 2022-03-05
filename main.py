import random
import timeit
class BSTree:
    def __init__(self):
        self.RB = None
        self.LB = None
        self.value = None
        self.parent = None
        self.lMost = None
    def genList(self, length):
        sortList = list(range(0, length))
        for i in range(length):
            rand = random.randint(0, length - 1)
            sortList[i], sortList[rand] = sortList[rand], sortList[i]
        return sortList
    def insert(self, int, root):
        if self.value == None:
            self.value = int
        elif self.RB == None and self.LB == None:
            if self.value < int:
                nNode = BSTree()
                nNode.insert(int, self)
                self.RB = nNode
            else:
                nNode = BSTree()
                nNode.insert(int, self)
                self.LB = nNode
        elif self.LB == None:
            if self.value < int:
                self.RB.insert(int, None)
            else:
                nNode = BSTree()
                nNode.insert(int, self)
                self.LB = nNode
        elif self.RB == None:
            if self.value < int:
                nNode = BSTree()
                nNode.insert(int, self)
                self.RB = nNode
            else:
                self.LB.insert(int, None)
        else:
            if self.value < int:
                self.RB.insert(int, None)
            else:
                self.LB.insert(int, None)
        if root != None:
            self.parent = root
    def MakeRandTree(self, length):
        array = self.genList(length)

        self.bTree(array)
    def bTree(self, Array):
        for val in Array:
            self.insert(val, None)
    def ioTraversal(self):
        if self.LB != None:
            self.LB.ioTraversal(int)
        print(self.value)
        if self.RB != None:
            self.RB.ioTraversal(int)
    def Search(self, int):
        integer = None
        if self.LB != None:
            integer = self.LB.Search(int)
        if self.value == int:
            return self.value
        if self.RB != None and integer == None:
            integer = self.RB.Search(int)
        return integer
def arList(array, int):
    for i in array:
        if i == int:
            return i
hello = BSTree()
print(hello.MakeRandTree(10000))
def bstSearch():
    hello.Search(10000)
def search():
    sortList = list(range(0, 10000))
    arList(sortList, 10000)
print("Sequential Array")
print(timeit.timeit(search, number=1000))
print("Binary Search Tree")
print(timeit.timeit(bstSearch, number=1000))






