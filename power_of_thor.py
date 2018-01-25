import sys
import math
import numpy as np
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
light_y = -light_y
initial_ty = -initial_ty
def checkExists(a, b, c, d):
    if (a + x[c]) < int(input()) and (b + y[d]) < int(input()):
        return True
    return False
    
def distance(a, b, c, d):
    return math.sqrt((a-c)*(a-c) + (b-d)*(b-d))

# game loop
dir = np.array(['N','NE','E','SE','S','SW','W','NW'])
x = np.array([0,1,1,1,0,-1,-1,-1])
y = np.array([1,1,0,-1,-1,-1,0,1])
dis = distance(light_x, light_y, initial_tx, initial_ty)
curr_x = initial_tx
curr_y = initial_ty
ind = 0
flag = True
while curr_x != light_x or curr_y != light_y:
    #remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # A single line providing the move to be made: N NE E SE S SW W or NW
    tempDis = distance(curr_x, curr_y, light_x, light_y)
    index = 0
    if flag == True:
        flag = False
        curr_x = curr_x
        curr_y = curr_y
    else:
        curr_x = curr_x + x[ind]
        curr_y = curr_y + y[ind]
        
    for i in range(8):
        if checkExists(curr_x, curr_y, i, i):
            now_x = curr_x + x[i]
            now_y = curr_y + y[i]
            now = distance(now_x, now_y, light_x, light_y)
            if(tempDis > now):
                tempDis = now
                index = i
                ind = i
            
            
    if curr_x != light_x or curr_y != light_y:
        print(dir[index])
