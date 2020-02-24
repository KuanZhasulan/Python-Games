# Cipher
import random
import simplegui

CIPHER = {'a': 'x', 'b': 'c', 'c': 'r', 'd': 'm', 'e': 'l'}

message = ""

LETTERS = "qwertyuiopasdfghjklzxcvbnm"

def init(text):
    count = 0
    my_list = list(text)
    my_list1 = list(text)
    random.shuffle(my_list1)
    dic1 = {}    
    for letter in my_list:
        dic1[letter] = my_list1[count]
        count += 1
    return dic1    
    

# Encode button
def encode():
    emsg = ""
    for ch in message:
        emsg += CIPHER_1[ch]
    print message, "encodes to", emsg

# Decode button
def decode():
    dmsg = ""
    for ch in message:
        for key, value in CIPHER_1.items():
            if ch == value:
                dmsg += key
    print message, "decodes to", dmsg

# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label("", 200)
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)
CIPHER_1 =  init(LETTERS)
# Start the frame animation
frame.start()
