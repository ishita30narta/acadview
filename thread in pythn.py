#1
'''import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        #time.sleep(5)
        print("Value send",self.h)

thread1 =mythread(1)
thread1.start()
thread2 =mythread(2)
time.sleep(5)
thread2.start()

#2
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        time.sleep(10)
        print("No is ",self.h)

for i in range(10):
    thread1 =mythread(i)
    thread1.start()
    time.sleep(1)

print("Active threads are",threading.activeCount())

#3
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):


#4
import threading
from threading import Thread
import time
def sleepMe(i):
    print("Thread %s going to sleep for 5 seconds",%i)
    time.sleep(5)
    print("Thread %s is awake now"%i)
for i in range(10):
    th=Thread(target=sleepMe, args=(i, ))'''