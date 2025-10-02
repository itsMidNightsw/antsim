###########################################################
###################### - ANTSIM - #########################
###########################################################

import random




class MakeWorld:
    def __init__(self, size):
        self.size = size
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)





class Ant:
    def __init__(self, pos_x, pos_y, world):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.world = world
        world.add_agent(self)


    def move(self):
        self.pos_x = self.pos_x + random.choice([-1, 0, 1])
        self.pos_y = self.pos_y + random.choice([-1, 0, 1])




monde = MakeWorld(size=10)
a1 = Ant(pos_x = 1, pos_y = 1, world = monde)
a2 = Ant(pos_x = 3, pos_y = 2, world = monde)




a1.move()
a2.move()
a1.move()
a2.move()

print("Fourmis dans monde:", len(monde.agents))
print("a1 se trouve en:", a1.pos_x, a1.pos_y)
print("a2 se trouve en:", a2.pos_x, a2.pos_y)