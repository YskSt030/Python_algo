class Eggs:
    def __init__(self,N,ANSWER):
        self.ANSWER = ANSWER
        self.TOP = N
        self.BOTTOM = 0
        self.count = 0
        self.numofEggs = 3
    def drop(self,num):
        if num <= self.ANSWER:
            return True
        else:
            return False
    def findthefloor(self):
        while self.TOP >= self.BOTTOM:
            #print((self.TOP+self.BOTTOM) // 2)
            if self.drop((self.TOP+self.BOTTOM) // 2) == True:
                self.BOTTOM = (self.TOP+self.BOTTOM) // 2
            else:
                self.TOP = (self.TOP + self.BOTTOM) // 2
                self.count += 1
                if self.count >= self.numofEggs:
                    break
        return self.BOTTOM


if __name__ == '__main__':
    egg = Eggs(200,125)
    answer = egg.findthefloor()
    print (answer)
    print (egg.count)