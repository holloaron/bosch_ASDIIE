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

"""
//*********************************************************************
//*********************************************************************
                            INCLUDES                              
//*********************************************************************
//*********************************************************************
"""

import time
import threading

"""

    TimeCounter class
    inherits from python thread class
    @params threading.Thread

"""


class TimeCounter(threading.Thread):
    """
        Timer Init
        Inits the timer variables
        @params self, *args **kwargs

    """

    def __init__(self, *args, **kwargs):
        super(TimeCounter, self).__init__(*args, **kwargs)
        self._flag = threading.Event()  # flag to pause the thread
        self._flag.set()  # Set true
        self._running = threading.Event()  # stop thread identification
        self._running.set()  # set running to True
        self._seconds_passed = 0  # value to track passed seconds

    """

        run method
        Starts the Timer Thread, increase the value of _seconds_passed by 1 in each iteration (-> 1s passed)
        @params self

    """

    def run(self):
        while self._running.isSet():
            self._flag.wait()
            self._seconds_passed = self._seconds_passed + 1
            time.sleep(1)

    """

        pause method
        Pauses the timer by blocking the Thread 
        @params self

    """

    def pause(self):
        self._flag.clear()  # Set the flag false -> block the thread

    """

        resume method
        Resumes the timer by stop blocking  the Thread 
        @params self

    """

    def resume(self):
        self._flag.set()  # stop blocking of the thread

    """

        stop method
        Stops the timer 
        @params self

    """

    def stop(self):
        self._flag.set()  # Resume the thread from the suspended state, it is already suspended
        self._running.clear()  # Set false -> block the thread

    """

        reset method
        Resets the _seconds_passed variable
        @params self

    """

    def reset(self):
        self._seconds_passed = 0
