from threading import Semaphore, Thread
from typing import Callable

class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooSemaphore = Semaphore(1)
        self.barSemaphore = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.fooSemaphore.acquire()
            printFoo()
            self.barSemaphore.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.barSemaphore.acquire()
            printBar()
            self.fooSemaphore.release()

def printbar():
    print("bar", end='')

def printfoo():
    print("foo", end='')

if __name__ == "__main__":
    n = 4
    fooBar = FooBar(n)

    fooThread = Thread(target=fooBar.foo, args=(printfoo,))
    barThread = Thread(target=fooBar.bar, args=(printbar,))

    fooThread.start()
    barThread.start()

    fooThread.join()
    barThread.join()

