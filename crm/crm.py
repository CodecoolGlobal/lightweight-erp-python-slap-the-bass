""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""
# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
from common import show_table, add, remove, update, sorting


def start_module():
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))

# special functions:
def get_longest_name_id(table):  # table

    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # your code
    longest = 0
    name_list = []
    for i in range(len(table)):
        if len(table[i][1]) > longest:
            longest = len(table[i][1])
    reli = []
    for i in range(len(table)):
        if len(table[i][1]) == longest:
            reli.append(table[i][0])
            name_list.append(table[i][1])
    sorting(name_list)
    name_list = name_list[::-1]
    longest_name = name_list[0]
    for i in range(len(table)):
        if table[i][1] == longest_name:
            return table[i][0]



# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code
    l = []
    for i in range(len(table)):
        if table[i][-1] == "1":
            l.append(str(table[i][2]) + ";" + str(table[i][1]))
    return l

    # your code
def choose(menu):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(["Press ENTER to continue...", "Name", "E-mail", "Subscribed"] ,data_manager.get_table_from_file("crm/customers.csv"))
    elif option == "2":
        table = add(data_manager.get_table_from_file("crm/customers.csv"),
               ui.get_inputs(["Press ENTER to continue...", "Name: ", "E-mail: ", "Subscribed: "], "Please provide the following information:"))
        data_manager.write_table_to_file("crm/customers.csv", table)
    elif option == "3":
        table = remove(data_manager.get_table_from_file("crm/customers.csv"),
                  ui.get_inputs(["ID: "], "Please provide the following information:"))
        data_manager.write_table_to_file("crm/customers.csv", table)
    elif option == "4":
        table = update(data_manager.get_table_from_file("crm/customers.csv"),
                  ui.get_inputs(["ID"], "Please provide the ID to identify the elemnt:"),
                  ui.get_inputs(["ID", "Name", "E-mail", "Subscribed"], "Please provide the following information to complete the update:"))
        data_manager.write_table_to_file("crm/customers.csv", table)
    elif option == "5":
        ui.print_result(get_longest_name_id(data_manager.get_table_from_file("crm/customers.csv")), "")
    elif option == "6":
        ui.print_result(get_subscribed_emails(data_manager.get_table_from_file("crm/customers.csv")), "")
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True

def handle_menu():
    options = ["Show table","Add","Remove","Update","Get longest name by ID", "Get Subscriber E-mails"]

    ui.print_menu("Customer Relationship Management (CRM)", options, "Back to main menu")



