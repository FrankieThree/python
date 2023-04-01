####################################################################
# Name: Norman Cook
# Date: 08/09/2019
# Description: A calculator made using Python's Tkinter library that
#   that can add, subtract, multiply, divide, and modulous.
####################################################################
from Tkinter import *

# the main GUI
class MainGUI(Frame):
  # the constructor
  def __init__(self, parent):
    Frame.__init__(self, parent, bg="white")
    self.setupGUI()

  # sets up the GUI
  def setupGUI(self):

    # display
    self.display = Label(self, text="", anchor=E, bg = "white", height=2,\
                         width=15, font=("TexGyreAdventor", 50))
    self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)

    for row in range(7):
      Grid.rowconfigure(self, row, weight=1)
    for col in range(4):
      Grid.columnconfigure(self, col, weight=1)

    # (
    img = PhotoImage(file="images/lpr.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("("))
    button.image = img
    button.grid(row=1, column=0, sticky=N+S+E+W)

    # )
    img = PhotoImage(file="images/rpr.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process(")"))
    button.image = img
    button.grid(row=1, column=1, sticky=N+S+E+W)

    # AC
    img = PhotoImage(file="images/clr.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("AC"))
    button.image = img
    button.grid(row=1, column=2, sticky=N+S+E+W)

    # **
    img = PhotoImage(file="images/pow.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("**"))
    button.image = img
    button.grid(row=6, column=2, sticky=N+S+E+W)

    # 7
    img = PhotoImage(file="images/7.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("7"))
    button.image = img
    button.grid(row=2, column=0, sticky=N+S+E+W)

    # 8
    img = PhotoImage(file="images/8.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("8"))
    button.image = img
    button.grid(row=2, column=1, sticky=N+S+E+W)

    # 9
    img = PhotoImage(file="images/9.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("9"))
    button.image = img
    button.grid(row=2, column=2, sticky=N+S+E+W)

    # /
    img = PhotoImage(file="images/div.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("/"))
    button.image = img
    button.grid(row=2, column=3, sticky=N+S+E+W)

    # 4
    img = PhotoImage(file="images/4.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("4"))
    button.image = img
    button.grid(row=3, column=0, sticky=N+S+E+W)

    # 5
    img = PhotoImage(file="images/5.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("5"))
    button.image = img
    button.grid(row=3, column=1, sticky=N+S+E+W)

    # 6
    img = PhotoImage(file="images/6.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("6"))
    button.image = img
    button.grid(row=3, column=2, sticky=N+S+E+W)

    # *
    img = PhotoImage(file="images/mul.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("*"))
    button.image = img
    button.grid(row=3, column=3, sticky=N+S+E+W)

    # 1
    img = PhotoImage(file="images/1.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("1"))
    button.image = img
    button.grid(row=4, column=0, sticky=N+S+E+W)

    # 2
    img = PhotoImage(file="images/2.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("2"))
    button.image = img
    button.grid(row=4, column=1, sticky=N+S+E+W)

    # 3
    img = PhotoImage(file="images/3.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("3"))
    button.image = img
    button.grid(row=4, column=2, sticky=N+S+E+W)

    # -
    img = PhotoImage(file="images/sub.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("-"))
    button.image = img
    button.grid(row=4, column=3, sticky=N+S+E+W)

    # 0
    img = PhotoImage(file="images/0.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("0"))
    button.image = img
    button.grid(row=5, column=0, sticky=N+S+E+W)

    # .
    img = PhotoImage(file="images/dot.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("."))
    button.image = img
    button.grid(row=5, column=1, sticky=N+S+E+W)

    # =
    img = PhotoImage(file="images/eql-wide.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("="))
    button.image = img
    button.grid(row=6, columnspan=2, sticky=N+S+E+W)

    # +
    img = PhotoImage(file="images/add.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("+"))
    button.image = img
    button.grid(row=5, column=3, sticky=N+S+E+W)

    # %
    img = PhotoImage(file="images/mod.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("%"))
    button.image = img
    button.grid(row=6, column=3, sticky=N+S+E+W)

    self.pack(fill=BOTH, expand=1)

    # back button
    img = PhotoImage(file="images/bak.gif")
    button = Button(self, bg="white", image=img, borderwidth=0,\
                    highlightthickness=0, activebackground="white",\
                    command=lambda: self.process("BACK"))
    button.image = img
    button.grid(row=1, column=3, sticky=N+S+E+W)

    self.pack(fill=BOTH, expand=1)
    
  def process(self, button):
    if (button == "AC"):
      self.display["text"] = ""
    elif (button == "="):
      expr = self.display["text"]
      try:
        result = eval(expr)
        self.display["text"] = str(result)
      except:
        self.display["text"] = "ERROR"
    elif (button == "BACK"):
      if (self.display["text"][0:5] == "ERROR"):
        self.display["text"] = self.display["text"][5:len(self.display["text"])]
      self.display["text"] = self.display["text"][:-1]
    else:
      if (self.display["text"][0:5] == "ERROR"):
        self.display["text"] = self.display["text"][5:len(self.display["text"])]
      self.display["text"] += button


    if (len(self.display["text"]) > 14):
      self.display["text"] = self.display["text"][0:11] + "..."
      
##########################
# main part of the program
##########################

# create the window
window = Tk()

# set the window title
window.title("The Reckoner")

# generate the GUI
p = MainGUI(window)

# display the GUI and wait for user interaction
window.mainloop()
