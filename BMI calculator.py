from Tkinter import *

class calculadora(Frame):

    def __init__(self, master):
        super(calculadora, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.bmi = None
        self.message = None

    def create_widgets(self):
        #input
        weigth_lbl = Label(self, text="Weight:").grid(column=0, row=0, sticky =W)
        weight_entry = Entry(self).grid(column=1, row=0, sticky=W)
        
        height_lbl = Label(self, text="Height:").grid(column=2, row=0, sticky=E)
        height_entry = Entry(self).grid(column=0, row=3, sticky=E)

        #submit
        submit_bttn = Button(self,
                             text="Submit",
                             command=self.bmi).grid(column=0, row=2, sticky=W)

        #output space
        output_txt = Text(self, height=50, width=50).grid(column=0, row=4, columnspan=2, rowspan=2, sticky=W)

    def bmi(self):
        weight = float(weight_entry.get())
        height =float(height_entry.get())*float(height_entry.get())
        bmi =  weight/height
        str(bmi + "\n")

        if bmi<18.5:
            bmi += "You are underweight."
        elif bmi>18.5 and bmi<25:
            bmi += "You are in the normal range."
        elif bmi>25 and bmi<30:
            bmi += "You are overweight."
        elif bmi>30:
            bmi += "You are obese."

        message ="BMI: " + bmi
        #return values
        output_txt.delete(0.0, END)
        output_txt.insert(0.0, message)

root = Tk()
root.title("BMI Calculator 1.0")
app = calculadora(root)
root.mainloop()

        
