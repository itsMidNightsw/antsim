###########################################################
###################### - ANTSIM - #########################
###########################################################

import random




class MakeWorld:
    def __init__(self, size):
        self.size = size
        self.agents = []
        self.agents_xy = []


    def add_agent(self, agent):
        self.agents.append(agent)
        self.agents_xy.append([agent.pos_x, agent.pos_y])





class Ant:
    def __init__(self, pos_x, pos_y, world):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.world = world
        world.add_agent(self)


    def move(self):
        pos_x_next = self.pos_x + random.choice([-1, 0, 1]) # Computes a new pos a first time
        pos_y_next = self.pos_y + random.choice([-1, 0, 1])
        while [pos_x_next, pos_y_next] in self.world.agents_xy: # while occupied, find a new one
            print("position conflict, calculating new position")
            pos_x_next = self.pos_x + random.choice([-1, 0, 1])
            pos_y_next = self.pos_y + random.choice([-1, 0, 1])
        self.pos_x = pos_x_next
        self.pos_y = pos_y_next



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
print("Il y a des foumis à ces coords:", monde.agents_xy)