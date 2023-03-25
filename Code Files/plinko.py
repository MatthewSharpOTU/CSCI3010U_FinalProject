import pygame, sys
import numpy as np
from scipy.integrate import ode
import math

pygame.init()

WINDOW_WIDTH = 840
WINDOW_HEIGHT = 680

# Set the colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Plinko Board')

# clock object that ensure that animation has the same
# on all machines, regardless of the actual machine speed.
clock = pygame.time.Clock()

p = False
peg_collide = []

# static variable for all peg locations
pegs = [[60, 120], [60, 200], [60, 280], [60, 360], [60, 440], [60,520]]

# Class to keep track of the disk
class MyCircle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
        cx = self.rect.centerx
        cy = self.rect.centery
        pygame.draw.circle(self.image, color, (width//2, height//2), cx, cy)
        self.rect = self.image.get_rect()

    def update(self):
        pass

# Class for Plinko Disk
class Simulation:
    def __init__(self):
        self.state = [0.0, 0.0, 0.0 ,0.0]
        self.t = 0
        self.dt = 0.025
        self.mass = 5
        self.gamma = 0.0001
        self.gravity = 9.8
        self.count = 10
        self.peg_local = []
        
        self.solver = ode(self.f)
        self.solver.set_integrator('dop853')
        self.solver.set_f_params(self.gamma, self.gravity)

    def f(self, t, state, args1, args2):
        dx = state[2]
        dy = state[3]
        dvx = (state[2] * args1) * self.mass
        dvy = (args2 - state[3] * args1) * self.mass
        return [dx, dy, dvx, dvy]

    def setup(self, x, y):
        self.state[0] = x
        self.state[1] = y
        
        self.solver.set_initial_value(self.state, self.t)

    def is_collision(self, state):
        if (state[0] <= 80 or state[0] >= 680):
            return True
        elif (state[1]>=560):
            if ((state[0]>=85 and state[0]<=100) or
                (state[0]<=115 and state[0]>=100) or
                (state[0]>=165 and state[0]<=180) or
                (state[0]<=195 and state[0]>=180) or
                (state[0]>=245 and state[0]<=260) or
                (state[0]<=275 and state[0]>=260) or
                (state[0]>=325 and state[0]<=340) or
                (state[0]<=355 and state[0]>=340) or
                (state[0]>=405 and state[0]<=420) or
                (state[0]<=435 and state[0]>=420) or
                (state[0]>=485 and state[0]<=500) or
                (state[0]<=515 and state[0]>=500) or
                (state[0]>=565 and state[0]<=580) or
                (state[0]<=595 and state[0]>=580) or
                (state[0]>=645 and state[0]<=660) or
                (state[0]<=675 and state[0]>=660)):
                return True
            
        return False

    def peg_collision(self, state):
        for i in range(len(pegs)):
            #print(pegs[i][0]-20)
            if ((state[0]>=(pegs[i][0]-15) and state[0]<=(pegs[i][0]+15)) and (state[1]>=(pegs[i][1]-15) and state[1]<=(pegs[i][1]+15))):
                print(pegs[i], "ji")
                self.peg_local = pegs[i]
                return True
        return False    

    def step(self):
        
        self.t += self.dt
        new_state = []
        self.count += 1
        
        if self.solver.successful():
            self.solver.integrate(self.t)
            self.state = self.solver.y[0:4]
            print(self.state)

            print(self.peg_collision(self.state))
            
            if self.is_collision(self.state):
                self.state[2] = -1*self.state[2]
                #print("hello")
            if self.peg_collision(self.state) and self.count > 15:
                #print("how are you")
                print(peg_collide)
                dist = math.sqrt(pow(self.peg_local[0]-self.state[0], 2) + pow(self.peg_local[1]-self.state[1],2))
                normal = (self.state[0:2]-self.peg_local)/dist
                print(normal)
                angle = math.acos((self.state[2]*normal[0]+self.state[3]*normal[1])/((math.sqrt(pow(self.state[2],2) + pow(self.state[3],2)))*(math.sqrt(pow(normal[0],2) + pow(normal[1],2)))))
                angle -= 3.14/2
                vel = math.sqrt(pow(self.state[2], 2) + pow(self.state[3], 2))
                
                self.state[2] = vel * -np.cos(angle) * 0.75
                self.state[3] = vel * -np.sin(angle) * 0.75
                self.count = 0
                
                if (self.state[0]> self.peg_local[0]):
                    self.state[2] = -1*self.state[2]
                print(angle)
                print(vel)
                
            
    
            
            
                
        

def sim_to_screen(win_width, win_height, x, y):
    return win_width//2 + x, win_height//2 - y

# Setup of Sim
my_sprite = MyCircle(RED, 15, 15)
my_group = pygame.sprite.Group([my_sprite])

# Manipulate to Change the Drop Location of the Puck
sim = Simulation()
sim.setup(230.0, 25.0)

print('--------------------------------')
print('Usage:')
print('Press (p) to pause simulation')
print('--------------------------------')

# Main game loop
running = True
while running:
    
    clock.tick(30)

    my_sprite.rect.x, my_sprite.rect.y = sim_to_screen(640, 640, sim.state[0], sim.state[1])


    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the board background
    window.fill(WHITE)

    # Draw the slots
    #for i in range(7):
        #for j in range(10):
           # x = 40 + i * 80 + j % 2 * 40
            #y = 60 + j * 40
           # pygame.draw.circle(window, BLUE, (x, y), 18)

    pygame.draw.circle(window, RED, (sim.state[0], sim.state[1]), 15)


    pygame.draw.circle(window, GRAY, (60, 120), 5)
    pygame.draw.circle(window, GRAY, (60, 200), 5)
    pygame.draw.circle(window, GRAY, (60, 280), 5)
    pygame.draw.circle(window, GRAY, (60, 360), 5)
    pygame.draw.circle(window, GRAY, (60, 440), 5)
    pygame.draw.circle(window, GRAY, (60, 520), 5)

    # Draw the pegs
    for i in range(8):
        for j in range(13):
            x = 100 + i * 80 + j % 2 * 40
            y = 80 + j * 40
            #print("x:",x," y:",y)
            if (p == False):
                pegs.append([x,y])
            #print(pegs)
            pygame.draw.circle(window, GRAY, (x, y), 5)
    if (p==False):
        p = True

    pygame.draw.line(window, BLACK, (60, 80), (60, 600))
    pygame.draw.line(window, BLACK, (700, 80), (700, 600))
    pygame.draw.line(window, BLACK, (60, 600), (700, 600))

    pygame.draw.line(window, BLACK, (100, 560), (100, 600))
    pygame.draw.line(window, BLACK, (180, 560), (180, 600))
    pygame.draw.line(window, BLACK, (260, 560), (260, 600))
    pygame.draw.line(window, BLACK, (340, 560), (340, 600))
    pygame.draw.line(window, BLACK, (420, 560), (420, 600))
    pygame.draw.line(window, BLACK, (500, 560), (500, 600))
    pygame.draw.line(window, BLACK, (580, 560), (580, 600))
    pygame.draw.line(window, BLACK, (660, 560), (660, 600))

    if sim.state[1] >= 585.:
            pygame.quit()
            break
    
    # Update the display
    pygame.display.update()
    
    sim.step()

# Quit Pygame
pygame.quit()