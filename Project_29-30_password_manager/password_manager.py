import json
from tkinter import *
from tkinter import messagebox

# TODO : -------------------------Password Generator Project--------------------------------
def password_generator():
    import random
    import pyperclip

    a = random.randint(6, 8)       # letters
    b = random.randint(2, 4)        # numbers
    c = random.randint(2, 4)        # symbols

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    password_list = [random.choice(letters) for i in range(1, a+1)] + [random.choice(symbols) for j in range(1, b+1)] + [random.choice(symbols) for k in range(1, c+1)]
    random.shuffle(password_list)               # shuffle() function

    password = ""
    for i in password_list:
        password += i                           # converting list into string

    entry3.delete(0, END)
    entry3.insert(0, password)
    pyperclip.copy(password)


# TODO : ------------------------------Saving into a txt file------------------------------------------
'''def add_button_clicked():
    if len(entry1.get()) == 0 or len(entry2.get()) == 0 or len(entry3.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure to fill all the fields.")
    else:
        is_ok = messagebox.askokcancel(title=entry1.get(), message=f"These are details entered: \nEmail: {entry2.get()}"
                               f"\nPassword: {entry3.get()}")
        if is_ok:
            with open("passwords.txt", mode='a') as f:
                f.write(f"{entry1.get()} | {entry2.get()} | {entry3.get()} \n")
            entry1.delete(0, END)
            entry3.delete(0, END)
'''

# TODO : ------------------------------Saving into a json file------------------------------------------
def add_button_clicked():
    new_data = {
        entry1.get(): {
            "Email": entry2.get(),
            "Password": entry3.get()
        }
    }

    import json
    if len(entry1.get()) == 0 or len(entry2.get()) == 0 or len(entry3.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure to fill all the fields.")
    else:
        try:
            with open("passwords.json", mode='r') as f:
                data = json.load(f)                             # reading the json
        except FileNotFoundError:
            with open("passwords.json", mode='w') as f:
                json.dump(new_data, f, indent=4)                # writing over json
        else:
            data.update(new_data)                               # adding new information
            with open("passwords.json", mode='w') as f:
                json.dump(data, f, indent=4)                    # appending in json
        finally:
            entry1.delete(0, END)
            entry3.delete(0, END)


# TODO : ----------------------------------Search website fn--------------------------------
def search_website():
    with open("passwords.json", 'r') as f:
        data = json.load(f)
        for (key, value) in data.items():
            if key == entry1.get():
                messagebox.showinfo(title=entry1.get(), message=value)
            else:
                messagebox.showinfo(title=entry1.get(), message="No password found!")



# TODO : ------------------------------------UI SETUP------------------------------------------
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=240, height=240)
image_lock = PhotoImage(file="logo.png")
canvas.create_image(135, 120, image=image_lock)
canvas.grid(row=1, column=2)


# TODO : Website ----------------------------------------------------------------------------
label1 = Label(text="Website:")
label1.grid(row=2, column=1)

entry1 = Entry(width=40)
entry1.grid(row=2, column=2)              # column span is used to apply this entry throughout two columns
entry1.focus()

search_button_website = Button(text="Search", width=15, command=search_website)
search_button_website.grid(row=2, column=3)


# TODO : Email/Username ----------------------------------------------------------------------------
label2 = Label(text="Email/Username:")
label2.grid(row=3, column=1)

entry2 = Entry(width=60)
entry2.grid(row=3, column=2, columnspan=2)
entry2.insert(0, "jg261001@gmail.com")


# TODO : Password ----------------------------------------------------------------------------
label3 = Label(text="Password:")
label3.grid(row=4, column=1)

entry3 = Entry(width=40)
entry3.grid(row=4, column=2)

generate_button = Button(text="Generate Password", command=password_generator, width=15)
generate_button.grid(row=4, column=3)



# TODO : Add button ----------------------------------------------------------------------------
add_button = Button(text="Add", width=50, command=add_button_clicked)
add_button.grid(row=5, column=2, columnspan=2)


window.mainloop()
