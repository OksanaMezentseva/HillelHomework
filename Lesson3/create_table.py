import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()


sql = '''
CREATE TABLE Phones (
    phoneID INTEGER PRIMARY KEY,
    contactName varchar(255),
    phoneValue varchar(255)
);
'''
cur.execute(sql)
con.commit()
con.close()