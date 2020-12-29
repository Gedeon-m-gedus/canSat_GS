import tkinter as tk

# counter = 0 

# def counter_label(label):
#   def count():
#     global counter
#     counter += 1
#     label.config(text=str(counter))
#     label.after(1000, count)
#   count()


def data_label(label,name,value):
    def count():
#         global counter
#         counter += 1
        dis =  name + ' ' + str(value)
        label.config(text=dis)
        label.after(1000, count)
    count()
 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")

# label.place(relx = 0.3,  
#             rely = 0.1, 
#             anchor = 'center')

label.pack()
data_label(label,'Temp',20)#

label2 = tk.Label(root, fg="green")
label2.pack()
data_label(label2,'HUM',70)

button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()


