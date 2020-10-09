from tkinter import * #*says import everything in library
import tkinter
from tkinter import messagebox

top =Tk()#our screen
top.title("Choose your pet")#To recognise what type of screen it is my name you given inside brackets
top.geometry("200x300")#How big the screen you want to be
top.configure(background="black")#background color

def submit_command():#A button always need a command which is a function
    info = "Your chosen pets:\n"
    if dog_var.get():
        info += "Your have selected a dog!\n" #simple saying you have selected a dog
    if cat_var.get():
        info += "Your have selected a cat!\n"
    if bird_var.get():
        info += "Your have selected a bird!\n"
    if info == "": #if you didn't choose anygthing
        info = "Your didn't choose anything!"
    messagebox.showinfo("Chosen Pets", info)


submit_button = Button(top, text="Submit", command=submit_command) #Button always in a command

dog_var = BooleanVar()#To get information for checkbutton
cat_var = BooleanVar()
bird_var = BooleanVar()

dog_cb = Checkbutton(top, text="Dog", variable=dog_var , onvalue=True, offvalue=False, height=2, width=20)# you have to define dog_var

cat_cb = Checkbutton(top, text="Cat", variable=cat_var , onvalue=True, offvalue=False, height=2, width=20)

bird_cb = Checkbutton(top, text="Bird", variable=bird_var , onvalue=True, offvalue=False, height=2, width=20)

dog_cb.pack()
cat_cb.pack()
bird_cb.pack()
submit_button.pack()

top.mainloop()#whem you to run it always .mainloop()

#############################################Reg Form####################################








