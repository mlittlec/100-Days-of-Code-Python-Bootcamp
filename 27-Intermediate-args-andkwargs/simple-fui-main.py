import tkinter import *

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "Bold")
my_label.pack(side="left")

my_label["text"] = "New text"
my_label.config(text="New Text")

# Button
def button_clicked():
    print("I go clicked")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.psck()



window.mainloop()
