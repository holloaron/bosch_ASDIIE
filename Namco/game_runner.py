from map import Map
from pac_man import PacMan
from visualizer import Visualizer


class GameRunner:
    def __init__(self, agent: PacMan, world: Map, visualizer: Visualizer, max_step_num: int = 100):
        """
        Runs the game
        :param agent: Agent that interacts the game
        :param world: The environment where the game takes place
        :param visualizer: Visualize the game to the user
        :param max_step_num: Maximum number of possible interactions (int)
        """
        self.agent = agent
        self.world = world
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
        self.agent.generate_init_pos(self.world.map, self.world.map_size, self.world.restricted_slot)
        self.world.update_map(self.agent.position, done)
        self.visualizer.render(self.world.map, self.score, done)

        while not done:
            done = self._step(done)

    def _step(self, done):
        """
        Steps the environment
        :param done: Whether the running should be terminated or not
        :return: Game terminating flag (bool)
        """
        action = input("Select your next action (w, a, s, d): ")

        # Processing current input and evaluating the situation
        self.agent.process_action(action)
        dot_hit, wall_hit = self.world.check_interaction(self.agent.position)

        # Increasing the step number
        self.step_num += 1

        # Terminating the game or increasing the score according to the situation
        if dot_hit:
            self.score += 1
        if wall_hit or (self.step_num == self.max_step_num):
            done = True

        # Updating the map and visualizing the current state
        self.world.update_map(self.agent.position, done)
        self.visualizer.render(self.world.map, self.score, done)

        return done


def main():
    game_runner = GameRunner(agent=PacMan(),
                             world=Map(map_size=10),
                             visualizer=Visualizer(),
                             max_step_num=100)

    game_runner.run()


if __name__ == "__main__":
    main()
