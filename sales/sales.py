""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""
# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
from common import add, remove, show_table, update, sorting


def start_module():
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

# special functions:

def get_lowest_price_item_id(table):
    pass
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code
    list_of_min = []
    list_of_prices = []
    for list in table:
        list_of_prices.append(list[2])
    min_price = min(list_of_prices)
    for list in table:
        if list[2] == min_price:
            list_of_min.append(list[0])
    sorting((list_of_min))
    for i in range(len(list_of_min)):
        if i == len(list_of_min) - 1:
            result = list_of_min[i]
    return result


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    # your code
    yf = year_from * 365
    mf = month_from * 30
    df = day_from
    yt = year_to * 365
    mt = month_to * 30
    dt = day_to
    reli = []
    for i in range(len(table)):
        yta = int(table[i][5]) * 365
        mta = int(table[i][3]) * 30
        dta = int(table[i][4])
        if yta + mta + dta > yf + mf + df and yta + mta + dta < yt + mt + dt:
            reli.append(table[i])
    result_list = []
    for list in reli:
        new_list = []
        for i in range(len(list)):
            if i <= 1:
                new_list.append(list[i])
            else:
                new_list.append(int(list[i]))
        result_list.append(new_list)
    return result_list

def choose(menu):
    file_name = "sales/sales.csv"
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = ["Press ENTER to continue...", "Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
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
        ui.print_result(get_lowest_price_item_id(data_manager.get_table_from_file(file_name)),"")
    elif option == "6":
        ui.print_result(get_items_sold_between(data_manager.get_table_from_file("sales/sales.csv"), 10, 1, 2015, 12, 12, 2016)[1],"")
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True

def handle_menu():
    options = ["Show table", "Add", "Remove", "Update", "sf1", "sf2"]

    ui.print_menu("Sales manager", options, "Back to main menu")