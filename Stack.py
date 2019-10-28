class Stack:
    def __init__(self):
        self.datas = []

    def add(self,num):
        if num not in self.datas:
            self.datas.append(num)
            return True
        else:
            return False

    def peek(self):
        print(self.datas[-1])

    def remove(self):
        if len(self.datas)<=0:
            return ("NONE")
        else:
            return self.datas.pop()


if __name__ == '__main__':
    datas = [1,2,3,6,5,4]
    stack = Stack()
    for i in range(len(datas)):
        stack.add(datas[i])
    stack.peek()
    stack.remove()
    stack.peek()