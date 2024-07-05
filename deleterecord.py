from connect import *

def delete_record():
    try:
        #select primary key with is unique to each film
        id_field= input("Enter the film ID: ")
    
        #use the id_field above to execute sql command

        db_cursor.execute("SELECT * FROM tblFilms WHERE filmID =? ",(id_field,))

        film_record = db_cursor.fetchone() # fetches the selected single record
        print(film_record)
        
        if film_record == None:
            print(f"The film with id {id_field} does not exists! ")
        else:
            
            db_cursor.execute("DELETE FROM tblFilms WHERE filmID=?", (id_field,))
            db_con.commit()
            print(f"The film with ID {id_field} has been deleted")
        
    except sql.ProgrammingError as pe:
        # handle the exception/error raised
        print(f"Failed operation: {pe}")
   
    finally:
        print("Operation completed")
 
if __name__ == "__main__":
    delete_record()    
        