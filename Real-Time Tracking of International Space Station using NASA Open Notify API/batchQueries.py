import mysql.connector

# establish a connection to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Password123#@!",
  database="Bitcoin"
)

# create a cursor object to execute SQL queries
mycursor = mydb.cursor()

#batch query 1
print("Batch query  1 on poundBitcoin-table  : ")
mycursor.execute("select AVG(rate) from poundBitcoin")

# fetch all rows from the resultset
rows = mycursor.fetchall()

# iterate over the rows and print each row
for row in rows:
  print(row)
  

  
print("Batch query 2 on USD table : ")
mycursor.execute("select AVG(rate) from updateBitcoin")

# fetch all rows from the resultset
rows = mycursor.fetchall()

# iterate over the rows and print each row
for row in rows:
  print(row)
  
print("Batch query 3 on euro-table : ")
mycursor.execute("select AVG(rate) from euroBitcoin")

# fetch all rows from the resultset
rows = mycursor.fetchall()

# iterate over the rows and print each row
for row in rows:
  print(row)
  

  



# close the cursor and the database connection
mycursor.close()
mydb.close()

