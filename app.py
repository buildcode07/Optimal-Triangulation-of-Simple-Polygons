import matplotlib
matplotlib.use('TkAgg')

from Tkinter import *
from PIL import ImageTk,Image
from tkFileDialog import askopenfilename
import tkFont, test, sys, main, ttk, tkMessageBox

file_name = ''

def openfile():
    global file_name
    file_name = askopenfilename()

def reset(option):
    main.reset(file_name, option)

def main_method(value):
    option = 1
    if value == "Minimum Weight Triangluation":
        option = 1
    elif value == "Minimizing the Maximum of the Internal Angles":
        option = 2
    else:
        option = 3
    reset(option)

# the structure of the desktop app on how it is displayed
def process():
    root = Tk()
    canv = Canvas(root, width=800, height=200, bg='white')
    canv.grid(row=10, column=10)
    img = ImageTk.PhotoImage(Image.open("cg_wall.jpg"))  # PIL solution
    canv.create_image(2, 2, anchor=NW, image=img)
    canv.pack()
    root.title("Optimal Polygon Triangluation")
    separator = Frame(height=2, bd=1, relief=SUNKEN)
    separator.pack(fill=X, padx=30, pady=10)
    ttk.Separator(root,orient=HORIZONTAL).grid(row=2, columnspan=5, sticky="ew")
    Topframe = Frame(root)
    Topframe.pack()
    Bottomframe = Frame(root)
    Bottomframe.pack()
    variable = StringVar(root)
    variable.set("Select Technique") # default value

    w1 = OptionMenu(root, variable, "Minimum Weight Triangluation", "Minimizing the Maximum of the Internal Angles", "Minimizing the Longest Edge", command = main_method)
    w1.config(width=50)
    w1.grid(row = 2, column = 0)
    w1.pack()

    Label2 = Label(Topframe, text = "Polygon Triangulation Optimization Techniques", font='Helvetica 26 bold', relief="ridge")
    Label2.config(height=2, width=100)
    Label2.grid(row = 0, column = 0)
    Label2.pack(fill=X, padx=30, pady=10)

    separator = Frame(height=2, bd=1, relief=SUNKEN)
    separator.pack(fill=X, padx=30, pady=10)

    Button2 = Button(Bottomframe, text = "Open File", command = openfile)
    Button2.grid(row = 10, column = 10)
    Button2.pack(side=BOTTOM)

    w = 1000
    h = 420

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.mainloop()

if __name__=='__main__':
    if len(sys.argv)>1:
        main.main(sys.argv[1], sys.argv[2])
    process()
