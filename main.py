import commands as cmd # our methods for commands handling

from tkinter import * # tkinter GUI library
import os # OS library
from PIL import Image#, ImageTk

def getCommand(event=''):
    enteredCommand = entryCommand.get()
    return cmd.run_command(enteredCommand)

def loadImage():
    canvas_width = 300
    canvas_height =300
    canvas = Canvas(main_screen, 
               width=canvas_width, 
               height=canvas_height)
    canvas.pack()
    img = PhotoImage(file="im.png")
    canvas.create_image(20,20, anchor=NW, image=img)

def main_account_screen():
    global main_screen
    global entryCommand
    main_screen = Tk()

    main_screen.resizable(0,0) #disabling the maximize button
    main_screen.geometry("700x500+0+0")#setting the size of my App
    main_screen.title("CanSat Ground Station")

    top_frame=Frame(main_screen,width = 700,height=50,bg="gray64",relief=SUNKEN)
    top_frame.pack(side=TOP)
    app_tittle = Label(top_frame,font=('arial',35,'bold'),text="CanSat GROUND STATION",fg="darkblue",bd=10)
    app_tittle.grid(row=0,column=0)

    entryCommand = Entry(main_screen,font = "Helvetica 20 bold")
    entryCommand.place(x = 0, y = 450, width=600, height=50)
    
    entryCommand.bind('<Return>', getCommand)## Binding enter key to the entry 
    
    enterButton = Button(main_screen,text="Enter", width=9, height=2, command = getCommand)# adding the enter button
    enterButton.place(x=600, y=450)


    menu_of_myapp = Window(main_screen)
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
       # self.pack(fill=BOTH, expand=1)


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
        setting.add_command(label='Add mission command',command=TopLevels.add_mission_command)
        setting.add_command(label='Remove mission command',command=TopLevels.remove_mission_command)
        setting.add_command(label='Add HKD command',command=TopLevels.add_HDK_command)
        setting.add_command(label='Remove HKD command',command=TopLevels.remove_HDK_command)
        setting.add_command(label='View all commands')
        
        data=Menu(menu)
        data.add_command(label='View HD data')
        data.add_command(label='View Mission data  ')
        data.add_command(label='Eport data')
        
        menu.add_cascade(label='File',menu=file)
        menu.add_cascade(label='Setting',menu=setting)
        menu.add_cascade(label='Data',menu=data)

class TopLevels:        
    def add_mission_command():
        global add_new_mission_command
        add_new_mission_command = Toplevel()
        add_new_mission_command.title("Add new mission command")
        add_new_mission_command.geometry("310x265+700+180")
        add_new_mission_command.resizable(0,0) #disabling the maximize button
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

    def remove_mission_command():
        global remove_mission_command
        remove_mission_command = Toplevel()
        remove_mission_command.title("Remove mission command")
        remove_mission_command.geometry("310x265+700+180")
        remove_mission_command.resizable(0,0) #disabling the maximize button
        Label(remove_mission_command, text="Please enter details for command to remove").pack()
        Label(remove_mission_command, text="").pack()

        global command_name
        global command_initials

        command_name = StringVar()
        command_initials = StringVar()

        global command_name_entry
        global command_initials_entry

        Label(remove_mission_command, text="Command to Remove").pack()
        command_name_entry = Entry(remove_mission_command)
        command_name_entry.pack()
        Label(remove_mission_command, text="").pack()
        Label(remove_mission_command, text="Command initials").pack()
        command_initials_entry = Entry(remove_mission_command)
        command_initials_entry.pack()
        Label(remove_mission_command, text="").pack()
        Button(remove_mission_command, text="Remove", width=10, height=1).pack() 
        

        
    def add_HDK_command():
        global add_new_HKD_command
        add_new_HKD_command = Toplevel()
        add_new_HKD_command.title("Add new HDK command")
        add_new_HKD_command.geometry("310x265+700+180")
        add_new_HKD_command.resizable(0,0) #disabling the maximize button
        Label(add_new_HKD_command, text="Please enter details for new command").pack()
        Label(add_new_HKD_command, text="").pack()

        global command_name
        global command_initials

        command_name = StringVar()
        command_initials = StringVar()

        global command_name_entry
        global command_initials_entry

        Label(add_new_HKD_command, text="New command to add").pack()
        command_name_entry = Entry(add_new_HKD_command)
        command_name_entry.pack()
        Label(add_new_HKD_command, text="").pack()
        Label(add_new_HKD_command, text="Command initials").pack()
        command_initials_entry = Entry(add_new_HKD_command,)
        command_initials_entry.pack()
        Label(add_new_HKD_command, text="").pack()
        Button(add_new_HKD_command, text="Add", width=10, height=1).pack()        

    def remove_HDK_command():
        global remove_HDK_command
        remove_HDK_command = Toplevel()
        remove_HDK_command.title("Remove HDK command")
        remove_HDK_command.geometry("310x265+700+180")
        remove_HDK_command.resizable(0,0) #disabling the maximize button
        Label(remove_HDK_command, text="Please enter details for command to remove").pack()
        Label(remove_HDK_command, text="").pack()

        global command_name
        global command_initials

        command_name = StringVar()
        command_initials = StringVar()

        global command_name_entry
        global command_initials_entry

        Label(remove_HDK_command, text="Command to Remove").pack()
        command_name_entry = Entry(remove_HDK_command)
        command_name_entry.pack()
        Label(remove_HDK_command, text="").pack()
        Label(remove_HDK_command, text="Command initials").pack()
        command_initials_entry = Entry(remove_HDK_command)
        command_initials_entry.pack()
        Label(remove_HDK_command, text="").pack()
        Button(remove_HDK_command, text="Remove", width=10, height=1).pack()
        
        
main_account_screen()

