""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
from common import add, remove, update, show_table, sorting


def start_module():
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

# special functions:


def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code
    list_of_genres = []
    for line in table:
        if line[2] not in list_of_genres:
            list_of_genres.append(line[2])
        else:
            continue
    dic_of_genres = {}
    for i in range(len(list_of_genres)):
        k = 0
        for line in table:
            if line[2] == list_of_genres[i]:
                k += 1
        dic_of_genres.update({list_of_genres[i]: k})
    return dic_of_genres


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
    list_of_games = []
    for line in table:
        if line[2].lower() == manufacturer.lower():
            list_of_games.append(int(line[4]))
    i = 0
    sum = 0
    while i < len(list_of_games):
        sum += list_of_games[i]
        i += 1
    avg = sum / len(list_of_games)
    return avg

def choose(menu):
    file_name = "store/games.csv"
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = ["Press ENTER to continue...", "Title: ", "Manifacturer: ", "Price: ", "In_stock: "]
    if option == "1":
        show_table(main_list, data_manager.get_table_from_file(file_name))
    elif option == "2":
        table = add(data_manager.get_table_from_file(file_name),
                    ui.get_inputs(main_list, "Please provide the following information:"))
        data_manager.write_table_to_file(file_name, table)
    elif option == "3":
        table = remove(data_manager.get_table_from_file(file_name),
                       ui.get_inputs(["ID: "], "Please provide the following information:"))
        data_manager.write_table_to_file(file_name, table)
    elif option == "4":
        table = update(data_manager.get_table_from_file(file_name),
                       ui.get_inputs(["ID"], "Please provide the ID to identify the elemnt:"),
                       ui.get_inputs(main_list, "Please provide the following information to complete the update"))
        data_manager.write_table_to_file(file_name, table)
    elif option == "5":
        ui.print_result(get_counts_by_manufacturers(data_manager.get_table_from_file(file_name)),"")
    elif option == "6":
        manufacturer = ui.get_inputs(["Manifacturer: "],
                                     "To calculate the avg. amount please specify which manifacturer you want to select.")[0]
        ui.print_result(get_average_by_manufacturer(data_manager.get_table_from_file(file_name), manufacturer), "")
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True

def handle_menu():
    options = ["Show table", "Add", "Remove", "Update", "sf1", "sf2"]

    ui.print_menu("Sales manager", options, "Back to main menu")