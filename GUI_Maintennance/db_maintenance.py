import sqlite3 
# Create connection for connect database
conn = sqlite3.connect('Maintenance.sqlite3')

# Creat cursor for sql commmand
c = conn.cursor()
# Create table
c.execute(""" CREATE TABLE IF NOT EXISTS mt_workorder (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    tsid TEXT, 
                    name TEXT,
                    department TEXT,
                    machine TEXT,
                    problem TEXT,
                    number TEXT,
                    tel TEXT) """) # SQL COMMMAND > REQUIRE UPPER LETTER CHARECTER (CREATE TABLE IF NOT EXISTS) #ts is timestamp # name ...... is field

def insert_mtworkorder(tsid,name,department,machine,problem,number,tel): # Add field 
    # Create
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)' # IN () follow as number field
        c.execute(command,(None,tsid,name,department,machine,problem,number,tel))
    conn.commit() #save database
   # print('SAVE')

#insert_mtworkorder('TS1002','NUT','PD','COM','Not working','PT1999','0891123123')
def view_mmtworkorder():
    with conn:
        command = 'SELECT * FROM mt_workorder'
        c.execute(command)
        result = c.fetchall()
       # print(result)
        return result

def update_mtworkorder(tsid,field,newvalue):
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?) WHERE tsid=(?)'.format(field) # .format(field) is reserved for {......} 
        c.execute(command,(newvalue,tsid)) 
    conn.commit()
   # print('update')

#update_mtworkorder('TS1002','problem','virus')

def delete_mtworkorder(tsid):
    with conn:
         command = 'DELETE FROM mt_workorder WHERE tsid=(?)'
         c.execute(command,([tsid]))
    conn.commit()