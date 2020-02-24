import random
import simplegui
import math

color_list = ['Red' ,  'Black', 'Blue', 'Fuchsia', 
                  'Gray', 'Green', 'Lime' ,'Navy', 
                 'Orange', 'Maroon']
# define draw handler
def draw(canvas):
    canvas.draw_text("Muahahaha", [65, 100], 15, "Aqua")
    canvas.draw_polyline([(10, 10), (50, 50), (50, 10), (100, 10), (100, 70)], 2.5, "Aqua")
    canvas.draw_polygon([(190, 190), (190, 150), (150, 150)], 4, 'Yellow')
    canvas.draw_circle([15, 180], 10, 2.5, 'Yellow','Teal')
    canvas.draw_point([15, 180], 'Yellow')
    canvas.draw_image(image1, (288/2, 259/2), (288, 259), (100, 170), (30, 30))
def change_back():
    global color_list
    rand_number = random.randrange(0, 10)
    frame.set_canvas_background(color_list[rand_number])

# create a frame
frame = simplegui.create_frame('My Little Canvas!!',
                               200, 200)
# register draw handler
frame.set_draw_handler(draw)
print frame.get_canvas_textwidth("Muahahaha", 15)
button1 = frame.add_button("Change Background color!!!", change_back, 100)
image1 = simplegui.load_image('https://www.google.kz/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjC-p_z95fVAhXDDpoKHaLUArsQjRwIBw&url=https%3A%2F%2Fvufind.org%2F&psig=AFQjCNFBAyvW3NExFTfy2XX_ut211B2E8Q&ust=1500642715368541')
#start a frame
frame.start()
