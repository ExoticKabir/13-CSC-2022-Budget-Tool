from email.mime import application
from tkinter import *
from tkinter import messagebox

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
        self.title_label.grid(row=0, 
                             padx=175, 
                             pady=175)      
        
        #Creating the "back" button which links back to the introduction component
        self.intro_button = Button(self, text="Back", 
                                  font=("Arial", 15), 
                                  command=lambda: controller.show_frame(BudgetIntro))
        self.intro_button.grid(row=1)


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
                            controller.show_frame(Budgeter)
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

class Budgeter(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.title_label = Label(self, text="What is your annual income?", bg = "plum1", font=("Arial Bold", 25))
        self.title_label.place(x=40, y=150)        
        self.login_button = Button(self, text="Login", font=("Arial", 15), command=lambda: controller.show_frame(Login))
        self.login_button.place(x=650, y=450)
        
        self.privacy_button = Button(self, text="Privacy Policy", font=("Arial", 15), command=lambda: controller.show_frame(PrivacyPolicy))
        self.privacy_button.place(x=100, y=450)


####### program start ##########

class Application(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
      
        self.window = Frame(self)
        self.window.pack()
        
        self.window.grid_rowconfigure(0, minsize = 500)
        self.window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (BudgetIntro, PrivacyPolicy, Login, Budgeter):
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
    app.maxsize(800,500)
    app.mainloop()