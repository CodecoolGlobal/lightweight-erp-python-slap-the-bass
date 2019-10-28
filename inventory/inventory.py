""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""
# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
from common import add, remove, update, show_table


def start_module():
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

# special functions:

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code
    reli = []
    for i in range(len(table)):
        n = int(table[i][3])
        if n <= year:
            n += int(table[i][4])
            if n >= year:
                reli.append(table[i])
    result_list = []
    for list in reli:
        new_list = []
        for i in range(len(list)):
            if i <= 2:
                new_list.append(list[i])
            else:
                new_list.append(int(list[i]))
        result_list.append(new_list)
    return result_list


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    l1 = []  # producer
    l2 = []  # durab
    nof = []
    for i in range(len(table)):
        l1.append(table[i][2])
        l2.append(table[i][4])
    dicc = {}
    for i in range(len(l1)):
        if l1[i] not in dicc:
            dicc.update({l1[i]: int(l2[i])})
        else:
            dicc[l1[i]] += int(l2[i])
    uniqP = []
    uniqN = [0, 0, 0]

    for key, value in dicc.items():
        temp = [key, value]
        uniqP.append(temp)

    uniqPL = [uniqP[0][0], uniqP[1][0], uniqP[2][0]]

    for i in range(len(uniqPL)):
        for j in range(len(l1)):
            if uniqPL[i] == l1[j]:
                uniqN[i] += 1
    list_of_keys = []
    list_of_values = []
    list_of_modified_values = []
    for key in dicc:
        list_of_values.append(dicc[key])
        list_of_keys.append(key)
    for i in range(len(uniqN)):
        update = list_of_values[i] / uniqN[i]
        list_of_modified_values.append(update)
    for i in range(len(list_of_keys)):
        dicc.update({list_of_keys[i]: list_of_modified_values[i]})

    return dicc

def choose(menu):
    file_name = "inventory/inventory.csv"
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = ["Press ENTER to continue...", "Name: ", "Manifacturer: ", "Purchase year: ", "Durability: "]
    table = get_available_items(data_manager.get_table_from_file(file_name),2006)
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
                       ui.get_inputs(main_list, "Please provide the following information to complete the update:"))
        data_manager.write_table_to_file(file_name, table)
    elif option == "5":
        list_of_items = [table[i][1] for i in range(len(table))]
        ui.print_result(list_of_items, "")
    elif option == "6":
        ui.print_result(get_average_durability_by_manufacturers(data_manager.get_table_from_file(file_name)),"")
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True

def handle_menu():
    options = ["Show table", "Add", "Remove", "Update", "Get available item", "Get average dur. by  manuf."]

    ui.print_menu("Inventory manager", options, "Back to main menu")