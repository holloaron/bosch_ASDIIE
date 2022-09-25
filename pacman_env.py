# Pacman Environment
# Author : Csorba Levente , Knáb István Gellért, Tóth Tibor Áron
# Team : I_NEED_A


#import the needed libraries
import cv2
import numpy as np

class PacMan:
    def __init__(self, map_size):
        self.map_size = map_size
        # lists for the map components
        self.body = None
        self.objects = []
        # initiate default values
        self.step_ = 100
        self.dir = 1

        self.last_obs = None
        # placeholder for additional information
        info = None
        self.time_step=40
        # Variables for visualizing the current grid world
        self.show_img_size = 300
        self.show_img = np.zeros((self.show_img_size, self.show_img_size, 3))
        self.ratio = int(self.show_img_size / self.map_size)
        self.score=0
        self.reset()


    def step(self , action):
        # setting basic env status
        done_ = False
        
        # getting the current position
        pos_x, pos_y = self.body

        x,y=self.choose_action(pos_x=pos_x , pos_y=pos_y)

        #coordinates of the PacMan object
        self.body = (x,y)
        self._wall_limit()

        #Eat and add to score
        self.eat(x,y)

            # create observation
        obs = self._create_observation()

        # save observation
        self.last_obs = obs

        #decrement for termination , by reaching 0
        self.step_ -=1

        #termination branch
        if self.step_ == 0:
            done_ = True
            print(f"Your score is {self.score}")

        #in this game not used
        info= None


        #end of episode
        return obs.flatten(), self.score, done_, info

    def choose_action(self , pos_x , pos_y):
        if action == 0:
            # going right
            x, y = self.right(pos_x, pos_y, action)
        elif action == 1:
            # going up
            x, y = self.up(pos_x, pos_y, action)

        elif action == 2:
            # going left
            x, y = self.left(pos_x, pos_y, action)

        elif action == 3:
            # going down
            x, y = self.down(pos_x, pos_y, action)

        else:
            print("You lose , wrong key")
            done_ = True
            self.score= -1
            print(f"Score {self.score}")

        return x,y

    def eat(self , x , y):
        if (x, y) in self.objects:
            # increment score by eating an object
            self.score += 1

            # if object reached  , remove
            self.objects.remove((x, y))

    def right(self , x,y,action):

        #only the x coordinate changes

        x += 1
        y = y
        return x,y


    def up(self, x,y,action):

        #only the y coordinate changes
        x = x
        y +=1
        return x,y


    def left(self, x,y,action):

        x -= 1
        y = y

        return x,y


    def down(self, x,y,action):

        # only the y coordinate changes
        x = x
        y -= 1

        return x,y


    def reset(self):

        self.body = None
        self.objects = []
        self.dir = 1

        self.step_ = 0
        self.last_obs = None

        self._create_body()
        self._create_objects(num=10)
        obs_ = self._create_observation()
        return obs_.flatten()

    def render(self, mode="human"):
        """
        This function creates a cv2 plot from the current game state
        :param mode: not used, legacy of gym environments
        :return:
        """

        if self.last_obs is not None:
            img = np.float32(self.last_obs)
        else:
            img = np.float32(self._create_observation())
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        # rescale original image from the grid world to visualize with OpenCv
        for i in range(self.show_img_size):
            for j in range(self.show_img_size):
                self.show_img[i][j] = img[i // self.ratio][j // self.ratio]
        cv2.imshow("PAC-MAN Env", self.show_img)
        # add wait to see the game
        cv2.waitKey(50)
             


    def _create_objects(self, num):
        for _ in range(num):
            coords = tuple(np.random.randint(0, self.map_size, (2,)))
            if self.body[0] != coords[0] and self.body[1] != coords[1]:
                self.objects.append(coords)


    def _create_body(self):
        self.body = (0,0)


    def _create_observation(self):
        """
        This funtion creates a grayscale observation (image) from the current state of the game.
        :return:
        """
        # init map
        obs_ = np.zeros((self.map_size, self.map_size, 1))

        # add objects
        for obj in self.objects:
            obs_[obj[0], obj[1], 0] = 0.25

        # add pac-man
        pac_man_coords = self.body
        obs_[pac_man_coords[0], pac_man_coords[1], 0] = 0.8
        return obs_

    def _wall_limit(self):
        limited_x = max(0, min(self.body[0], self.map_size-1))
        limited_y = max(0, min(self.body[1], self.map_size-1))
        
        self.body = (limited_x,limited_y)
        

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

    #render before first step
    env.render()

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

    print(f" Game over , your score is{env.score}")
