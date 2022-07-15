from tkinter import *

names_list = []

class BudgetIntro:
    def __init__(self, parent):
        background_color = "plum1"
        #setting up first frame
        self.budget_frame = Frame(parent,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.budget_frame.grid()

        #Label widget for our heading
        self.heading_label = Label(self.budget_frame,
                                   text = "This app will help you budget!",
                                   bg=background_color)
        self.heading_label.grid(row=0, padx=20)

        #creates a label to ask for the name
        self.user_label = Label(self.budget_frame,
                                text="Enter your name to begin this journey...",
                                bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20)

        #create an entry box for the name
        self.entry_box = Entry(self.budget_frame)
        self.entry_box.grid(row=2, padx=20, pady=25)

        #create a Button - continue button
        self.continue_button = Button(self.budget_frame,
                                      text="Continue",
                                      font=("Arial", "13"),
                                      bg="SpringGreen2",
                                      command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)

    def name_collection(self):
        name = self.entry_box.get()  #this will collect the name from the entry box
        names_list.append(name)  #adds the user name to names list declared at the beginning
        self.budget_frame.destroy()  #this will destroy the starter window



####### program start ##########

if __name__ == "__main__":
    root = Tk()
    root.title("Budgeting Tool")
    BudgetIntro_object = BudgetIntro(root)
    root.mainloop() #This loops the window for to it stay and not disappear.