from tkinter import *
import os
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import uuid
from datetime import datetime

global dt
global unique_id


# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S -----> formating the date 
dt = now.strftime("%d/%m/%Y %H:%M:%S")

# generation d'un nombre unique et aleatoire 
unique_id = str(uuid.uuid4().fields[-1])[:7]




# Creation de la fenetre principale root
root = Tk()
root.geometry("1161x653")
root.title("customer")


# Creation e variables utiles pour la suite du programme 
username = StringVar()
password = StringVar()
product_name = StringVar()
quantity = StringVar()




def vider_fenetre() :
    for x in root.winfo_children():
        x.destroy() 


class login_page:
    def __init__(self, top=None):
        top.geometry("1161x653")
        top.resizable(0, 0)
        top.title("customer")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1161, height=653)
        self.img = PhotoImage(file= f"images/costumer_login.png")
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
        global usernam
        usernam = username.get()
        passwor = password.get()
        with sqlite3.connect("./database/database.db") as db:
            cur = db.cursor()
        find_user = "SELECT * FROM Customers WHERE USERNAME = ? and PASSWORD = ?"
        cur.execute(find_user, [usernam, passwor])
        results = cur.fetchall()
        global full_name
        full_name = results[0][1]
        db.close()
        if results:
                            
            messagebox.showinfo("Login Page", "The login is successful.")
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)

            vider_fenetre()
            global orders_management_page
            orders_management_page = Orders_management_page(root)
            root.mainloop()
                            
                
        else:
            messagebox.showerror("Error", "Incorrect username or password.")
            self.entry2.delete(0, END) 


def btn_clicked():
    root.destroy()

    
class Orders_management_page:
    def __init__(self , top = None):
        top.geometry("1161x653")
        top.resizable(0, 0)
        top.title("Orders management interface")
        top.configure(bg = "#ffffff")

        self.canvas = Canvas(
                 root,
                 bg = "#ffffff",
                 height = 653,
                 width = 1161,
                 bd = 0,
                 highlightthickness = 0,
                 relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"pictures/orders_management.png")
        self.background = self.canvas.create_image(580.5, 326.5, image=self.background_img)
        self.img0 = PhotoImage(file = f"pictures/exit_button.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")
        self.b0.place(
            x = 259, y = 546,
            width = 99,
            height = 43)
        
        self.img1 = PhotoImage(file = f"pictures/buy_button.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.buy_button,
            relief = "flat")
        
        self.b1.place(
            x = 107, y = 545,
            width = 99,
            height = 44)

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.18, rely=0.675, width=210, height=25)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=product_name)

        self.entry2 = Entry(root)
        self.entry2.place(relx=0.14, rely=0.765, width=250, height=25)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(textvariable=quantity)

        self.button20 = Button(root)
        self.button20.place(relx=0.05, rely=0.13, width=60, height=23)
        self.button20.configure(relief="flat")
        self.button20.configure(overrelief="flat")
        self.button20.configure(activebackground="#CF1E14")
        self.button20.configure(cursor="hand2")
        self.button20.configure(foreground="#ffffff")
        self.button20.configure(background="#CF1E14")
        self.button20.configure(font="-family {Poppins SemiBold} -size 12")
        self.button20.configure(borderwidth="0")
        self.button20.configure(text="""Logout""")
        self.button20.configure(command=self.Logout)


        self.tree = ttk.Treeview(root , show='headings')
        self.scrollbarx = Scrollbar(root, orient=HORIZONTAL , command=self.tree.xview)
        self.scrollbary = Scrollbar(root , orient=VERTICAL , command=self.tree.yview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=440)
        self.scrollbarx.place(relx=0.400, rely=0.924, width=630, height=22)
        self.tree.place(relx=0.400, rely=0.203, width=630, height=450)

        self.tree.configure(
                    yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
                )
        self.tree.configure(selectmode="extended")

        self.tree.configure(
                    columns=['Order ID', 'Purchase date', 'Product name', 'Quantity',
                    'Unit price', 'Total price', 'Delivery charge', 'Customer name']
                        )

        self.tree.heading("Order ID", text="Order ID", anchor=W)
        self.tree.heading("Purchase date", text='Purchase date', anchor=W)
        self.tree.heading("Product name", text="Product name", anchor=W)
        self.tree.heading("Quantity", text="Quantity", anchor=W)
        self.tree.heading("Unit price", text="Unit price", anchor=W)
        self.tree.heading("Total price", text="Total price", anchor=W)
        self.tree.heading("Delivery charge", text="Delivery charge", anchor=W)
        self.tree.heading("Customer name", text="Customer name", anchor=W)

        # another tree 
        self.tree2 = ttk.Treeview(root , show='headings')
        self.scrollbarx2 = Scrollbar(root, orient=HORIZONTAL , command=self.tree2.xview)
        self.scrollbary2 = Scrollbar(root , orient=VERTICAL , command=self.tree2.yview)

        self.scrollbary2.place(relx=0.368, rely=0.210, width=15, height=300)
        self.scrollbarx2.place(relx=0.047, rely=0.208, width=370, height=15)
        self.tree2.place(relx=0.045, rely=0.240, width=370, height=270)

        self.tree2.configure(
                    yscrollcommand=self.scrollbary2.set, xscrollcommand=self.scrollbarx2.set
                )
        self.tree2.configure(selectmode="extended")
        self.tree2.configure(
                    columns=['Product name', 'Price', 'Stock available']
                        )

        self.tree2.heading("Product name", text="Product name", anchor=W)
        self.tree2.heading("Price", text='Price', anchor=W)
        self.tree2.heading("Stock available", text="Stock available", anchor=W)
        self.display_products()
        self.display_historique_client()

    def display_products(self) :
        with sqlite3.connect("./database/database.db") as db:
            cur = db.cursor()       
        cur.execute("SELECT * FROM Products ")
        fetch = cur.fetchall()
        for data in fetch :
            self.tree2.insert("" , "end" , values = (data[0] , data[8] , data[9]))
        db.close()

    def display_historique_client(self) :
        with sqlite3.connect("./database/database.db") as db:
            cur = db.cursor()
        cur.execute('SELECT * FROM Historique_client WHERE CUSTOMER_NAME = ?'  , (full_name,))
        fetch2 = cur.fetchall()
        for data in fetch2:
            self.tree.insert("", "end", values=(data))
        db.close()

    def clear_tree(self) :
        for i in self.tree.get_children():
            self.tree.delete(i)
        for i in self.tree2.get_children():
            self.tree2.delete(i)

    def Logout(self):
       sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=root)
       if sure == True:
            vider_fenetre()
            global login_return3
            login_return3 = login_page(root)
            root.mainloop()

    def buy_button(self) :
        product_name_got = product_name.get()
        quantity_got = quantity.get()
        quantity_got = int(quantity_got)
        with sqlite3.connect("./database/database.db") as db:
            cur = db.cursor()
        find_user = "SELECT * FROM Products WHERE DESIGNATION = ? "
        cur.execute(find_user, [product_name_got])
        result_product_name = cur.fetchall()
        quantity_product = result_product_name[0][9]
        price_product = result_product_name[0][8]
        class_product = result_product_name[0][10]
        if result_product_name:
            if quantity_product >= quantity_got & quantity_got > 0  :
                new_quantity = quantity_product - quantity_got
                
                cur.execute('INSERT INTO Historique_client VALUES (?, ? , ? , ? , ?, ? , ?,?)' , (str(uuid.uuid4().fields[-1])[:7], dt , product_name_got , quantity_got , price_product , price_product*quantity_got, 50 , full_name))
                cur.execute("UPDATE Products SET STOCK_DISPONIBLE = ?  WHERE DESIGNATION = ? "  ,(new_quantity , product_name_got) ) 
                cur.execute('INSERT OR IGNORE INTO Tableau_dynamique VALUES (?, ? , ? , ? , ?)' , (product_name_got , dt , 0 , quantity_got , new_quantity))  

                if class_product == 'A' :
                    cur.execute('SELECT * FROM CLASS_A WHERE PRODUCT_NAME = ?' , ( product_name_got,))
                    resultat =cur.fetchall()
                    seuil = resultat[0][9]
                    QEC = resultat[0][8]
                    CCU = resultat[0][3]
                    fournisseur = result_product_name[0][7]
                    if new_quantity <= seuil:
                        cur.execute('SELECT * FROM HISTORIQUE_FOURNISSEUR WHERE PRODUCT_NAME = ?' , ( product_name_got,))
                        resultat2 = cur.fetchall()
                        
                        if not resultat2   :
                            cur.execute('INSERT OR IGNORE INTO HISTORIQUE_FOURNISSEUR VALUES (?, ? , ? , ? , ? ,?,?,?)' , (str(uuid.uuid4().fields[-1])[:7] , dt , product_name_got , QEC, CCU , QEC*CCU ,'not processed' , fournisseur))
                            print('COMMANDE ENVOYEE')
                        elif resultat2 :
                            if resultat2[-1][6] == 'processed' :
                                cur.execute('INSERT OR IGNORE INTO HISTORIQUE_FOURNISSEUR VALUES (?, ? , ? , ? , ? ,?,?,?)' , (str(uuid.uuid4().fields[-1])[:7] , dt , product_name_got , QEC, CCU , QEC*CCU ,'not processed' , fournisseur))
                                print('COMMANDE ENVOYEE')

                if class_product == 'C' :
                    cur.execute('SELECT * FROM CLASS_C WHERE PRODUCT_NAME = ?' , ( product_name_got,))
                    resultat =cur.fetchall()
                    QMIN = resultat[0][6]
                    QMAX = resultat[0][5]
                    CCU = resultat[0][3]
                    QC = QMAX - new_quantity
                    fournisseur = result_product_name[0][7]
                    if new_quantity <= QMIN:
                        cur.execute('SELECT * FROM HISTORIQUE_FOURNISSEUR WHERE PRODUCT_NAME = ?' , ( product_name_got,))
                        resultat2 = cur.fetchall()
                        if not resultat2 :
                            cur.execute('INSERT OR IGNORE INTO HISTORIQUE_FOURNISSEUR VALUES (?, ? , ? , ? , ? ,?,?,?)' , (str(uuid.uuid4().fields[-1])[:7] , dt , product_name_got , QC, CCU , QC*CCU ,'not processed' , fournisseur))
                            print('COMMANDE ENVOYEE')
                        elif resultat2:
                            if resultat2[-1][6] == 'processed' :
                                cur.execute('INSERT OR IGNORE INTO HISTORIQUE_FOURNISSEUR VALUES (?, ? , ? , ? , ? ,?,?,?)' , (str(uuid.uuid4().fields[-1])[:7] , dt , product_name_got , QC, CCU , QC*CCU ,'not processed' , fournisseur))
                                print('COMMANDE ENVOYEE')

                db.commit()
                self.clear_tree()
                self.display_historique_client()    
                self.display_products()  

            else :
                messagebox.showerror("Error", "Incorrect quantity")


                            
                
        else:
            messagebox.showerror("Error", "Incorrect product name")
            self.entry2.delete(0, END) 

        db.close()





Login_page = login_page(root)
root.mainloop()