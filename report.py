import logging
import time
from connect import *

error_log_format= '[%(filename)s:%(lineno)d in function %(funcName)s located at %(pathname)s] %(message)s'
date_format='%Y-%m-%d %H:%M%S'
logging.basicConfig(filename=r"PythonFlimFlix/CRUD_App.log",format=error_log_format, datefmt=date_format, level=logging.DEBUG)

def search_report():
    try:
        field = input("Search Options: FilmID or Title or YearReleased or Rating or Duration or Genre: ")

        if field == "FilmID":
            id_field = input("Enter FilmID: ")

            db_cursor.execute("SELECT * FROM tblFilms WHERE FilmID = ?", (id_field,))
            a_record = db_cursor.fetchone()

            if a_record == None:
                print(f"A record with the FilmID {id_field} does not exist in the films table!")
                logging.warning(f"On{time.asctime()} No FilmID {id_field} found in the film table!")
            else:
                print(a_record)
                logging.info(f"Found the record with FilmID {id_field} in film table")

        elif field == "Title" or field == "YearReleased" or field == "Rating" or field == "Duration" or field == "Genre":
            search_str = input("Enter search string/criteria: ")
            db_cursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{search_str}%' ")

            search_results = db_cursor.fetchall()
            # print(search_results)
            # print(type(search_results))
            # print(search_results == None)

            if search_results == []:
                print(f"No record(s) with the {field} matched the '{search_str}'! ")
                logging.warning(f"On {time.asctime()} No {field} matched the '{search_str}'! ")

            else:
                for record in search_results:
                    print(record)
                    logging.info(f"On{time.asctime()} returned records relating to {search_str}'! ")
        else:
            print(f"Invalid search performed {field} \nUse FilmID or Title or YearReleased or Rating or Duration or Genre")
            logging.warning(f"Invalid search {field} field name")
    except sql.ProgrammingError as pe:
        print(f"Failed operation: {pe}")

    finally:
        print("Operation completed")

if __name__ == "__main__":
    search_report()

