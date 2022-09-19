# Pacman Environment
# Author : Csorba Levente , Knáb István Gellért
#Team : I_NEED_A


#import the needed libraries
import cv2
import numpy as np

class PacMan:
    def __init__(self, map_size):
        self.map_size = map_size
        # lists for the map components
        self.body = []
        self.objects = []
        # initiate default values
        self.step_ = 0
        self.dir = 1
        self.size = 5
        self.last_obs = None
        self.time_step=40
        # Variables for visualizing the current grid world
        self.show_img_size = 300
        self.show_img = np.zeros((self.show_img_size, self.show_img_size, 3))
        self.ratio = int(self.show_img_size / self.map_size)
        self.reset()


    def step(self , action):
        # setting base reward
        score = 0
        # setting basic env status
        is_dead = False
        # getting the current head position (always the last body part)
        pos_x, pos_y = self.body[-1]

        #choose action
        if action==0:
            #going right
            x,y = self.right(pos_x,pos_y,action)
        if action == 1:
            #going up
            x, y = self.up(pos_x, pos_y, action)

        if action == 2:
            #going left
            x, y = self.left(pos_x, pos_y, action)

        if action == 3:
            #going down
            x, y = self.down(pos_x, pos_y, action)



        return state, reward, done_, info

    def right(self , x,y,action):
        return x,y


    def up(self, x,y,action):
        return x,y


    def left(self, x,y,action):
        return x,y


    def down(self, x,y,action):
        return x,y


    def reset(self):


        return state


    def render(self):
        pass


def initialize_parameters():
    global map_size , done_
    map_size = 20
    done_ = False



if __name__ == "__main__":

    #initial parameters
    initialize_parameters()

    #Calling Constructor for the game
    env = PacMan(map_size=map_size)

    #starting state
    state = env.reset()

    #play loop
    while not done_:
        # here are declared the control keys
        print("control assist TODO")

        #add the next action
        action = int(input("Next action:\n"))

        #gym compatible return of step
        state, reward, done_, info = env.step(action=action)

        #visualization of the game
        env.render()






