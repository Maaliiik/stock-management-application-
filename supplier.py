from tkinter import *
from tkinter import ttk
import sqlite3
from datetime import datetime
from tkinter import messagebox
from tkinter import scrolledtext as tkst







def vider_fenetre() :
    for x in window.winfo_children():
        x.destroy()

def btn_clicked():
    print("Button Clicked")



def clear_tree() :
    for i in tree.get_children():
        tree.delete(i)



def display_historique_client() :
    with sqlite3.connect("./database/database.db") as db:
        cur = db.cursor()
    cur.execute('SELECT * FROM Historique_FOURNISSEUR WHERE COMPANY_NAME = ?'  , (full_name,))
    fetch2 = cur.fetchall()
    for data in fetch2:
        tree.insert("", "end", values=(data))
    db.close()




sel = []
def on_tree_select(Event):
    sel.clear()
    for i in tree.selection():
        if i not in sel:
            sel.append(i)




def double_tap(Event):
    item = tree.identify('item', Event.x, Event.y)
    global bill_num
    global bill , date , productName ,qtt , unitPrice , totalPrice
    bill_num = tree.item(item)['values'][0]
    date = tree.item(item)['values'][1]
    date = date[:11]
    productName = tree.item(item)['values'][2]
    qtt = tree.item(item)['values'][3]
    unitPrice = tree.item(item)['values'][4]
    totalPrice = tree.item(item)['values'][5]
    bill = Toplevel()
    pg = open_bill(bill)
    bill.mainloop()
        



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


class login_page:
    def __init__(self, top=None):
        top.geometry("1161x653")
        top.resizable(0, 0)
        top.title("Supplier")
        global username , password
        username = StringVar()
        password = StringVar()

        self.label1 = Label(window)
        self.label1.place(relx=0, rely=0, width=1161, height=653)
        self.img = PhotoImage(file= f"images/costumer_login.png")
        self.label1.configure(image=self.img)
        

        self.entry1 = Entry(window)
        self.entry1.place(relx=0.373, rely=0.273, width=300, height=24)
        self.entry1.configure(font="-family {Poppins} -size 10")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=username)

        self.entry2 = Entry(window)
        self.entry2.place(relx=0.373, rely=0.384, width=300, height=24)
        self.entry2.configure(font="-family {Poppins} -size 10")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(textvariable=password)

        self.button1 = Button(window)
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
        find_user = "SELECT * FROM Products WHERE FOURNISSEUR = ?"
        cur.execute(find_user, [usernam])
        results = cur.fetchall()
        
        
        db.close()
        if results :
            if passwor == usernam :
                global full_name
                full_name = results[0][7]
                            
                messagebox.showinfo("Login Page", "The login is successful.")
                self.entry1.delete(0, END)
                self.entry2.delete(0, END)

                vider_fenetre()
                billing_system()

        else:
            messagebox.showerror("Error", "Incorrect username or password.")
            self.entry2.delete(0, END) 





def send_bill():
	if sel :
		values = tree.item(sel[0])["values"]
		order_id = values[0]
		product_name = values[2]
		quantity = values[3]
		processed = 'processed'
		print(values[6])
		if values[6] !='processed' :
			with sqlite3.connect("./database/database.db") as db:
				cur = db.cursor()
			cur.execute('UPDATE Historique_FOURNISSEUR SET BILL_STATE = ? WHERE ORDER_ID = ? ' , (processed , order_id))

			cur.execute('SELECT * FROM Products WHERE DESIGNATION = ?'  , (product_name,))
			product_got = cur.fetchall()
			last_quantity = product_got[0][9]
			new_quantity = last_quantity + quantity
			cur.execute("UPDATE Products SET STOCK_DISPONIBLE = ?  WHERE DESIGNATION = ? "  ,(new_quantity , product_name) ) 
			cur.execute('INSERT INTO Tableau_dynamique VALUES (?, ? , ? , ? , ?)' , (product_name , datetime.now().strftime("%d/%m/%Y %H:%M:%S") , quantity , 0 , new_quantity))
			db.commit()
			print(last_quantity , quantity , new_quantity)
			messagebox.showinfo("Success !", "The bill is sent and the database is updated.")
			db.close()

		else :
			messagebox.showerror("Error", "the bill is already sent.")


		clear_tree()
		display_historique_client()

	else :
		messagebox.showerror("Error", "select an item")

def Logout():
    sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=window)
    if sure == True:
        vider_fenetre()
        global login_return3
        login_return3 = login_page(window)
        window.mainloop()


def billing_system() :	
    window.geometry("1161x653")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 653,
        width = 1161,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"pictures/invoices_bg.png")
    background = canvas.create_image(
        580.5, 326.5,
        image=background_img)

    img0 = PhotoImage(file = f"pictures/generate_bill_button.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = send_bill,
        relief = "flat")

    b0.place(
        x = 495, y = 570,
        width = 167,
        height = 46)

    button2 = Button(window)
    button2.place(relx=0.035, rely=0.106, width=60, height=23)
    button2.configure(relief="flat")
    button2.configure(overrelief="flat")
    button2.configure(activebackground="#CF1E14")
    button2.configure(cursor="hand2")
    button2.configure(foreground="#ffffff")
    button2.configure(background="#CF1E14")
    button2.configure(font="-family {Poppins SemiBold} -size 12")
    button2.configure(borderwidth="0")
    button2.configure(text="""Logout""")
    button2.configure(command=Logout)


    global tree 
    tree = ttk.Treeview(window , show='headings')
    scrollbarx = Scrollbar(window, orient=HORIZONTAL , command=tree.xview)
    scrollbary = Scrollbar(window , orient=VERTICAL , command=tree.yview)

    scrollbary.place(relx=0.954, rely=0.203, width=22, height=370)
    scrollbarx.place(relx=0.07, rely=0.800, width=980, height=22)
    tree.place(relx=0.07, rely=0.203, width=980, height=370)

    tree.configure(
                        yscrollcommand=scrollbary.set , xscrollcommand=scrollbarx.set
                    )

    tree.configure(selectmode="browse")

    tree.bind("<<TreeviewSelect>>", on_tree_select)


    tree.configure(
                        columns=['Order ID', 'Purchase date', 'Product name', 'Quantity',
                        'Unit price', 'Total price', 'Bill state', 'Company name']
                            )

    tree.heading("Order ID", text="Order ID", anchor=W)
    tree.heading("Purchase date", text='Purchase date', anchor=W)
    tree.heading("Product name", text="Product name", anchor=W)
    tree.heading("Quantity", text="Quantity", anchor=W)
    tree.heading("Unit price", text="Unit price", anchor=W)
    tree.heading("Total price", text="Total price", anchor=W)
    tree.heading("Bill state", text="Bill state", anchor=W)
    tree.heading("Company name", text="Company name", anchor=W)

    tree.bind("<<TreeviewSelect>>", on_tree_select)
    tree.bind("<Double-1>", double_tap)



    display_historique_client()
    window.mainloop()


window = Tk()
fournisseur_login = login_page(window)


window.resizable(False, False)
window.mainloop()