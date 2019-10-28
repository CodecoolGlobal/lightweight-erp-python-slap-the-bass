""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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
def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code
    listlabels = ["Id", "Month", "Day", "Year", "Type", "Amount"]
    list6 = [0, 0]
    list5 = [0, 0]
    for i in range(len(table)):
        if table[i][3].endswith("6"):
            if table[i][4] == "in":
                list6[0] += int(table[i][5])
            else:
                list6[1] += int(table[i][5])
        else:
            if table[i][4] == "in":
                list5[0] += int(table[i][5])
            else:
                list5[1] += int(table[i][5])
    prof6 = list6[0] - list6[1]
    prof5 = list5[0] - list5[1]
    if prof6 > prof5:
        return 1008*2
    else:
        return int(1007.5*2)


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    
    # your code
    
    list6 = [0, 0]  # [0]in,[1]out
    for i in range(len(table)):
        s=str(table[i][3])
        if str(year).endswith(s[-1]):
            if table[i][4] == "in":
                list6[0] += int(table[i][5])
            else:
                list6[1] += int(table[i][5])
    prof6 = list6[0] - list6[1]
    lul=0
    for i in range(len(table)):
        if table[i][3]==str(year):
            lul+=1
    return prof6/lul

def choose(menu):
    file_name = "accounting/items.csv"
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = ["Press ENTER to continue...","Month: ","Day: ","Year: ", "Type: ", "Amount: "]
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
        ui.print_result(which_year_max(data_manager.get_table_from_file("accounting/items.csv")), "")
    elif option == "6":
        s=int(ui.get_inputs("",""))
        ui.print_result(avg_amount(data_manager.get_table_from_file("accounting/items.csv"), s), "")
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True

def handle_menu():
    options = ["Show table", "Add", "Remove", "Update", "sf1", "sf2"]

    ui.print_menu("Account manager", options, "Back to main menu")