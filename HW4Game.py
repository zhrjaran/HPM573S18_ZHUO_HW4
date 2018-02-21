from enum import Enum
# a class allows you attach strings to integers, actually we would use text to represent the meaning


# import packages

import numpy as np


class Upside(Enum):

    HEAD=1
    TAIL=0
    BEGIN = None


class Game:
    def __init__(self, tail_prob):
        self._rnd = np.random
        #self._rnd.seed(id)
        self._tailProb = tail_prob
        self._upside = Upside.BEGIN
        self._X = 0

        self._coins = [] # create a list to store the flip result

    def simulate(self, n_flip_times, win_mon, start_mon):
        n=0  # flip time counter

        while n < n_flip_times:
            value = self._rnd.sample()

            if value > self._tailProb:  # then the patient would die at next time
                self._upside = Upside.HEAD
                self._coins.append(self._upside)

            else:
                self._upside = Upside.TAIL
                self._coins.append(self._upside)

            n += 1

        i=0
        j=0  # the number of "TTH"

        for i in range(0, 17):
            if self._coins[i]==0 and self._coins[i+1] ==0 and self._coins[i+2] ==1:
                j += 1
            i += 1

        self.X = j*win_mon - start_mon
        #return self._coins, j
        print self._coins, j

    def get_reward(self):
        return self.X

class repeatation:
    def __init__(self, repeat_size, tail_prob):
        self._coins = []
        self._X =[]

     # populate the repeatation
        for i in range(repeat_size):
            gametime = Game(tail_prob)
            self._coins.append(gametime)

    def simulate(self, n_flip_times, win_mon, start_mon):
        # simulate all games
        for gametime in self._coins:
            gametime.simulate(n_flip_times, win_mon, start_mon)

            reward = gametime.get_reward()
            self._X.append(reward)

    def get_ave_reward(self):

        return len(self._X), sum(self._X)/len(self._X)






