from tkinter import *
import random
import string

symbols = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890*!+-&$#?=@<>()^"

def generate_pass():
    for n in range(int(number_entry.get())):
        password = ""
        for i in range(int(length_entry.get())):
            password += random.choice(symbols)
        calculated_text.insert(END, password + "\n")

def erase():
    calculated_text.delete("1.0", END)


root = Tk()
root.resizable(width=False, height=False)
root.title("7D MLG 360 Password Generator")
root.geometry("450x375")
calculated_text = Text(root, height=15, width=50)

display_button = Button(text="Generate", command=generate_pass)
erase_button = Button(text="Erase", command=erase)

number_entry = Entry(width=10, justify=CENTER)
length_entry = Entry(width=10, justify=CENTER)
number_entry.insert(0, "8")
length_entry.insert(0,"24")

number_label = Label(text=" Amount of passwords")
length_label = Label(text=" Length of password")
number_label.grid(row=0, column=0, sticky="w")
length_label.grid(row=1, column=0, sticky="w")
number_entry.grid(row=0,column=1, padx=1, pady=5)
length_entry.grid(row=1,column=1, padx=1, pady=5)

display_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")
erase_button.grid(row=2, column=2, padx=15, pady=5, sticky="w")
calculated_text.grid(row=4, column=0, sticky='nsew', columnspan=3)

scrollb = Scrollbar(root, command=calculated_text.yview)
scrollb.grid(row=4, column=4, sticky='nsew')
calculated_text.configure(yscrollcommand=scrollb.set)


root.mainloop()