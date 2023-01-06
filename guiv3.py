import tkinter as tk
from PIL import Image, ImageTk



class MyGUI:

    def __init__(self):
        def click():
            self.entered_text = self.textentry.get()
            self.orderbox.delete(0.0, tk.END)
            self.pizza_size = ""
            self.message = ""
            toppings = "Cheese "
            crust = ""
            price = 0.0
            crust_cheker = 0
            for crust_type in self.checks_crust:
                crust_cheker += crust_type[1].get()

            if self.entered_text.lower() not in ["small", "medium", "large"]:
                self.message = "Please Enter a Pizza Size!"
                self.orderbox.insert(tk.END, self.message)
            elif crust_cheker > 1:
                self.message = "Please select only one crust type!"
                self.orderbox.insert(tk.END, self.message)
            elif crust_cheker == 0:
                self.pizza_size = "Please select a crust type!"
                self.orderbox.insert(tk.END, self.pizza_size)
            else:    

                try:
                    for topping in self.checks:
                        if topping[1].get() == 1:
                            toppings = toppings + topping[0] + " "
                            price += 1.25
                    for crust_type in self.checks_crust:
                        if crust_type[1].get() == 1:
                            crust = crust_type[0] + "\n"

                    if self.entered_text.lower() == "small":
                        price += 10.99
                    if self.entered_text.lower() == "medium":
                        price += 12.99
                    if self.entered_text.lower() == "large":
                        price += 14.99
                    
                    tax = price * .0875
                    price += tax
                    self.pizza_size = self.entered_text
                    self.pizza_size = "Your order is:" + "\n" + crust + self.pizza_size.title() + " Pizza" + "\nToppings are: " + toppings + "\n" + "Tax is: " + f'{tax:.2f}' + "\n" + "Your final cost is: " + f'{price:.2f}'
                except:
                    self.pizza_size = "poop"
                self.orderbox.insert(tk.END, self.pizza_size)

        self.root = tk.Tk()
        self.root.geometry("1200x1000")

        self.label = tk.Label(self.root, text="Pizza", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)


        image = Image.open("pizza.png")
        self.resize_image = image.resize((600, 300))
        self.img = ImageTk.PhotoImage(self.resize_image)


        tk.Label(self.root, image=self.img, bg="black").pack()


        self.textentry = tk.Entry(self.root, font=('Arial', 16))
        self.textentry.pack(padx=10, pady=10)

        self.checks = []
        self.checks.append(["Pepperoni", tk.IntVar()])
        self.checks.append(["Sausage", tk.IntVar()])
        self.checks.append(["Onions", tk.IntVar()])
        self.checks.append(["Mushrooms", tk.IntVar()])
        
        self.checks_crust = []
        self.checks_crust.append(["Thin-Crust", tk.IntVar()])
        self.checks_crust.append(["Deep-Dish", tk.IntVar()])
        self.checks_crust.append(["Hand-Tossed", tk.IntVar()])



        self.check_toppings = tk.Checkbutton(
            self.root, text=self.checks[0][0], font=('Arial, 12'), variable=self.checks[0][1])
        self.check1_toppings = tk.Checkbutton(
            self.root, text=self.checks[1][0], font=('Arial, 12'), variable=self.checks[1][1])
        self.check2_toppings = tk.Checkbutton(
            self.root, text=self.checks[2][0], font=('Arial, 12'), variable=self.checks[2][1])
        self.check3_toppings = tk.Checkbutton(
            self.root, text=self.checks[3][0], font=('Arial, 12'), variable=self.checks[3][1])

        self.crust_place = .0
        self.crust1_place = self.crust_place + .13
        self.crust2_place = self.crust1_place + .12
        self.crust3_place = self.crust2_place + .12
        self.check_place = .85

        self.check_toppings.place(relx=self.crust_place, rely=self.check_place)
        self.check1_toppings.place(
            relx=self.crust1_place, rely=self.check_place)
        self.check2_toppings.place(
            relx=self.crust2_place, rely=self.check_place)
        self.check3_toppings.place(
            relx=self.crust3_place, rely=self.check_place)

        self.check_crust = tk.Checkbutton(
            self.root, text=self.checks_crust[0][0], font=('Arial, 12'), variable=self.checks_crust[0][1])
        self.check1_crust = tk.Checkbutton(
            self.root, text=self.checks_crust[1][0], font=('Arial, 12'), variable=self.checks_crust[1][1])
        self.check2_crust = tk.Checkbutton(
            self.root, text=self.checks_crust[2][0], font=('Arial, 12'), variable=self.checks_crust[2][1])

        self.crust_place = .61
        self.crust1_place = self.crust_place + .13
        self.crust2_place = self.crust1_place + .12
        self.check_crust.place(relx=self.crust_place, rely=self.check_place)
        self.check1_crust.place(relx=self.crust1_place, rely=self.check_place)
        self.check2_crust.place(relx=self.crust2_place, rely=self.check_place)

        self.button = tk.Button(
            self.root, text="Click to Submit Your Order", command=click, font=('Arial', 18))
        self.button.pack(padx=10, pady=10)

        self.orderbox = tk.Text(self.root, width=75,
                                height=9, background="black")
        self.orderbox.pack(padx=10, pady=10)

        self.root.mainloop()


MyGUI()
