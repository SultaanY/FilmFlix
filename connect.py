#connect file will allow for sqlite module to be used across files 


import sqlite3 as sql # imported the sqlite3 module and assigned it an alias 'sql'
 

try:
    with sql.connect("PythonFlimFlix/filmflix.db") as db_con:
        #this provides a connection to the database
        db_cursor = db_con.cursor() # the cursor method is use to execute sql statements

except sql.OperationalError as oe: # raise a sql error
    #handle the exception/error raised
    print(f"Connection to the database failed because: {oe}")
