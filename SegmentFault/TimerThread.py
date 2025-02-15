"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : TimerThread.py
/ AUTHOR       : Pál Juhász
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Timer module to measure and handle time while the program is running

/*********************************************************************
/*********************************************************************
"""
import time
import threading

class TimeCounter(threading.Thread):
    """ inherits from python thread class
    
    @args:
        threading.Thread
    """
    def __init__(self, *args, **kwargs):
        """ Inits the timer variables
        
        @args:
            self,
            *args [] - 
            **kwargs [] -
        """
        super(TimeCounter, self).__init__(*args, **kwargs)
        self._flag = threading.Event()  # flag to pause the thread
        self._flag.set()  # Set true
        self._running = threading.Event()  # stop thread identification
        self._running.set()  # set running to True
        self._seconds_passed = 0  # value to track passed seconds


    def run(self):
        """ Starts the Timer Thread, increase the value of _seconds_passed by 1 in each iteration (-> 1s passed)
        
        @args:
            self
        """
        while self._running.isSet():
            self._flag.wait()
            self._seconds_passed = self._seconds_passed + 1
            time.sleep(1)


    def pause(self):
        """ Pauses the timer by blocking the Thread
        
        @args:
            self
        """
        self._flag.clear()  # Set the flag false -> block the thread


    def resume(self):
        """ Resumes the timer by stop blocking  the Thread
        
        @args:
            self
        """
        self._flag.set()  # stop blocking of the thread


    def stop(self):
        """ Stops the timer

        @args:
            self
        """

        self._flag.set()  # Resume the thread from the suspended state, it is already suspended
        self._running.clear()  # Set false -> block the thread


    def reset(self):
        """ Resets the _seconds_passed variable

        @args:
            self
        """
        self._seconds_passed = 0


    @property
    def seconds_passed(self):
        return self._seconds_passed
