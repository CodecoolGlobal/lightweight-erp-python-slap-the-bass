""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code

    lnu = []
    for i in range(len(table)):
        lnu.append(str(2019 - int(table[i][-1])) + table[i][1])
    nu = []
    for i in range(len(lnu)):
        nu.append(lnu[i][0] + lnu[i][1])
    sorting(nu)
    nu = nu[::-1]
    hm = 0
    for i in range(len(nu)):
        if nu[0] == nu[i]:
            hm += 1
    reli = []
    ma = nu[0]
    for i in range(len(lnu)):
        s = lnu[i][0] + lnu[i][1]
        l = ""
        if s == ma:
            for j in range(len(lnu[i])):
                if j > 1:
                    l += lnu[i][j]
        if len(l) > 0:
            reli.append(l)
    return reli


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
    lnu = []
    for i in range(len(table)):
        lnu.append(str(2019 - int(table[i][-1])) + table[i][1])
    nu = []
    nusum = 0
    for i in range(len(lnu)):
        nu.append(lnu[i][0] + lnu[i][1])
        nusum += int(nu[i])
    navg = nusum / len(lnu)
    avg=int(navg*-1// 1)
    avg=avg*-1
    reli = []
    nums=[]
    name=[]
    numsort=[]
    for i in range(len(nu)):
        nums.append(abs(int(nu[i])-46))
        numsort.append(abs(int(nu[i])-46))
        s=""
        for j in range(2,len(lnu[i])):
            s+=lnu[i][j]
        name.append(s)

    result_list=[]
    sorting(numsort)
    for i in range(len(nums)):
        if nums[i]==numsort[0]:
            result_list.append(name[i])

    return result_list

    # your code
def choose(menu):
    file_name = "hr/persons.csv"
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    main_list = ["Press ENTER to continue...", "Name: ", "Birth year: "]
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
        ui.print_result(get_oldest_person(data_manager.get_table_from_file(file_name)),"")
    elif option == "6":
        ui.print_result(get_persons_closest_to_average(data_manager.get_table_from_file(file_name)), "")
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True

def handle_menu():
    options = ["Show table", "Add", "Remove", "Update", "Get oldest person", "Get person closest to avg."]

    ui.print_menu("Human Recourses (HR)", options, "Back to main menu")