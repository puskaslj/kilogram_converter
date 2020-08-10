from tkinter import *

root = Tk()
root.title("Test App4.")

def kg_to_grams():
    try:
        kg_conversion = float(user_input.get())*1000
        grams.delete(1.0, END)
        grams.insert(END, kg_conversion)
    except ValueError:
        if user_input.get().strip() in ("kocka", "Kocka"):
            grams.delete(1.0, END)
            grams.insert(END, "Peder.")
        else:
            grams.delete(1.0, END)
            grams.insert(END, "INVALID")

def kg_to_pounds():
    try:
        pounds_conversion = float(user_input.get())*2.20462
        pounds.delete(1.0, END)
        pounds.insert(END, pounds_conversion)
    except ValueError:
        if user_input.get().strip() in ("kocka", "Kocka"):
            pounds.delete(1.0, END)
            pounds.insert(END, "Peder.")
        else: 
            pounds.delete(1.0, END)
            pounds.insert(END, "INVALID.")

def kg_to_ounces():
    try:
        ounces_conversion = float(user_input.get())*35.274
        ounces.delete(1.0, END)
        ounces.insert(END, ounces_conversion)
    except ValueError:
        if user_input.get().strip() in ("kocka", "Kocka"):
            ounces.delete(1.0, END)
            ounces.insert(END, "Peder.")
        else: 
            ounces.delete(1.0, END)
            ounces.insert(END, "INVALID.")

def Convert():
    kg_to_grams()
    kg_to_ounces()
    kg_to_pounds()

#Display text on the far left.
user_input_instructions = Label(
    root,
    text = "Please insert a kilogram value."
)
user_input_instructions.grid(
    row = 0,
    column = 0
)

#User's input area in the middle. 
user_input = StringVar()
user_entry = Entry(
    root,
    textvariable = user_input
)
user_entry.grid(
    row = 0,
    column = 1
)

user_entry_check = user_input

#Conversion button
convert_button = Button(
    root,
    command = Convert,
    text = "Convert",
)
convert_button.grid(
    row = 0,
    column = 2
)

#Middle row labels.
grams_label = Label(
    root,
    width = 20,
    text = "Grams"
)
grams_label.grid(
    row = 1,
    column = 0
)

pounds_label = Label(
    root,
    width = 20,
    text = "Pounds"
)
pounds_label.grid(
    row = 1,
    column = 1
)

ounces_label = Label(
    root,
    width = 20,
    text = "Ounces"
)
ounces_label.grid(
    row = 1,
    column = 2
)

grams = Text(
    root,
    height = 1,
    width = 20
)
grams.grid(
    row = 2,
    column = 0
)

pounds = Text(
    root,
    height = 1,
    width = 20
)
pounds.grid(
    row = 2,
    column = 1
)

ounces = Text(
    root,
    height = 1,
    width = 20
)
ounces.grid(
    row = 2,
    column = 2
)

root.mainloop()