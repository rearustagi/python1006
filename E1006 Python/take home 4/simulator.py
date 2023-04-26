import random
import math
from matplotlib import pyplot as plt
import numpy as np

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    
recovery_time = 5 # recovery time in time-steps
virality = 0.25   # probability that a neighbor cell is infected in 
                  # each time step                                                  

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        self.time = 0
    
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
    
    def infect(self):
        self.time = 0
        self.state = "I"
    
    def process(self, adjacent_cells):
        self.adjacent_cells = adjacent_cells
        if self.state == "I" and self.time >= 1:
            if self.time == recovery_time:
                self.state = "S"
            else:
                x, mean, sd = self.time, 6, 2 
                indiv_death = random.random()
                prob_death = pdeath(x, mean, sd)
                if (indiv_death <= prob_death):
                    self.state = "R"
                else:
                    for each_adj_cell in self.adjacent_cells:
                        if each_adj_cell.state == "S":
                            cell_vir = random.random()
                            if cell_vir <= virality:
                                each_adj_cell.infect()
        self.time += 1
        
class Map(object):
    
    cells = dict()
    a = np.zeros((150,150,3))
    
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell):
        self.cell = cell
        key = (cell.x, cell.y)
        self.cells[key] = self.cell
        
    def display(self):
        for cell in self.cells:
            x_coord = cell[0]
            y_coord = cell[1]
            if self.cells[cell].state == "S":
                self.a[x_coord, y_coord] = [0, 1.0, 0.2]
            if self.cells[cell].state == "I":
                self.a[x_coord, y_coord] = [1.0, 0.2, 0.2]
            if self.cells[cell].state == "R":
                self.a[x_coord, y_coord] = [0.5, 0.5, 0.5]
                
        plt.imshow(self.a)

    def adjacent_cells(self, x, y):
        self.x = x
        self.y = y
        adj_cells = []
        cell_loc = [(self.x, self.y + 1), (self.x, self.y - 1), (self.x + 1, self.y), (self.x - 1, self.y)]
        if 1 <= self.x <= 149 and 1 <= self.y <= 149:
            for loc in cell_loc:
                if loc in self.cells:
                    adj_cells.append(self.cells[loc])
                    
        return adj_cells
    
    def time_step(self):        
        for each_cell in self.cells.values():
            adj = self.adjacent_cells(each_cell.x, each_cell.y)
            Cell.process(each_cell, adj)
            
        self.display()
            
def read_map(filename):
    
    m = Map()
    
    f = open(filename,'r')
    
    for line in f:
        coordinates = line.strip().split(',')
        c = Cell(int(coordinates[0]),int(coordinates[1]))
        Map.add_cell(m, c)

    return m
