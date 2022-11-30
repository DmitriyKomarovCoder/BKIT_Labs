from contextlib import contextmanager
from time import perf_counter, sleep, time

class cm_timer2():
    def __init__(self):
        self.start = 0
        self.end = 0
    
    def __enter__(self):
        self.start = time()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        print(f'time: {self.end-self.start:0.4f}')


@contextmanager
def cm_timer_1():
    start = time()
    yield
    end = time()
    print(f'time: {end-start:0.4f}')

def main():
    with cm_timer_1():
        sleep(5.5)

    with cm_timer2():
        sleep(5.5)
        
if __name__ == '__main__':
    main()