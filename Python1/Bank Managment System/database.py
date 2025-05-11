
import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "8448",
        database = "bank"
)
mycursor = mydb.cursor()


table = " "
def createcustomer() :
        mycursor.execute(" CREATE TABLE customer  (username VARCHAR(50) , password VARCHAR(20), name VARCHAR(20) , age INTEGER ,  city VARCHAR(20) , acc_no INTEGER , Balance INTEGER,  status BOOLEAN DEFAULT TRUE)")
        
mydb.commit()

if __name__ == "__main__" :
                 createcustomer()

def exe(stt):
        mycursor.execute(stt)
        result = mycursor.fetchall()
        return result