#import modules
 
from tkinter import *
import tkinter
import os
from tkinter import messagebox as tkMessageBox

#our defined library
#import data_ploter as dp

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
def register_user():
     
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    register_screen.destroy()
    tkMessageBox.showinfo( "Hello user", "You are now registered")

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
  
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            #login_sucess()
            login_screen.destroy()
            tkMessageBox.showinfo( "Hello user", "You are logged in, Click OK to view data")
            #dp.plot_my_data()
            #____________________________________________________________________________
 
        else:
            #password_not_recognised()
            login_screen.destroy()
            tkMessageBox.showinfo( "Hello user", "You have entered wrong password")
 
    else:
        #user_not_found()
        login_screen.destroy()
        tkMessageBox.showinfo( "Hello user", "Username not found")

    #delete the login screen
    


def main_account_screen():
    global main_screen
    main_screen = Tk()

    main_screen.resizable(0,0) #disabling the maximize button
    # sbmyapp = Scrollbar(main_screen)  #scroll bar of my App
    # sbmyapp.pack(side = RIGHT, fill = Y)

    #__________APP FRAMES_____________________________________
    #__________top frame______________________________________
    top_frame=Frame(main_screen,width = 700,height=50,bg="gray64",relief=SUNKEN)
    top_frame.pack(side=TOP)
    app_tittle = Label(top_frame,font=('arial',35,'bold'),text="CanSat GROUND STATION",fg="darkblue",bd=10)
    app_tittle.grid(row=0,column=0)

    # user_frame=Frame(main_screen,width = 340,height=300,bg="gray64",relief=SUNKEN)
    # user_frame.pack(side=RIGHT)

    # user_frame2=Frame(main_screen,width = 340,height=300,bg="gray64",relief=SUNKEN)
    # user_frame2.pack(side=LEFT)

    bottom_frame=Frame(main_screen,width = 700,height=60,bg="gray64",relief=SUNKEN)
    bottom_frame.pack(side=BOTTOM)

    entryExample = Entry(bottom_frame,font = "Helvetica 20 bold")
    entryExample.place(
        x = 0,
        y = 5,
        width=700,
        height=50)
    
    main_screen.geometry("700x500+0+0")#setting the size of my App
    menu_of_myapp = Window(main_screen)

    Label(text="").pack()
 
    main_screen.mainloop()
 
#__________MENU BAR CLASS & FUNCTIONS________________
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("CanSat Ground Station")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)


        #this commands help to use menu
        menu=Menu(self.master)
        self.master.config(menu=menu)


        #these that follows are for file
        file=Menu(menu)
        file.add_command(label='New')
        file.add_command(label='Open')
        file.add_command(label='Recents')
        file.add_command(label='Examples          ')
        #file.add_command(label='Capture screen       ',command=control_functions.screenshoot)
        file.add_separator()
        file.add_command(label='Quit')
        #file.add_command(label='Quit',command=control_functions.quitfunction)


        setting=Menu(menu)
        setting.add_command(label='Add mission command',command=TopLevels.add_mission_command())
        setting.add_command(label='Remove mission command')
        setting.add_command(label='Add HKD command')
        setting.add_command(label='Remove HKD command')
        setting.add_command(label='View all commands')

        menu.add_cascade(label='File',menu=file)
        menu.add_cascade(label='Setting',menu=setting)


class TopLevels:        
    def add_mission_command():
        global add_new_mission_command
        add_new_mission_command = Toplevel()
        add_new_mission_command.title("Add new mission command")
        add_new_mission_command.geometry("310x265+700+180")
        Label(add_new_mission_command, text="Please enter details for new command").pack()
        Label(add_new_mission_command, text="").pack()

        global command_name
        global command_initials

        command_name = StringVar()
        command_initials = StringVar()

        global command_name_entry
        global command_initials_entry

        Label(add_new_mission_command, text="New command to add").pack()
        command_name_entry = Entry(add_new_mission_command)
        command_name_entry.pack()
        Label(add_new_mission_command, text="").pack()
        Label(add_new_mission_command, text="Command initials").pack()
        command_initials_entry = Entry(add_new_mission_command,)
        command_initials_entry.pack()
        Label(add_new_mission_command, text="").pack()
        Button(add_new_mission_command, text="Add", width=10, height=1).pack()
        
#__________calling the menu class___________
# menu_of_myapp = Window(myapp)

#main_account_screen()
