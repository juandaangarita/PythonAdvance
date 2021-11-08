import time

class FiboIter():
    
    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self        

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        elif not self.max or self.counter <= self.max:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
        else:
            raise StopIteration


def run():
    a = int(input('Enter a number: ') or 0)
    fibonnacci = FiboIter(a)
    for element in fibonnacci:
        print(element)
        time.sleep(0.05)

if __name__ == '__main__':
    run()