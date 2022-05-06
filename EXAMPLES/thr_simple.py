#!/usr/bin/env python

from threading import Thread, Lock
import random
import time

stdout_lock = Lock()

my_stuff =[]

class SimpleThread(Thread):
    def __init__(self, num):
        super().__init__()  # <1>
        self._threadnum = num

    def run(self):  # <2>
        time.sleep(random.randint(1, 3))
        with stdout_lock:
            print("Hello from thread {}".format(self._threadnum))
        self.result = self._threadnum * 100

for i in range(10):
    t = SimpleThread(i)  # <3>
    t.start()  # <4>

print("Done.")
