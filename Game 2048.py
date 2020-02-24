import simplegui
import random
import math



class Grid():
    
    def __init__(self):
        self.grid = []
        for n in range(4):
            newrow = []
            for d in range(4):
                newrow.append(0)
            self.grid.append(newrow)
            
        def get_grid(self):
            return self.grid
        
        def start_grid(self):
            choice = [0, 1, 2, 3]
            self.grid[random.choice(choice)][random.choice(choice)] = 2
            
        def get_row(self, num):
            return self.grid[num]
        def merge_lines_left(self):
            for row in range(4):
                self.grid[row] = merge(self.grid[row])
            
        def merge_lines_right(self):
            for row in range(4):
                newrow = list(self.grid[row])
                self.grid[row] = merge(newrow.reverse())
                   
        def merge_lines_top(self):
            for m in range(4):
                for row in range(4):
                    
            
        

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = []
    count = 0
    newline  = []
    result2 = []
    count2 = 0
    for a in range(len(line)):
        result.append(0)
    for a in range(len(line)):
        result2.append(0)    
    for num in line:
        if num != 0:
            result[count] = num
            count += 1
    for num in range(len(result)):
        if num != len(result)-1 and result[num] == result[num+1]:
            newline.append(result[num]+result[num+1])
            result[num+1] = 0
        else:
            newline.append(result[num])
    for num in newline:
        if num != 0:
            result2[count2] = num
            count2 += 1 
    return result2

def keydown(key):
    pass
def keyup(key):
    pass

frame = simplegui.create_frame("New Frame", 300, 200)
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)

frame.start()