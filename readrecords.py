from connect import *
def read_records():

    try:

        db_cursor.execute("SELECT * FROM tblFilms")
        all_records = db_cursor.fetchall() # all selected records from the table

        if all_records: #if the records exists
            for aRecord in all_records: #transverse through each record in all_records
                print(aRecord) 
        else:
            print("No record found in the films table")
    except sql.ProgrammingError as pe:
        print(f"Failed operation: {pe}")
   
    finally:
        print(f"All records")
if __name__ == "__main__":
    read_records()