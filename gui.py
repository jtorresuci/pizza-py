from tkinter import *

#key down function



def run():

    def click():
        entered_text = textentry.get()
        output.delete(0.0, END)
        try:
            definition = entered_text
        except:
            definition = "poop"
        output.insert(END, definition)

    # create window
    window = Tk()

    # create checkboxes 

    # define width and height
    width = 1000
    height = 500

    wxh = str(width) + "x" + str(height)
    window.columnconfigure((0, 1, 2), weight=1)
    window.rowconfigure((0, 1, 2), weight=1)
    
    # window.attributes('-fullscreen', True)

    window.title("Pizza")
    window.configure(background="black")


    # create label
    photo1 = PhotoImage(file="w.png")
    Label(window, width=200, height=200, image=photo1, bg="black").grid(row=1, column=0, columnspan=3, sticky="nsew")

    # create a text entry box
    textentry = Entry(window, width=20, bg="black")
    textentry.grid(row=2, column=0, sticky=W)

    # submit button
    Button(window, text="Submit", width=6, command=click).grid(row=3, column=0, sticky=W)

    # create a text box
    output = Text(window, width=75, height=6, wrap=WORD, background="black")
    output.grid(row=5, column=0, columnspan=2, sticky=W)

    # exit label
    Label(window, text="Click to Exit", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)


    # exit function
    def close_window():
        window.destroy()
        exit()

    # add exit button
    Button(window, text="Exit", width=14, command=close_window).grid(row=7, column=0, sticky=W)


    window.mainloop()

run()


# # from tkinter import *
# # import _tkinter

# window = Tk()
# window.title("Pizza")

# window.mainloop()

# # import tkinter
# # import _tkinter
# # tkinter._test()

# # window = tkinter()

# from tkinter import *
# from tkinter import ttk


# def click():
#     entered_text = 1


# # main
# # root = Tk()
# # frm = ttk.Frame(root, padding=10)
# # frm.grid()
# # ttk.Label(frm, text="Hello World!").grid(column=0, row=0)


# textentry = Entry(window, width=20, bg="white")


# # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# # root.mainloop()
