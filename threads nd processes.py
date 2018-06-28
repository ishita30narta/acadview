#1
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(5)
        print("Thread is awake now")

thread1 = mythread()
thread1.start()


#2
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        time.sleep(6)
        print("No is ",self.h)

for i in range(1,11):
    thread1 =mythread(i)
    thread1.start()
    time.sleep(1)

#3
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        a = (6,8,10,12,14)
        for i in range(5):
           time.sleep(a[i])
           print(self.h[i])


thread1 = mythread(["Ishita","Prachi","Shivangi","Akanksha","Sayima"])
thread1.start()

#4
import threading
from threading import Thread
import time,math
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
         time.sleep(20)
         print(math.factorial(self.h))

thread1 = mythread(4)
thread1.start()




