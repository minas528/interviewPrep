from threading import Lock
from threading import Semaphore
class H2O:
    def __init__(self):
        self.h_lock = Semaphore(2)  # h_lock can be acquired twice
        self.o_lock = Lock()
        self.o_lock.acquire()
        self.h_count = 0


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        self.h_lock.acquire()    
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h_count += 1
        if self.h_count % 2 == 0:
            self.o_lock.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_lock.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        # Reset h_lock semaphore
        self.h_lock.release()
        self.h_lock.release()