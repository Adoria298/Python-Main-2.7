#PercentageConverter
#Tkinter app to convert percentages with

from Tkinter import *

class porcentaje(Frame):

    def __init__(self, master):
        super(self, porcentaje).__init__(master)
        self.grid()
        self.mode = None
        self.create_widgets()

    def create_widgets(self):
        #create instruction label
        Label(self,
              text="Select to or from, depending if you want to go to a percentage, or from a percentage, then fill in the necessary informarion."
              ).grid(row=0, column=0, sticky=W)
              
        #create to/from radiobuttons
        RadioButton(self,
                    variable=self.mode,
                    value="TO").grid(row=1, column=0, sticky=W)
        Label(self,
              text="To"
              ).grid(row=1, column=0, sticky=E)

        RadioButton(self,
                    variable=self.mode,
                    value="FROM").grid(row=1, column=0, sticky=W)
        Label(self,
              text="From"
              ).grid(row=1, column=0, sticky=E)
        
