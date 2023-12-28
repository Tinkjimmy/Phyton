cursor.execute("ALTER TABLE stock RENAME COLUMN qty TO quantity")

cursor.execute("ALTER TABLE stock ADD COLUMN manifacturer_name TEXT")


#dropping(deleting) columns

ALTER TABLE stock DROP COLUMN quantity

#PRINT A TABLE
cursor.execute("describe <name of the table>")
result= cursor.fetchall()
for row in result:
    print(row[0])

# dropping a table
    
    cursor.execute("DROP TABLE <NAME OF TABLE>")

#Adding Entries to Your Table
INSERT INTO <table name> (<columns to enter data into>) VALUES (<corresponding values for each column>)

cursor.execute('''INSERT INTO stock(item_name,item_id,price, quantity, manifacturer_name) VALUES('Water',1,'Acquafina',10, 20,'Acquafina' ''')
#another way to insert values

sql = 'INSERT INTO stock (item_id, item_name, price, quantity, manifacturer_name) VALUES (%s, %s, %s, %s, %s)'
val = (2, 'Coca-Cola', 2.5, 30, 'The Coca-Cola Company')
cursor.execute(sql, val)

#Automatically Assigning IDs to Rows

CREATE TABLE movie (
    id      INT PRIMARY KEY,
    name        VARCHAR(20),
    year        INT,
    imdb_rating INT,
    language    VARCHAR(20)
);

cursor.execute("ALTER TABLE movie MODIFY COLUMN id INT PRIMARY KEY AUTO_INCREMENT;")
cursor.execute("ALTER TABLE stock MODIFY COLUMN item_id INT PRIMARY KEY AUTO_INCREMENT;")

#displaying content of table
SELECT <columns to display> FROM <table name>
cursor.execute("SELECT item_id,item_name, manufacturer_name,price,quantity FROM stock")

result= cursor.fetchall
for row in result:
        print("ID: ", row[0])
        print("Name: ", row[1])
        print("Manufacturer: ", row[4])
        print("Price: ", row[2])
        print("Quantities Available:", row[3])
        print()
#dispalying content using asterix
cursor.execute("SELECT * FROM stock")
results = cursor.fetchall()
      
    for row in result:
        print("ID: ", row[0])
        print("Name: ", row[1])
        print("Manufacturer: ", row[4])
        print("Price: ", row[2])
        print("Quantities Available:", row[3])
        print()
        

#updating values in the table
        
UPDATE <table name> SET <column name> = <new value> WHERE <condition describing the row> 
            
            
#Deleting Rows
DELETE FROM <table name> WHERE <condition describing the row>
#EX:
cursor.execute("DELETE FROM stock WHERE item_id = 5")


#Committing Your Changes
conn.commit()
conn.close()




