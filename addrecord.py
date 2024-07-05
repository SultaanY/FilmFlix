#import connect file 
from connect import *

def insert_record(): #code to import a record into the db
    try:
        #title, yearRelease, rating, duration, genre
        film_title = input("Enter the film name: ")
        film_year = input("Enter the release year: ")
        film_rating = input("Enter the film age rating: ")
        film_duration = input("Enter the film duration in minutes: ")
        film_genre = input("Enter the film genre: ")

        # execute sql insert statement
        db_cursor.execute("insert into tblFilms VALUES(NULL,?,?,?,?,?)", (film_title,film_year,film_rating,film_duration,film_genre))

        db_con.commit() # Permanently insert/write the record to the database table
        print(f"{film_title} inserted in the films table. ")

    except sql.ProgrammingError as pe:
        print(f"Failed due to {pe}")
    
    finally:
        print(f"Operation completed")

if __name__ == "__main__":
    insert_record()
    
