class EvenNumbers:
    """This class implements an iterator of all of the even numbers, or the even numbers untyl a maximum
    """

    def __init__(self, init=0, max=None):
        self.init = init
        self.max = max

    def __iter__(self):
        if self.init % 2 == 0:
            self.num = self.init
        else:
            self.num = self.init + 1
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration

def run():
    low_limit = int(input('Enter low limit: ') or 0)
    upper_limit = int(input('Enter upper limit: '))
    even_numbers = EvenNumbers(low_limit, upper_limit)
    for element in even_numbers:
        print(element)


if __name__ == '__main__':
    run()