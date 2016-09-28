""" Name: Min Khant Tin
    Date: 22/9/2016
    Brief Program Details: This is GUI for the Shopping List Program
    Link: https://github.com/minkhanttin123/CP1404-Assignment-2 """

from kivy.app import App #This Import kivy app function
from kivy.lang import Builder #This Import kivy builder function



file = open("items2.txt", "r") #open the file containing the shopping items
for line in file:
    x = line.split(",") #split the data by commas


class shoppinglist(App): #Class for the shoppinglist App


    def build(self):   #Here the ShoppingList.kv is loaded with it BoxLayout
        self.title = "Shopping List"
        self.root = Builder.load_file('ShoppingList.kv')
        return self.root

    def req(self):  #Show the require item from the csv list
        self.root.ids.item1.text = x[0]
        self.root.ids.item2.text = x[4]
        self.root.ids.item3.text = x[8]
        self.root.ids.status_bar.text = "Click items to mark item as completed"

    def comp1(self): #Whec click the item will be marked as completed
        self.root.ids.item1.background_color = (1,1,1,1)
        self.root.ids.status_bar.text = x[0]+" $" + x[1] + "  Priority " + x[2]+ "  " + "Completed"
        self.root.ids.header.text = " $" + x[1]

    def comp2(self):
        self.root.ids.item2.background_color = (1,1,1,1)
        self.root.ids.status_bar.text = x[4]+ "  $" + x[5] + "  Priority " + x[6]+ "  " + "Completed"
        self.root.ids.header.text = " $" + x[5]

    def comp3(self):
        self.root.ids.item3.background_color = (1,1,1,1)
        self.root.ids.status_bar.text = x[8]+ "  $" + x[9] + "  Priority " + x[10]+ "  " + "Completed"
        self.root.ids.header.text = " $" + x[9]

    def add_list(self): #Allow the user to add more item

        if self.root.ids.name.text == "":
                self.root.ids.status_bar.text = "Name cannot be blank"
        else:
            self.root.ids.item_new.background_color = (10, 1, 10, 1)
            self.root.ids.item_new.size_hint_y = 1
            self.root.ids.item_new.font_size=20
            self.root.ids.item_new.text = self.root.ids.name.text
            self.root.ids.status_bar.text = self.root.ids.name.text + "  $" + self.root.ids.price.text + "  Priority " + self.root.ids.priority.text + " is Added"

    def comp4(self):
        self.root.ids.item_new.background_color = (1,1,1,1)
        self.root.ids.status_bar.text = self.root.ids.name.text+ "  $" + self.root.ids.price.text + "  Priority " + self.root.ids.priority.text+ "  " + "Completed"
        self.root.ids.header.text = "  $" + self.root.ids.price.text

    def clearbox(self): #Clear the name, price & priority boxes
        self.root.ids.name.text = ''
        self.root.ids.price.text = ''
        self.root.ids.priority.text= ''


shoppinglist().run() #run the program!