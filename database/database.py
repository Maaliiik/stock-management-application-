import sqlite3
import pandas as pd
import sys 
from datetime import datetime
import uuid
sys.path.append("c:/users/pc/anaconda3/lib/site-packages")
#---- load products data
#data = pd.read_excel('BDD.xlsx' , sheet_name=0)

#data.loc[data["Quantité vendue"] == 19 , "Csu ( euros)"] = 10.5
#data.loc[data["Quantité vendue"] == 15 , "Csu ( euros)"] = 6.9
#data.loc[data["Quantité vendue"] == 175 , "Prix de vente"] = 23.1
#data.loc[data["Quantité vendue"] == 160 , "Prix de vente"] = 18.9




#------load class a , b, c  data 

#data2 = pd.read_excel('classe_a.xlsx')
#data3 = pd.read_excel('classe_b.xlsx')
#data4 = pd.read_excel('classe_c.xlsx')



# datetime object containing current date and time
#now = datetime.now()

# dd/mm/YY H:M:S
#dt = now.strftime("%d/%m/%Y %H:%M:%S")

#unique_id = str(uuid.uuid4().fields[-1])[:7]
#unique_id2 = str(uuid.uuid4().fields[-1])[:7]

conn = sqlite3.connect('C:/Users/pc/Desktop/projet znija/database/database.db')

cursor = conn.cursor()

#CREATE CUSTOMERS TABLE

#conn.execute('''CREATE TABLE IF NOT EXISTS Customers (ID INT PRIMARY KEY     NOT NULL, FULL_NAME TEXT NOT NULL,USERNAME TEXT NOT NULL,PASSWORD TEXT NOT NULL ,AGE INT NOT NULL,CONTACT_NUMBER INT ,ADDRESS TEXT NOT NULL) ''' )


#conn.execute('INSERT OR IGNORE INTO Customers VALUES (?, ? , ? , ? , ?, ? , ?)' , (1111, "Ammar khodja malik" , 'malik' , 'malik' , 21 , 555817998 , 'garidi kouba'))
#conn.execute('INSERT OR IGNORE INTO Customers VALUES (?, ? , ? , ? , ?, ? , ?)' , (1000, "Ammar khodja yasmine" , 'mimine' , 'mimine' , 14 , 555817999 , 'garidi kouba'))
#conn.execute('INSERT OR IGNORE INTO Customers VALUES (?, ? , ? , ? , ?, ? , ?)' , (1001, "Belkadi hassna zineb" , 'zineb' , 'zineb' , 22 , 555657842 , 'hydra alger'))
#----------------------------------------
#CREATE PRODUCTS TABLE

#conn.execute('''CREATE TABLE IF NOT EXISTS Products (DESIGNATION TEXT PRIMARY KEY  NOT NULL, CAU FLOAT NOT NULL,QTT_VENDUE FLOAT NOT NULL,CSU FLOAT NOT NULL ,CCU FLOAT NOT NULL,TS FLOAT ,D FLOAT NOT NULL , FOURNISSEUR TEXT , PRIX_VENTE FLOAT , STOCK_DISPONIBLE INT) ''' )
#conn.execute('ALTER TABLE Products ADD COLUMN CLASS TEXT')

#for index, row in data.iterrows():
#	conn.execute('INSERT OR IGNORE INTO Products VALUES (?, ? , ? , ? , ?, ? , ?, ? , ?,?)' , (row["Articles"],row["Cau ( en euros)"],row["Quantité vendue"],row["Csu ( euros)"],row["Ccu ( euros)"],row["ts"],row["D ( en jours)"],row["Fournisseurs"],row["Prix de vente"],row["stock disponible"]))

#------------------------------------------
#CREATE ADMINS TABLE
#conn.execute('''CREATE TABLE IF NOT EXISTS Admins (ID INT PRIMARY KEY     NOT NULL, FULL_NAME TEXT NOT NULL,USERNAME TEXT NOT NULL,PASSWORD TEXT NOT NULL ,AGE INT NOT NULL,CONTACT_NUMBER INT ,ADDRESS TEXT NOT NULL) ''' )


#conn.execute('INSERT OR IGNORE INTO Admins VALUES (?, ? , ? , ? , ?, ? , ?)' , (1111, "Ammar khodja malik" , 'malik' , 'malik' , 21 , 555817998 , 'garidi kouba'))
#conn.execute('INSERT OR IGNORE INTO Admins VALUES (?, ? , ? , ? , ?, ? , ?)' , (1001, "Belkadi hassna zineb" , 'zineb' , 'zineb' , 22 , 555657842 , 'hydra alger'))

#-----------------------------------------
#CREATE HISTORIQUE CLIENT TABLE
#conn.execute('''CREATE TABLE IF NOT EXISTS Historique_client (ORDER_ID TEXT PRIMARY KEY NOT NULL,PURCHASE_DATE TEXT, PRODUCT_NAME TEXT NOT NULL ,QUANTITY INT NOT NULL,UNIT_PRICE FLOAT ,TOTAL_PRICE FLOAT , DELIVERY_CHARGE FLOAT ,CUSTOMER_NAME TEXT NOT NULL ) ''' )

#conn.execute('INSERT OR IGNORE INTO Historique_client VALUES (?, ? , ? , ? , ?, ? , ?,?)' , (unique_id , dt , 'PC HP 850' , 1 , 400+0.05*400 , 400+0.05*400, 50 , 'Ammar khodja malik'))
#conn.execute('INSERT OR IGNORE INTO Historique_client VALUES (?, ? , ? , ? , ?, ? , ?,?)' , (unique_id2 , dt , 'PC HP 850' , 1 , 400+0.05*400 , 400+0.05*400, 50 , 'Belkadi hassna zineb'))

#------------------------------------------
#CREATE CLASSE A TABLE

#conn.execute('''CREATE TABLE IF NOT EXISTS CLASS_A (PRODUCT_NAME TEXT PRIMARY KEY  NOT NULL, CAU FLOAT NOT NULL,CSU FLOAT NOT NULL ,CCU FLOAT NOT NULL,TS FLOAT ,CONSOMATION_MOYENNE_SEMAINE FLOAT, SS INT  ,D FLOAT NOT NULL, QEC INT , SEUIL INT ) ''' )

#for index, row in data2.iterrows():
#	conn.execute('INSERT OR IGNORE INTO CLASS_A VALUES (?, ? , ? , ? , ?, ? , ?, ? , ?,?)' , (row['Articles de classe A'],row["Cau"],row["Csu"],row["Ccu"],row["ts"],row["Conso moy par semaine"],row["SS"],row["Délai de livraison: D"],row["QEC"],row["SEUIL"]))


#------------------------------------------
#CREATE CLASSE B TABLE

#conn.execute('''CREATE TABLE IF NOT EXISTS CLASS_B (PRODUCT_NAME TEXT PRIMARY KEY  NOT NULL, CAU FLOAT NOT NULL,CSU FLOAT NOT NULL ,CCU FLOAT NOT NULL,TS FLOAT ,INTERVALLE FLOAT, NdR INT  ,D FLOAT NOT NULL ) ''' )

#for index, row in data3.iterrows():
#	conn.execute('INSERT OR IGNORE INTO CLASS_B VALUES (?, ? , ? , ? , ?, ? , ?, ?)' , (row['Articles de classe B'],row["Cau"],row["Csu"],row["Ccu"],row["ts"],row["intervalle"],row["NdR"],row["Délai de livraison: D"]))

#------------------------------------------
#CREATE CLASSE C TABLE

#conn.execute('''CREATE TABLE IF NOT EXISTS CLASS_C (PRODUCT_NAME TEXT PRIMARY KEY  NOT NULL, CAU FLOAT NOT NULL,CSU FLOAT NOT NULL ,CCU FLOAT NOT NULL,TS FLOAT ,QMAX INT, QMIN INT  ,D FLOAT NOT NULL ) ''' )

#for index, row in data4.iterrows():
#	conn.execute('INSERT OR IGNORE INTO CLASS_C VALUES (?, ? , ? , ? , ?, ? , ?, ?)' , (row['Articles de classe C'],row["Cau"],row["Csu"],row["Ccu"],row["ts"],row["Qmax"],row["Qmin "],row["Délai de livraison: D"]))

#===========================#Create tableau dynamique 
#conn.execute('''CREATE TABLE IF NOT EXISTS Tableau_dynamique (PRODUCT_NAME TEXT , DATE_CL TEXT , INPUT INT , OUTPUT INT , STOCK_AVAILABLE INT ) ''' )

#conn.execute('CREATE TABLE IF NOT EXISTS HISTORIQUE_FOURNISSEUR (ORDER_ID TEXT PRIMARY KEY NOT NULL,PURCHASE_DATE TEXT, PRODUCT_NAME TEXT NOT NULL ,QUANTITY INT NOT NULL,UNIT_PRICE FLOAT ,TOTAL_PRICE FLOAT , BILL_STATE TEXT NOT NULL )')



conn.commit()
conn.close()

