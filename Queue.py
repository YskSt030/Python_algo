class Queue:
    def __init__(self):
        self.datas = []

    def add(self,num):
        if num not in self.datas:
            self.datas.append(num)
            return True
        else:
            return False
    def remove(self):
        if len(self.datas)<=0:
            return ("NONE")
        else:
            del self.datas[0]
            return self.datas
    def peek(self):
        print(self.datas[-1])


if __name__ == '__main__':
    datas = [1,2,3,6,5,4]
    q = Queue()
    for i in range(len(datas)):
        q.add(datas[i])
    q.peek()
    q.remove()
    q.peek()