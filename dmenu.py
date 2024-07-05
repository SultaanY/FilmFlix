
import readrecords, addrecord, updaterecord, updaterecordall, deleterecord, report

def get_file(p_file_path):
    try:
        with open(p_file_path) as file_location:
            read_file = file_location.read()
        return read_file
    
    except FileExistsError as nf:
        print(nf)

folder_path=get_file("PythonFlimFlix/dbMenu.txt")
print(folder_path)


def films_menu():
    option = 0
    optionList = ["1","2","3","4","5","6","7"]

    menu_choices = get_file("PythonFlimFlix/dbMenu.txt")

    #while loop to repeatedly display menu

    while option not in optionList:
        print(menu_choices)

        option = input("Enter an option from the menu choices above: ")

        if option not in optionList:
            print(f"{option} is not a valid choice!")
    return option


main_program = True

while main_program:
    main_menu = films_menu()

    #match case
    match main_menu:
        case "1":
            readrecords.read_records()
        case "2":
            addrecord.insert_record()
        case "3":
            updaterecord.update_record()
        case "4":
            updaterecordall.update_recordall()
        case "5":
            deleterecord.delete_record()
        case "6":
            report.search_report()
        case _:
            main_program = False
input("Presse enter key to exit the program")
        




