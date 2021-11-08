from datetime import datetime

def mayuscula(func):
    def wrapper(string):
        return func(string).upper()
    return wrapper


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Function elapsed time '+ str(time_elapsed.total_seconds()) + ' seconds')
    return wrapper


def run():
    # @mayuscula
    # def mensaje(name):
    #     return f'{name}, you got a message'
    
    # print(mensaje('Juan'))
    
    @execution_time    
    def random_func():
        for _ in range (1, 1000000000):
            pass
    
    # random_func()

    @execution_time
    def sum(a: int, b: int) -> int:
        return a + b

    sum(2 , 3)

if __name__ == '__main__':
    run()