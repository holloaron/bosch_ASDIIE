from map import Map
from pac_man import PacMan
from position_comparison import PositionComparison
from visualizer import Visualizer


class GameRunner:
    def __init__(self, agent: PacMan, world: Map, eval_situation: PositionComparison, visualizer: Visualizer,
                 max_step_num: int = 100):
        """
        Runs the game
        :param agent: Agent that interacts the game
        :param world: The environment where the game takes place
        :param eval_situation: Evaluates the current state of the game
        :param visualizer: Visualize the game to the user
        :param max_step_num: Maximum number of possible interactions (int)
        """
        self.agent = agent
        self.world = world
        self.eval_situation = eval_situation
        self.visualizer = visualizer

        self.score = 0
        self.step_num = 0
        self.max_step_num = max_step_num

    def run(self):
        """
        Runs the game
        :return: -
        """
        done = False
        self.visualizer.render(self.world.map, self.score)

        while not done:
            action = input("Select your next action (w, a, s, d): ")

            # Processing current input and evaluating the situation
            pacman_x, pacman_y = self.agent.process_action(action)
            wall, dot = self.eval_situation.check_collision(self.world.map, pacman_x, pacman_y)

            # Increasing the score or terminating the game according to the situation
            if dot:
                self.score += 1
            if wall or (self.step_num > self.max_step_num):
                done = True

            # Updating the map and visualizing the current state
            self.world.update_map(pacman_x, pacman_y)
            self.visualizer.render(self.world.map, self.score)


def main():
    game_runner = GameRunner(agent=PacMan(x=6, y=6),
                             world=Map("map.txt"),
                             eval_situation=PositionComparison(),
                             visualizer=Visualizer(),
                             max_step_num=100)

    game_runner.run()


if __name__ == "__main__":
    main()
