import time
import threading

class TimeCounter(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(TimeCounter, self).__init__(*args,**kwargs)
        self._flag = threading.Event()  #flag to pause the thread
        self._flag.set() #Set true
        self._running = threading.Event() #stop thread identification
        self._running.set() #set running to True
        self._seconds_passed = 0 #value to track passed seconds


    def run(self):
        while self._running.isSet():
            self._flag.wait()
            self._seconds_passed = self._seconds_passed + 1
            time.sleep(1)

    def pause(self):
        self._flag.clear() #Set the flag false -> block the thread

    def resume(self):
        self._flag.set() #stop blocking of the thread