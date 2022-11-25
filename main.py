from tkinter import *
import os
from tkinter import messagebox
import sqlite3
import uuid
from datetime import datetime


#----FONCTION RESPONSABLE DE LA VERIFICATION ET DE L'EXECUTION DE L'APPROVISIONNEMENT DES 
#---------------------------PRODUITS DE LA CLASSE B : 
#----Elle envoie une facture automatiquement au fournisseur si les conditions d'approvisionnement sont respectes 

def approvisionnement_class_B() :
    with sqlite3.connect("./database/database.db") as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM CLASS_B ")
        liste_products = cur.fetchall()
        for i in range(len(liste_products)) :
            product_name = liste_products[i][0]
            
            CCU =liste_products[i][3]
            NDR = liste_products[i][6]
            cur.execute("SELECT * FROM Products WHERE DESIGNATION = ? " , (product_name,))
            productfetch = cur.fetchall()
            
            supplier = productfetch[0][7]
            stock_dispo = productfetch[0][9]
            cur.execute("SELECT * FROM Tableau_dynamique WHERE PRODUCT_NAME = ? AND INPUT != 0 " , (product_name,))                       
            fetch = cur.fetchall()
            
            if not fetch :
                cur.execute('SELECT * FROM HISTORIQUE_FOURNISSEUR WHERE PRODUCT_NAME = ?' , ( product_name,))
                resultat = cur.fetchall()
                if not resultat :
                    present_date = datetime.now()
                    present_date = present_date.strftime("%Y-%m-%d")
                    
                    cur.execute('INSERT INTO HISTORIQUE_FOURNISSEUR VALUES (?, ? , ? , ? , ? ,?,?,?)' , (str(uuid.uuid4().fields[-1])[:7] , present_date , product_name , abs(NDR- stock_dispo), CCU , abs(NDR- stock_dispo)*CCU ,'not processed' , supplier))
                
                    db.commit()
                else :
                    if resultat[-1][6] == 'processed' :
                        present_date = datetime.now()
                        present_date = present_date.strftime("%Y-%m-%d")
                        
                        cur.execute('INSERT INTO HISTORIQUE_FOURNISSEUR VALUES (?, ? , ? , ? , ? ,?,?,?)' , (str(uuid.uuid4().fields[-1])[:7] , present_date , product_name , abs(NDR- stock_dispo), CCU , abs(NDR- stock_dispo)*CCU ,'not processed' , supplier))
                    
                        db.commit()

            else :
                last_date = fetch[-1][1]
                last_date = time.strptime(last_date, "%d/%m/%Y")
                present_date = datetime.now()
                present_date = present_date.strftime("%Y-%m-%d")
                if (present_date - last_date).days > 30 :
                    cur.execute('SELECT * FROM HISTORIQUE_FOURNISSEUR WHERE PRODUCT_NAME = ?' , ( product_name,))
                    resultat = cur.fetchall()
                    if not resultat :

                        #approvisionnement .............
                        cur.execute('INSERT INTO HISTORIQUE_FOURNISSEUR VALUES (?, ? , ? , ? , ? ,?,?,?)' , (str(uuid.uuid4().fields[-1])[:7] , present_date , product_name , abs(NDR- stock_dispo), CCU , abs(NDR- stock_dispo)*CCU ,'not processed' , supplier))
                    
                        db.commit()
                    else :
                        if resultat[-1][6] == 'processed' :
                            cur.execute('INSERT INTO HISTORIQUE_FOURNISSEUR VALUES (?, ? , ? , ? , ? ,?,?,?)' , (str(uuid.uuid4().fields[-1])[:7] , present_date , product_name , abs(NDR- stock_dispo), CCU , abs(NDR- stock_dispo)*CCU ,'not processed' , supplier))
                        
                            db.commit()
        db.commit()



approvisionnement_class_B()




#---Executer le programme customer.py

def custumer_login() :
    window.withdraw()
    os.system("python customer.py")
    window.deiconify()


#---Executer le programme supplier.py
def supplier_login() :
    window.withdraw()
    os.system("python supplier.py")
    window.deiconify()


#---Executer le programme admin.py
def admin_login() :
    window.withdraw()
    os.system("python admin.py")
    window.deiconify()

#---Fermer le programme 
def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=window)
    if sure == True:
        window.destroy()

def about_us() :
    global toplevel
    global pageaboutus
    toplevel = Toplevel()
    pageaboutus = About_us(toplevel)
    toplevel.mainloop()



        


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#                  Interface graphique du menu principal 



class About_us:
    def __init__(self, top=None):
        top.geometry("1161x653")
        top.resizable(0, 0)
        top.title("Qui sommes nous ?")

        self.label1 = Label(toplevel)
        self.label1.place(relx=0, rely=0, width=1161, height=653)
        self.img = PhotoImage(file="./pictures/aboutus.png")
        self.label1.configure(image=self.img)


window = Tk()
window.geometry("1161x653")
window.configure(bg = "#ffffff")
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", Exit)
 
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 653,
    width = 1161,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"pictures/background.png")

background = canvas.create_image(
    580.5, 326.5,
    image=background_img)

img0 = PhotoImage(file = f"pictures/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = supplier_login,
    relief = "flat")

b0.place(
    x = 641, y = 406,
    width = 139,
    height = 50)

img1 = PhotoImage(file = f"pictures/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = admin_login,
    relief = "flat")

b1.place(
    x = 95, y = 406,
    width = 141,
    height = 50)

img2 = PhotoImage(file = f"pictures/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = about_us,
    relief = "flat")

b2.place(
    x = 917, y = 406,
    width = 141,
    height = 50)

img3 = PhotoImage(file = f"pictures/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = custumer_login,
    relief = "flat")

b3.place(
    x = 368, y = 406,
    width = 141,
    height = 50)



window.mainloop()


