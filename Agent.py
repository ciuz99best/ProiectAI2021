import random


class Agent:
    def __init__(self, method, size):
        self.method = method  # 1, 2, or 3 are the picking options for the Agent
        self.size = size

    def random(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        return x, y

    def min_max(self):
        pass

    def something(self):
        pass

    def pick(self):
        if self.method == 1:
            return self.random()
        elif self.method == 2:
            return self.min_max()
        elif self.method == 3:
            return self.something()
