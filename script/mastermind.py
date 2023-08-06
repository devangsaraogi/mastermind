import random
import threading
from tkinter import *
import imageio
from PIL import Image, ImageTk
import string_utils
import tkinter.font as tkFont

# creating tkinter window
root = Tk()
root.title("MasterMind")
root.resizable(height=FALSE, width=FALSE)
root.config(bg="black")
root.geometry("325x750")

video_name = "MMind.mp4" # this is video file path
video = imageio.get_reader(video_name)

user_input = []
secret_code = []
colors = ["red", "blue", "purple", "white", "green", "orange"]

class Solution:
    # store the four colours of the secret code

    def __init__(self):
        # intializing a secret code, comprising of 4 colours chosen at random
        # colours: 1=red, 2=blue, 3=purple, 4=white, 5=green, 6=orange

        # firstly we generate 4 randomly-chosen colors and store them in a list
        global secret_code
        secret_code = [colors[random.randrange(0, 6)] for x in range(4)]
        
        # printing the secret code for testing purposes
        # print("secret code is ", secret_code)

        # create the secret_code_string by joining four elements, each seperated by a single space
        self.secret_code_string = " ".join(secret_code)
        
        # assign the four elements of the secret code to the four secret pegs.
        [
            self.secret_peg1,
            self.secret_peg2,
            self.secret_peg3,
            self.secret_peg4,
        ] = secret_code

class outcome:
    # build a string of the hint pegs that go on the black label

    def __init__(self, out_come, out_come1, out_come2, out_come3, out_come4):
        self.out_come  = out_come
        self.out_come1 = out_come1
        self.out_come2 = out_come2
        self.out_come3 = out_come3
        self.out_come4 = out_come4

class button_up_row1:
    # row 1 button colours

    def __init__(
        self,
        but_col_1_1,
        current_but_col,
        but_col_1_2,
        current_but_col2,
        but_col_1_3,
        current_but_col3,
        but_col_1_4,
        current_but_col4,
    ):
        # initialize the button_up_row1 class
        self.but_col_1_1 = but_col_1_1
        self.current_but_col = current_but_col
        self.but_col_1_2 = but_col_1_2
        self.current_but_col2 = current_but_col2
        self.but_col_1_3 = but_col_1_3
        self.current_but_col3 = current_but_col3
        self.but_col_1_4 = but_col_1_4
        self.current_but_col4 = current_but_col4
        # s1 = button_up_row1 (0,"",0,"",0,"",0,"")

class button_up_row2:
    # row 2 button colours

    def __init__(self, but_col_2_1, but_col_2_2, but_col_2_3, but_col_2_4):
        # initialize the button_up_row2 class
        self.but_col_2_1 = but_col_2_1
        self.but_col_2_2 = but_col_2_2
        self.but_col_2_3 = but_col_2_3
        self.but_col_2_4 = but_col_2_4
        # t1 = button_up_row2 (0,0,0,0)

class button_up_row3:
    # row 3 button colours

    def __init__(self, but_col_3_1, but_col_3_2, but_col_3_3, but_col_3_4):
        # initialize the button_up_row3 class
        self.but_col_3_1 = but_col_3_1
        self.but_col_3_2 = but_col_3_2
        self.but_col_3_3 = but_col_3_3
        self.but_col_3_4 = but_col_3_4
        # u1 = button_up_row3 (0,0,0,0)

class button_up_row4:
    # row 4 button colours

    def __init__(self, but_col_4_1, but_col_4_2, but_col_4_3, but_col_4_4):
        # initialize the button_up_row4 class
        self.but_col_4_1 = but_col_4_1
        self.but_col_4_2 = but_col_4_2
        self.but_col_4_3 = but_col_4_3
        self.but_col_4_4 = but_col_4_4
        # v1 = button_up_row4 (0,0,0,0)

class button_up_row5:
    # row 5 button colours

    def __init__(self, but_col_5_1, but_col_5_2, but_col_5_3, but_col_5_4):
        # initialize the button_up_row5 class
        self.but_col_5_1 = but_col_5_1
        self.but_col_5_2 = but_col_5_2
        self.but_col_5_3 = but_col_5_3
        self.but_col_5_4 = but_col_5_4
        # w1 = button_up_row5 (0,0,0,0)

class button_up_row6:
    # row 6 button colours 

    def __init__(self, but_col_6_1, but_col_6_2, but_col_6_3, but_col_6_4):
        # initialize the button_up_row6 class
        self.but_col_6_1 = but_col_6_1
        self.but_col_6_2 = but_col_6_2
        self.but_col_6_3 = but_col_6_3
        self.but_col_6_4 = but_col_6_4
        # x1 = button_up_row6 (0,0,0,0)

class button_up_row7:
    # row 7 button colours 

    def __init__(self, but_col_7_1, but_col_7_2, but_col_7_3, but_col_7_4):
        # initialize the button_up_row7 class
        self.but_col_7_1 = but_col_7_1
        self.but_col_7_2 = but_col_7_2
        self.but_col_7_3 = but_col_7_3
        self.but_col_7_4 = but_col_7_4
        # y1 = button_up_row7 (0,0,0,0)

class button_up_row8:
    # row 8 button colours 

    def __init__(self, but_col_8_1, but_col_8_2, but_col_8_3, but_col_8_4):
        # initialize the button_up_row8 class
        self.but_col_8_1 = but_col_8_1
        self.but_col_8_2 = but_col_8_2
        self.but_col_8_3 = but_col_8_3
        self.but_col_8_4 = but_col_8_4
        # z1 = button_up_row8 (0,0,0,0)

class button_up_row9:
    # row 9 button colours 

    def __init__(self, but_col_9_1, but_col_9_2, but_col_9_3, but_col_9_4):
        # initialize the button_up_row9 class
        self.but_col_9_1 = but_col_9_1
        self.but_col_9_2 = but_col_9_2
        self.but_col_9_3 = but_col_9_3
        self.but_col_9_4 = but_col_9_4 
        # m1 = button_up_row9 (0,0,0,0)
        
class button_up_rowX:
    # row X button colours 

    def __init__(self, but_col_X_1, but_col_X_2, but_col_X_3, but_col_X_4):
        # initialize the button_up_rowX class
        self.but_col_X_1 = but_col_X_1
        self.but_col_X_2 = but_col_X_2
        self.but_col_X_3 = but_col_X_3
        self.but_col_X_4 = but_col_X_4
        # n1 = button_up_rowX (0,0,0,0)


# -----------------------------row 1 functions----------------------------
def decode_row1():
    # check result, decode button pressed for row 1
    global user_input

    # exit if all 4 colours are yet to be entered
    if (
        s1.but_col_1_1 == 0
        or s1.but_col_1_2 == 0
        or s1.but_col_1_3 == 0
        or s1.but_col_1_4 == 0
    ):
        return

    # disable decode button, so no cheating
    BUT1_5.configure(state=DISABLED)

    # build user_input string
    user_input = [temp_bc1_1, temp_bc1_2, temp_bc1_3, temp_bc1_4]

    # check user-input against secret_code
    compare_guess_solution(user_input, secret_code)

    # construct the outcome string for output to the yellow label
    r1.out_come = ""
    if black:
        r1.out_come = "*" * black
    if white:
        r1.out_come = r1.out_come + "x" * white

    if black == 0 and white == 0:
        r1.out_come = "0000"

    # rnd shuffle the out_come answer so player does not see order of results
    shuffled = string_utils.shuffle(r1.out_come)

    # display outcome in gui on black label
    LAB1 = Label(FRAME1, bg="black", fg="white", text=shuffled)
    LAB1.grid(row=7, column=4, pady=5, padx=5, sticky=W)

    # disable row 1 buttons, so cant now be changed by user
    # for some reason have to rebuild the button first
    # without the call, and with its user selected colour
    # otherwise colour selected by user is lost and can still click
    # and change the button colours, which is not good
    BUT1_1 = Button(FRAME1, bg=temp_bc1_1, relief=FLAT, height=1, width=2)
    BUT1_1.grid(row=7, column=0, pady=5, padx=5)
    BUT1_1.configure(state=DISABLED)
    BUT1_2 = Button(FRAME1, bg=temp_bc1_2, relief=FLAT, height=1, width=2)
    BUT1_1.grid(row=7, column=0, pady=5, padx=5)
    BUT1_2.configure(state=DISABLED)
    BUT1_3 = Button(FRAME1, bg=temp_bc1_3, relief=FLAT, height=1, width=2)
    BUT1_1.grid(row=7, column=0, pady=5, padx=5)
    BUT1_3.configure(state=DISABLED)
    BUT1_4 = Button(FRAME1, bg=temp_bc1_4, relief=FLAT, height=1, width=2)
    BUT1_1.grid(row=7, column=0, pady=5, padx=5)
    BUT1_4.configure(state=DISABLED)

    # now we need to enable row2's decode button
    BUT2_5.configure(state=NORMAL)

def clk_but_1_1():
    # player clicks button to change its colour
    global temp_bc1_1

    # Select next colour 1-6.
    s1.but_col_1_1 += 1

    # If last colour+1 (6+1), then loop it to first colour.
    if s1.but_col_1_1 == 7:
        s1.but_col_1_1 = 1

    # Convert integer to actual text colour to use as button fg colour.
    bc = s1.but_col_1_1
    s1.current_but_col = str(colors[bc - 1])
    
    # Store colour selected for later use in disabling this button.
    temp_bc1_1 = s1.current_but_col

    # Now actually change the button colour and display
    BUT1_1 = Button(
        FRAME1, bg=s1.current_but_col, command=clk_but_1_1, 
        relief = FLAT, bd=2, height=1, width=2       
    )
    BUT1_1.grid(row=7, column=0, pady=5, padx=5)

def clk_but_1_2():
    # player clicks button to change its colour
    global temp_bc1_2

    s1.but_col_1_2 += 1

    if s1.but_col_1_2 == 7:
        s1.but_col_1_2 = 1

    bc = s1.but_col_1_2
    s1.current_but_col2 = str(colors[bc - 1])

    temp_bc1_2 = s1.current_but_col2

    BUT1_2 = Button(
        FRAME1, bg=s1.current_but_col2, command=clk_but_1_2, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT1_2.grid(row=7, column=1, pady=5, padx=5)

def clk_but_1_3():
    # player clicks button to change its colour
    global temp_bc1_3

    s1.but_col_1_3 += 1

    if s1.but_col_1_3 == 7:
        s1.but_col_1_3 = 1

    bc = s1.but_col_1_3
    s1.current_but_col3 = str(colors[bc - 1])

    temp_bc1_3 = s1.current_but_col3

    BUT1_3 = Button(
        FRAME1, bg=s1.current_but_col3, command=clk_but_1_3, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT1_3.grid(row=7, column=2, pady=5, padx=5)

def clk_but_1_4():
    # player clicks button to change its colour
    global temp_bc1_4

    s1.but_col_1_4 += 1

    if s1.but_col_1_4 == 7:
        s1.but_col_1_4 = 1

    bc = s1.but_col_1_4
    s1.current_but_col4 = str(colors[bc - 1])

    temp_bc1_4 = s1.current_but_col4

    BUT1_4 = Button(
        FRAME1, bg=s1.current_but_col4, command=clk_but_1_4, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT1_4.grid(row=7, column=3, pady=5, padx=5)


# -------------------------row 2-------------------------------------------

def decode_row2():
    # check result, decode button pressed for row 2
    global user_input

    if (
        t1.but_col_2_1 == 0
        or t1.but_col_2_2 == 0
        or t1.but_col_2_3 == 0
        or t1.but_col_2_4 == 0
    ):
        return

    BUT2_5.configure(state=DISABLED)

    user_input = [temp_bc2_1, temp_bc2_2, temp_bc2_3, temp_bc2_4]

    compare_guess_solution(user_input, secret_code)

    r1.out_come = ""
    if black:
        r1.out_come = "*" * black
    if white:
        r1.out_come = r1.out_come + "x" * white
    if black == 0 and white == 0:
        r1.out_come = "0000"

    shuffled = string_utils.shuffle(r1.out_come)

    LAB1 = Label(FRAME2, bg="black", fg="white", text=shuffled)
    LAB1.grid(row=8, column=4, pady=5, padx=5, sticky=W)

    BUT3_5.configure(state=NORMAL)
    BUT2_1 = Button(FRAME2, bg=temp_bc2_1, relief=FLAT, height=1, width=2)
    BUT2_1.grid(row=8, column=0, pady=5, padx=5)
    BUT2_1.configure(state=DISABLED)
    BUT2_2 = Button(FRAME2, bg=temp_bc2_2, relief=FLAT, height=1, width=2)
    BUT2_2.grid(row=8, column=1, pady=5, padx=5)
    BUT2_2.configure(state=DISABLED)
    BUT2_3 = Button(FRAME2, bg=temp_bc2_3, relief=FLAT, height=1, width=2)
    BUT2_3.grid(row=8, column=2, pady=5, padx=5)
    BUT2_3.configure(state=DISABLED)
    BUT2_4 = Button(FRAME2, bg=temp_bc2_4, relief=FLAT, height=1, width=2)
    BUT2_4.grid(row=8, column=3, pady=5, padx=5)

    BUT2_4.configure(state=DISABLED)

def clk_but_2_1():
    # player clicks button to change its colour
    global temp_bc2_1

    t1.but_col_2_1 += 1

    if t1.but_col_2_1 == 7:
        t1.but_col_2_1 = 1

    bc = t1.but_col_2_1
    s1.current_but_col = str(colors[bc - 1])

    BUT2_1 = Button(
        FRAME2, bg=s1.current_but_col, command=clk_but_2_1, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT2_1.grid(row=8, column=0, pady=5, padx=5)

    temp_bc2_1 = s1.current_but_col

def clk_but_2_2():
    # player clicks button to change its colour
    global temp_bc2_2

    t1.but_col_2_2 += 1

    if t1.but_col_2_2 == 7:
        t1.but_col_2_2 = 1

    bc = t1.but_col_2_2
    s1.current_but_col2 = str(colors[bc - 1])

    BUT2_2 = Button(
        FRAME2, bg=s1.current_but_col2, command=clk_but_2_2, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT2_2.grid(row=8, column=1, pady=5, padx=5)

    temp_bc2_2 = s1.current_but_col2

def clk_but_2_3():
    # player clicks button to change its colour
    global temp_bc2_3

    t1.but_col_2_3 += 1

    if t1.but_col_2_3 == 7:
        t1.but_col_2_3 = 1

    bc = t1.but_col_2_3
    s1.current_but_col3 = str(colors[bc - 1])

    BUT2_3 = Button(
        FRAME2, bg=s1.current_but_col3, command=clk_but_2_3, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT2_3.grid(row=8, column=2, pady=5, padx=5)

    temp_bc2_3 = s1.current_but_col3

def clk_but_2_4():
    # player clicks button to change its colour
    global temp_bc2_4

    t1.but_col_2_4 += 1

    if t1.but_col_2_4 == 7:
        t1.but_col_2_4 = 1

    bc = t1.but_col_2_4
    s1.current_but_col4 = str(colors[bc - 1])

    BUT2_4 = Button(
        FRAME2, bg=s1.current_but_col4, command=clk_but_2_4, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT2_4.grid(row=8, column=3, pady=5, padx=5)

    temp_bc2_4 = s1.current_but_col4

# -------------------------row 3-----------------------------------------------

def decode_row3():
    # check result, decode button pressed for row 3
    global user_input

    if (
        u1.but_col_3_1 == 0
        or u1.but_col_3_2 == 0
        or u1.but_col_3_3 == 0
        or u1.but_col_3_4 == 0
    ):
        return

    BUT3_5.configure(state=DISABLED)
    user_input = [temp_bc3_1, temp_bc3_2, temp_bc3_3, temp_bc3_4]

    compare_guess_solution(user_input, secret_code)

    r1.out_come = ""
    if black:
        r1.out_come = "*" * black
    if white:
        r1.out_come = r1.out_come + "x" * white
    if black == 0 and white == 0:
        r1.out_come = "0000"

    shuffled = string_utils.shuffle(r1.out_come)

    LAB1 = Label(FRAME3, bg="black", fg="white", text=shuffled)
    LAB1.grid(row=9, column=4, pady=5, padx=5, sticky=W)

    BUT3_1 = Button(FRAME3, bg=temp_bc3_1, relief=FLAT, height=1, width=2)
    BUT3_1.grid(row=9, column=0, pady=5, padx=5)
    BUT3_1.configure(state=DISABLED)
    BUT3_2 = Button(FRAME3, bg=temp_bc3_2, relief=FLAT, height=1, width=2)
    BUT3_2.grid(row=9, column=1, pady=5, padx=5)
    BUT3_2.configure(state=DISABLED)
    BUT3_3 = Button(FRAME3, bg=temp_bc3_3, relief=FLAT, height=1, width=2)
    BUT3_3.grid(row=9, column=2, pady=5, padx=5)
    BUT3_3.configure(state=DISABLED)
    BUT3_4 = Button(FRAME3, bg=temp_bc3_4, relief=FLAT, height=1, width=2)
    BUT3_4.grid(row=9, column=3, pady=5, padx=5)
    BUT3_4.configure(state=DISABLED)

    BUT4_5.configure(state=NORMAL)

def clk_but_3_1():
    # player clicks button to change its colour
    global temp_bc3_1

    u1.but_col_3_1 += 1

    if u1.but_col_3_1 == 7:
        u1.but_col_3_1 = 1

    bc = u1.but_col_3_1
    s1.current_but_col = str(colors[bc - 1])

    BUT3_1 = Button(
        FRAME3, bg=s1.current_but_col, command=clk_but_3_1, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT3_1.grid(row=9, column=0, pady=5, padx=5)

    temp_bc3_1 = s1.current_but_col

def clk_but_3_2():
    # player clicks button to change its colour
    global temp_bc3_2

    u1.but_col_3_2 += 1

    if u1.but_col_3_2 == 7:
        u1.but_col_3_2 = 1

    bc = u1.but_col_3_2
    s1.current_but_col2 = str(colors[bc - 1])

    BUT3_2 = Button(
        FRAME3, bg=s1.current_but_col2, command=clk_but_3_2, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT3_2.grid(row=9, column=1, pady=5, padx=5)

    temp_bc3_2 = s1.current_but_col2

def clk_but_3_3():
    # player clicks button to change its colour
    global temp_bc3_3

    u1.but_col_3_3 += 1

    if u1.but_col_3_3 == 7:
        u1.but_col_3_3 = 1

    bc = u1.but_col_3_3
    s1.current_but_col3 = str(colors[bc - 1])

    BUT3_3 = Button(
        FRAME3, bg=s1.current_but_col3, command=clk_but_3_3, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT3_3.grid(row=9, column=2, pady=5, padx=5)

    temp_bc3_3 = s1.current_but_col3

def clk_but_3_4():
    # player clicks button to change its colour
    global temp_bc3_4

    u1.but_col_3_4 += 1

    if u1.but_col_3_4 == 7:
        u1.but_col_3_4 = 1

    bc = u1.but_col_3_4
    s1.current_but_col4 = str(colors[bc - 1])

    BUT3_4 = Button(
        FRAME3, bg=s1.current_but_col4, command=clk_but_3_4, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT3_4.grid(row=9, column=3, pady=5, padx=5)

    temp_bc3_4 = s1.current_but_col4

# --------------------------start row 4----------------------------------------

def decode_row4():
    # check result, decode button pressed for row 4
    global user_input

    if (
        v1.but_col_4_1 == 0
        or v1.but_col_4_2 == 0
        or v1.but_col_4_3 == 0
        or v1.but_col_4_4 == 0
    ):
        return

    BUT4_5.configure(state=DISABLED)
    user_input = [temp_bc4_1, temp_bc4_2, temp_bc4_3, temp_bc4_4]

    compare_guess_solution(user_input, secret_code)

    r1.out_come = ""
    if black:
        r1.out_come = "*" * black
    if white:
        r1.out_come = r1.out_come + "x" * white
    if black == 0 and white == 0:
        r1.out_come = "0000"

    shuffled = string_utils.shuffle(r1.out_come)

    LAB1 = Label(FRAME4, bg="black", fg="white", text=shuffled)
    LAB1.grid(row=10, column=4, pady=5, padx=5, sticky=W)
    BUT4_1 = Button(FRAME4, bg=temp_bc4_1, relief=FLAT, height=1, width=2)
    BUT4_1.grid(row=10, column=0, pady=5, padx=5)
    BUT4_1.configure(state=DISABLED)
    BUT4_2 = Button(FRAME4, bg=temp_bc4_2, relief=FLAT, height=1, width=2)
    BUT4_2.grid(row=10, column=1, pady=5, padx=5)
    BUT4_2.configure(state=DISABLED)
    BUT4_3 = Button(FRAME4, bg=temp_bc4_3, relief=FLAT, height=1, width=2)
    BUT4_3.grid(row=10, column=2, pady=5, padx=5)
    BUT4_3.configure(state=DISABLED)
    BUT4_4 = Button(FRAME4, bg=temp_bc4_4, relief=FLAT, height=1, width=2)
    BUT4_4.grid(row=10, column=3, pady=5, padx=5)
    BUT4_4.configure(state=DISABLED)

    BUT5_5.configure(state=NORMAL)

def clk_but_4_1():
    # player clicks button to change its colour
    global temp_bc4_1

    v1.but_col_4_1 += 1

    if v1.but_col_4_1 == 7:
        v1.but_col_4_1 = 1

    bc = v1.but_col_4_1
    s1.current_but_col = str(colors[bc - 1])

    BUT4_1 = Button(
        FRAME4, bg=s1.current_but_col, command=clk_but_4_1, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT4_1.grid(row=10, column=0, pady=5, padx=5)

    temp_bc4_1 = s1.current_but_col

def clk_but_4_2():
    # player clicks button to change its colour
    global temp_bc4_2

    v1.but_col_4_2 += 1

    if v1.but_col_4_2 == 7:
        v1.but_col_4_2 = 1

    bc = v1.but_col_4_2
    s1.current_but_col2 = str(colors[bc - 1])

    BUT4_2 = Button(
        FRAME4, bg=s1.current_but_col2, command=clk_but_4_2, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT4_2.grid(row=10, column=1, pady=5, padx=5)

    temp_bc4_2 = s1.current_but_col2

def clk_but_4_3():
    # player clicks button to change its colour
    global temp_bc4_3

    v1.but_col_4_3 += 1

    if v1.but_col_4_3 == 7:
        v1.but_col_4_3 = 1

    bc = v1.but_col_4_3
    s1.current_but_col3 = str(colors[bc - 1])

    BUT4_3 = Button(
        FRAME4, bg=s1.current_but_col3, command=clk_but_4_3, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT4_3.grid(row=10, column=2, pady=5, padx=5)

    temp_bc4_3 = s1.current_but_col3

def clk_but_4_4():
    # player clicks button to change its colour
    global temp_bc4_4

    v1.but_col_4_4 += 1

    if v1.but_col_4_4 == 7:
        v1.but_col_4_4 = 1

    bc = v1.but_col_4_4
    s1.current_but_col4 = str(colors[bc - 1])

    BUT4_4 = Button(
        FRAME4, bg=s1.current_but_col4, command=clk_but_4_4, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT4_4.grid(row=10, column=3, pady=5, padx=5)

    temp_bc4_4 = s1.current_but_col4

# ---------------------------start row 5---------------------------------------
def decode_row5():
    # check result, decode button pressed for row 5
    global user_input

    if (
        w1.but_col_5_1 == 0
        or w1.but_col_5_2 == 0
        or w1.but_col_5_3 == 0
        or w1.but_col_5_4 == 0
    ):
        return

    BUT5_5.configure(state=DISABLED)

    user_input = [temp_bc5_1, temp_bc5_2, temp_bc5_3, temp_bc5_4]

    compare_guess_solution(user_input, secret_code)

    r1.out_come = ""
    if black:
        r1.out_come = "*" * black
    if white:
        r1.out_come = r1.out_come + "x" * white
    if black == 0 and white == 0:
        r1.out_come = "0000"

    shuffled = string_utils.shuffle(r1.out_come)

    LAB5 = Label(FRAME5, bg="black", fg="white", text=shuffled)
    LAB5.grid(row=11, column=4, pady=5, padx=5, sticky=W)

    BUT5_1 = Button(FRAME5, bg=temp_bc5_1, relief=FLAT, height=1, width=2)
    BUT5_1.grid(row=11, column=0, pady=5, padx=5)
    BUT5_1.configure(state=DISABLED)
    BUT5_2 = Button(FRAME5, bg=temp_bc5_2, relief=FLAT, height=1, width=2)
    BUT5_2.grid(row=11, column=1, pady=5, padx=5)
    BUT5_2.configure(state=DISABLED)
    BUT5_3 = Button(FRAME5, bg=temp_bc5_3, relief=FLAT, height=1, width=2)
    BUT5_3.grid(row=11, column=2, pady=5, padx=5)
    BUT5_3.configure(state=DISABLED)
    BUT5_4 = Button(FRAME5, bg=temp_bc5_4, relief=FLAT, height=1, width=2)
    BUT5_4.grid(row=11, column=3, pady=5, padx=5)
    BUT5_4.configure(state=DISABLED)

    BUT6_5.configure(state=NORMAL)

def clk_but_5_1():
    # player clicks button to change its colour
    global temp_bc5_1

    w1.but_col_5_1 += 1

    if w1.but_col_5_1 == 7:
        w1.but_col_5_1 = 1

    bc = w1.but_col_5_1
    s1.current_but_col = str(colors[bc - 1])

    BUT5_1 = Button(
        FRAME5, bg=s1.current_but_col, command=clk_but_5_1, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT5_1.grid(row=11, column=0, pady=5, padx=5)

    temp_bc5_1 = s1.current_but_col

def clk_but_5_2():
    # player clicks button to change its colour
    global temp_bc5_2

    w1.but_col_5_2 += 1

    if w1.but_col_5_2 == 7:
        w1.but_col_5_2 = 1

    bc = w1.but_col_5_2
    s1.current_but_col2 = str(colors[bc - 1])

    BUT5_2 = Button(
        FRAME5, bg=s1.current_but_col2, command=clk_but_5_2, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT5_2.grid(row=11, column=1, pady=5, padx=5)

    temp_bc5_2 = s1.current_but_col2

def clk_but_5_3():
    # player clicks button to change its colour
    global temp_bc5_3

    w1.but_col_5_3 += 1

    if w1.but_col_5_3 == 7:
        w1.but_col_5_3 = 1

    bc = w1.but_col_5_3
    s1.current_but_col3 = str(colors[bc - 1])

    BUT5_3 = Button(
        FRAME5, bg=s1.current_but_col3, command=clk_but_5_3, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT5_3.grid(row=11, column=2, pady=5, padx=5)

    temp_bc5_3 = s1.current_but_col3

def clk_but_5_4():
    # player clicks button to change its colour
    global temp_bc5_4

    w1.but_col_5_4 += 1

    if w1.but_col_5_4 == 7:
        w1.but_col_5_4 = 1

    bc = w1.but_col_5_4
    s1.current_but_col4 = str(colors[bc - 1])

    BUT5_4 = Button(
        FRAME5, bg=s1.current_but_col4, command=clk_but_5_4, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT5_4.grid(row=11, column=3, pady=5, padx=5)

    temp_bc5_4 = s1.current_but_col4

# ---start row 6---------------------------------------------------------------
def decode_row6():
    # check result, decode button pressed for row 6
    global user_input

    if (
        x1.but_col_6_1 == 0
        or x1.but_col_6_2 == 0
        or x1.but_col_6_3 == 0
        or x1.but_col_6_4 == 0
    ):
        return

    BUT6_5.configure(state=DISABLED)
    user_input = [temp_bc6_1, temp_bc6_2, temp_bc6_3, temp_bc6_4]

    compare_guess_solution(user_input, secret_code)

    r1.out_come = ""
    if black:
        r1.out_come = "*" * black
    if white:
        r1.out_come = r1.out_come + "x" * white
    if black == 0 and white == 0:
        r1.out_come = "0000"

    shuffled = string_utils.shuffle(r1.out_come)
    LAB6 = Label(FRAME6, bg="black", fg="white", text=shuffled)
    LAB6.grid(row=12, column=4, pady=5, padx=5, sticky=W)

    BUT6_1 = Button(FRAME6, bg=temp_bc6_1, relief=FLAT, height=1, width=2)
    BUT6_1.grid(row=12, column=0, pady=5, padx=5)
    BUT6_1.configure(state=DISABLED)
    BUT6_2 = Button(FRAME6, bg=temp_bc6_2, relief=FLAT, height=1, width=2)
    BUT6_2.grid(row=12, column=1, pady=5, padx=5)
    BUT6_2.configure(state=DISABLED)
    BUT6_3 = Button(FRAME6, bg=temp_bc6_3, relief=FLAT, height=1, width=2)
    BUT6_3.grid(row=12, column=2, pady=5, padx=5)
    BUT6_3.configure(state=DISABLED)
    BUT6_4 = Button(FRAME6, bg=temp_bc6_4, relief=FLAT, height=1, width=2)
    BUT6_4.grid(row=12, column=3, pady=5, padx=5)
    BUT6_4.configure(state=DISABLED)
    
    BUT7_5.configure(state=NORMAL)

def clk_but_6_1():
    # player clicks button to change its colour
    global temp_bc6_1

    x1.but_col_6_1 += 1

    if x1.but_col_6_1 == 7:
        x1.but_col_6_1 = 1

    bc = x1.but_col_6_1
    s1.current_but_col = str(colors[bc - 1])

    BUT6_1 = Button(
        FRAME6, bg=s1.current_but_col, command=clk_but_6_1, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT6_1.grid(row=12, column=0, pady=5, padx=5)

    temp_bc6_1 = s1.current_but_col

def clk_but_6_2():
    # player clicks button to change its colour
    global temp_bc6_2

    x1.but_col_6_2 += 1

    if x1.but_col_6_2 == 7:
        x1.but_col_6_2 = 1

    bc = x1.but_col_6_2
    s1.current_but_col2 = str(colors[bc - 1])

    BUT6_2 = Button(
        FRAME6, bg=s1.current_but_col2, command=clk_but_6_2, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT6_2.grid(row=12, column=1, pady=5, padx=5)

    temp_bc6_2 = s1.current_but_col2

def clk_but_6_3():
    # player clicks button to change its colour
    global temp_bc6_3

    x1.but_col_6_3 += 1

    if x1.but_col_6_3 == 7:
        x1.but_col_6_3 = 1

    bc = x1.but_col_6_3
    s1.current_but_col3 = str(colors[bc - 1])

    BUT6_3 = Button(
        FRAME6, bg=s1.current_but_col3, command=clk_but_6_3, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT6_3.grid(row=12, column=2, pady=5, padx=5)

    temp_bc6_3 = s1.current_but_col3

def clk_but_6_4():
    # player clicks button to change its colour
    global temp_bc6_4

    x1.but_col_6_4 += 1

    if x1.but_col_6_4 == 7:
        x1.but_col_6_4 = 1

    bc = x1.but_col_6_4
    s1.current_but_col4 = str(colors[bc - 1])

    BUT6_4 = Button(
        FRAME6, bg=s1.current_but_col4, command=clk_but_6_4, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT6_4.grid(row=12, column=3, pady=5, padx=5)

    temp_bc6_4 = s1.current_but_col4

# ---------------------------start row 7---------------------------------------
def decode_row7():
    # check result, decode button pressed for row 7
    global user_input

    if (
        y1.but_col_7_1 == 0
        or y1.but_col_7_2 == 0
        or y1.but_col_7_3 == 0
        or y1.but_col_7_4 == 0
    ):
        return

    BUT7_5.configure(state=DISABLED)

    user_input = [temp_bc7_1, temp_bc7_2, temp_bc7_3, temp_bc7_4]

    compare_guess_solution(user_input, secret_code)

    r1.out_come = ""
    if black:
        r1.out_come = "*" * black
    if white:
        r1.out_come = r1.out_come + "x" * white
    if black == 0 and white == 0:
        r1.out_come = "0000"

    shuffled = string_utils.shuffle(r1.out_come)

    LAB7 = Label(FRAME7, bg="black", fg="white", text=shuffled)
    LAB7.grid(row=13, column=4, pady=5, padx=5, sticky=W)

    BUT7_1 = Button(FRAME7, bg=temp_bc7_1, relief=FLAT, height=1, width=2)
    BUT7_1.grid(row=13, column=0, pady=5, padx=5)
    BUT7_1.configure(state=DISABLED)
    BUT7_2 = Button(FRAME7, bg=temp_bc7_2, relief=FLAT, height=1, width=2)
    BUT7_2.grid(row=13, column=1, pady=5, padx=5)
    BUT7_2.configure(state=DISABLED)
    BUT7_3 = Button(FRAME7, bg=temp_bc7_3, relief=FLAT, height=1, width=2)
    BUT7_3.grid(row=13, column=2, pady=5, padx=5)
    BUT7_3.configure(state=DISABLED)
    BUT7_4 = Button(FRAME7, bg=temp_bc7_4, relief=FLAT, height=1, width=2)
    BUT7_4.grid(row=13, column=3, pady=5, padx=5)
    BUT7_4.configure(state=DISABLED)

    BUT8_5.configure(state=NORMAL)

def clk_but_7_1():
    # player clicks button to change its colour
    global temp_bc7_1

    y1.but_col_7_1 += 1

    if y1.but_col_7_1 == 7:
        y1.but_col_7_1 = 1

    bc = y1.but_col_7_1
    s1.current_but_col = str(colors[bc - 1])

    BUT7_1 = Button(
        FRAME7, bg=s1.current_but_col, command=clk_but_7_1, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT7_1.grid(row=13, column=0, pady=5, padx=5)

    temp_bc7_1 = s1.current_but_col

def clk_but_7_2():
    # player clicks button to change its colour
    global temp_bc7_2

    y1.but_col_7_2 += 1

    if y1.but_col_7_2 == 7:
        y1.but_col_7_2 = 1

    bc = y1.but_col_7_2
    s1.current_but_col2 = str(colors[bc - 1])

    BUT7_2 = Button(
        FRAME7, bg=s1.current_but_col2, command=clk_but_7_2, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT7_2.grid(row=13, column=1, pady=5, padx=5)

    temp_bc7_2 = s1.current_but_col2

def clk_but_7_3():
    # player clicks button to change its colour
    global temp_bc7_3

    y1.but_col_7_3 += 1

    if y1.but_col_7_3 == 7:
        y1.but_col_7_3 = 1

    bc = y1.but_col_7_3
    s1.current_but_col3 = str(colors[bc - 1])

    BUT7_3 = Button(
        FRAME7, bg=s1.current_but_col3, command=clk_but_7_3, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT7_3.grid(row=13, column=2, pady=5, padx=5)

    temp_bc7_3 = s1.current_but_col3

def clk_but_7_4():
    # player clicks button to change its colour
    global temp_bc7_4

    y1.but_col_7_4 += 1

    if y1.but_col_7_4 == 7:
        y1.but_col_7_4 = 1

    bc = y1.but_col_7_4
    s1.current_but_col4 = str(colors[bc - 1])

    BUT7_4 = Button(
        FRAME7, bg=s1.current_but_col4, command=clk_but_7_4, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT7_4.grid(row=13, column=3, pady=5, padx=5)

    temp_bc7_4 = s1.current_but_col4

# ---------------------------start row 8---------------------------------------
def decode_row8():
    # check result, decode button pressed for row 8
    global user_input

    if (
        z1.but_col_8_1 == 0
        or z1.but_col_8_2 == 0
        or z1.but_col_8_3 == 0
        or z1.but_col_8_4 == 0
    ):
        return

    BUT8_5.configure(state=DISABLED)

    user_input = [temp_bc8_1, temp_bc8_2, temp_bc8_3, temp_bc8_4]

    compare_guess_solution(user_input, secret_code)

    r1.out_come = ""
    if black:
        r1.out_come = "*" * black
    if white:
        r1.out_come = r1.out_come + "x" * white
    if black == 0 and white == 0:
        r1.out_come = "0000"

    shuffled = string_utils.shuffle(r1.out_come)

    LAB8 = Label(FRAME8, bg="black", fg="white", text=shuffled)
    LAB8.grid(row=14, column=4, pady=5, padx=5, sticky=W)

    BUT8_1 = Button(FRAME8, bg=temp_bc8_1, relief=FLAT, height=1, width=2)
    BUT8_1.grid(row=14, column=0, pady=5, padx=5)
    BUT8_1.configure(state=DISABLED)
    BUT8_2 = Button(FRAME8, bg=temp_bc8_2, relief=FLAT, height=1, width=2)
    BUT8_2.grid(row=14, column=1, pady=5, padx=5)
    BUT8_2.configure(state=DISABLED)
    BUT8_3 = Button(FRAME8, bg=temp_bc8_3, relief=FLAT, height=1, width=2)
    BUT8_3.grid(row=14, column=2, pady=5, padx=5)
    BUT8_3.configure(state=DISABLED)
    BUT8_4 = Button(FRAME8, bg=temp_bc8_4, relief=FLAT, height=1, width=2)
    BUT8_4.grid(row=14, column=3, pady=5, padx=5)
    BUT8_4.configure(state=DISABLED)

    BUT9_5.configure(state=NORMAL)

def clk_but_8_1():
    # player clicks button to change its colour
    global temp_bc8_1

    z1.but_col_8_1 += 1

    if z1.but_col_8_1 == 7:
        z1.but_col_8_1 = 1

    bc = z1.but_col_8_1
    s1.current_but_col = str(colors[bc - 1])

    BUT8_1 = Button(
        FRAME8, bg=s1.current_but_col, command=clk_but_8_1, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT8_1.grid(row=14, column=0, pady=5, padx=5)

    temp_bc8_1 = s1.current_but_col

def clk_but_8_2():
    # player clicks button to change its colour
    global temp_bc8_2

    z1.but_col_8_2 += 1

    if z1.but_col_8_2 == 7:
        z1.but_col_8_2 = 1

    bc = z1.but_col_8_2
    s1.current_but_col2 = str(colors[bc - 1])

    BUT8_2 = Button(
        FRAME8, bg=s1.current_but_col2, command=clk_but_8_2, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT8_2.grid(row=14, column=1, pady=5, padx=5)

    temp_bc8_2 = s1.current_but_col2

def clk_but_8_3():
    # player clicks button to change its colour
    global temp_bc8_3

    z1.but_col_8_3 += 1

    if z1.but_col_8_3 == 7:
        z1.but_col_8_3 = 1

    bc = z1.but_col_8_3
    s1.current_but_col3 = str(colors[bc - 1])

    BUT8_3 = Button(
        FRAME8, bg=s1.current_but_col3, command=clk_but_8_3, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT8_3.grid(row=14, column=2, pady=5, padx=5)

    temp_bc8_3 = s1.current_but_col3

def clk_but_8_4():
    # player clicks button to change its colour
    global temp_bc8_4

    z1.but_col_8_4 += 1

    if z1.but_col_8_4 == 7:
        z1.but_col_8_4 = 1

    bc = z1.but_col_8_4
    s1.current_but_col4 = str(colors[bc - 1])

    BUT8_4 = Button(
        FRAME8, bg=s1.current_but_col4, command=clk_but_8_4, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT8_4.grid(row=14, column=3, pady=5, padx=5)

    temp_bc8_4 = s1.current_but_col4

# ---------------------------start row 9---------------------------------------
def decode_row9():
    # check result, decode button pressed for row 9
    global user_input

    if (
        m1.but_col_9_1 == 0
        or m1.but_col_9_2 == 0
        or m1.but_col_9_3 == 0
        or m1.but_col_9_4 == 0
    ):
        return

    BUT9_5.configure(state=DISABLED)

    user_input = [temp_bc9_1, temp_bc9_2, temp_bc9_3, temp_bc9_4]

    compare_guess_solution(user_input, secret_code)

    r1.out_come = ""
    if black:
        r1.out_come = "*" * black
    if white:
        r1.out_come = r1.out_come + "x" * white
    if black == 0 and white == 0:
        r1.out_come = "0000"

    shuffled = string_utils.shuffle(r1.out_come)

    LAB8 = Label(FRAME9, bg="black", fg="white", text=shuffled)
    LAB8.grid(row=15, column=4, pady=5, padx=5, sticky=W)

    BUT9_1 = Button(FRAME9, bg=temp_bc9_1, relief=FLAT, height=1, width=2)
    BUT9_1.grid(row=15, column=0, pady=5, padx=5)
    BUT9_1.configure(state=DISABLED)
    BUT9_2 = Button(FRAME9, bg=temp_bc9_2, relief=FLAT, height=1, width=2)
    BUT9_2.grid(row=15, column=1, pady=5, padx=5)
    BUT9_2.configure(state=DISABLED)
    BUT9_3 = Button(FRAME9, bg=temp_bc9_3, relief=FLAT, height=1, width=2)
    BUT9_3.grid(row=15, column=2, pady=5, padx=5)
    BUT9_3.configure(state=DISABLED)
    BUT9_4 = Button(FRAME9, bg=temp_bc9_4, relief=FLAT, height=1, width=2)
    BUT9_4.grid(row=15, column=3, pady=5, padx=5)
    BUT9_4.configure(state=DISABLED)

    BUTX_5.configure(state=NORMAL)

def clk_but_9_1():
    # player clicks button to change its colour
    global temp_bc9_1

    m1.but_col_9_1 += 1

    if m1.but_col_9_1 == 7:
        m1.but_col_9_1 = 1

    bc = m1.but_col_9_1
    s1.current_but_col = str(colors[bc - 1])

    BUT9_1 = Button(
        FRAME9, bg=s1.current_but_col, command=clk_but_9_1, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT9_1.grid(row=15, column=0, pady=5, padx=5)

    temp_bc9_1 = s1.current_but_col

def clk_but_9_2():
    # player clicks button to change its colour
    global temp_bc9_2

    m1.but_col_9_2 += 1

    if m1.but_col_9_2 == 7:
        m1.but_col_9_2 = 1

    bc = m1.but_col_9_2
    s1.current_but_col2 = str(colors[bc - 1])

    BUT9_2 = Button(
        FRAME9, bg=s1.current_but_col2, command=clk_but_9_2, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT9_2.grid(row=15, column=1, pady=5, padx=5)

    temp_bc9_2 = s1.current_but_col2

def clk_but_9_3():
    # player clicks button to change its colour
    global temp_bc9_3

    m1.but_col_9_3 += 1

    if m1.but_col_9_3 == 7:
        m1.but_col_9_3 = 1

    bc = m1.but_col_9_3
    s1.current_but_col3 = str(colors[bc - 1])

    BUT9_3 = Button(
        FRAME9, bg=s1.current_but_col3, command=clk_but_9_3, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT9_3.grid(row=15, column=2, pady=5, padx=5)

    temp_bc9_3 = s1.current_but_col3

def clk_but_9_4():
    # player clicks button to change its colour
    global temp_bc9_4

    m1.but_col_9_4 += 1

    if m1.but_col_9_4 == 7:
        m1.but_col_9_4 = 1

    bc = m1.but_col_9_4
    s1.current_but_col4 = str(colors[bc - 1])

    BUT9_4 = Button(
        FRAME9, bg=s1.current_but_col4, command=clk_but_9_4, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUT9_4.grid(row=15, column=3, pady=5, padx=5)

    temp_bc9_4 = s1.current_but_col4

# ---------------------------start row X---------------------------------------
def decode_rowX():
    # check result, decode button pressed for row 10
    global user_input
    global black

    if (
        n1.but_col_X_1 == 0
        or n1.but_col_X_2 == 0
        or n1.but_col_X_3 == 0
        or n1.but_col_X_4 == 0
    ):
        return

    BUTX_5.configure(state=DISABLED)

    user_input = [temp_bcX_1, temp_bcX_2, temp_bcX_3, temp_bcX_4]

    compare_guess_solution(user_input, secret_code)

    r1.out_come = ""
    if black:
        r1.out_come = "*" * black
    if white:
        r1.out_come = r1.out_come + "x" * white
    if black == 0 and white == 0:
        r1.out_come = "0000"

    if black<4:
        reveal_solution()
        loss()
        
    shuffled = string_utils.shuffle(r1.out_come)

    LAB8 = Label(FRAMEX, bg="black", fg="white", text=shuffled)
    LAB8.grid(row=16, column=4, pady=5, padx=5, sticky=W)

    BUTX_1 = Button(FRAMEX, bg=temp_bcX_1, relief=FLAT, height=1, width=2)
    BUTX_1.grid(row=16, column=0, pady=5, padx=5)
    BUTX_1.configure(state=DISABLED)
    BUTX_2 = Button(FRAMEX, bg=temp_bcX_2, relief=FLAT, height=1, width=2)
    BUTX_2.grid(row=16, column=1, pady=5, padx=5)
    BUTX_2.configure(state=DISABLED)
    BUTX_3 = Button(FRAMEX, bg=temp_bcX_3, relief=FLAT, height=1, width=2)
    BUTX_3.grid(row=16, column=2, pady=5, padx=5)
    BUTX_3.configure(state=DISABLED)
    BUTX_4 = Button(FRAMEX, bg=temp_bcX_4, relief=FLAT, height=1, width=2)
    BUTX_4.grid(row=16, column=3, pady=5, padx=5)
    BUTX_4.configure(state=DISABLED)

def clk_but_X_1():
    # player clicks button to change its colour
    global temp_bcX_1

    n1.but_col_X_1 += 1

    if n1.but_col_X_1 == 7:
        n1.but_col_X_1 = 1

    bc = n1.but_col_X_1
    s1.current_but_col = str(colors[bc - 1])

    BUTX_1 = Button(
        FRAMEX, bg=s1.current_but_col, command=clk_but_X_1, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUTX_1.grid(row=16, column=0, pady=5, padx=5)

    temp_bcX_1 = s1.current_but_col

def clk_but_X_2():
    # player clicks button to change its colour
    global temp_bcX_2

    n1.but_col_X_2 += 1

    if n1.but_col_X_2 == 7:
        n1.but_col_X_2 = 1

    bc = n1.but_col_X_2
    s1.current_but_col2 = str(colors[bc - 1])

    BUTX_2 = Button(
        FRAMEX, bg=s1.current_but_col2, command=clk_but_X_2, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUTX_2.grid(row=16, column=1, pady=5, padx=5)

    temp_bcX_2 = s1.current_but_col2

def clk_but_X_3():
    # player clicks button to change its colour
    global temp_bcX_3

    n1.but_col_X_3 += 1

    if n1.but_col_X_3 == 7:
        n1.but_col_X_3 = 1

    bc = n1.but_col_X_3
    s1.current_but_col3 = str(colors[bc - 1])

    BUTX_3 = Button(
        FRAMEX, bg=s1.current_but_col3, command=clk_but_X_3, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUTX_3.grid(row=16, column=2, pady=5, padx=5)

    temp_bcX_3 = s1.current_but_col3

def clk_but_X_4():
    # player clicks button to change its colour
    global temp_bcX_4

    n1.but_col_X_4 += 1

    if n1.but_col_X_4 == 7:
        n1.but_col_X_4 = 1

    bc = n1.but_col_X_4
    s1.current_but_col4 = str(colors[bc - 1])

    BUTX_4 = Button(
        FRAMEX, bg=s1.current_but_col4, command=clk_but_X_4, 
        relief = FLAT, bd=2, height=1, width=2
    )
    BUTX_4.grid(row=16, column=3, pady=5, padx=5)

    temp_bcX_4 = s1.current_but_col4

# ---------------------------end of row's---------------------------------------

def display_solution():
    # solution reveal
    BUT_SECRET1 = Button(FRAMEC, bg=p1.secret_peg1, relief=FLAT, height=1, width=2)
    BUT_SECRET1.grid(row=0, column=4, pady=5, padx=5)
    BUT_SECRET2 = Button(FRAMEC, bg=p1.secret_peg2, relief=FLAT, height=1, width=2)
    BUT_SECRET2.grid(row=0, column=5, pady=5, padx=5)
    BUT_SECRET3 = Button(FRAMEC, bg=p1.secret_peg3, relief=FLAT, height=1, width=2)
    BUT_SECRET3.grid(row=0, column=6, pady=5, padx=5)
    BUT_SECRET3 = Button(FRAMEC, bg=p1.secret_peg4, relief=FLAT, height=1, width=2)
    BUT_SECRET3.grid(row=0, column=7, pady=5, padx=5)

def check_victory():
    # player is a mastermind, he has cracked the code
    global black

    if black < 4:
        return

    # delete the "REVEAL" button to reveal secret code
    BUT3_9.destroy()
    victory()
    display_solution()
    root.update()

def reveal_solution():
    # reveal button has been clicked, so show secret_code
    BUT3_9.destroy()
    display_solution()

    BUT1_5.configure(state=DISABLED)
    BUT2_5.configure(state=DISABLED)
    BUT3_5.configure(state=DISABLED)
    BUT4_5.configure(state=DISABLED)
    BUT5_5.configure(state=DISABLED)
    BUT6_5.configure(state=DISABLED)
    BUT7_5.configure(state=DISABLED)
    BUT8_5.configure(state=DISABLED)
    BUT9_5.configure(state=DISABLED)
    BUTX_5.configure(state=DISABLED)

def stream(label):
    # splits the imported video into frames and updates every second
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image

def compare_guess_solution(user_input, secret_code):
    # check what player pegs match secret code
    global black
    global white
    black = 0
    white = 0
    secret_copy = secret_code[:]
    user_copy = user_input[:]

    for index, input in enumerate(user_copy):
        if input == secret_copy[index]:
            black += 1
            secret_copy[index] = "checked solution"
            user_copy[index] = "checked user"

    for index, input in enumerate(user_copy):
        for i, p in enumerate(secret_copy):
            if p == input:
                white += 1
                secret_copy[i] = "checked solution"
                break

    check_victory()

def loss():
    fonty = tkFont.Font(size=13, weight="bold")
    label = Label(root,text="GAME OVER, YOU LOSE", height=4, width=30,
                  fg="white", bg="black", font=fonty)
    label.grid(row=1, column=0)

def victory():
    fonty = tkFont.Font(size=13, weight="bold")
    label = Label(root,text="GAME OVER, YOU WIN", height=4, width=30,
                  fg="white", bg="black", font=fonty)
    label.grid(row=1, column=0)

FRAME0 = LabelFrame(root, bg="black", relief=RIDGE, bd=0)
FRAME0.grid(padx=15,pady=25)

vid_label = Label(FRAME0, bg="black", height=35, width=285)
vid_label.grid(padx=2,pady=2)
thread = threading.Thread(target=stream, args=(vid_label,))
thread.daemon = 1
thread.start()

FRAME_H = LabelFrame(root, bg="black", relief=RIDGE, bd=0)
FRAME_H.grid(padx=5,pady=0)
HELP = Label(
    FRAME_H, bg="black", fg="white", justify=LEFT, width=40,
    text="Can you crack the code?                    \n\n"
         "Star                   = Correct colour and position.         \n"
         "Cross                = Correct colour, wrong position.      \n"
         "Zero                  = No colours in code.",
)
HELP.grid(pady=2, padx=2)


# ---------------------------Attempt 1 Widgets--------------------------------------
FRAME1 = LabelFrame(root, bg="black", relief=RIDGE, bd=2)
FRAME1.grid(padx=15,pady=5)
a1_lab = Label(FRAME1, bg="black", fg="white", text="A1", height=1, width=3)
a1_lab.grid(row=7, column=6, pady=5, padx=5)
BUT1_1 = Button(FRAME1,bg="skyblue", command=clk_but_1_1, relief=FLAT, height=1, width=2)
BUT1_1.grid(row=7, column=0, pady=5, padx=5)
BUT1_2 = Button(FRAME1,bg="skyblue", command=clk_but_1_2, relief=FLAT, height=1, width=2)
BUT1_2.grid(row=7, column=1, pady=5, padx=5)
BUT1_3 = Button(FRAME1,bg="skyblue", command=clk_but_1_3, relief=FLAT, height=1, width=2)
BUT1_3.grid(row=7, column=2, pady=5, padx=5)
BUT1_4 = Button(FRAME1,bg="skyblue", command=clk_but_1_4, relief=FLAT, height=1, width=2)
BUT1_4.grid(row=7, column=3, pady=5, padx=5)
LAB1 = Label(FRAME1, bg="black", text="        ")
LAB1.grid(row=7, column=4, pady=5, padx=5)
BUT1_5 = Button(FRAME1, bg="green2", text="DECODE", command=decode_row1)
BUT1_5.grid(row=7, column=5, pady=5, padx=5)

# ---------------------------Attempt 2 Widgets--------------------------------------
FRAME2 = LabelFrame(root, bg="black", relief=RIDGE, bd=2)
FRAME2.grid(padx=15,pady=5)
a2_lab = Label(FRAME2, bg="black", fg="white", text="A2", height=1, width=3)
a2_lab.grid(row=8, column=6, pady=5, padx=5)
BUT2_1 = Button(FRAME2, bg="skyblue", command=clk_but_2_1, relief=FLAT, height=1, width=2)
BUT2_1.grid(row=8, column=0, pady=5, padx=5)
BUT2_2 = Button(FRAME2, bg="skyblue", command=clk_but_2_2, relief=FLAT, height=1, width=2)
BUT2_2.grid(row=8, column=1, pady=5, padx=5)
BUT2_3 = Button(FRAME2, bg="skyblue", command=clk_but_2_3, relief=FLAT, height=1, width=2)
BUT2_3.grid(row=8, column=2, pady=5, padx=5)
BUT2_4 = Button(FRAME2, bg="skyblue", command=clk_but_2_4, relief=FLAT, height=1, width=2)
BUT2_4.grid(row=8, column=3, pady=5, padx=5)
LAB2 = Label(FRAME2, bg="black", text="        ")
LAB2.grid(row=8, column=4, pady=5, padx=5)
BUT2_5 = Button(FRAME2, bg="green2", text="DECODE", command=decode_row2)
BUT2_5.grid(row=8, column=5, pady=5, padx=5)

# ---------------------------Attempt 3 Widgets--------------------------------------
FRAME3 = LabelFrame(root, bg="black", relief=RIDGE, bd=2)
FRAME3.grid(padx=15,pady=5)
a3_lab = Label(FRAME3, bg="black", fg="white", text="A3", height=1, width=3)
a3_lab.grid(row=9, column=6, pady=5, padx=5)
BUT3_1 = Button(FRAME3, bg="skyblue", command=clk_but_3_1, relief=FLAT, height=1, width=2)
BUT3_1.grid(row=9, column=0, pady=5, padx=5)
BUT3_2 = Button(FRAME3, bg="skyblue", command=clk_but_3_2, relief=FLAT, height=1, width=2)
BUT3_2.grid(row=9, column=1, pady=5, padx=5)
BUT3_3 = Button(FRAME3, bg="skyblue", command=clk_but_3_3, relief=FLAT, height=1, width=2)
BUT3_3.grid(row=9, column=2, pady=5, padx=5)
BUT3_4 = Button(FRAME3, bg="skyblue", command=clk_but_3_4, relief=FLAT, height=1, width=2)
BUT3_4.grid(row=9, column=3, pady=5, padx=5)
LAB3 = Label(FRAME3, bg="black", text="        ")
LAB3.grid(row=9, column=4, pady=5, padx=5)
BUT3_5 = Button(FRAME3, bg="green2", text="DECODE", command=decode_row3)
BUT3_5.grid(row=9, column=5, pady=5, padx=5)

# ---------------------------Attempt 4 Widgets--------------------------------------
FRAME4 = LabelFrame(root, bg="black", relief=RIDGE, bd=2)
FRAME4.grid(padx=15,pady=5)
a4_lab = Label(FRAME4, bg="black", fg="white", text="A4", height=1, width=3)
a4_lab.grid(row=10, column=6, pady=5, padx=5)
BUT4_1 = Button(FRAME4, bg="skyblue", command=clk_but_4_1, relief=FLAT, height=1, width=2)
BUT4_1.grid(row=10, column=0, pady=5, padx=5)
BUT4_2 = Button(FRAME4, bg="skyblue", command=clk_but_4_2, relief=FLAT, height=1, width=2)
BUT4_2.grid(row=10, column=1, pady=5, padx=5)
BUT4_3 = Button(FRAME4, bg="skyblue", command=clk_but_4_3, relief=FLAT, height=1, width=2)
BUT4_3.grid(row=10, column=2, pady=5, padx=5)
BUT4_4 = Button(FRAME4, bg="skyblue", command=clk_but_4_4, relief=FLAT, height=1, width=2)
BUT4_4.grid(row=10, column=3, pady=5, padx=5)
LAB4 = Label(FRAME4, bg="black", text="        ")
LAB4.grid(row=10, column=4, pady=5, padx=5)
BUT4_5 = Button(FRAME4, bg="green2", text="DECODE", command=decode_row4)
BUT4_5.grid(row=10, column=5, pady=5, padx=5)

# ---------------------------Attempt 5 Widgets--------------------------------------
FRAME5 = LabelFrame(root, bg="black", relief=RIDGE, bd=2)
FRAME5.grid(padx=15,pady=5)
a5_lab = Label(FRAME5, bg="black", fg="white", text="A5", height=1, width=3)
a5_lab.grid(row=11, column=6, pady=5, padx=5)
BUT5_1 = Button(FRAME5, bg="skyblue", command=clk_but_5_1, relief=FLAT, height=1, width=2)
BUT5_1.grid(row=11, column=0, pady=5, padx=5)
BUT5_2 = Button(FRAME5, bg="skyblue", command=clk_but_5_2, relief=FLAT, height=1, width=2)
BUT5_2.grid(row=11, column=1, pady=5, padx=5)
BUT5_3 = Button(FRAME5, bg="skyblue", command=clk_but_5_3, relief=FLAT, height=1, width=2)
BUT5_3.grid(row=11, column=2, pady=5, padx=5)
BUT5_4 = Button(FRAME5, bg="skyblue", command=clk_but_5_4, relief=FLAT, height=1, width=2)
BUT5_4.grid(row=11, column=3, pady=5, padx=5)
LAB5 = Label(FRAME5, bg="black", text="        ")
LAB5.grid(row=11, column=4, pady=5, padx=5)
BUT5_5 = Button(FRAME5, bg="green2", text="DECODE", command=decode_row5)
BUT5_5.grid(row=11, column=5, pady=5, padx=5)

# ---------------------------Attempt 6 Widgets--------------------------------------
FRAME6 = LabelFrame(root, bg="black", relief=RIDGE, bd=2)
FRAME6.grid(padx=15,pady=5)
a6_lab = Label(FRAME6, bg="black", fg="white", text="A6", height=1, width=3)
a6_lab.grid(row=12, column=6, pady=5, padx=5)
BUT6_1 = Button(FRAME6, bg="skyblue", command=clk_but_6_1, relief=FLAT, height=1, width=2)
BUT6_1.grid(row=12, column=0, pady=5, padx=5)
BUT6_2 = Button(FRAME6, bg="skyblue", command=clk_but_6_2, relief=FLAT, height=1, width=2)
BUT6_2.grid(row=12, column=1, pady=5, padx=5)
BUT6_3 = Button(FRAME6, bg="skyblue", command=clk_but_6_3, relief=FLAT, height=1, width=2)
BUT6_3.grid(row=12, column=2, pady=5, padx=5)
BUT6_4 = Button(FRAME6, bg="skyblue", command=clk_but_6_4, relief=FLAT, height=1, width=2)
BUT6_4.grid(row=12, column=3, pady=5, padx=5)
LAB6 = Label(FRAME6, bg="black", text="        ")
LAB6.grid(row=12, column=4, pady=5, padx=5)
BUT6_5 = Button(FRAME6, bg="green2", text="DECODE", command=decode_row6)
BUT6_5.grid(row=12, column=5, pady=5, padx=5)

# ---------------------------Attempt 7 Widgets--------------------------------------
FRAME7 = LabelFrame(root, bg="black", relief=RIDGE, bd=2)
FRAME7.grid(padx=15,pady=5)
a7_lab = Label(FRAME7, bg="black", fg="white", text="A7", height=1, width=3)
a7_lab.grid(row=13, column=6, pady=5, padx=5)
BUT7_1 = Button(FRAME7,bg="skyblue", command=clk_but_7_1, relief=FLAT, height=1, width=2)
BUT7_1.grid(row=13, column=0, pady=5, padx=5)
BUT7_2 = Button(FRAME7,bg="skyblue", command=clk_but_7_2, relief=FLAT, height=1, width=2)
BUT7_2.grid(row=13, column=1, pady=5, padx=5)
BUT7_3 = Button(FRAME7,bg="skyblue", command=clk_but_7_3, relief=FLAT, height=1, width=2)
BUT7_3.grid(row=13, column=2, pady=5, padx=5)
BUT7_4 = Button(FRAME7,bg="skyblue", command=clk_but_7_4, relief=FLAT, height=1, width=2)
BUT7_4.grid(row=13, column=3, pady=5, padx=5)
LAB7 = Label(FRAME7, bg="black", text="        ")
LAB7.grid(row=13, column=4, pady=5, padx=5)
BUT7_5 = Button(FRAME7, bg="green2", text="DECODE", command=decode_row7)
BUT7_5.grid(row=13, column=5, pady=5, padx=5)

# ---------------------------Attempt 8 Widgets--------------------------------------
FRAME8 = LabelFrame(root, bg="black", relief=RIDGE, bd=2)
FRAME8.grid(padx=15,pady=5)
a8_lab = Label(FRAME8, bg="black", fg="white", text="A8", height=1, width=3)
a8_lab.grid(row=14, column=6, pady=5, padx=5)
BUT8_1 = Button(FRAME8,bg="skyblue", command=clk_but_8_1, relief=FLAT, height=1, width=2)
BUT8_1.grid(row=14, column=0, pady=5, padx=5)
BUT8_2 = Button(FRAME8,bg="skyblue", command=clk_but_8_2, relief=FLAT, height=1, width=2)
BUT8_2.grid(row=14, column=1, pady=5, padx=5)
BUT8_3 = Button(FRAME8,bg="skyblue", command=clk_but_8_3,  relief=FLAT, height=1, width=2)
BUT8_3.grid(row=14, column=2, pady=5, padx=5)
BUT8_4 = Button(FRAME8,bg="skyblue", command=clk_but_8_4,  relief=FLAT, height=1, width=2)
BUT8_4.grid(row=14, column=3, pady=5, padx=5)
LAB8 = Label(FRAME8, bg="black", text="        ")
LAB8.grid(row=14, column=4, pady=5, padx=5)
BUT8_5 = Button(FRAME8, bg="green2", text="DECODE", command=decode_row8)
BUT8_5.grid(row=14, column=5, pady=5, padx=5)

# ---------------------------Attempt 9 Widgets--------------------------------------
FRAME9 = LabelFrame(root, bg="black", relief=RIDGE, bd=2)
FRAME9.grid(padx=15,pady=5)
a8_lab = Label(FRAME9, bg="black", fg="white", text="A9", height=1, width=3)
a8_lab.grid(row=15, column=6, pady=5, padx=5)
BUT9_1 = Button(FRAME9,bg="skyblue", command=clk_but_9_1, relief=FLAT, height=1, width=2)
BUT9_1.grid(row=15, column=0, pady=5, padx=5)
BUT9_2 = Button(FRAME9,bg="skyblue", command=clk_but_9_2, relief=FLAT, height=1, width=2)
BUT9_2.grid(row=15, column=1, pady=5, padx=5)
BUT9_3 = Button(FRAME9,bg="skyblue", command=clk_but_9_3, relief=FLAT, height=1, width=2)
BUT9_3.grid(row=15, column=2, pady=5, padx=5)
BUT9_4 = Button(FRAME9,bg="skyblue", command=clk_but_9_4, relief=FLAT, height=1, width=2)
BUT9_4.grid(row=15, column=3, pady=5, padx=5)
LAB9 = Label(FRAME9, bg="black", text="        ")
LAB9.grid(row=15, column=4, pady=5, padx=5)
BUT9_5 = Button(FRAME9, bg="green2", text="DECODE", command=decode_row9)
BUT9_5.grid(row=15, column=5, pady=5, padx=5)

# ---------------------------Attempt X Widgets--------------------------------------
FRAMEX = LabelFrame(root, bg="black", relief=RIDGE, bd=2)
FRAMEX.grid(padx=15,pady=5)
aX_lab = Label(FRAMEX, bg="black", fg="white", text="AX", height=1, width=3)
aX_lab.grid(row=16, column=6, pady=5, padx=5)
BUTX_1 = Button(FRAMEX,bg="skyblue", command=clk_but_X_1, relief=FLAT, height=1, width=2)
BUTX_1.grid(row=16, column=0, pady=5, padx=5)
BUTX_2 = Button(FRAMEX,bg="skyblue", command=clk_but_X_2, relief=FLAT, height=1, width=2)
BUTX_2.grid(row=16, column=1, pady=5, padx=5)
BUTX_3 = Button(FRAMEX,bg="skyblue", command=clk_but_X_3, relief=FLAT, height=1, width=2)
BUTX_3.grid(row=16, column=2, pady=5, padx=5)
BUTX_4 = Button(FRAMEX,bg="skyblue", command=clk_but_X_4, relief=FLAT, height=1, width=2)
BUTX_4.grid(row=16, column=3, pady=5, padx=5)
LABX = Label(FRAMEX, bg="black", text="        ")
LABX.grid(row=16, column=4, pady=5, padx=5)
BUTX_5 = Button(FRAMEX, bg="green2", text="DECODE", command=decode_rowX)
BUTX_5.grid(row=16, column=5, pady=5, padx=5)

# initiaize classes
# p1 ect. is just a name we can make up to reference the class
# and pass the initial state of the variables to it
p1 = Solution()
r1 = outcome(0, 0, 0, 0, 0)
s1 = button_up_row1(0, "", 0, "", 0, "", 0, "")
t1 = button_up_row2(0, 0, 0, 0)
u1 = button_up_row3(0, 0, 0, 0)
v1 = button_up_row4(0, 0, 0, 0)
w1 = button_up_row5(0, 0, 0, 0)
x1 = button_up_row6(0, 0, 0, 0)
y1 = button_up_row7(0, 0, 0, 0)
z1 = button_up_row8(0, 0, 0, 0)
m1 = button_up_row9(0, 0, 0, 0)
n1 = button_up_rowX(0, 0, 0, 0)

# make sure player can only decode row 1 to start with
# by disabling all other decode buttons
BUT2_5.configure(state=DISABLED)
BUT3_5.configure(state=DISABLED)
BUT4_5.configure(state=DISABLED)
BUT5_5.configure(state=DISABLED)
BUT6_5.configure(state=DISABLED)
BUT7_5.configure(state=DISABLED)
BUT8_5.configure(state=DISABLED)
BUT9_5.configure(state=DISABLED)
BUTX_5.configure(state=DISABLED)

# cover up secret code with a button
FRAMEC = LabelFrame(root, bg="black", relief=RIDGE, bd=2)
FRAMEC.grid()
BUT3_9 = Button(FRAMEC, bg="gold", text="REVEAL", command=reveal_solution)
BUT3_9.grid(row=9, column=5, pady=5, padx=5)

# ---now program control is waiting for button clicks to commence game-------

root.mainloop()