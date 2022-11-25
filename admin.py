import os
import sqlite3
import re
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst


root = Tk()
root.geometry("1161x653")
root.title("admin")

username = StringVar()
password = StringVar()



def vider_fenetre() :
    for x in root.winfo_children():
        x.destroy()


#----Fenetre login

class login_page:
    def __init__(self, top=None):
        top.geometry("1161x653")
        top.resizable(0, 0)
        top.title("admin")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1161, height=653)
        self.img = PhotoImage(file= f"images/admin_login.png")
        self.label1.configure(image=self.img)
        

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.373, rely=0.273, width=300, height=24)
        self.entry1.configure(font="-family {Poppins} -size 10")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=username)

        self.entry2 = Entry(root)
        self.entry2.place(relx=0.373, rely=0.384, width=300, height=24)
        self.entry2.configure(font="-family {Poppins} -size 10")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(textvariable=password)

        self.button1 = Button(root)
        self.button1.place(relx=0.366, rely=0.683, width=300, height=40)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#D2463E")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#D2463E")
        self.button1.configure(font="-family {Poppins SemiBold} -size 20")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""LOGIN""")
        self.button1.configure(command=self.login)

    def login(self, Event=None):
        usernam = username.get()
        passwor = password.get()
        with sqlite3.connect("./database/database.db") as db:
            cur = db.cursor()
        find_user = "SELECT * FROM Admins WHERE USERNAME = ? and PASSWORD = ?"
        cur.execute(find_user, [usernam, passwor])
        results = cur.fetchall()
        db.close()
        if results:
                            
            messagebox.showinfo("Login Page", "The login is successful.")
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            vider_fenetre()  
            global adm
            global page2
            page2 = Admin_Page(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Incorrect username or password.")
            self.entry2.delete(0, END)

    
def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()

def inventory():
    vider_fenetre()
    global page3
    page3 = Inventory(root)
    page3.time()
    root.protocol("WM_DELETE_WINDOW", exitt)
    root.mainloop()


def customers():
    vider_fenetre()
    global page5
    page5 = Customers(root)
    page5.time()
    root.protocol("WM_DELETE_WINDOW", exitt)
    root.mainloop()


def invoices():
    vider_fenetre()
    global page7
    page7 = Invoices(root)
    page7.time()
    root.protocol("WM_DELETE_WINDOW", exitt)
    root.mainloop()


def about_us() :
    global toplevel
    global pageaboutus
    toplevel = Toplevel()
    pageaboutus = About_us(toplevel)
    toplevel.mainloop()

#----Fenetre About us
class About_us:
    def __init__(self, top=None):
        top.geometry("1161x653")
        top.resizable(0, 0)
        top.title("Qui sommes nous ?")

        self.label1 = Label(toplevel)
        self.label1.place(relx=0, rely=0, width=1161, height=653)
        self.img = PhotoImage(file="./pictures/aboutus.png")
        self.label1.configure(image=self.img)



#----Menu principal

class Admin_Page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("ADMIN Mode")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/admin.png")
        self.label1.configure(image=self.img)

        self.message = Label(root)
        self.message.place(relx=0.046, rely=0.056, width=62, height=30)
        self.message.configure(font="-family {Poppins} -size 12")
        self.message.configure(foreground="#ffffff")
        self.message.configure(background="#FE6B61")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.button1 = Button(root)
        self.button1.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 12")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Logout""")
        self.button1.configure(command=self.Logout)

        self.button2 = Button(root)
        self.button2.place(relx=0.14, rely=0.508, width=146, height=63)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#ffffff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#333333")
        self.button2.configure(background="#ffffff")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Inventory""")
        self.button2.configure(command=inventory)

        self.button3 = Button(root)
        self.button3.place(relx=0.338, rely=0.508, width=146, height=63)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#ffffff")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#333333")
        self.button3.configure(background="#ffffff")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Customers""")
        self.button3.configure(command=customers)


        self.button4 = Button(root)
        self.button4.place(relx=0.536, rely=0.508, width=146, height=63)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#ffffff")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#333333")
        self.button4.configure(background="#ffffff")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Invoices""")
        self.button4.configure(command=invoices)


        self.button5 = Button(root)
        self.button5.place(relx=0.732, rely=0.508, width=146, height=63)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#ffffff")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#333333")
        self.button5.configure(background="#ffffff")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""About Us""")
        self.button5.configure(command=about_us)

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=root)
        if sure == True:
            vider_fenetre()
            global login_return
            login_return = login_page(root)
            root.mainloop()





class Inventory:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Inventory")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/inventory.png")
        self.label1.configure(image=self.img)

        self.message = Label(root)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(root)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(root)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_product)

        self.button2 = Button(root)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(root)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""DELETE PRODUCT""")
        self.button3.configure(command=self.delete_product)


        self.button6 = Button(root)
        self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=self.Exit)

        self.scrollbarx = Scrollbar(root, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(root, orient=VERTICAL)
        self.tree = ttk.Treeview(root)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Product name",
                "CAU",
                "Selled quantity",
                "CSU",
                "CCU",
                "TS",
                "D",
                "Supplier",
                "Selling Price",
                "Available quantity",
                "Class"
            )
        )

        self.tree.heading("Product name", text="Product name", anchor=W)
        self.tree.heading("CAU", text="CAU", anchor=W)
        self.tree.heading("Selled quantity", text="Selled quantity", anchor=W)
        self.tree.heading("CSU", text="CSU", anchor=W)
        self.tree.heading("CCU", text="CCU", anchor=W)
        self.tree.heading("TS", text="TS", anchor=W)
        self.tree.heading("D", text="D", anchor=W)
        self.tree.heading("Supplier", text="Supplier", anchor=W)
        self.tree.heading("Selling Price", text="Selling Price", anchor=W)
        self.tree.heading("Available quantity", text="Available quantity", anchor=W)
        self.tree.heading("Class", text="Class", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=120)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)
        self.tree.column("#8", stretch=NO, minwidth=0, width=100)
        self.tree.column("#9", stretch=NO, minwidth=0, width=100)
        self.tree.column("#10", stretch=NO, minwidth=0, width=100)
        self.tree.column("#11", stretch=NO, minwidth=0, width=100)
        self.tree.bind("<Double-1>", self.double_tap)


        self.DisplayData()

    def double_tap(self , Event) :
        item = self.tree.identify('item', Event.x, Event.y)
        global bill_num
        global bill , productName 
        productName = self.tree.item(item)['values'][0]
        bill = Toplevel()
        pg = open_dynamique_table(bill)
        bill.mainloop()

    def DisplayData(self):
        with sqlite3.connect("./database/database.db") as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM Products")
            fetch = cur.fetchall()
            for data in fetch:
                self.tree.insert("", "end", values=(data))

    def search_product(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        try:
            to_search = str(self.entry1.get())
        except ValueError:
            messagebox.showerror("Oops!!", "Invalid Product Id.", parent=root)
        else:
            for search in val:
                if search==to_search:
                    self.tree.selection_set(val[val.index(search)-1])
                    self.tree.focus(val[val.index(search)-1])
                    messagebox.showinfo("Success!!", "Product ID: {} found.".format(self.entry1.get()), parent=root)
                    break
            else: 
                messagebox.showerror("Oops!!", "Product ID: {} not found.".format(self.entry1.get()), parent=root)
    
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)



    def delete_product(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected products?", parent=root)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%11==0:
                        to_delete.append(val[j])
                
                for k in to_delete:
                    with sqlite3.connect("./database/database.db") as db:
                        cur = db.cursor()
                        delete = "DELETE FROM Products WHERE DESIGNATION = ?"
                        cur.execute(delete, [k])
                        db.commit()

                messagebox.showinfo("Success!!", "Products deleted from database.", parent=root)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())

                self.DisplayData()
        else:
            messagebox.showerror("Error!!","Please select a product.", parent=root)
    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
        if sure == True:
            vider_fenetre()
            global adminmode_return1
            adminmode_return1 = Admin_Page(root)
            root.mainloop()

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=root)
        if sure == True:
            vider_fenetre()
            global login_return1
            login_return1 = login_page(root)
            root.mainloop()


class open_dynamique_table:
    def __init__(self, top=None):
        
        top.geometry("900x600")
        top.resizable(0, 0)
        top.title("Tableau dynamique")

        self.scrollbarx = Scrollbar(bill, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(bill, orient=VERTICAL)
        self.tree = ttk.Treeview(bill)
        self.tree.place(relx=0.01, rely=0.01, width=880, height=590)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")


        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Product name",
                "Transaction date",
                "Input",
                "Output",
                "Available quantity"

            )
        )

        self.tree.heading("Product name", text="Product name", anchor=W)
        self.tree.heading("Transaction date", text="Transaction date", anchor=W)
        self.tree.heading("Input", text="Input", anchor=W)
        self.tree.heading("Output", text="Output", anchor=W)
        self.tree.heading("Available quantity", text="Available quantity", anchor=W)


        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=120)
        self.DisplayData()

    def DisplayData(self):
        with sqlite3.connect("./database/database.db") as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM Tableau_dynamique WHERE PRODUCT_NAME = ?" , (productName,))
            fetch = cur.fetchall()
            for data in fetch:
                self.tree.insert("", "end", values=(data))

#--------------------------------------------------------
class Customers:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Customers Management")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/employee.png")
        self.label1.configure(image=self.img)

        self.message = Label(root)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(root)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(root)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_emp)

        self.button2 = Button(root)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(root)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""DELETE CUSTOMER""")
        self.button3.configure(command=self.delete_emp)


        self.button6 = Button(root)
        self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=self.Exit)

        self.scrollbarx = Scrollbar(root, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(root, orient=VERTICAL)
        self.tree = ttk.Treeview(root)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Employee ID",
                "Employee Name",
                "Username",
                "Password",
                "Age",
                "Contact number",
                "Adress"
            )
        )

        self.tree.heading("Employee ID", text="Employee ID", anchor=W)
        self.tree.heading("Employee Name", text="Employee Name", anchor=W)
        self.tree.heading("Username", text="Username", anchor=W)
        self.tree.heading("Password", text="Password", anchor=W)
        self.tree.heading("Age", text="Age", anchor=W)
        self.tree.heading("Contact number", text="Contact number", anchor=W)
        self.tree.heading("Adress", text="Adress", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=198)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)

        self.DisplayData()

    def DisplayData(self):
        with sqlite3.connect("./database/database.db") as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM Customers")
            fetch = cur.fetchall()
            for data in fetch:
                self.tree.insert("", "end", values=(data))

    def search_emp(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        to_search = int(to_search)
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Customer ID: {} found.".format(self.entry1.get()), parent=root)
                break
        else: 
            messagebox.showerror("Oops!!", "Customer ID: {} not found.".format(self.entry1.get()), parent=root)
    
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_emp(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected customer(s)?", parent=root)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%7==0:
                        to_delete.append(val[j])
                
                flag = 1
                with sqlite3.connect("./database/database.db") as db:
                    cur = db.cursor()
                    for k in to_delete:
                        delete = "DELETE FROM Customers WHERE ID = ?"                        
                        cur.execute(delete, [k])
                    db.commit()

                if flag==1:
                    messagebox.showinfo("Success!!", "Customer(s) deleted from database.", parent=root)
                    self.sel.clear()
                    self.tree.delete(*self.tree.get_children())
                    self.DisplayData()
        else:
            messagebox.showerror("Error!!","Please select a customer.", parent=root)

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
        if sure == True:
            vider_fenetre()
            global adminmode_return2
            adminmode_return2 = Admin_Page(root)
            root.mainloop()

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=root)
        if sure == True:
            vider_fenetre()
            global login_return2
            login_return2 = login_page(root)
            root.mainloop()
#---------------------------------------------------------
#---------------------------------------------------------


class Invoices:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Invoices Management")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/invoices.png")
        self.label1.configure(image=self.img)

        self.message = Label(root)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(root)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(root)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_bill)

        self.button2 = Button(root)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)


        self.button5 = Button(root)
        self.button5.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#CF1E14")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""DELETE BILL""")
        self.button5.configure(command=self.delete_bill)

        self.button6 = Button(root)
        self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=self.Exit)

        self.scrollbarx = Scrollbar(root, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(root, orient=VERTICAL)
        self.tree = ttk.Treeview(root)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Order ID",
                "Purchase date",
                "Product name",
                "Quantity",
                "Unit price",
                "Total price",
                "Bill state" ,
                "Supplier"
            )
        )

        self.tree.heading("Order ID", text="Order ID", anchor=W)
        self.tree.heading("Purchase date", text="Purchase date", anchor=W)
        self.tree.heading("Product name", text="Product name", anchor=W)
        self.tree.heading("Quantity", text="Quantity", anchor=W)
        self.tree.heading("Unit price", text="Unit price", anchor=W)
        self.tree.heading("Total price", text="Total price", anchor=W)
        self.tree.heading("Bill state", text="Bill state", anchor=W)
        self.tree.heading("Supplier", text="Supplier", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=198)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)

        self.tree.bind("<Double-1>", self.double_tap)


        self.DisplayData()

    def double_tap(self , Event) :
        item = self.tree.identify('item', Event.x, Event.y)
        global bill_num
        global bill , date , productName ,qtt , unitPrice , totalPrice
        bill_num = self.tree.item(item)['values'][0]
        date = self.tree.item(item)['values'][1]
        date = date[:11]
        productName = self.tree.item(item)['values'][0]
        qtt = self.tree.item(item)['values'][3]
        unitPrice = self.tree.item(item)['values'][4]
        totalPrice = self.tree.item(item)['values'][5]
        bill = Toplevel()
        pg = open_bill(bill)
        bill.mainloop()





    def DisplayData(self):
        with sqlite3.connect("./database/database.db") as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM HISTORIQUE_FOURNISSEUR")
            fetch = cur.fetchall()
            for data in fetch:
                self.tree.insert("", "end", values=(data))

    def search_bill(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        to_search = int(to_search)
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Bill number: {} found.".format(self.entry1.get()), parent=root)
                break
        else: 
            messagebox.showerror("Oops!!", "Bill number: {} not found.".format(self.entry1.get()), parent=root)
    
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_bill(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected bill(s)?", parent=root)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%7==0:
                        to_delete.append(val[j])
                
                flag = 1
                with sqlite3.connect("./database/database.db") as db:
                    cur = db.cursor()
                    for k in to_delete:
                        select = "SELECT * FROM HISTORIQUE_FOURNISSEUR WHERE ORDER_ID = ?"
                        cur.execute(select , [k])
                        result = cur.fetchall()
                        if not result :
                            break 
                        elif result[0][6] == 'not processed' :
                            delete = "DELETE FROM HISTORIQUE_FOURNISSEUR WHERE ORDER_ID = ?"                        
                            cur.execute(delete, [k])
                        elif result[0][6] =='processed' :
                            flag = 0 
                            messagebox.showerror("Error!!","You can not delete a bill which is already processed.", parent=root)
                            self.sel.clear()
                            self.tree.delete(*self.tree.get_children())
                            self.DisplayData()

                    db.commit()

                if flag==1:
                    messagebox.showinfo("Success!!", "Bill(s) deleted from database.", parent=root)
                    self.sel.clear()
                    self.tree.delete(*self.tree.get_children())
                    self.DisplayData()
        else:
            messagebox.showerror("Error!!","Please select a bill.", parent=root)

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
        if sure == True:
            vider_fenetre()
            global adminmode_return3
            adminmode_return3 = Admin_Page(root)
            root.mainloop()


    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=root)
        if sure == True:
            vider_fenetre()
            global login_return3
            login_return3 = login_page(root)
            root.mainloop()



class open_bill:
    def __init__(self, top=None):
        
        top.geometry("765x488")
        top.resizable(0, 0)
        top.title("Bill")

        self.label1 = Label(bill)
        self.label1.place(relx=0, rely=0, width=765, height=488)
        self.img = PhotoImage(file="./images/bill.png")
        self.label1.configure(image=self.img)

        self.bill_message = Text(bill)
        self.bill_message.place(relx=0.150, rely=0.246, width=90, height=18)
        self.bill_message.configure(font="-family {Podkova} -size 10")
        self.bill_message.configure(borderwidth=0)
        self.bill_message.configure(background="#ffffff")

        self.bill_date_message = Text(bill)
        self.bill_date_message.place(relx=0.780, rely=0.247, width=90, height=18)
        self.bill_date_message.configure(font="-family {Podkova} -size 10")
        self.bill_date_message.configure(borderwidth=0)
        self.bill_date_message.configure(background="#ffffff")


        self.Scrolledtext1 = tkst.ScrolledText(top)
        self.Scrolledtext1.place(relx=0.044, rely=0.41, width=695, height=284)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
        self.Scrolledtext1.configure(state="disabled")

    
        self.bill_message.insert(END, bill_num)
        self.bill_message.configure(state="disabled")

        self.bill_date_message.insert(END, date)
        self.bill_date_message.configure(state="disabled")


        self.Scrolledtext1.configure(state="normal")
        bill_text = "{}\t\t\t\t\t\t\t{}\t\t\t\t\t\t{}\n".format(productName, qtt, unitPrice)
        self.Scrolledtext1.insert('insert', bill_text)           

        divider = "\n\n\n"+("─"*70)
        self.Scrolledtext1.insert('insert', divider)
        total = "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t{}".format(totalPrice)
        self.Scrolledtext1.insert('insert', total)
        divider2 = "\n"+("─"*70)
        self.Scrolledtext1.insert('insert', divider2)
        self.Scrolledtext1.configure(state="disabled")



Login_page = login_page(root)
root.mainloop()
