from multiprocessing import Process

class Myprocess(Process):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        super().__init__()
        #super(Myprocess, self).__init__()

    def run(self):
        print(self.a, self.b)




if __name__ == '__main__':
    for i in range(10):
        p = Myprocess(1,2)
        p.start()