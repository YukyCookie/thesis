import gym
from gym.spaces import Discrete
from gym.envs.users.config import *
from gym.envs.users.utils import *

class BasicEnv(gym.Env):
    def __init__(self):
        nodefile = NODE_DIR
        datafile = DATA_DIR
        
        self.action_space = read_data(filepath=nodefile)
        self.state_space = read_data(filepath=datafile)
        self.state_index = 0
        self.state = self.state_space[self.state_index]
        # self.state_lenth = len(self.state_space)-1
    
    def step(self, action):
        self.state_index += 1
         
        if self.state_index <= len(self.state_space)-1 :
            self.state = self.state_space[self.state_index]  
            done = False
        else:
            done = True
            
        reward = cal_reward(self.state[0], self.state[1], action[0], action[1])
        # Setting the placeholder for info
        info = {}
        return self.state, reward, done, info
        
    def reset(self):
        self.state_index = 0
        self.state = self.state_space[self.state_index]
        self.state_lenth = len(self.state_space)
        return self.state
    
    