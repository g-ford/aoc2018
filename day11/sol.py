#!/usr/bin/env python3
from collections import defaultdict

max_xy = 300
serial = 7315

def powerVal(x, y, s):
    # Find the fuel cell's rack ID, which is its X coordinate plus 10.  
    # Begin with a power level of the rack ID times the Y coordinate.  
    # Increase the power level by the value of the grid serial number (your puzzle input).  
    # Set the power level to itself multiplied by the rack ID.  
    # Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).  
    # Subtract 5 from the power level.  
    p = (((x + 10) * y) + s) * (x + 10)
    if p >= 100:
        return int(str(p)[-3]) - 5
    else:
        return -5

def summedAreaVal(x, y, s, grid):
    return powerVal(x, y, s) + grid[(x, y-1)] + grid[(x-1, y)] - grid[(x-1, y-1)]


def summedAreaPowerGrid():
    # defaultdict to avoid the negative indexing on the first row
    grid = defaultdict(int)
    for y in range(0, max_xy):
        for x in range(0, max_xy):
            grid[(x,y)] = summedAreaVal(x, y, serial, grid)
    return grid

def summedArea9(x, y, grid):
    return grid[(x+3, y+3)] + grid[(x,y)] - grid[(x+3, y)] - grid[(x, y+3)]


grid = summedAreaPowerGrid()
current_max = (0, (1,1))
for x in range(0, max_xy-3):
    for y in range(0, max_xy-3):
       a = summedArea9(x, y, grid)
       if a > current_max[0]:
           current_max = (a, (x+1,y+1))

print("Largest cell: ", current_max[1])
