from tkinter import *

def convert():
    km = int(enter.get()) * 1.60934
    label_3.config(text=km)


screen = Tk()
screen.title("Mile to Km Converter")

enter = Entry()
enter.grid(row=1, column=2)

label_1 = Label(text="Miles")
label_1.grid(row=1, column=3)

label_2 = Label(text="is equal to")
label_2.grid(row=2, column=1)

label_3 = Label(text="0")
label_3.grid(row=2, column=2)

label_4 = Label(text="Km")
label_4.grid(row=2, column=3)

button = Button(text="Calculate", command=convert)
button.grid(row=3, column=2)

screen.mainloop()