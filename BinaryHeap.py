"""
This is my first trial of implemantation of binary heap
class BinaryHeap:
    def __init__(self, val_):
        self.parent = None
        self.root = Node(val_)
        self.right = None
        self.left = None

    def insert(self,val_):
        if self.root.left is None:
            if self.root.val < val_:
                self.left = Node(self.val)
                self.val = val_
            else:
                self.left = Node(val_)


    def swap(self,heap_):
        if heap_.parent.val > heap_.val:
            temp = heap_.parent.val
            heap_.parent.val = heap_.val
            heap_.val = temp


    def printHeap(self):
        print('val:' + str(self.val) + ',layer:' + str(self.layer))
        if self.left:
            self.left.printHeap()
        if self.right:
            self.right.printHeap()
    def printHeap2(self):

        if self.left:
            self.left.printHeap()

        if self.right:
            self.right.printHeap()
        else:
            print('val:' + str(self.val) + ',layer:' + str(self.layer))

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


"""
And this is the example quote:
http://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html
"""
class BinHeap:
    def __init__(self):
        self.heapList = [-99]#Insert num to the list in the Heap inveriane order
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0: # i // 2 ... see the parent
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,num):
        self.heapList.append(num)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i) ##return index not value
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    def printHeap(self):
        print(self.heapList)

if __name__ == '__main__':
    data = [1,9,3,11,5,6,2]
    heap = BinHeap()
    for i in range(len(data)):
        heap.insert(data[i])
    print('printTree1')
    heap.printHeap()


