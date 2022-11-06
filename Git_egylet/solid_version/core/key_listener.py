import threading

from bosch_ASDIIE_Git_egylet.Git_egylet.solid_version.core.key_event import KeyEvent


class KeyListener:
    def __init__(self):
        self.screen = None
        self.last_key = None
        self.thread = None
        self.stopped = False