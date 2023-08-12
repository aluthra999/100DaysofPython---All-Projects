import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# TODO Add Label
my_label = tkinter.Label(text="This is a label", font=('Arial', 20, 'bold'))
my_label.pack()

# my_label['text'] = "New Text"
# my_label.config(text="New text 2")


# TODO Add Button

def button_clicked():
    my_label.config(text=input1.get())


button = tkinter.Button(text="Button", command=button_clicked)
button.pack()

# TODO Entry

input1 = tkinter.Entry(width=10)
input1.pack()


window.mainloop()
