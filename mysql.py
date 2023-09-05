import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
user=os.getenv("user")
password=os.getenv("password")
host=os.getenv("host")
database=os.getenv("db")
port=os.getenv("port")
conn = psycopg2.connect(database = database, user = user, password = password, host = host, port = port)

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
print("Table created successfully")
cur.execute('''INSERT INTO COMPANY (id,name,age,address,salary) VALUES(1,'pooaraz',22,'29,guruvareddiyur,erode',70000)   ''')
print("record created")

cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()

cur.execute('''SELECT * FROM COMPANY''')
print(cur.fetchall())
rows=cur.fetchall()
i=0
for row in rows:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
conn.commit()
conn.close()