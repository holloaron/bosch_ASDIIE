from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.canvas import Canvas
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.visualizable import Visualizable
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent


class Walls(GameElement, Visualizable):

    def __init__(self):
        pass

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        pass

    def draw(self, canvas: Canvas) -> None:
        pass
