from pacman_env import Pacman

if __name__ == "__main__":

    env = Pacman()
    done = False
    state = env.reset()
    while not done:
        env.render()
        action = int(input("Choose your action:\n"))
        next_state, reward, done, info = env.step(action=action)
        print(info)
        state = next_state
    print("End of game")
