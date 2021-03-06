#Version 5 of budget tool by Mohammad Tousif Kabir - 2022 Lvl 3 Computer Science Project 
#This version implements design and fixes bugs
#Uses pack instead of grid

from tkinter import * #For GUI
from tkinter import messagebox #This is to produce the error box
import math #Will be using this to count number of digits to limit large entries; boundary testing
import webbrowser #This is needed to launch the user to certain websites

#income list, takes user income and appends to this list
income_list = []

#expenses list: living expenses, everyday expenses and irregular expenses
#Each class will append expenses to expenses lists respectively
living_expenses_list = [] #monthly so x12
everyday_expenses_list = [] #monthly so x12
irregular_expenses_list = [] #yearly so x1(no need to multiply)


#The introduction class, or the landing screen
class BudgetIntro:
    def __init__(self, parent):

        #Setting the background colour
        background_color = "#fcdf95"
        
        #setting up first frame
        self.budget_frame = Frame(parent,
                                bg = background_color,
                                padx = 100,
                                pady = 100)
        self.budget_frame.pack(fill = "both", expand = True)

        #Simply a title label with the text below:
        self.title_label = Label(self.budget_frame, text = "Budgeting Tool", 
                                bg = background_color, 
                                font = ("Open Sans", 30))
        self.title_label.pack()

        self.title_label1 = Label(self.budget_frame, text = "This app will give you an idea of your spending.", 
                                bg = background_color, 
                                font = ("Open Sans", 18), pady = 40)
        self.title_label1.pack()       
        
        #Creating the register button
        self.register_button = Button(self.budget_frame, text = "Register", bg = "orange", font = ("Open Sans",15), width = 15, command = self.register_continue)
        self.register_button.pack(pady = 10)

        #Creating the login button
        self.login_button = Button(self.budget_frame, text = "Login", bg = "#69e051", fg = "white",
                                  font = ("Open Sans", 15), width = 15,
                                  command = self.login_continue)
        self.login_button.pack()
        
        #Creating the privacy policy button
        self.privacy_button = Button(self.budget_frame, text = "Privacy Policy", bg = "#2234d6", fg = "white",
                                    font = ("Open Sans", 15), width = 15,
                                    command = self.pp)
        self.privacy_button.pack(pady = 10)

        
    #Will run the privacy policy class and destroy the quiz frame or the introduction page
    def pp(self):
        self.budget_frame.destroy()
        PrivacyPolicy(root)
    
    #Will move on to the login class so they can login
    def login_continue(self):
        self.budget_frame.destroy()
        Login(root)

    #will move on to the register class so they can register
    def register_continue(self):
        self.budget_frame.destroy()
        Register(root)

#Class for the privacy policy of my program
class PrivacyPolicy:
    def __init__(self, parent):
        
        #Setting the background colour
        background_color = "#fcdf95"

        self.pp_frame = Frame(parent, bg = background_color, padx = 30, pady = 50)
        self.pp_frame.pack(fill = "both", expand = True) #creating the frame

        self.pp_heading = Label(self.pp_frame, text = "   Privacy Policy   ", font = ("Open Sans", 30), bg = background_color, pady = 15)
        self.pp_heading.pack() #setting the heading to privacy policy so the user knows it's the privacy policy page

        #pp_info 1, 2 and 3 display what I want the privacy policy to state
        self.pp_info1 = Label(self.pp_frame, text = "This privacy policy explains the privacy practices of this program. This program was created by Tousif Kabir.", font = ("Open Sans", 14), bg = background_color, pady = 5)
        self.pp_info1.pack()

        self.pp_info1 = Label(self.pp_frame, text = "I created this program for my level 3 computer science internal. I do not intend on making this program commercial.", font = ("Open Sans", 14), bg = background_color, pady = 5)
        self.pp_info1.pack()

        self.pp_info2 = Label(self.pp_frame, text = "No data is stored or shared. The code for this project can also be found on GitHub.", font = ("Open Sans", 14), bg = background_color, pady = 5)
        self.pp_info2.pack()

        #This is a back button which will bring the user back to the introduction page
        self.ppback_button = Button(self.pp_frame, text = " Back ", width = 15, bg = "orange", font = ("Open Sans", 15), command = self.privacy_policy_back)
        self.ppback_button.pack(pady = 15)

        #An exit button which allows the user to exit the app
        self.exit_button = Button(self.pp_frame, text = "Exit", width = 15, bg = "Red", font = ("Open Sans", 15), command = self.close_end)
        self.exit_button.pack(pady = 10)

    #the function to go back to the introduction component
    def privacy_policy_back(self):
        self.pp_frame.destroy()  #this will destroy the window
        BudgetIntro(root)  #Makes my app display the introduction component(landing screen)

    #function which closes app
    def close_end(self):
        self.pp_frame.destroy() #this will destroy the window
        root.destroy() #closes entire app

#Creating the register page
class Register:
    def __init__(self, parent):    
        
        #setting the background colour
        background_color = "#fcdf95"

        #setting up the frame
        self.register_frame = Frame(parent,
                                bg = background_color,
                                padx = 100,
                                pady = 25)
        self.register_frame.pack(fill = "both", expand = True)

        #Simply a title label with the text below:
        self.title_label = Label(self.register_frame, text = "Registration Page", 
                                bg = "#fcdf95", 
                                font = ("Open Sans", 30))
        self.title_label.pack()

        #These are a label and an entry. The label for "username". The entry box so the user can type their username
        self.reg_name_label = Label(self.register_frame, text = "Username:", font = ("Open Sans", 25), bg = background_color,)
        self.reg_name_label.pack()
        self.reg_name_entry = Entry(self.register_frame, width = 25, bd = 5, font = ("Open Sans", 15))
        self.reg_name_entry.pack()
        
        #These are a label and an entry. The label for "password". The entry box so the user can type their password
        self.reg_password_label = Label(self.register_frame, text = "Password:", font = ("Open Sans", 25), bg = background_color,)
        self.reg_password_label.pack()
        self.reg_password_entry = Entry(self.register_frame, width = 25, show = "*", bd = 5 , font = ("Open Sans", 15))
        self.reg_password_entry.pack()

        #These are a label and an entry. The label for "confirm password". The entry box so the user can type their password again    
        self.confirm_password_label = Label(self.register_frame, text = "Confirm Password:", font = ("Open Sans", 25), bg = background_color)
        self.confirm_password_label.pack()
        self.confirm_password_entry = Entry(self.register_frame, width = 25, show = "*", bd = 5 , font = ("Open Sans", 15))
        self.confirm_password_entry.pack()
        
        #creating the register button which will run the check function
        self.register_button = Button(self.register_frame, text = "Sign up", font = ("Open Sans", 15), width = 15, bg = "#69e051", fg = "white", command = self.check)
        self.register_button.pack(pady = 10)

        #This is a back button which will bring the user back to the introduction page
        self.regback_button = Button(self.register_frame, text = " Back ", width = 15, bg = "orange", font = ("Open Sans", 15), command = self.registry_back)
        self.regback_button.pack(pady = 15)
            
    #the check function does two things:
    #A) It makes sure all fields are filled
    #B) It checks if the "confirm password" entry and the "password" entry are the same
    def check(self):
        #The following line ensures there's no blanks
        if self.reg_name_entry.get() != "" and self.reg_password_entry.get() != "" and self.confirm_password_entry.get() != "":
            #If the following entries match, then execute
            if self.reg_password_entry.get() == self.confirm_password_entry.get():
                #opens the following txt file to write to (add user entry)
                with open("testfile.txt", "a") as f:
                    #writes the username and user password seperated by ","
                    f.write(self.reg_name_entry.get()+","+self.reg_password_entry.get()+"\n")
                    #displays a messagebox with the following text
                    messagebox.showinfo("Welcome","You are registered successfully!")
                    #destroys the frame and displays the login component
                    self.register_frame.destroy()
                    Login(root)
            #else, if the two entries don't match
            else:
                messagebox.showinfo("Error","Your passwords didn't get match!")
        #else, if fields are left empty
        else:
            messagebox.showinfo("Error", "Please complete all required fields!")
    
    #the function to go back to the introduction component
    def registry_back(self):
        self.register_frame.destroy()  #this will destroy the window
        BudgetIntro(root)  #Makes my app display the introduction component(landing screen)

#the login component
class Login:
    def __init__(self, parent):        
        
        #setting the background colour
        background_color = "#fcdf95"

        #setting up the frame
        self.login_frame = Frame(parent,
                                bg = background_color,
                                padx = 100,
                                pady = 25)
        self.login_frame.pack(fill = "both", expand = True)

        #Simply a title label with the text below:
        self.title_label = Label(self.login_frame, text = "Login Page", 
                                bg = background_color, 
                                font = ("Open Sans", 30))
        self.title_label.pack(pady = 20)

        #user label and entry for username        
        self.user_label = Label(self.login_frame, text = "Username", font = ("Open Sans Bold", 25), bg = background_color)
        self.user_label.pack(pady = 5)
        self.user_entry = Entry(self.login_frame, width = 30, bd = 5, font = ("Open Sans", 15))
        self.user_entry.pack()

        #user label and entry for password
        self.password_label = Label(self.login_frame, text = "Password", font = ("Open Sans Bold", 25), bg = background_color)
        self.password_label.pack()
        self.password_entry = Entry(self.login_frame, width = 30, show = '*', bd = 5, font=("Open Sans", 15))
        self.password_entry.pack(pady = 5)
        
        #submit button which runs the verification function
        self.submitbutton = Button(self.login_frame, text = "Submit", font = ("Open Sans", 15), width = 15, bg = "#69e051", fg = "white", command = self.verification)
        self.submitbutton.pack(pady = 5)

        #This is a back button which will bring the user back to the introduction page
        self.logback_button = Button(self.login_frame, text = " Back ", width = 15, bg = "orange", font = ("Open Sans", 15), command = self.log_back)
        self.logback_button.pack(pady = 15)

    #verification function, primary job is match user entries with data in the txt file            
    def verification(self):
        #The try block lets us test a block of code for errors.
        try:
            #opens the txt file
            with open("testfile.txt", "r") as f:
                #The readlines() method returns a list containing each line in the file as a list item.
                info = f.readlines()
                i = 0
                for e in info:
                    self.user_name, self.user_password =e.split(",") #Splits the username and password using ","
                    #if file password/username match with entrybox password/username, then allows access
                    if self.user_name.strip() == self.user_entry.get() and self.user_password.strip() == self.password_entry.get():
                        #destroys login frame
                        self.login_frame.destroy()
                        #runs the Budgeter Income class
                        BudgeterInc(root)
                        i = 1
                        messagebox.showinfo("Welcome", "Password and Username accepted.") #runs a messagebox with the given text
                        break #'Break' in Python is a loop control statement.

                if i == 0: #If it doesn't match, then the following dialouge will be provided
                    messagebox.showinfo("Error", "Please provide correct username and password!")
        #The except block lets us handle the error
        except:
            messagebox.showerror("Error", "Could not open file") #runs a messagebox with the given text

    #the function to go back to the introduction component
    def log_back(self):
        self.login_frame.destroy()  #this will destroy the window
        BudgetIntro(root)  #Makes my app display the introduction component(landing screen)


#Start of the main components, BudgeterInc = Budgeter Income, which mainly gathers user's disposable income
class BudgeterInc: 
    def __init__(self, parent):
        
        #setting the background colour
        background_color = "#fcdf95"

        #setting up the frame
        self.income_frame = Frame(parent,
                                bg = background_color,
                                padx = 100,
                                pady = 25)
        self.income_frame.pack(fill = "both", expand = True)

        #title label
        self.title_label = Label(self.income_frame, text = "Prerequisites", bg = background_color, font = ("Open Sans Bold", 25))
        self.title_label.pack(pady = 10)

        #label with following text
        self.inc_info1 = Label(self.income_frame, text = "This budgeting tool uses NZD. Please use appropriate number of integers.", font = ("Open Sans", 14), bg = background_color, pady = 5)
        self.inc_info1.pack(pady = 10)

        #label with following text which asks for user's disposable income
        self.inc_info2 = Label(self.income_frame, text = "What is your disposable income ($)?", font = ("Open Sans", 14), bg = background_color, pady = 5)
        self.inc_info2.pack(pady = 10)

        #Entry box so the user can answer
        self.entry_box = Entry(self.income_frame, width = 35, font = ("Open Sans", "15"))
        self.entry_box.pack(pady = 10)

        #continue button with the income_collection function
        self.continue_button = Button(self.income_frame, text="Continue", font = ("Open Sans", 15), width = 15, bg = "#69e051", fg = "white", command = self.income_collection)
        self.continue_button.pack(pady = 5)
    
    #this function appends the user's income to the income list declared at the beginning
    def income_collection(self):
        #The try block lets us test a block of code for errors.
        try:
            income = int(self.entry_box.get())  #this will collect the income from the entry box in the form of an integer
            if int((math.log10(income)))+1 > 3 and int((math.log10(income)))+1 < 8: #Boundary testing, the income has to be between 3 and 8 characters, using math.log10 this is possible
                income_list.append(income)  #adds the user income to income list declared at the beginning
                self.income_frame.destroy()  #this will destroy the income_frame
                BudgeterLE(root) #shows the living expenses frame

            #if the income is less than or equal to 3 or greater than or equal to 8 characters, returns the error message below
            else:
                messagebox.showerror(" Error", "Your income must be between 4-7 digits! ")
        
        #The except block lets us handle the error
        except:
            messagebox.showinfo("Warning", "Please respond with digits only.") #runs a messagebox with the given text


#This is the BudgetLE class which asks for living expenses
class BudgeterLE:
    def __init__(self, parent):
        
        #setting the background colour
        background_color = "#fcdf95"

        #setting up the frame
        self.le_frame = Frame(parent,
                                bg = background_color,
                                padx = 100,
                                pady = 25)
        self.le_frame.pack(fill = "both", expand = True)

        #label for title
        self.title_label = Label(self.le_frame, text = "Living expenses", bg = background_color, font = ("Open Sans Bold", 30))
        self.title_label.pack(pady = 10)
        
        #rent/mortgage expense
        self.le_info1 = Label(self.le_frame, text = "What is your rent/mortage (monthly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.le_info1.pack()
        #rent/mortgage expense entry
        self.entry_box1 = Entry(self.le_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box1.pack()

        #power expense
        self.le_info2 = Label(self.le_frame, text = "What is your power bill (monthly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.le_info2.pack()
        #power expense entry
        self.entry_box2 = Entry(self.le_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box2.pack()

        #water expense
        self.le_info3 = Label(self.le_frame, text = "What is your water bill (monthly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.le_info3.pack()
        #water expense entry
        self.entry_box3 = Entry(self.le_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box3.pack()

        #internet/home phone expense
        self.le_info4 = Label(self.le_frame, text = "What is your internet/home phone expense (monthly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.le_info4.pack()
        #internet/home phone expense entry
        self.entry_box4 = Entry(self.le_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box4.pack()

        #laundry/drycleaning expense
        self.le_info5 = Label(self.le_frame, text = "What is your laundry/drycleaning expense (monthly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.le_info5.pack()
        #laundry/drycleaning expense entry
        self.entry_box5 = Entry(self.le_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box5.pack()

        #mobile phone expense
        self.le_info6 = Label(self.le_frame, text = "What is your mobile phone expense (monthly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.le_info6.pack()
        #mobile phone expense entry
        self.entry_box6 = Entry(self.le_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box6.pack()

        #continue button with the function living_expenses_collection
        self.continue_button = Button(self.le_frame, text = "Continue", font = ("Open Sans", 15), width = 15, bg = "#69e051", fg = "white", command = self.living_expenses_collection)
        self.continue_button.pack(pady = 15)

        #back button which goes back to previous page(income page)
        self.back_button = Button(self.le_frame, text = "Back", font = ("Open Sans", 15), width = 15, bg = "orange", command = self.remove_previous_income)
        self.back_button.pack()

    #This will collect the user's living_expenses from the entry box
    def living_expenses_collection(self): 
        #The try block lets us test a block of code for errors.
        try:
            #the following variables get the user entries and converts to integer
            housing_expense = int(self.entry_box1.get())
            power_expense = int(self.entry_box2.get())
            water_expense = int(self.entry_box3.get())
            internet_expense = int(self.entry_box4.get())
            laundry_expense = int(self.entry_box5.get())
            mobile_expense = int(self.entry_box6.get())

            #boundary testing, setting specific allowed digits for each expense using math.log10
            if int((math.log10(housing_expense)))+1 > 2 and int((math.log10(housing_expense)))+1 < 5 and int((math.log10(power_expense)))+1 > 1 and int((math.log10(power_expense)))+1 < 5 and int((math.log10(water_expense)))+1 > 1 and int((math.log10(water_expense)))+1 < 4 and int((math.log10(internet_expense)))+1 > 1 and int((math.log10(internet_expense)))+1 < 4 and int((math.log10(laundry_expense)))+1 > 1 and int((math.log10(laundry_expense)))+1 < 4 and int((math.log10(mobile_expense)))+1 > 1 and int((math.log10(mobile_expense)))+1 < 4:
                #adds each entry to the living_expenses_list declared at the beginning
                living_expenses_list.append(housing_expense)
                living_expenses_list.append(power_expense)
                living_expenses_list.append(water_expense)
                living_expenses_list.append(internet_expense)
                living_expenses_list.append(laundry_expense)
                living_expenses_list.append(mobile_expense)

                #destroys the living expenses frame and proceeds to the everyday expenses class
                self.le_frame.destroy()
                BudgeterEE(root)

            #if the entry boxes aren't filled properly, returns the error message below
            else:
                messagebox.showerror(" Error", "Use appropriate figures. ")

        #The except block lets us handle the error
        except:
            messagebox.showinfo("Warning", "Please fill all boxes and respond with digits only.") #runs a messagebox with the given text


    #removing previous stated income so it doesn't double record and goes back to previous class(BudgeterInc)
    def remove_previous_income(self):
        income_list.clear()
        self.le_frame.destroy()
        BudgeterInc(root)


#Everyday expenses class
class BudgeterEE:
    def __init__(self, parent):
        
        #setting background colour
        background_color = "#fcdf95"

        #setting up the frame
        self.ee_frame = Frame(parent,
                                bg = background_color,
                                padx = 100,
                                pady = 25)
        self.ee_frame.pack(fill = "both", expand = True)

        #label for the title
        self.title_label = Label(self.ee_frame, text = "Everyday expenses", bg = background_color, font = ("Open Sans Bold", 30))
        self.title_label.pack(pady = 10)
        
        #fuel expense
        self.ee_info7 = Label(self.ee_frame, text = "What is your fuel expense (monthly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.ee_info7.pack()
        #fuel expense entry
        self.entry_box7 = Entry(self.ee_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box7.pack()

        #groceries expense
        self.ee_info8 = Label(self.ee_frame, text = "What is your groceries expense (monthly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.ee_info8.pack()
        #groceries expense entry
        self.entry_box8 = Entry(self.ee_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box8.pack()

        #takeaways expense
        self.ee_info9 = Label(self.ee_frame, text = "What is your takeaways expense (monthly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.ee_info9.pack()
        #takeaways expense entry
        self.entry_box9 = Entry(self.ee_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box9.pack()

        #entertainment expense
        self.ee_info10 = Label(self.ee_frame, text = "What is your entertainment expense (monthly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.ee_info10.pack()
        #entertainment expense entry
        self.entry_box10 = Entry(self.ee_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box10.pack()

        #dineout expense
        self.ee_info11 = Label(self.ee_frame, text = "What is your dineout expense (monthly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.ee_info11.pack()
        #dineout expense entry
        self.entry_box11 = Entry(self.ee_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box11.pack()

        #continue button with function everyday_expenses_collection
        self.continue_button = Button(self.ee_frame, text = "Continue", font = ("Open Sans", 15), width = 15, bg = "#69e051", fg = "white", command = self.everyday_expenses_collection)
        self.continue_button.pack(pady = 15)

        #back button which goes back to previous class
        self.back_button = Button(self.ee_frame, text = "Back", font = ("Open Sans", 15), width = 15, bg = "orange", command = self.remove_previous_living_expenses)
        self.back_button.pack()

    #This will collect the user's everyday expenses from the entry boxes and add it to the everyday_expenses_list
    def everyday_expenses_collection(self): 
        #The try block lets us test a block of code for errors.
        try:
            #the following variables get the user entries and converts to integer
            fuel_expense = int(self.entry_box7.get())
            groceries_expense = int(self.entry_box8.get())
            takeaways_expense = int(self.entry_box9.get())
            entertainment_expense = int(self.entry_box10.get())
            dineout_expense = int(self.entry_box11.get())

            #boundary testing, setting specific allowed digits for each expense using math.log10
            if int((math.log10(fuel_expense)))+1 > 1 and int((math.log10(fuel_expense)))+1 < 5 and int((math.log10(groceries_expense)))+1 > 1 and int((math.log10(groceries_expense)))+1 < 5 and int((math.log10(takeaways_expense)))+1 > 0 and int((math.log10(takeaways_expense)))+1 < 5 and int((math.log10(entertainment_expense)))+1 > 0 and int((math.log10(entertainment_expense)))+1 < 5 and int((math.log10(dineout_expense)))+1 > 0 and int((math.log10(dineout_expense)))+1 < 5:
                #adds the user expenses to the everyday_expenses_list
                everyday_expenses_list.append(fuel_expense)
                everyday_expenses_list.append(groceries_expense)
                everyday_expenses_list.append(takeaways_expense)
                everyday_expenses_list.append(entertainment_expense)
                everyday_expenses_list.append(dineout_expense)

                #destroys the everyday expenses frame and proceeds to the irregular expenses class
                self.ee_frame.destroy()
                BudgeterIE(root)

            #if the entry boxes aren't filled properly, returns the error message below
            else:
                messagebox.showerror(" Error", "Use appropriate figures. ")
        
        #The except block lets us handle the error
        except:
            messagebox.showinfo("Warning", "Please fill all boxes and respond with digits only.") #runs a messagebox with the given text


        
    #removing previous stated living expenses so it doesn't double record then goes back
    def remove_previous_living_expenses(self):
        living_expenses_list.clear()
        self.ee_frame.destroy()
        BudgeterLE(root)


#Irregular expenses class
class BudgeterIE:
    def __init__(self, parent):
        
        #setting the background colour
        background_color = "#fcdf95"

        #setting up the frame
        self.ie_frame = Frame(parent,
                                bg = background_color,
                                padx = 100,
                                pady = 25)
        self.ie_frame.pack(fill = "both", expand = True)

        #label for title
        self.title_label = Label(self.ie_frame, text = "Irregular expenses", bg = background_color, font = ("Open Sans Bold", 30))
        self.title_label.pack(pady = 10)

        #vehicle maintenance expense
        self.ie_info12 = Label(self.ie_frame, text = "What is your vehicle maintenance (yearly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.ie_info12.pack()
        #vehicle maintenance expense entry
        self.entry_box12 = Entry(self.ie_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box12.pack()

        #WOF expense
        self.ie_info13 = Label(self.ie_frame, text = "What is your WOF expense (yearly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.ie_info13.pack()
        #WOF expense entry
        self.entry_box13 = Entry(self.ie_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box13.pack()

        #life_insurance expense
        self.ie_info14 = Label(self.ie_frame, text = "What is your life insurance (yearly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.ie_info14.pack()
        #life insurance expense entry
        self.entry_box14 = Entry(self.ie_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box14.pack()

        #doctors expense
        self.ie_info15 = Label(self.ie_frame, text = "What is your doctor appointments expense (yearly $)?", font = ("Open Sans", 15), bg = background_color, pady = 5)
        self.ie_info15.pack()
        #doctors expense entry
        self.entry_box15 = Entry(self.ie_frame, width = 20, font = ("Open Sans", "15"))
        self.entry_box15.pack()

        #continue button with the function irregular_expenses_collection
        self.continue_button = Button(self.ie_frame, text = "Continue", font = ("Open Sans", 15), width = 15, bg = "#69e051", fg = "white", command = self.irregular_expenses_collection)
        self.continue_button.pack(pady = 10)

        #back button which goes back to previous class
        self.back_button = Button(self.ie_frame, text = "Back", font = ("Open Sans", 15), width = 15, bg = "orange", command = self.remove_previous_everyday_expenses)
        self.back_button.pack()

    #This will collect the user's irregular expenses from the entry boxes and add it to the irregular_expenses_list
    def irregular_expenses_collection(self):
        #The try block lets us test a block of code for errors.
        try:
            #the following variables get the user entries and converts to integer
            vehicle_expense = int(self.entry_box12.get())
            wof_expense = int(self.entry_box13.get())
            life_insurance_expense = int(self.entry_box14.get())
            doctors_expense = int(self.entry_box15.get())

            #boundary testing, setting specific allowed digits for each expense using math.log10
            if int((math.log10(vehicle_expense)))+1 > 1 and int((math.log10(vehicle_expense)))+1 < 5 and int((math.log10(wof_expense)))+1 > 1 and int((math.log10(wof_expense)))+1 < 5 and int((math.log10(life_insurance_expense)))+1 > 0 and int((math.log10(life_insurance_expense)))+1 < 6 and int((math.log10(doctors_expense)))+1 > 0 and int((math.log10(doctors_expense)))+1 < 5:
                #adds the user expenses to the irregular_expenses_list at the beginning
                irregular_expenses_list.append(vehicle_expense)
                irregular_expenses_list.append(wof_expense)
                irregular_expenses_list.append(life_insurance_expense)
                irregular_expenses_list.append(doctors_expense)

                #destroys the irregular expenses frame and goes forward to next class(Results)
                self.ie_frame.destroy()
                Results(root)

            #if the entry boxes aren't filled properly, returns the error message below
            else:
                messagebox.showerror(" Error", "Use appropriate figures. ")

        #The except block lets us handle the error
        except:
            messagebox.showinfo("Warning", "Please fill all boxes and respond with digits only.") #runs a messagebox with the given text

    #removing previous stated everyday expenses so it doesn't double record
    def remove_previous_everyday_expenses(self):
        everyday_expenses_list.clear()
        #destroys the irregular expenses frame and goes back to the previous class(BudgeterEE)
        self.ie_frame.destroy()
        BudgeterEE(root)


#Results class, which displays information about user's spending
class Results:
    def __init__(self, parent):
        
        #setting background colour
        background_color = "#fcdf95"

        #setting up the frame
        self.results_frame = Frame(parent,
                                bg = background_color,
                                padx = 50,
                                pady = 25)
        self.results_frame.pack(fill = "both", expand = True)

        #the following are calculations which will be used. these are mostly self explanatory
        #sum adds every item in the list, provided it's an integer
        total_income = int(sum(income_list)) #disposable income number
        total_living_expenses = int((sum(living_expenses_list))*12) #total living expenses x 12 since it was monthly
        total_everyday_expenses = int((sum(everyday_expenses_list))*12) #total everyday expenses x 12 since it was also monthly
        total_irregular_expenses = int(sum(irregular_expenses_list)) #total irregular expenses, yearly

        #total expenses
        total_expenses = (total_living_expenses + total_everyday_expenses + total_irregular_expenses)

        #income - total expenses
        total_remainder = (total_income - total_expenses)

        #label for title
        self.title_label = Label(self.results_frame, text = "Results", bg = background_color, font = ("Open Sans Bold", 30))
        self.title_label.pack(pady = 15)

        #labels 16-20 display information about user's spending
        self.results_info16 = Label(self.results_frame, text = "Your disposable income is $" + str(total_income), font = ("Open Sans", 14), bg = background_color, pady = 5)
        self.results_info16.pack()

        self.results_info17 = Label(self.results_frame, text = "Your total expenditure was $" + str(total_expenses) , font = ("Open Sans", 14), bg = background_color, pady = 5)
        self.results_info17.pack()

        #round(number[, ndigits]). Returns number rounded to ndigits precision after the decimal point
        self.results_info18 = Label(self.results_frame, text = "Your total living expenses for the year was $" + str(total_living_expenses) + ". This is " + str(round(((total_living_expenses/total_expenses)*100), 2)) + "% of your total expenditure.", font = ("Open Sans", 14), bg = background_color, pady = 5)
        self.results_info18.pack()

        #round(number[, ndigits]). Returns number rounded to ndigits precision after the decimal point
        self.results_info19 = Label(self.results_frame, text = "Your total everyday expenses for the year was $" + str(total_everyday_expenses) + ". This is " + str(round(((total_everyday_expenses/total_expenses)*100), 2)) + "% of your total expenditure.", font = ("Open Sans", 14), bg = background_color, pady = 5)
        self.results_info19.pack()

        #round(number[, ndigits]). Returns number rounded to ndigits precision after the decimal point
        self.results_info20 = Label(self.results_frame, text = "Your total irregular expenses for the year was $" + str(total_irregular_expenses) + ". This is " + str(round(((total_irregular_expenses/total_expenses)*100), 2)) + "% of your total expenditure.", font = ("Open Sans", 14), bg = background_color, pady = 5)
        self.results_info20.pack()

        #if they have a positive leftover, then the following shows up
        if total_remainder > 0:
            self.results_info21 = Label(self.results_frame, text = "Your profit for the year is $" + str(total_remainder) + ". You can save this amount for the future.", font = ("Open Sans", 14), bg = background_color, pady = 5)
            self.results_info21.pack()
        
        #if they have a negative leftover, then the following shows up
        else:
            self.results_info22 = Label(self.results_frame, text = "Your defecit for the year was $" + str(total_remainder) + ". You have used more than your income. Be careful in the future.", font = ("Open Sans", 14), bg = background_color, pady = 5)
            self.results_info22.pack()

        #continue button with the function finish_budget
        self.continue_button = Button(self.results_frame, text = "Finish", font = ("Open Sans", 15), width = 15, bg = "#69e051", fg = "white", command =self.finish_budget)
        self.continue_button.pack(pady = 15)

        #back button to go to back to previous class
        self.back_button = Button(self.results_frame, text = "Back", font = ("Open Sans", 15), width = 15, bg = "orange", command = self.remove_previous_irregular_expenses)
        self.back_button.pack()

    #function destroys the results_frame and proceeds to the resources class
    def finish_budget(self):
        self.results_frame.destroy()
        Resources(root)

    #removing previous stated irregular expenses so it doesn't double record
    def remove_previous_irregular_expenses(self):
        irregular_expenses_list.clear()
        #destroys the results_frame and proceeds to the previous class(BudgeterIE)
        self.results_frame.destroy()
        BudgeterIE(root)


#Resources class for sending user to useful websites
class Resources:
    def __init__(self, parent):
        
        #setting up background colour
        background_color = "#fcdf95"

        #setting up frame
        self.resources_frame = Frame(parent,
                                bg = background_color,
                                padx = 100,
                                pady = 25)
        self.resources_frame.pack(fill = "both", expand = True)
        
        #label for title
        self.help_heading = Label(self.resources_frame, text = "  Below are helpful resources! ", font = ("Open Sans", 30), bg = background_color, pady = 15)
        self.help_heading.pack() #the heading label

        #another label with given text
        self.help_heading_2 = Label(self.resources_frame, text = "These resources gives information about money management.", font = ("Open Sans", 16), bg = background_color, pady = 15)
        self.help_heading_2.pack() 

        #link buttons 1-3 are three buttons which launch the user to the given website
        self.link_button_1 = Button(self.resources_frame, text = "Resource 1", width = 15, bg = "#ffd64f", font = ("Open Sans", 15), command=self.moneyhelper) #links
        self.link_button_1.pack(pady = 20)

        self.link_button_2 = Button(self.resources_frame, text = "Resource 2", width = 15, bg = "#ffd64f", font = ("Open Sans", 15), command=self.westpac) #links
        self.link_button_2.pack(pady = 20)

        self.link_button_3 = Button(self.resources_frame, text = "Resource 3", width = 15, bg = "#ffd64f", font = ("Open Sans", 15), command=self.usnews) #links
        self.link_button_3.pack(pady = 20)

        #exit button to exit the app
        self.exit_button = Button(self.resources_frame, text = "Exit", width = 15, bg = "Red", font = ("Open Sans", 15), command = self.close_end) #exit
        self.exit_button.pack(pady = 20)

    def moneyhelper(self):
        #opens the following website
        webbrowser.open("https://www.moneyhelper.org.uk/en/everyday-money/budgeting/beginners-guide-to-managing-your-money") #this will launch them to that website

    def westpac(self):
        #opens the following website
        webbrowser.open("https://www.westpac.co.nz/personal/life-money/managing-your-money/") #this will launch them to that website

    def usnews(self):
        #opens the following website
        webbrowser.open("https://money.usnews.com/money/personal-finance/articles/steps-to-manage-your-money") #this will launch them to that website

    def close_end(self):
        #exits the app
        self.resources_frame.destroy()
        root.destroy()

        

####### program start ##########

if __name__ == "__main__":
    root = Tk()
    root.title("Budgeting Tool") #the title of my program
    BudgetIntro_object = BudgetIntro(root) #starts the BudgetIntro class
    root.geometry("1200x650") #starts program with this resolution (X.Y)
    root.configure(bg = "#fcdf95") #configuring background colour of window
    root.minsize(1000,650) #setting a max resolution for program
    root.mainloop() #This loops the window for to it stay and not disappear.