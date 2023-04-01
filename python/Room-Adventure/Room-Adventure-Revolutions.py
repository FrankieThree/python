####################################################################
# Name: Norman Cook
# Date: 7/29/2019
# Description: A simple point and click video game made entirely in
#   python. There are normal items, grabbable items, hidden doors, 
#   keys, and locks. You're goal is to find a way out of the house
#   through the front door.
####################################################################
from Tkinter import *

# the room class
class Room(object):
  # the constructor
  def __init__(self, name, image):
    # rooms have a name, an image (the name of a file),
    # exits, exit locations, items, item locations,
    # item description and grabbables
    self.name = name
    self.image = image
    self.lock = []
    self.exits = {}
    self.hidden = {}
    self.items = {}
    self.grabbables = []

  # getters and setters for the instance variables
  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value

  @property
  def image(self):
    return self._image

  @image.setter
  def image(self, value):
    self._image = value

  @property
  def exits(self):
    return self._exits

  @exits.setter
  def exits(self, value):
    self._exits = value

  @property
  def items(self):
    return self._items

  @items.setter
  def items(self, value):
    self._items = value

  @property
  def grabbables(self):
    return self._grabbables

  @grabbables.setter
  def grabbables(self, value):
    self._grabbables = value

  @property
  def lock(self):
    return self._lock

  @lock.setter
  def lock(self, value):
    self._lock = value

  @property
  def hidden(self):
    return self._hidden

  @hidden.setter
  def hidden(self, value):
    self._hidden = value

  # adds an exit to the room
  # the exit is a string and the room is an instance of a room
  def addExit(self, exit, room):
    # append the exit and room to the appropriate dictionary
    self._exits[exit] = room

  # adds an item to the room
  # the item is a string and the desc is a description of the item
  def addItem(self, item, desc):
    # append the item and description to the appropriate dictionary
    self._items[item] = desc

  # adds a grabbable item to the room
  # the item is a string
  def addGrabbable(self, item):
    # append the item to the list and description appropriately
    self._grabbables.append(item)

  # removes a grabbable item from the room
  # the item is a string
  def delGrabbable(self, item):
    # remove the item from the list
    self._grabbables.remove(item)

  # returns a string description of the room
  def __str__(self):
    s = "-------------------------------------------------"
    
    # the room name
    s += "\nYou are in {}.\n".format(self.name)
    
    # the items in the room
    s += "You see:  "
    for item in self.items:
      s += item + "  "
    s += "\n"
    
    # the exits from the room
    s += "Exits:  "
    for exit in self.exits:
      s += exit + "  "

    s += "\n-------------------------------------------------"

    return s

  # add a lock to a room
  def addLock(self, value):
    self._lock.append(value)

  # delete lock to a room
  def delLock(self, value):
    self._lock.remove(value)

  def addHidden(self, hidden, room):
    # append the exit and room to the appropriate dictionary
    self._hidden[hidden] = room

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
  # the constructor
  def __init__(self, parent):
    # call the constructor in the superclass
    Frame.__init__(self, parent)

  # creates the rooms
  def createRooms(self):
    # r1 through r4 are the four rooms in the mansion
    # currentRoom is the room the player is currently in (which
    # can be one of r1 through r4)

    # create the rooms and give them meaningful names and images
    r1 = Room("Room 1", "room1.gif")
    r2 = Room("Room 2", "room2.gif")
    r3 = Room("Room 3", "room3.gif")
    r4 = Room("Room 4", "room4.gif")
    r5 = Room("Room 5", "room5.gif")
    r6 = Room("Room 6", "room6.gif")
    r7 = Room("Room 7", "room7.gif")
    r8 = Room("Room 8", "room8.gif")
    r9 = Room("Room 9", "room9.gif")
    r10 = Room("Room 10", "room10.gif")
    r11 = Room("Room 11", "room11.gif")
    r12 = Room("Room 12", "room12.gif")
    r13 = Room("Room 13", "room13.gif")
    r14 = Room("Room 14", "room14.gif")

    # add exits to room 1
    r1.addExit("south", r3)
    r1.addExit("east", r2)
    # add grabbables to room 1
    r1.addGrabbable("bread")
    r1.addGrabbable("kettle")
    # add items to room 1
    r1.addItem("stove", "A black stove powered by charcoal. A kettle rests \non top.")
    r1.addItem("oven", "A small oven is against the north wall.")
    r1.addItem("counter", "A stone countertop with bread and knives on its \nsurface.")

    # add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r5)
    # add items to room 2
    r2.addItem("chandelier", "A massive intricate design hanging above this \nlarge ballroom.")
    r2.addItem("wall", "A spot on the north wall is out of place. \nThere is a key hole here!")
    # add hidden room
    r2.addHidden("down", r12)
    # add lock to room 12
    r2.addLock("gold_key")

    # add exits to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    # add grabbables to room 3
    r3.addGrabbable("candle")
    # add items to room 3
    r3.addItem("table", "A table made of maple that could seat 12 people. \nAn unlit candle sits at the center.")
    r3.addItem("chairs", "Seven chairs made of maple sit around the table.")
    r3.addItem("silverware", "The table is set as if a feast is about to be \nserved.")

    # add exits to room 4
    r4.addExit("west", r3)
    r4.addExit("east", r5)
    r4.addExit("up", r7)
    # add items to room 4
    r4.addItem("door", "The front door to the mansion. \nI have to get out of here.")
    r4.addItem("staircase", "There are stairs leading to the second floor.")
    # add hidden room
    r4.addHidden("south", None)
    # add a lock to room 4
    r4.addLock("silver_key")

    # add exits to room 5
    r5.addExit("north", r2)
    r5.addExit("west", r4)
    # add items to room 5
    r5.addItem("piano", "It's a little out of tune... and dusty.")
    r5.addItem("couch", "The fabric is rough but it looks nice \nwith the room.")

    # add exits to room 6
    r6.addExit("east", r7)
    r6.addExit("south", r9)
    # add grabbables to room 6
    r6.addGrabbable("eight_ball")
    # add items to room 6
    r6.addItem("billiards", "The balls are set at the far end \nof the table.")
    r6.addItem("sticks", "Sticks are spread around the room.")

    # add exits to room 7
    r7.addExit("west", r6)
    r7.addExit("east", r8)
    r7.addExit("down", r4)
    # add items to room 7
    r7.addItem("staircase", "There are stairs back to the first floor.")

    # add exits to room 8
    r8.addExit("west", r7)
    r8.addExit("south", r10)
    # add grabbables to room 8
    r8.addGrabbable("book")
    r8.addGrabbable("map")
    # add items to room 8
    r8.addItem("bookshelves", "Grand bookshelves are against the walls.")
    r8.addItem("table", "There is a table at the center with open \nbooks and maps.")

    # add exits to room 9
    r9.addExit("north", r6)
    r9.addExit("east", r10)
    # add items to room 9
    r9.addItem("rug", "A black bear's coat. ...the face is haunting")
    r9.addItem("fireplace", "There are still embers in the ashes.")
    r9.addItem("lion", "Such majesty.")

    # add exits to room 10
    r10.addExit("north", r8)
    r10.addExit("west", r9)
    # add grabbables to room 10
    r10.addGrabbable("notes")
    r10.addGrabbable("gold_key")
    # add items to room 10
    r10.addItem("desk", "A nameplate that reads 'Dr. Gourd' and notes lie next to it. \nA gold key is next to it!")
    r10.addItem("chair", "A leather chair is behind the desk.")
    r10.addItem("statue", "A marble statue of Dr. cherry's face?")

    # add exits to room 11
    r11.addExit("east", r12)
    r11.addExit("south", r13)
    # add grabbables to room 11
    r11.addGrabbable("blueprint")
    r11.addGrabbable("silver_key")
    # add items to room 11
    r11.addItem("laboratory", "The whole room has been repurposed and filled \nwith unknown equipment.")
    r11.addItem("equipment", "Black screens stare back at you above the \nalphabet. There is a silver key here!")
    r11.addItem("blueprints", "Plans to release a game on 'steam.'")

    # add exits to room 12
    r12.addExit("up", r2)
    r12.addExit("west", r11)
    r12.addExit("south", r14)
    # add grabbables to room 12
    r12.addGrabbable("wine")
    # add items to room 12
    r12.addItem("barrels", "Barrels of wine line most of the walls.")
    r12.addItem("wine", "Wine bottles are scattered across the floor.")

    # add exits to room 13
    r13.addExit("north", r11)
    r13.addExit("east", r14)
    # add items to room 13
    r13.addItem("unknown", "..It's human but not, and it is made of metal. \n...I don't think it's alive.")

    # add exits to room 14
    r14.addExit("north", r12)
    r14.addExit("west", r13)
    # add grabbable
    r14.addGrabbable("6_pack")
    # add items to room 14
    r14.addItem("distillery", "Dr. Gourd has been brewing something. There \nis a 6-pack on the ground.")

    # set room 1 as the current room
    Game.currentRoom = r4

    # initialize the player's inventory
    Game.inventory = []

  # sets up the GUI
  def setupGUI(self):
    # organize the GUI
    self.pack(fill=BOTH, expand=1)

    # setup the player input at the bottom of the GUI
    # the widget is a Tkinter Entry
    # set its background to white and bind the return key to the
    # function process in the class
    # push it to the bottom of the GUI and let it fill
    # horizontally
    # give it focus so the player doesn't have ot click on it
    Game.player_input = Entry(self, bg="white")
    Game.player_input.bind("<Return>", self.process)
    Game.player_input.pack(side=BOTTOM, fill=X)
    Game.player_input.focus()

    # setup the image to the left of the GUI
    # the widget is a Tkinter label
    # don't let the image control the widget's size
    img = None
    Game.image = Label(self, width=WIDTH / 2, image=img)
    Game.image.image = img
    Game.image.pack(side=LEFT, fill=Y)
    Game.image.pack_propagate(False)

    # setup the text to the right of the GUI
    # first, the frame in which the text will be place
    text_frame = Frame(self, width=WIDTH / 2)
    # the widget is a Tkinter Text
    # disable it by default
    # don't let the widget control the frame's size
    Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
    Game.text.pack(fill=Y, expand=Y)
    text_frame.pack(side=RIGHT, fill=Y)
    text_frame.pack_propagate(False)

  # set the current room image
  def setRoomImage(self):
    if (Game.currentRoom == None):
      # if dead, set the skull image
      Game.img = PhotoImage(file="skull.gif")
    else:
      # otherwise grab the image for the current room
      Game.img = PhotoImage(file=Game.currentRoom.image)

    # display the image on the left of the GUI
    Game.image.config(image=Game.img)
    Game.image.image = Game.img

  # sets the status displayed on the right of the GUI
  def setStatus(self, status):
    # enable the text widget, clear it, set it, and disabled it
    Game.text.config(state=NORMAL)
    Game.text.delete("1.0", END)
    if (Game.currentRoom == None):
      # if dead, let the player know
      Game.text.insert(END, "Dr.Gourd was waiting outside the whole time! \nNo one can escape! \nThe only thing you can do now is quit.\n")
    else:
      # otherwise, display the appropriate status
      Game.text.insert(END, str(Game.currentRoom) +\
                       "\nYou are carrying: " + str(Game.inventory) +\
                       "\n\n" + status)
      Game.text.config(state=DISABLED)

  # play the game
  def play(self):
    # add the rooms to the game
    self.createRooms()
    # configure the GUI
    self.setupGUI()
    # set the current room
    self.setRoomImage()
    # set the current status
    self.setStatus("")

  # processes the player's input
  def process(self, event):
    # grab the player's input from the input at the bottom of
    # the GUI
    action = Game.player_input.get()
    # set the user's input to lowercase to make it easier to
    # compare the verb and noun to known values
    action = action.lower()
    # set a default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, use, and take."

    # exit the game if the player wants to leave (supports quit
    # exit, and bye)
    if (action == "quit" or action == "exit" or action == "bye"\
        or action == "sionara!"):
      exit(0)

    # if the player is dead if goes/went south from room 4
    if (Game.currentRoom == None):
      # clear the player's input
      Game.player_input.delete(0, END)
      return

    # split the user input into words (words are separated by
    # spaces) and stare the words in a list
    words = action.split()

    # the game only understands two word inputs
    if (len(words) == 2):
      # isolate the verb and noun
      verb = words[0]
      noun = words[1]

      # the verb is: go
      if (verb == "go"):
        # set a default respons
        response = "Invalid exit."

        # check for valid exits in the current room
        if (noun in Game.currentRoom.exits):
            # if one is found, change the current room to
            # the one that is associated with the
            # specified exit
            Game.currentRoom = Game.currentRoom.exits[noun]
            # set the response (success)
            response = "Room changed."

      # the verb is: look
      elif (verb == "look"):
        # set a default response
        response = "I don't see that item."

        # check for valid items in the current room
        if (noun in Game.currentRoom.items):
          # if one is found, set the response to the
          # item's description
          response = Game.currentRoom.items[noun]

      # the verb is: take
      elif (verb == "take"):
        # set a default response
        response = "I don't see that item."

        # check for valid grabbable items in the current room
        for grabbable in Game.currentRoom.grabbables:
          # a valid grabbable item is found
          if (noun == grabbable):
            # add the grabbable item to the player's inventory
            Game.inventory.append(grabbable)
            # remove the grabbable item from the room
            Game.currentRoom.delGrabbable(grabbable)
            # set the response (success)
            response = "Item grabbed."
            # no need to check any more grabbable items
            break

      # the verb is: use
      elif (verb == "use"):
        # set a default response
        response = "I don't have that item."

        # check if item is in the inventory
        for item in Game.inventory:
          if (item == noun):
            # set the response
            response = "This item cannot be used here."

        # check if the item can unlock a door in the current room
        if (len(Game.currentRoom.lock) > 0):
          if (Game.currentRoom.lock[0] == noun):
            response = "A door unlocks!"
            Game.currentRoom.exits.update(Game.currentRoom.hidden)

    # display the response on the right of the GUI
    # display the room's image on the left of the GUI
    # clear the player's input
    self.setStatus(response)
    self.setRoomImage()
    Game.player_input.delete(0, END)

#########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
