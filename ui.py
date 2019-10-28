def get_max_len(table):
    max = 0
    for list in table:
        for item in list:
            for item2 in list:
                if len(item) >= len(item2):
                    if max < len(item):
                        max = len(item)
    return max

""" User Interface (UI) module """


def print_table(table, title_list):
    list_of_column_len = []
    list_of_title_leng = []
    list_of_width = []
    temp = []

    for j in range(len(title_list)):
        list_of_title_leng.append(len(title_list[j]))

    for i in range(len(table[0])):
        for j in range(len(table)):
            temp.append(float(len(table[j][i])))
        list_of_column_len.append(max(temp))
        temp = []

    for i in range(len(list_of_title_leng)):
        if list_of_column_len[i] >= list_of_title_leng[i]:
            list_of_width.append(list_of_column_len[i])
        else:
            list_of_width.append(list_of_title_leng[i])
    i = 0
    j = 0
    betw_line = ""
    betw_line += "╠"
    top_line = ""
    bottom_line = ""
    top_line += "╔"
    bottom_line += "╚"
    for leng in list_of_width:
        top_line += "═" * (int(leng) + 2) + "╦"
    for leng in list_of_width:
        betw_line += "═" * (int(leng) + 2) + "╬"
    for leng in list_of_width:
        bottom_line += "═" * (int(leng) + 2) + "╩"
    print(top_line[:-1] + "╗")
    print("║", end="")
    n = 0
    for item in title_list:
        if n <= len(title_list) - 2:
            print(" ", end="")
            print('{0:^{1}}'.format(item, int(list_of_width[n])) + " ║", end="")
        else:
            print(" ", end="")
            print('{0:^{1}}'.format(item, int(list_of_width[n])) + " ║")
        n += 1
    print(betw_line[:-1] + "╣")
    for list in table:
        print("║", end="")
        for item in list:
            print(" ", end="")
            print('{0:^{1}}'.format(item, int(list_of_width[i])) + " ║", end="")
            i += 1
        j += 1
        print()
        if j < len(table):
            print(betw_line[:-1] + "╣")
        i = 0
    print(bottom_line[:-1] + "╝")
    print()





def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(label, result)

def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(title)
    for option in range(len(list_options)):
        print("   (" + str(option + 1) + ")", list_options[option] )
    print("   (0) " + exit_message)

def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    # your code
    print(title)
    for input_num in range(len(list_labels)):
        inputs.append(input(list_labels[input_num]))
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print("ERROR:", message)
