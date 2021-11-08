import time

def fibo_gene(max_counter=None):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        elif not max_counter or counter <= max_counter:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux
        else:
            break


def run():
    fibonacci = fibo_gene(6)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)


if __name__ == '__main__':
    run()