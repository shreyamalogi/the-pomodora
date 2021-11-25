# pomodora PROJECT
# author @shreyamalogi
# date: 25/11/21

from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
#imported from colorhunt.com

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("pomodora")
window.config(padx=100,pady=50, bg=YELLOW)                                                                  #dont write bg as a string, we have it in constants so import it directly  #adjust window screen padding``


title_label = Label(text = "Timer", fg=GREEN)               #font=("SERIF",20, "bold"))
title_label.grid(column=1, row=0)





canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)                                 #the last 2 are used to remove that white border around the canvas
tomato_img = PhotoImage(file="tomato.png")                                                                  #photoimage method comes from tkinter library and store it in tomato_img variable
canvas.create_image(100, 112, image=tomato_img)                                                             #we specify x and y coordinates as half the width and height of the actual image and call the variable (not as string)
canvas.create_text(100, 130, text = "00:00", fill="white", font=(FONT_NAME, 35, "bold"))                    #here text is the unlimited keyword argument and the font takes 3 values as a tuple

canvas.grid(column=1, row=1)


#canvas.pack()                                                                                                #pack method is for output in tkinter





window.mainloop()





