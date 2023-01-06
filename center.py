from tkinter import *

root = Tk()
root.geometry('300x200')
root.columnconfigure((0,1,2), weight=1)   # Set weight to row and 
root.rowconfigure((0,1,2), weight=1)      # column where the widget is
root.configure()

container = Frame(root)   # bg color to show extent
container.grid(row=0, column=1)     # Grid cell with weight

# A couple of widgets to illustrate the principle.


photo1 = PhotoImage(file="w.png")
Label(root, width=200, height=200, image=photo1, bg="black").grid(row=1, column=0, columnspan=3, sticky="nsew")


b1 = Button(container, text='First', width=10)
b1.grid(pady=10, padx=20)
b2 = Button(container, text='second', width=10)
b2.grid(pady=(0,10), padx=20)

root.mainloop()