import tkinter as tk
from tkinter import ttk, messagebox
import random
from datetime import datetime

class RestaurantBillingApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x750+0+0")
        self.root.title("Restaurant Management System")
        self.root.configure(background='lightblue')
        self.initialize_variables()
        self.create_ui()

    def initialize_variables(self):
        # Checkbox variables
        self.variable1 = tk.IntVar()
        self.variable2 = tk.IntVar()
        self.variable3 = tk.IntVar()
        self.variable4 = tk.IntVar()
        self.variable5 = tk.IntVar()
        self.variable6 = tk.IntVar()
        self.variable7 = tk.IntVar()
        self.variable8 = tk.IntVar()
        self.variable9 = tk.IntVar()
        self.variable10 = tk.IntVar()
        self.variable11 = tk.IntVar()
        self.variable12 = tk.IntVar()
        self.variable13 = tk.IntVar()
        self.variable14 = tk.IntVar()
        self.variable15 = tk.IntVar()
        self.variable16 = tk.IntVar()

        # String variables for totals and inputs
        self.Date_of_Order = tk.StringVar()
        self.Receipt_Ref = tk.StringVar()
        self.PaidTax = tk.StringVar()
        self.SubTotal = tk.StringVar()
        self.TotalCost = tk.StringVar()
        self.Total_of_Food = tk.StringVar()
        self.Total_of_Drinks = tk.StringVar()
        self.ServiceCharge = tk.StringVar()

        self.text_Input = tk.StringVar()
        self.operator = ""

        # Drink quantities
        self.cocktail = tk.StringVar()
        self.iced_tea = tk.StringVar()
        self.hot_chocolate = tk.StringVar()
        self.orange_juice = tk.StringVar()
        self.milkshake = tk.StringVar()
        self.mountain_dew = tk.StringVar()
        self.coke = tk.StringVar()
        self.soup = tk.StringVar()

        # Food quantities
        self.fried_chicken = tk.StringVar()
        self.kare_kare = tk.StringVar()
        self.crispy_pata = tk.StringVar()
        self.sinigang_baboy = tk.StringVar()
        self.sinigang_hipon = tk.StringVar()
        self.paneer_peri_peri = tk.StringVar()
        self.asparagus_tofu = tk.StringVar()
        self.chicken_sisig = tk.StringVar()

        # Initialize quantities to "0"
        self.cocktail.set("0")
        self.iced_tea.set("0")
        self.hot_chocolate.set("0")
        self.orange_juice.set("0")
        self.milkshake.set("0")
        self.mountain_dew.set("0")
        self.coke.set("0")
        self.soup.set("0")

        self.fried_chicken.set("0")
        self.kare_kare.set("0")
        self.crispy_pata.set("0")
        self.sinigang_baboy.set("0")
        self.sinigang_hipon.set("0")
        self.paneer_peri_peri.set("0")
        self.asparagus_tofu.set("0")
        self.chicken_sisig.set("0")

        # Set date to current date in YYYY-MM-DD format
        self.Date_of_Order.set(datetime.now().strftime("%Y-%m-%d"))

    def create_ui(self):
        # Top frame
        self.Tops = tk.Frame(self.root, bg='dark blue', bd=25, pady=20, relief=tk.GROOVE)
        self.Tops.pack(side=tk.TOP)

        self.lblTitle = tk.Label(self.Tops, font=('arial', 30, 'bold'), text='Restaurant Management System', bd=15, bg='lightblue',
                        fg='dark blue', justify=tk.CENTER)
        self.lblTitle.grid(row=0)

        # Main frames
        self.ReceiptCal_Function = tk.Frame(self.root, bg='dark blue', bd=10, relief=tk.GROOVE)
        self.ReceiptCal_Function.pack(side=tk.LEFT)

        self.Buttons_Function = tk.Frame(self.ReceiptCal_Function, bg='dark blue', bd=3, relief=tk.GROOVE)
        self.Buttons_Function.pack(side=tk.TOP)

        self.Calculator_Function = tk.Frame(self.ReceiptCal_Function, bg='dark blue', bd=6, relief=tk.GROOVE)
        self.Calculator_Function.pack(side=tk.BOTTOM)

        self.Receipt_Function = tk.Frame(self.ReceiptCal_Function, bg='dark blue', bd=4, relief=tk.GROOVE)
        self.Receipt_Function.pack(side=tk.BOTTOM)

        self.MenuFrame = tk.Frame(self.root, bg='dark blue', bd=32, relief=tk.GROOVE)
        self.MenuFrame.pack(side=tk.RIGHT)
        self.Total_Function = tk.Frame(self.MenuFrame, bg='lightblue', bd=4)
        self.Total_Function.pack(side=tk.BOTTOM)
        self.Drinks_Function = tk.Frame(self.MenuFrame, bg='lightblue', bd=4, relief=tk.GROOVE)
        self.Drinks_Function.pack(side=tk.LEFT)
        self.Food_Function = tk.Frame(self.MenuFrame, bg='lightblue', bd=4, relief=tk.GROOVE)
        self.Food_Function.pack(side=tk.RIGHT)

        # Drinks Checkbuttons and Entries
        ttk.Checkbutton(self.Drinks_Function, text='Cocktail', variable=self.variable1, onvalue=1, offvalue=0,
                       command=self.drinksCocktail).grid(row=0, sticky=tk.W)
        ttk.Checkbutton(self.Drinks_Function, text='Iced Tea', variable=self.variable2, onvalue=1, offvalue=0,
                       command=self.drinksIceTea).grid(row=1, sticky=tk.W)
        ttk.Checkbutton(self.Drinks_Function, text='Hot Chocolate', variable=self.variable3, onvalue=1, offvalue=0,
                       command=self.drinksHotChocolate).grid(row=2, sticky=tk.W)
        ttk.Checkbutton(self.Drinks_Function, text='Orange Juice', variable=self.variable4, onvalue=1, offvalue=0,
                       command=self.drinksOrangeJuice).grid(row=3, sticky=tk.W)
        ttk.Checkbutton(self.Drinks_Function, text='Milk Shake', variable=self.variable5, onvalue=1, offvalue=0,
                       command=self.drinksMilkShake).grid(row=4, sticky=tk.W)
        ttk.Checkbutton(self.Drinks_Function, text='Mountain Dew', variable=self.variable6, onvalue=1, offvalue=0,
                       command=self.drinksMountainDew).grid(row=5, sticky=tk.W)
        ttk.Checkbutton(self.Drinks_Function, text='Coke', variable=self.variable7, onvalue=1, offvalue=0,
                       command=self.drinksCoke).grid(row=6, sticky=tk.W)
        ttk.Checkbutton(self.Drinks_Function, text='Cobra', variable=self.variable8, onvalue=1, offvalue=0,
                       command=self.drinksCobra).grid(row=7, sticky=tk.W)

        self.textCocktail = ttk.Entry(self.Drinks_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.cocktail)
        self.textCocktail.grid(row=0, column=1)
        self.textIcedTea = ttk.Entry(self.Drinks_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.iced_tea)
        self.textIcedTea.grid(row=1, column=1)
        self.textHotChocolate = ttk.Entry(self.Drinks_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.hot_chocolate)
        self.textHotChocolate.grid(row=2, column=1)
        self.textOrangeJuice = ttk.Entry(self.Drinks_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.orange_juice)
        self.textOrangeJuice.grid(row=3, column=1)
        self.textMilkShake = ttk.Entry(self.Drinks_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.milkshake)
        self.textMilkShake.grid(row=4, column=1)
        self.textMountainDew = ttk.Entry(self.Drinks_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.mountain_dew)
        self.textMountainDew.grid(row=5, column=1)
        self.textCoke = ttk.Entry(self.Drinks_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.coke)
        self.textCoke.grid(row=6, column=1)
        self.textCobra = ttk.Entry(self.Drinks_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.cobra)
        self.textCobra.grid(row=7, column=1)

        # Food Checkbuttons and Entries
        ttk.Checkbutton(self.Food_Function, text="Fried Chicken", variable=self.variable9, onvalue=1, offvalue=0,
                       command=self.foodsFriedChicken).grid(row=0, sticky=tk.W)
        ttk.Checkbutton(self.Food_Function, text="Kare Kare", variable=self.variable10, onvalue=1, offvalue=0,
                       command=self.foodsKareKare).grid(row=1, sticky=tk.W)
        ttk.Checkbutton(self.Food_Function, text="Crispy Pata", variable=self.variable11, onvalue=1, offvalue=0,
                       command=self.foodsCrispyPata).grid(row=2, sticky=tk.W)
        ttk.Checkbutton(self.Food_Function, text="Sinigang Baboy", variable=self.variable12, onvalue=1, offvalue=0,
                       command=self.foodsSinigangBaboy).grid(row=3, sticky=tk.W)
        ttk.Checkbutton(self.Food_Function, text="Sinigang Hipon", variable=self.variable13, onvalue=1, offvalue=0,
                       command=self.foodsSinigangHipon).grid(row=4, sticky=tk.W)
        ttk.Checkbutton(self.Food_Function, text="Paneer Peri Peri", variable=self.variable14, onvalue=1, offvalue=0,
                       command=self.foodsPaneerPeriPeri).grid(row=5, sticky=tk.W)
        ttk.Checkbutton(self.Food_Function, text="Asparagus Tofu", variable=self.variable15, onvalue=1, offvalue=0,
                       command=self.foodsAsparagusTofu).grid(row=6, sticky=tk.W)
        ttk.Checkbutton(self.Food_Function, text="Chicken Sisig", variable=self.variable16, onvalue=1, offvalue=0,
                       command=self.foodsChickenSisig).grid(row=7, sticky=tk.W)

        self.textFriedChicken = ttk.Entry(self.Food_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.fried_chicken)
        self.textFriedChicken.grid(row=0, column=1)
        self.textKareKAre = ttk.Entry(self.Food_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.kare_kare)
        self.textKareKAre.grid(row=1, column=1)
        self.textCrispyPata = ttk.Entry(self.Food_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.crispy_pata)
        self.textCrispyPata.grid(row=2, column=1)
        self.textSinigangBaboy = ttk.Entry(self.Food_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.sinigang_baboy)
        self.textSinigangBaboy.grid(row=3, column=1)
        self.textSinigangHipon = ttk.Entry(self.Food_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.sinigang_hipon)
        self.textSinigangHipon.grid(row=4, column=1)
        self.textPaneerPeriPeri = ttk.Entry(self.Food_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.paneer_peri_peri)
        self.textPaneerPeriPeri.grid(row=5, column=1)
        self.textAsparagusTofu = ttk.Entry(self.Food_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.asparagus_tofu)
        self.textAsparagusTofu.grid(row=6, column=1)
        self.textChickenSisig = ttk.Entry(self.Food_Function, font=('arial', 16, 'bold'), width=6, justify=tk.LEFT, state=tk.DISABLED, textvariable=self.chicken_sisig)
        self.textChickenSisig.grid(row=7, column=1)

        # Total Cost Labels and Entries
        tk.Label(self.Total_Function, font=('arial', 14, 'bold'), text='Total of Drinks', bg='lightblue', fg='black', justify=tk.CENTER).grid(row=0, column=0, sticky=tk.W)
        self.textTotalofDrinks = ttk.Entry(self.Total_Function, font=('arial', 14, 'bold'), justify=tk.RIGHT, textvariable=self.Total_of_Drinks)
        self.textTotalofDrinks.grid(row=0, column=1)

        tk.Label(self.Total_Function, font=('arial', 14, 'bold'), text='Total of Foods', bg='lightblue', fg='black', justify=tk.CENTER).grid(row=1, column=0, sticky=tk.W)
        self.textTotalofFood = ttk.Entry(self.Total_Function, font=('arial', 14, 'bold'), justify=tk.RIGHT, textvariable=self.Total_of_Food)
        self.textTotalofFood.grid(row=1, column=1)

        tk.Label(self.Total_Function, font=('arial', 14, 'bold'), text='Service Charge', bg='lightblue', fg='black', justify=tk.CENTER).grid(row=2, column=0, sticky=tk.W)
        self.txtServiceCharge = ttk.Entry(self.Total_Function, font=('arial', 14, 'bold'), justify=tk.RIGHT, textvariable=self.ServiceCharge)
        self.txtServiceCharge.grid(row=2, column=1)

        tk.Label(self.Total_Function, font=('arial', 14, 'bold'), text='Paid Tax', bg='lightblue', fg='black', justify=tk.CENTER).grid(row=0, column=2, sticky=tk.W)
        self.textPaidTax = ttk.Entry(self.Total_Function, font=('arial', 14, 'bold'), justify=tk.RIGHT, textvariable=self.PaidTax)
        self.textPaidTax.grid(row=0, column=3)

        tk.Label(self.Total_Function, font=('arial', 14, 'bold'), text='Sub Total', bg='lightblue', fg='black', justify=tk.CENTER).grid(row=1, column=2, sticky=tk.W)
        self.textSubTotal = ttk.Entry(self.Total_Function, font=('arial', 14, 'bold'), justify=tk.RIGHT, textvariable=self.SubTotal)
        self.textSubTotal.grid(row=1, column=3)

        tk.Label(self.Total_Function, font=('arial', 14, 'bold'), text='Total', bg='lightblue', fg='black', justify=tk.CENTER).grid(row=2, column=2, sticky=tk.W)
        self.textTotalCost = ttk.Entry(self.Total_Function, font=('arial', 14, 'bold'), justify=tk.RIGHT, textvariable=self.TotalCost)
        self.textTotalCost.grid(row=2, column=3)

        # Receipt Text Area
        self.textReceipt = tk.Text(self.Receipt_Function, width=46, height=12, bg='white', bd=4, font=('arial', 12, 'bold'))
        self.textReceipt.grid(row=0, column=0)

        # Buttons
        ttk.Button(self.Buttons_Function, text='Total', command=self.TotalofUnit).grid(row=0, column=0, padx=16, pady=1)
        ttk.Button(self.Buttons_Function, text='Receipt', command=self.Receipt).grid(row=0, column=1, padx=16, pady=1)
        ttk.Button(self.Buttons_Function, text='Reset', command=self.Reset).grid(row=0, column=2, padx=16, pady=1)
        ttk.Button(self.Buttons_Function, text='Exit', command=self.iExit).grid(row=0, column=3, padx=16, pady=1)

        # Calculator
        self.txtDisplay = ttk.Entry(self.Calculator_Function, width=45, font=('arial', 12, 'bold'), justify=tk.RIGHT, textvariable=self.text_Input)
        self.txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
        self.txtDisplay.insert(0, "0")

        # Calculator Buttons
        ttk.Button(self.Calculator_Function, text='7', command=lambda: self.btnClick(7)).grid(row=2, column=0, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='8', command=lambda: self.btnClick(8)).grid(row=2, column=1, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='9', command=lambda: self.btnClick(9)).grid(row=2, column=2, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='+', command=lambda: self.btnClick('+')).grid(row=2, column=3, padx=16, pady=1)

        ttk.Button(self.Calculator_Function, text='4', command=lambda: self.btnClick(4)).grid(row=3, column=0, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='5', command=lambda: self.btnClick(5)).grid(row=3, column=1, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='6', command=lambda: self.btnClick(6)).grid(row=3, column=2, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='-', command=lambda: self.btnClick('-')).grid(row=3, column=3, padx=16, pady=1)

        ttk.Button(self.Calculator_Function, text='1', command=lambda: self.btnClick(1)).grid(row=4, column=0, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='2', command=lambda: self.btnClick(2)).grid(row=4, column=1, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='3', command=lambda: self.btnClick(3)).grid(row=4, column=2, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='*', command=lambda: self.btnClick('*')).grid(row=4, column=3, padx=16, pady=1)

        ttk.Button(self.Calculator_Function, text='0', command=lambda: self.btnClick(0)).grid(row=5, column=0, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='C', command=self.btnClear).grid(row=5, column=1, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='=', command=self.btnEquals).grid(row=5, column=2, padx=16, pady=1)
        ttk.Button(self.Calculator_Function, text='/', command=lambda: self.btnClick('/')).grid(row=5, column=3, padx=16, pady=1)

    # Function Definitions
    def iExit(self):
        iExit = tk.messagebox.askyesno("Exit Restaurant system", "Confirm if you want to exit")
        if iExit > 0:
            self.root.destroy()
            return

    def Reset(self):
        self.PaidTax.set("")
        self.SubTotal.set("")
        self.TotalCost.set("")
        self.Total_of_Food.set("")
        self.Total_of_Drinks.set("")
        self.ServiceCharge.set("")
        self.textReceipt.delete("1.0", tk.END)

        self.cocktail.set("0")
        self.iced_tea.set("0")
        self.hot_chocolate.set("0")
        self.orange_juice.set("0")
        self.milkshake.set("0")
        self.mountain_dew.set("0")
        self.coke.set("0")
        self.cobra.set("0")

        self.fried_chicken.set("0")
        self.kare_kare.set("0")
        self.crispy_pata.set("0")
        self.sinigang_baboy.set("0")
        self.sinigang_hipon.set("0")
        self.paneer_peri_peri.set("0")
        self.asparagus_tofu.set("0")
        self.chicken_sisig.set("0")

        self.variable1.set(0)
        self.variable2.set(0)
        self.variable3.set(0)
        self.variable4.set(0)
        self.variable5.set(0)
        self.variable6.set(0)
        self.variable7.set(0)
        self.variable8.set(0)
        self.variable9.set(0)
        self.variable10.set(0)
        self.variable11.set(0)
        self.variable12.set(0)
        self.variable13.set(0)
        self.variable14.set(0)
        self.variable15.set(0)
        self.variable16.set(0)

        self.textCocktail.configure(state=tk.DISABLED)
        self.textIcedTea.configure(state=tk.DISABLED)
        self.textHotChocolate.configure(state=tk.DISABLED)
        self.textOrangeJuice.configure(state=tk.DISABLED)
        self.textMilkShake.configure(state=tk.DISABLED)
        self.textMountainDew.configure(state=tk.DISABLED)
        self.textCoke.configure(state=tk.DISABLED)
        self.textCobra.configure(state=tk.DISABLED)
        self.textFriedChicken.configure(state=tk.DISABLED)
        self.textKareKAre.configure(state=tk.DISABLED)
        self.textCrispyPata.configure(state=tk.DISABLED)
        self.textSinigangBaboy.configure(state=tk.DISABLED)
        self.textSinigangHipon.configure(state=tk.DISABLED)
        self.textPaneerPeriPeri.configure(state=tk.DISABLED)
        self.textAsparagusTofu.configure(state=tk.DISABLED)
        self.textChickenSisig.configure(state=tk.DISABLED)

    def TotalofUnit(self):
        try:
            Unit1 = float(self.cocktail.get())
            Unit2 = float(self.iced_tea.get())
            Unit3 = float(self.hot_chocolate.get())
            Unit4 = float(self.orange_juice.get())
            Unit5 = float(self.milkshake.get())
            Unit6 = float(self.mountain_dew.get())
            Unit7 = float(self.coke.get())
            Unit8 = float(self.cobra.get())

            Unit9 = float(self.fried_chicken.get())
            Unit10 = float(self.kare_kare.get())
            Unit11 = float(self.crispy_pata.get())
            Unit12 = float(self.sinigang_baboy.get())
            Unit13 = float(self.sinigang_hipon.get())
            Unit14 = float(self.paneer_peri_peri.get())
            Unit15 = float(self.asparagus_tofu.get())
            Unit16 = float(self.chicken_sisig.get())

            Prices_Drinks = (Unit1 * 50) + (Unit2 * 45) + (Unit3 * 60) + (Unit4 * 35) + (Unit5 * 70) + (Unit6 * 40) + (Unit7 * 55) + (Unit8 * 75)
            Prices_Food = (Unit9 * 490) + (Unit10 * 450) + (Unit11 * 350) + (Unit12 * 400) + (Unit13 * 500) + (Unit14 * 250) + (Unit15 * 650) + (Unit16 * 370)

            DrinksPrices = "P" + str('%.2f' % Prices_Drinks)
            FoodsPrices = "P" + str('%.2f' % Prices_Food)
            self.Total_of_Food.set(FoodsPrices)
            self.Total_of_Drinks.set(DrinksPrices)
            SC = "P" + str('%.2f' % 1.59)
            self.ServiceCharge.set(SC)

            Sub_Total_of_Unit = "P" + str('%.2f' % (Prices_Drinks + Prices_Food + 1.59))
            self.SubTotal.set(Sub_Total_of_Unit)

            Tax = "P" + str('%.2f' % ((Prices_Drinks + Prices_Food + 1.59) * 0.15))
            self.PaidTax.set(Tax)

            TT = ((Prices_Drinks + Prices_Food + 1.59) * 0.15)
            TC = "P" + str('%.2f' % (Prices_Drinks + Prices_Food + 1.59 + TT))
            self.TotalCost.set(TC)
        except ValueError:
            tk.messagebox.showerror("Input Error", "Please enter valid numeric quantities.")

    def drinksCocktail(self):
        if self.variable1.get() == 1:
            self.textCocktail.configure(state=tk.NORMAL)
            self.textCocktail.focus()
            self.textCocktail.delete('0', tk.END)
            self.cocktail.set("")
        elif self.variable1.get() == 0:
            self.textCocktail.configure(state=tk.DISABLED)
            self.cocktail.set("0")

    def drinksIceTea(self):
        if self.variable2.get() == 1:
            self.textIcedTea.configure(state=tk.NORMAL)
            self.textIcedTea.focus()
            self.textIcedTea.delete('0', tk.END)
            self.iced_tea.set("")
        elif self.variable2.get() == 0:
            self.textIcedTea.configure(state=tk.DISABLED)
            self.iced_tea.set("0")

    def drinksHotChocolate(self):
        if self.variable3.get() == 1:
            self.textHotChocolate.configure(state=tk.NORMAL)
            self.textHotChocolate.delete('0', tk.END)
            self.textHotChocolate.focus()
        elif self.variable3.get() == 0:
            self.textHotChocolate.configure(state=tk.DISABLED)
            self.hot_chocolate.set("0")

    def drinksOrangeJuice(self):
        if self.variable4.get() == 1:
            self.textOrangeJuice.configure(state=tk.NORMAL)
            self.textOrangeJuice.delete('0', tk.END)
            self.textOrangeJuice.focus()
        elif self.variable4.get() == 0:
            self.textOrangeJuice.configure(state=tk.DISABLED)
            self.orange_juice.set("0")

    def drinksMilkShake(self):
        if self.variable5.get() == 1:
            self.textMilkShake.configure(state=tk.NORMAL)
            self.textMilkShake.delete('0', tk.END)
            self.textMilkShake.focus()
        elif self.variable5.get() == 0:
            self.textMilkShake.configure(state=tk.DISABLED)
            self.milkshake.set("0")

    def drinksMountainDew(self):
        if self.variable6.get() == 1:
            self.textMountainDew.configure(state=tk.NORMAL)
            self.textMountainDew.delete('0', tk.END)
            self.textMountainDew.focus()
        elif self.variable6.get() == 0:
            self.textMountainDew.configure(state=tk.DISABLED)
            self.mountain_dew.set("0")

    def drinksCoke(self):
        if self.variable7.get() == 1:
            self.textCoke.configure(state=tk.NORMAL)
            self.textCoke.delete('0', tk.END)
            self.textCoke.focus()
        elif self.variable7.get() == 0:
            self.textCoke.configure(state=tk.DISABLED)
            self.coke.set("0")

    def drinksCobra(self):
        if self.variable8.get() == 1:
            self.textCobra.configure(state=tk.NORMAL)
            self.textCobra.delete('0', tk.END)
            self.textCobra.focus()
        elif self.variable8.get() == 0:
            self.textCobra.configure(state=tk.DISABLED)
            self.cobra.set("0")

    def foodsFriedChicken(self):
        if self.variable9.get() == 1:
            self.textFriedChicken.configure(state=tk.NORMAL)
            self.textFriedChicken.delete('0', tk.END)
            self.textFriedChicken.focus()
        elif self.variable9.get() == 0:
            self.textFriedChicken.configure(state=tk.DISABLED)
            self.fried_chicken.set("0")

    def foodsKareKare(self):
        if self.variable10.get() == 1:
            self.textKareKAre.configure(state=tk.NORMAL)
            self.textKareKAre.delete('0', tk.END)
            self.textKareKAre.focus()
        elif self.variable10.get() == 0:
            self.textKareKAre.configure(state=tk.DISABLED)
            self.kare_kare.set("0")

    def foodsCrispyPata(self):
        if self.variable11.get() == 1:
            self.textCrispyPata.configure(state=tk.NORMAL)
            self.textCrispyPata.delete('0', tk.END)
            self.textCrispyPata.focus()
        elif self.variable11.get() == 0:
            self.textCrispyPata.configure(state=tk.DISABLED)
            self.crispy_pata.set("0")

    def foodsSinigangBaboy(self):
        if self.variable12.get() == 1:
            self.textSinigangBaboy.configure(state=tk.NORMAL)
            self.textSinigangBaboy.delete('0', tk.END)
            self.textSinigangBaboy.focus()
        elif self.variable12.get() == 0:
            self.textSinigangBaboy.configure(state=tk.DISABLED)
            self.sinigang_baboy.set("0")

    def foodsSinigangHipon(self):
        if self.variable13.get() == 1:
            self.textSinigangHipon.configure(state=tk.NORMAL)
            self.textSinigangHipon.delete('0', tk.END)
            self.textSinigangHipon.focus()
        elif self.variable13.get() == 0:
            self.textSinigangHipon.configure(state=tk.DISABLED)
            self.sinigang_hipon.set("0")

    def foodsPaneerPeriPeri(self):
        if self.variable14.get() == 1:
            self.textPaneerPeriPeri.configure(state=tk.NORMAL)
            self.textPaneerPeriPeri.delete('0', tk.END)
            self.textPaneerPeriPeri.focus()
        elif self.variable14.get() == 0:
            self.textPaneerPeriPeri.configure(state=tk.DISABLED)
            self.paneer_peri_peri.set("0")

    def foodsAsparagusTofu(self):
        if self.variable15.get() == 1:
            self.textAsparagusTofu.configure(state=tk.NORMAL)
            self.textAsparagusTofu.delete('0', tk.END)
            self.textAsparagusTofu.focus()
        elif self.variable15.get() == 0:
            self.textAsparagusTofu.configure(state=tk.DISABLED)
            self.asparagus_tofu.set("0")

    def foodsChickenSisig(self):
        if self.variable16.get() == 1:
            self.textChickenSisig.configure(state=tk.NORMAL)
            self.textChickenSisig.delete('0', tk.END)
            self.textChickenSisig.focus()
        elif self.variable16.get() == 0:
            self.textChickenSisig.configure(state=tk.DISABLED)
            self.chicken_sisig.set("0")

    def Receipt(self):
        self.textReceipt.delete("1.0", tk.END)
        x = random.randint(10908, 500876)
        randomRef = str(x)
        self.Receipt_Ref.set("Bill" + randomRef)

        self.textReceipt.insert(tk.END, 'Receipt Ref:\t\t\t' + self.Receipt_Ref.get() + '\t' + self.Date_of_Order.get() + '\n')
        self.textReceipt.insert(tk.END, 'Unit\t\t\t\t' + "Total of Unit \n")
        self.textReceipt.insert(tk.END, 'Cocktail:\t\t\t\t\t' + self.cocktail.get() + '\n')
        self.textReceipt.insert(tk.END, 'Iced Tea:\t\t\t\t\t' + self.iced_tea.get() + '\n')
        self.textReceipt.insert(tk.END, 'Hot Chocolate:\t\t\t\t\t' + self.hot_chocolate.get() + '\n')
        self.textReceipt.insert(tk.END, 'Orange Juice:\t\t\t\t\t' + self.orange_juice.get() + '\n')
        self.textReceipt.insert(tk.END, 'Milk Shake:\t\t\t\t\t' + self.milkshake.get() + '\n')
        self.textReceipt.insert(tk.END, 'Mountain Dew:\t\t\t\t\t' + self.mountain_dew.get() + '\n')
        self.textReceipt.insert(tk.END, 'Coke:\t\t\t\t\t' + self.coke.get() + '\n')
        self.textReceipt.insert(tk.END, 'Cobra:\t\t\t\t\t' + self.cobra.get() + '\n')
        self.textReceipt.insert(tk.END, 'Fried Chicken:\t\t\t\t\t' + self.fried_chicken.get() + '\n')
        self.textReceipt.insert(tk.END, 'Kare Kare:\t\t\t\t\t' + self.kare_kare.get() + '\n')
        self.textReceipt.insert(tk.END, 'Crispy Pata:\t\t\t\t\t' + self.crispy_pata.get() + '\n')
        self.textReceipt.insert(tk.END, 'Sinigang Baboy:\t\t\t\t\t' + self.sinigang_baboy.get() + '\n')
        self.textReceipt.insert(tk.END, 'Sinigang Hipon:\t\t\t\t\t' + self.sinigang_hipon.get() + '\n')
        self.textReceipt.insert(tk.END, 'Paneer Peri Peri:\t\t\t\t\t' + self.paneer_peri_peri.get() + '\n')
        self.textReceipt.insert(tk.END, 'Asparagus Tofu:\t\t\t\t\t' + self.asparagus_tofu.get() + '\n')
        self.textReceipt.insert(tk.END, 'Chicken Sisig:\t\t\t\t\t' + self.chicken_sisig.get() + '\n')
        self.textReceipt.insert(tk.END, 'Total of Drinks:\t\t\t\t' + self.Total_of_Drinks.get() + '\nTax Paid:\t\t\t\t' + self.PaidTax.get() + "\n")
        self.textReceipt.insert(tk.END, 'Total of Foods:\t\t\t\t' + self.Total_of_Food.get() + '\nSubTotal:\t\t\t\t' + str(self.SubTotal.get()) + "\n")
        self.textReceipt.insert(tk.END, 'Service Charge:\t\t\t\t' + self.ServiceCharge.get() + '\nTotal Cost:\t\t\t\t' + str(self.TotalCost.get()) + "\n")

    def btnClick(self, numbers):
        self.operator = self.operator + str(numbers)
        self.text_Input.set(self.operator)

    def btnClear(self):
        self.operator = ""
        self.text_Input.set("")

    def btnEquals(self):
        try:
            sumup = str(eval(self.operator))
            self.text_Input.set(sumup)
            self.operator = ""
        except:
            tk.messagebox.showerror("Calculator Error", "Invalid expression")
            self.operator = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantBillingApp(root)
    root.mainloop()
