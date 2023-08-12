from tkinter import *

window = Tk()
window.title("Miles to KMs")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)


def calc():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_output.config(text=km)

# # TODO blank label
# blank_label = Label(text="This is a label")
# blank_label.grid(column=0, row=0)


# TODO Add input textbox
# Text
miles_input = Entry(width=7)
# Puts cursor in textbox.
miles_input.focus()
miles_input.grid(column=1, row=0)

# TODO Add 'Miles' label next to input Textbox
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)
#
# TODO Add 'is equal to' label
label = Label(text="is equal to")
label.grid(column=0, row=1)
#
# TODO add output label
km_output = Label(text="0")
km_output.grid(column=1, row=1)
#
# TODO Add 'Km' label
label_km = Label(text='Km')
label_km.grid(column=2, row=1)


# TODO Add Calculate button
calc_button = Button(text="Calculate", command=calc)
calc_button.grid(column=1, row=2)

window.mainloop()
