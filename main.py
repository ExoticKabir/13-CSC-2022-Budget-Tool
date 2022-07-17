from email.mime import application
from tkinter import *
from tkinter import messagebox

income_list = [] #This will contain the user's disposable income, which will be used later on

living_expenses_list = [] #monthly so x12
everyday_expenses_list = [] #monthly so x12
irregular_expenses_list = [] #yearly so x1

#The simple formula will be = (income - total expenses), where a positive figure is desired


class BudgetIntro(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        #Simply a label with the text below:
        self.title_label = Label(self, text="Welcome to my budgeting app!", 
                                bg = "plum1", 
                                font=("Arial Bold", 25))
        self.title_label.grid(row=0, 
                             padx=150, 
                             pady=175)       
        
        #Creating the login button
        self.login_button = Button(self, text="Login", 
                                  font=("Arial", 15), 
                                  command=lambda: controller.show_frame(Login))
        self.login_button.grid(row=1)
        
        #Creating the privacy policy button
        self.privacy_button = Button(self, text="Privacy Policy", 
                                    font=("Arial", 15), 
                                    command=lambda: controller.show_frame(PrivacyPolicy))
        self.privacy_button.grid(row=2)


class PrivacyPolicy(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        #Simply a label with the text below:
        self.title_label = Label(self, text="This is the privacy policy.", 
                                bg = "plum1", 
                                font=("Arial Bold", 25))
        self.title_label.place(x=300, y=50)

        self.pp_info1 = Label(self, text = "This privacy policy explains the privacy practices of this program.", font = ("Comic Sans MS", 14), pady = 5)
        self.pp_info1.place(x=100, y=200)

        self.pp_info2 = Label(self, text = "I created this program for my level 3 computer science internal.", font = ("Comic Sans MS", 14), pady = 5)
        self.pp_info2.place(x=100, y=250)

        self.pp_info3 = Label(self, text = "No data is stored or shared. The code for this project can also be found on GitHub.", font = ("Comic Sans MS", 14), pady = 5)
        self.pp_info3.place(x=100, y=300)      
        
        #Creating the "back" button which links back to the introduction component
        self.intro_button = Button(self, text="Back", 
                                  font=("Arial", 15), 
                                  command=lambda: controller.show_frame(BudgetIntro))
        self.intro_button.place(x=400, y=500)  


class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
              
        self.border = LabelFrame(self, text='Login', bg='plum1', bd = 10, font=("Arial", 20))
        self.border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        self.user_label = Label(self.border, text="Username", font=("Arial Bold", 15), bg='plum1')
        self.user_label.place(x=50, y=20)
        self.user_entry = Entry(self.border, width = 30, bd = 5)
        self.user_entry.place(x=180, y=20)
        
        self.password_label = Label(self.border, text="Password", font=("Arial Bold", 15), bg='plum1')
        self.password_label.place(x=50, y=80)
        self.password_entry = Entry(self.border, width = 30, show='*', bd = 5)
        self.password_entry.place(x=180, y=80)
        
        def verification():
            try:
                with open("users.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        self.user_name, self.user_password =e.split(",") #Splits the username and password using ","
                        #if file password/username match with entrybox password/username, then allows access
                        if self.user_name.strip() == self.user_entry.get() and self.user_password.strip() == self.password_entry.get():
                            controller.show_frame(BudgeterInc)
                            i = 1
                            break
                    if i==0: #If it doesn't match, then the following dialouge will be provided
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Couldnt open file")
     
        #Creating the submit button 
        self.submitbutton = Button(self.border, text="Submit", font=("Arial", 15), command=verification)
        self.submitbutton.place(x=320, y=115)
        
        def register():
            register_window = Tk()
            register_window.resizable(0,0)
            register_window.configure(bg="plum1")
            register_window.title("Register")
            reg_name_label = Label(register_window, text="Username:", font=("Arial",15), bg="deep sky blue")
            reg_name_label.place(x=10, y=10)
            reg_name_entry = Entry(register_window, width=30, bd=5)
            reg_name_entry.place(x = 200, y=10)
            
            reg_password_label = Label(register_window, text="Password:", font=("Arial",15), bg="deep sky blue")
            reg_password_label.place(x=10, y=60)
            reg_password_entry = Entry(register_window, width=30, show="*", bd=5)
            reg_password_entry.place(x = 200, y=60)
            
            confirm_password_label = Label(register_window, text="Confirm Password:", font=("Arial",15), bg="deep sky blue")
            confirm_password_label.place(x=10, y=110)
            confirm_password_entry = Entry(register_window, width=30, show="*", bd=5)
            confirm_password_entry.place(x = 200, y=110)
            
            def check():
                if reg_name_entry.get()!="" or reg_password_entry.get()!="" or confirm_password_entry.get()!="":
                    if reg_password_entry.get()==confirm_password_entry.get():
                        with open("users.txt", "a") as f:
                            f.write(reg_name_entry.get()+","+reg_password_entry.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!")
                            register_window.destroy()
                    else:
                        messagebox.showinfo("Error","Your password didn't get match!")
                else:
                    messagebox.showinfo("Error", "Please complete all required fields!")
                    
            self.register_button = Button(register_window, text="Sign up", font=("Arial",15), bg="#ffc22a", command=check)
            self.register_button.place(x=170, y=150)
            
            register_window.geometry("470x220")
            register_window.mainloop()
            
        self.register_button = Button(self, text="Register", bg = "dark orange", font=("Arial",15), command=register)
        self.register_button.place(x=650, y=20)

class BudgeterInc(Frame): #Income frame
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.title_label = Label(self, text="Prerequisites", bg = "plum1", font=("Arial Bold", 25))
        self.title_label.place(x=300, y=50)

        self.inc_info1 = Label(self, text = "This budgeting tool uses NZD and annual calculations.", font = ("Comic Sans MS", 14), pady = 5)
        self.inc_info1.place(x=100, y=100)

        self.inc_info2 = Label(self, text = "What is your disposable income?", font = ("Comic Sans MS", 14), pady = 5)
        self.inc_info2.place(x=100, y=175)

        self.entry_box = Entry(self, width = 35, font = ("Comic Sans MS", "14"))
        self.entry_box.place(x=100, y=250)

        #The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False
        #This will collect the user's disposable income from the entry box
        def income_collection():
            income = self.entry_box.get()  #this will collect the income from the entry box
            if len(income) > 3 and len(income) < 8 and income.isnumeric(): #Boundary testing, the income has to be between 3 and 8 characters, using len this is possible
                income_list.append(income)  #adds the user income to income list declared at the beginning
                controller.show_frame(BudgeterLE) #shows the living expenses frame

            #if the name is less than 1 or greater than 13 characters, returns the error message below
            else:
                messagebox.showerror(" Error", "Your income must be between 4-7 digits! ")

            print(income_list)

        self.continue_button = Button(self, text="Continue", font=("Arial", 15), command = income_collection)
        self.continue_button.place(x=650, y=450)
    
    

class BudgeterLE(Frame): #Living expenses frame
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.title_label = Label(self, text="Living expenses", bg = "plum1", font=("Arial Bold", 25))
        self.title_label.place(x=300, y=50)
        
        #rent/mortgage expense
        self.le_info1 = Label(self, text = "what is your rent/mortage (monthly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.le_info1.place(x=100, y=100)
        #rent/mortgage expense entry
        self.entry_box1 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box1.place(x=100, y=150)

        #power expense
        self.le_info2 = Label(self, text = "what is your power bill (monthly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.le_info2.place(x=100, y=200)
        #power expense entry
        self.entry_box2 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box2.place(x=100, y=250)

        #water expense
        self.le_info3 = Label(self, text = "what is your water bill (monthly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.le_info3.place(x=100, y=300)
        #water expense entry
        self.entry_box3 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box3.place(x=100, y=350)

        #internet/home phone expense
        self.le_info4 = Label(self, text = "what is your internet/home phone expense (monthly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.le_info4.place(x=500, y=100)
        #internet/home phone expense entry
        self.entry_box4 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box4.place(x=500, y=150)

        #laundry/drycleaning expense
        self.le_info5 = Label(self, text = "what is your laundry/drycleaning expense (monthly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.le_info5.place(x=500, y=200)
        #laundry/drycleaning expense entry
        self.entry_box5 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box5.place(x=500, y=250)

        #mobile phone expense
        self.le_info6 = Label(self, text = "what is your mobile phone expense (monthly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.le_info6.place(x=500, y=300)
        #mobile phone expense entry
        self.entry_box6 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box6.place(x=500, y=350)

        #The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False
        #This will collect the user's disposable income from the entry box
        def living_expenses_collection():
            housing_expense = self.entry_box1.get()
            power_expense = self.entry_box2.get()
            water_expense = self.entry_box3.get()
            internet_expense = self.entry_box4.get()
            laundry_expense = self.entry_box5.get()
            mobile_expense = self.entry_box6.get()

            if len(housing_expense) > 2 and len(housing_expense) < 6 and housing_expense.isnumeric() and len(power_expense) > 2 and len(power_expense) < 6 and power_expense.isnumeric() and len(water_expense) > 2 and len(water_expense) < 6 and water_expense.isnumeric() and len(internet_expense) > 2 and len(internet_expense) < 6 and internet_expense.isnumeric() and len(laundry_expense) > 2 and len(laundry_expense) < 6 and laundry_expense.isnumeric() and len(mobile_expense) > 2 and len(mobile_expense) < 6 and mobile_expense.isnumeric():
                living_expenses_list.append(housing_expense)
                living_expenses_list.append(power_expense)
                living_expenses_list.append(water_expense)
                living_expenses_list.append(internet_expense)
                living_expenses_list.append(laundry_expense)
                living_expenses_list.append(mobile_expense)

                controller.show_frame(BudgeterEE) #shows the everyday expenses frame

            #if the name is less than 1 or greater than 13 characters, returns the error message below
            else:
                messagebox.showerror(" Error", "Use appropriate figures. ")

            print(living_expenses_list)


        self.continue_button = Button(self, text="Continue", font=("Arial", 15), command = living_expenses_collection)
        self.continue_button.place(x=650, y=450)

        #removing previous stated income so it doesn't double record
        def remove_previous_income():
            income_list.clear()
            controller.show_frame(BudgeterInc)


        self.back_button = Button(self, text="Back", font=("Arial", 15), command = remove_previous_income)
        self.back_button.place(x=100, y=450)

class BudgeterEE(Frame): #Everyday expenses
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.title_label = Label(self, text="Everyday expenses", bg = "plum1", font=("Arial Bold", 25))
        self.title_label.place(x=300, y=50)
        
        #fuel expense
        self.ee_info7 = Label(self, text = "what is your fuel expense (monthly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.ee_info7.place(x=100, y=100)
        #fuel expense entry
        self.entry_box7 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box7.place(x=100, y=150)

        #groceries expense
        self.ee_info8 = Label(self, text = "your groceries expense (monthly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.ee_info8.place(x=100, y=200)
        #groceries expense entry
        self.entry_box8 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box8.place(x=100, y=250)

        #takeaways expense
        self.ee_info9 = Label(self, text = "what is your takeaways expense (monthly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.ee_info9.place(x=100, y=300)
        #takeaways expense entry
        self.entry_box9 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box9.place(x=100, y=350)

        #entertainment expense
        self.ee_info10 = Label(self, text = "what is your entertainment expense (monthly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.ee_info10.place(x=500, y=100)
        #entertainment expense entry
        self.entry_box10 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box10.place(x=500, y=150)

        #dineout expense
        self.ee_info11 = Label(self, text = "what is your dineout expense (monthly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.ee_info11.place(x=500, y=200)
        #dineout expense entry
        self.entry_box11 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box11.place(x=500, y=250)

        #The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False
        #This will collect the user's disposable income from the entry box
        def everyday_expenses_collection():
            fuel_expense = self.entry_box7.get()
            groceries_expense = self.entry_box8.get()
            takeaways_expense = self.entry_box9.get()
            entertainment_expense = self.entry_box10.get()
            dineout_expense = self.entry_box11.get()

            if len(fuel_expense) > 2 and len(fuel_expense) < 6 and fuel_expense.isnumeric() and len(groceries_expense) > 2 and len(groceries_expense) < 6 and groceries_expense.isnumeric() and len(takeaways_expense) > 2 and len(takeaways_expense) < 6 and takeaways_expense.isnumeric() and len(entertainment_expense) > 2 and len(entertainment_expense) < 6 and entertainment_expense.isnumeric() and len(dineout_expense) > 2 and len(dineout_expense) < 6 and dineout_expense.isnumeric():
                everyday_expenses_list.append(fuel_expense)
                everyday_expenses_list.append(groceries_expense)
                everyday_expenses_list.append(takeaways_expense)
                everyday_expenses_list.append(entertainment_expense)
                everyday_expenses_list.append(dineout_expense)

                controller.show_frame(BudgeterIE) #shows the living expenses frame

            #if the name is less than 1 or greater than 13 characters, returns the error message below
            else:
                messagebox.showerror(" Error", "Use appropriate figures. ")

            print(everyday_expenses_list)
        
        
        self.continue_button = Button(self, text="Continue", font=("Arial", 15), command = everyday_expenses_collection)
        self.continue_button.place(x=650, y=450)
        
        #removing previous stated living expenses so it doesn't double record
        def remove_previous_living_expenses():
            living_expenses_list.clear()
            controller.show_frame(BudgeterLE) #goes back to living expenses frame

        self.back_button = Button(self, text="Back", font=("Arial", 15), command = remove_previous_living_expenses)
        self.back_button.place(x=100, y=450)

class BudgeterIE(Frame): #Irregular expenses frame
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.title_label = Label(self, text="Irregular expenses", bg = "plum1", font=("Arial Bold", 25))
        self.title_label.place(x=300, y=50)

        #vehicle maintenance expense
        self.ie_info12 = Label(self, text = "what is your vehicle maintenance (yearly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.ie_info12.place(x=100, y=100)
        #vehicle maintenance expense entry
        self.entry_box12 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box12.place(x=100, y=150)

        #WOF expense
        self.ie_info13 = Label(self, text = "what is your WOF (yearly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.ie_info13.place(x=100, y=200)
        #WOF expense entry
        self.entry_box13 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box13.place(x=100, y=250)

        #life_insurance expense
        self.ie_info14 = Label(self, text = "what is your life insurance (yearly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.ie_info14.place(x=100, y=300)
        #life insurance expense entry
        self.entry_box14 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box14.place(x=100, y=350)

        #doctors expense
        self.ie_info15 = Label(self, text = "what is your doctor appointments (yearly)?", font = ("Comic Sans MS", 14), pady = 5)
        self.ie_info15.place(x=500, y=100)
        #doctors expense entry
        self.entry_box15 = Entry(self, width = 20, font = ("Comic Sans MS", "14"))
        self.entry_box15.place(x=500, y=150)

        #The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False
        #This will collect the user's disposable income from the entry box
        def irregular_expenses_collection():
            vehicle_expense = self.entry_box12.get()
            wof_expense = self.entry_box13.get()
            life_insurance_expense = self.entry_box14.get()
            doctors_expense = self.entry_box15.get()

            if len(vehicle_expense) > 2 and len(vehicle_expense) < 6 and vehicle_expense.isnumeric() and len(wof_expense) > 2 and len(wof_expense) < 6 and wof_expense.isnumeric() and len(life_insurance_expense) > 2 and len(life_insurance_expense) < 6 and life_insurance_expense.isnumeric() and len(doctors_expense) > 2 and len(doctors_expense) < 6 and doctors_expense.isnumeric():
                irregular_expenses_list.append(vehicle_expense)
                irregular_expenses_list.append(wof_expense)
                irregular_expenses_list.append(life_insurance_expense)
                irregular_expenses_list.append(doctors_expense)

                controller.show_frame(Results) #shows the living expenses frame

            #if the name is less than 1 or greater than 13 characters, returns the error message below
            else:
                messagebox.showerror(" Error", "Use appropriate figures. ")

            print(irregular_expenses_list)



        self.continue_button = Button(self, text="Continue", font=("Arial", 15), command = irregular_expenses_collection)
        self.continue_button.place(x=650, y=450)


        #removing previous stated everyday expenses so it doesn't double record
        def remove_previous_everyday_expenses():
            everyday_expenses_list.clear()
            controller.show_frame(BudgeterEE) #goes back to everyday expenses frame
        
        self.back_button = Button(self, text="Back", font=("Arial", 15), command = remove_previous_everyday_expenses)
        self.back_button.place(x=100, y=450)

class Results(Frame): #Other expenses frame
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.title_label = Label(self, text="Results", bg = "plum1", font=("Arial Bold", 25))
        self.title_label.place(x=300, y=50)

        self.results_info16 = Label(self, text = "your disposable income is $", font = ("Comic Sans MS", 14), pady = 5)
        self.results_info16.place(x=100, y=100)

        self.continue_button = Button(self, text="PP", font=("Arial", 15), command=lambda: controller.show_frame(PrivacyPolicy))
        self.continue_button.place(x=650, y=450)


        #removing previous stated irregular expenses so it doesn't double record
        def remove_previous_irregular_expenses():
            irregular_expenses_list.clear()
            controller.show_frame(BudgeterIE) #goes back to everyday expenses frame
        
        self.back_button = Button(self, text="Back", font=("Arial", 15), command = remove_previous_irregular_expenses)
        self.back_button.place(x=100, y=450)   




####### program start ##########

class Application(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
      
        self.window = Frame(self)
        self.window.pack()
        
        self.window.grid_rowconfigure(0, minsize = 600)
        self.window.grid_columnconfigure(0, minsize = 1000)
        
        self.frames = {}
        for F in (BudgetIntro, PrivacyPolicy, Login, BudgeterInc, BudgeterLE, BudgeterEE, BudgeterIE, Results):
            frame = F(self.window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(BudgetIntro)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        frame.configure(bg="plum1")
        self.title("Budgeting Tool")


#start of program
if __name__ == '__main__':           
    app = Application()
    app.maxsize(1000,600)
    app.mainloop()