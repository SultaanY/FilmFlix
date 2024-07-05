from connect import *

def update_record():
    try:
        #filmID is the primary/unique key required to update a specific record
        id_field= input("Select the film ID you would like to edit: ")

        # selects single record
        db_cursor.execute("SELECT * FROM tblFilms WHERE filmID =?",(id_field,))

        film_record = db_cursor.fetchone() #fetches a single record
        print(film_record)

        if film_record == None: #checks if record exists
            print(f"Please select an existing film record") 
        else:
            field_name= input("Please enter the field you would like to be updated: ")
            #value you want to change and new input
            field_value= input(f"Enter the new value for the {field_name} field: ")
            db_cursor.execute("SELECT * FROM tblFilms WHERE filmID =? ",(id_field,))

            field_value = "'"+field_value+"'" #  = paul = 'paul' ensures that there ' either side

            db_cursor.execute(f"UPDATE tblFilms SET {field_name} = {field_value} WHERE filmID= {id_field}")

            db_con.commit()

    except sql.ProgrammingError as pe:
        # handle the exception/error raised
        print(f"Failed operation: {pe}")
   
    finally:
        print("Operation completed")
 
if __name__ == "__main__":
    update_record()
