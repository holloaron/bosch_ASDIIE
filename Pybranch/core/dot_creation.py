from Pybranch.core.dot_creator import DotCreator


class DotCreation:
    def __init__(self) -> None:
        self.creation = DotCreator()
        self.dot_number = 60

    def dot_creation(self, wall_sprite, dots_sprite, every_sprite) -> None:
        """
            Create the points here by calling the dot_creator function
        """
        self.creation.dot_creator(self.dot_number, wall_sprite,  dots_sprite, every_sprite)

