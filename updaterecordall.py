from connect import *

def update_recordall():
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
            film_title = input("Enter the film name: ")
            film_year = input("Enter the release year: ")
            film_rating = input("Enter the film age rating: ")
            film_duration = input("Enter the film duration in minutes: ")
            film_genre = input("Enter the film genre: ")
            db_cursor.execute("SELECT * FROM tblFilms WHERE filmID =? ",(id_field,))

            film_title = "'"+film_title+"'"
            film_year = "'"+film_year+"'"
            film_rating = "'"+film_rating+"'"
            film_duration = "'"+film_duration+"'"
            film_genre = "'"+film_genre+"'"


             #  = paul = 'paul' ensures that there ' either side

            db_cursor.execute(f"UPDATE tblFilms SET Title=?, YearReleased=?, Rating=?, Duration=?, Genre=? WHERE filmID=?",(film_title, film_year, film_rating, film_duration, film_genre, id_field))

            db_con.commit()

    except sql.ProgrammingError as pe:
        # handle the exception/error raised
        print(f"Failed operation: {pe}")
   
    finally:
        print("Operation completed")
 
if __name__ == "__main__":
    update_recordall()
