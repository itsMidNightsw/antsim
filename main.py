###########################################################
###################### - ANTSIM - #########################
###########################################################

import random

class Box:
    def __init__(self, size):
        self.size = size


class Ant:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self):
        self.pos_x = self.pos_x + random.choice([-1, 0, 1])
        self.pos_y = self.pos_y + random.choice([-1, 0, 1])




world = Box(size=10)
a1 = Ant(pos_x = 1, pos_y = 1)




print(world.size)
print(a1.pos_x, a1.pos_y)
a1.move()
print(a1.pos_x, a1.pos_y)
a1.move()
print(a1.pos_x, a1.pos_y)
a1.move()
print(a1.pos_x, a1.pos_y)