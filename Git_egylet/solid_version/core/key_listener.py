import threading

from bosch_ASDIIE_Git_egylet.Git_egylet.solid_version.core.key_event import KeyEvent


class KeyListener:
    KEYPRESS_TO_KEY_EVENT = {
        "KEY_UP": KeyEvent.UP,
        "KEY_DOWN": KeyEvent.DOWN,
        "KEY_LEFT": KeyEvent.LEFT,
        "KEY_RIGHT": KeyEvent.RIGHT,
    }
    MILLISECONDS = 1000

    def __init__(self):
        self.screen = None
        self.last_key = None
        self.thread = None
        self.stopped = False

    def listen(self):
        self.screen.keypad(True)
        self.screen.timeout(self.MILLISECONDS)

        while not self.stopped:
            try:
                key = self.screen.getkey()
                if key in self.KEYPRESS_TO_KEY_EVENT:
                    self.last_key = key
            except:
                pass