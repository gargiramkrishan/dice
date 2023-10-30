from tkinter import *
import random
root = Tk()
root.geometry("500x500")

def num(x):
    if x == '\u2680':
        return(1)
    elif x == '\u2681':
        return(2)
    elif x == '\u2682':
        return(3)
    elif x == '\u2683':
        return(4)
    elif x == '\u2684':
        return(5)
    elif x == '\u2685':
        return(6)

def roll():
    d1 = random.choice(dice)
    d2 = random.choice(dice)

    sd1 = num(d1)
    sd2 = num(d2)

    label.config(text=d1)
    label2.config(text=d2)

    label1.config(text=sd1)
    label4.config(text=sd2)

    total = sd1+sd2

    label3.config(text=f"You rolled{total}")


dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
my_frame = Frame(root)
my_frame.pack(pady = 20)
label = Label(my_frame,text='', font=('Helvetica',100),fg="black")
label.grid(row=0, column=0,padx=5)
label1 = Label(my_frame, text=" ")
label1.grid(row = 1, column=0)

label2 = Label(my_frame,text='', font=('Helvetica',100),fg="black")
label2.grid(row=0, column=1,padx=5)
label4 = Label(my_frame, text=" ")
label4.grid(row = 1, column=1)

button = Button(root, text="Roll",command=roll,font=('Helvetica',24))
button.pack(pady =20)

label3 = Label(root, text='',font=('Helvetica'),fg="grey")
label3.pack(pady=40)
roll()
root.mainloop()