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
        
    def draw_new(self, canvas):
            distance = 15
            for row in range(4):
                for num in range(4):
                    canvas.draw_text(str(self.grid[row][num]), [10 + num*distance, 10 + row*distance], 10, "Red")
        
    def start_grid(self):
            choice = [0, 1, 2, 3]
            self.grid[random.choice(choice)][random.choice(choice)] = 2
            
    def get_row(self, num):
            return self.grid[num]
    def merge_lines_left(self):
            for row in range(4):
                self.grid[row] = merge(list(self.grid[row]))
            
    def merge_lines_right(self):
            for row in range(4):
                newrow = []
                for num in self.grid[row]:
                    newrow.append(num)
                newrow.reverse()    
                newnewrow = merge(newrow)
                newnewrow.reverse()
                count = 0
                for num in newnewrow:
                    self.grid[row][count] = num
                    count+= 1
                   
    def merge_lines_top(self):
            for row in range(4):
                merger  = []
                for m in range(4):
                     merger.append(self.grid[m][row])
                merger = merge(merger)
                for m in range(4):
                    self.grid[m][row] = merger[m]
                    
    def merge_lines_bottom(self):
            for row in range(4):
                merger  = []
                for m in range(4):
                     merger.append(self.grid[m][row])
                newrow = list(merger)
                newrow.reverse()
                merger = merge(newrow)
                
                for m in range(4):
                    self.grid[m][row] = merger[m]
        
        
            

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = []
    count = 0
    newline  = []
    result2 = []
    count2 = 0
    for a in range(4):
        result.append(0)
    for a in range(4):
        result2.append(0)    
    for num in list(line):
        if num != 0:
            result[count] = num
            count += 1
    for num in range(len(list(result))):
        if num != len(result)-1 and (result[num] == result[num+1] or result[num] ==0 or result[num+1] ==0):
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
    if key == simplegui.KEY_MAP['up']:
        newgrid.merge_lines_top()
    elif key == simplegui.KEY_MAP['down']:
        newgrid.merge_lines_bottom()
    elif key == simplegui.KEY_MAP['right']:
        newgrid.merge_lines_right()
    elif key == simplegui.KEY_MAP['left']:
        newgrid.merge_lines_right()
        
def keyup(key):
    pass

def draw(canvas):
    global newgrid
    newgrid.draw_new(canvas)
   

frame = simplegui.create_frame("New Frame", 300, 200)
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)
newgrid = Grid()
newgrid.start_grid()
frame.start()