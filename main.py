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
    def __init__(self, id, pos_x, pos_y, world):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.id = id
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
        self.world.agents_xy[self.id][0] = self.pos_x
        self.world.agents_xy[self.id][1] = self.pos_y



monde = MakeWorld(size=10)
a0 = Ant(id = 0, pos_x = 1, pos_y = 1, world = monde)
a1 = Ant(id = 1, pos_x = 3, pos_y = 2, world = monde)




a0.move()
a1.move()
a0.move()
a1.move()

print("Fourmis dans monde:", len(monde.agents))
print("a0 se trouve en:", a0.pos_x, a0.pos_y)
print("a1 se trouve en:", a1.pos_x, a1.pos_y)
print("le monde voit foumis à ces coords:", monde.agents_xy)