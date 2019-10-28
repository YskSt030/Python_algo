class BinaryTree:
    def __init__(self, val_):
        self.val = val_
        self.left = None
        self.right = None

    def insert(self,val_):
        if val_ < self.val:
            if self.left == None:
                self.left = BinaryTree(val_)
            else:
                self.left.insert(val_)
        else:
            if self.right == None:
                self.right = BinaryTree(val_)
            else:
                self.right.insert(val_)

    def find(self,tgtval):
        if self.val == tgtval:
            print('found')
        elif self.val > tgtval:
            if self.left == None:
                print('Not found')
            else:
                self.left.find(tgtval)
        else:
            if self.right == None:
                print('Not found')
            else:
                self.right.find(tgtval)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()

    def printTree2(self):
        if self.right:
            self.right.printTree()

        if self.left:
            self.left.printTree()
        print(self.val)

if __name__ == '__main__':
    data = [1,9,3,11,5,6,2]
    tree = BinaryTree(data[0])
    for i in range(1,len(data)):
        tree.insert(data[i])
    print('printTree1')
    tree.printTree()
    print('printTree2')
    tree.printTree2()
    tgt = 6
    print('find '+str(tgt))
    tree.find(tgt)

