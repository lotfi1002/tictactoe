from lib.agent import Qlearning 
import argparse
import os
import pickle
import sys
import numpy as np
import matplotlib.pylab as plt

from lib.game import Game
from lib.teacher import Teacher

def plot_agent_reward(rewards):
    pass

class GameLearning:
    """
    A class that holds the state of the learning process. Learning
    agents are created/loaded here, and a count is kept of the
    games that have been played.
    """
    def __init__(self, alpha=0.5, gamma=0.9, epsilon=0.1):
        self.games_played = 0
        self.agent = Qlearning(alpha,gamma,epsilon)

    def beginPlaying(self):
        """ Loop through game iterations with a human player. """
        pass
    
    def beginTeaching(self, episodes):
       pass


if __name__ == "__main__":
   pass

   
