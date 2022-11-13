import threading

from core.key_interaction.key_event import KeyEvent


class KeyListener:
    """
     Keyboard listener class for the keyboard events, usable in remote environments, in a side-thread
    """
    KEY_PRESS_TO_KEY_EVENT = {
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
                if key in self.KEY_PRESS_TO_KEY_EVENT:
                    self.last_key = key
            except:
                pass

    def stop(self) -> None:
        """
        Stop the thread for scanning the keyboard actions
        :return: None
        """
        self.stopped = True
        self.thread.join()

        self.screen.timeout(-1)
        self.screen = None

    def start(self, screen) -> None:
        """
        Starts the thread for scanning the keyboard actions
        :param screen: Screen object.
        :return: None
        """
        self.screen = screen
        self.thread = threading.Thread(target=self.listen, daemon=True)
        self.stopped = False
        self.thread.start()

    def has_happened(self) -> bool:
        """
        Checks that a valid keyboard event has happened.
        :return: return True if it is valid, False otherwise.
        """
        return self.last_key is not None

    def read_last_key_event(self) -> KeyEvent:
        """
        Read the last keyevent from the keyboard
        :return: Returns the last read keyevent.
        """
        if self.last_key is None:
            raise ValueError("KeyBoardListener has not noticed "
                             "any key event that could be read.")
        key_event = self.KEY_PRESS_TO_KEY_EVENT[self.last_key]
        self.last_key = None

        return key_event
