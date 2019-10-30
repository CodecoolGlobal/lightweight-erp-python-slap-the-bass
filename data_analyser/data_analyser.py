"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoid using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm


def start_module():
    menu = True
    while menu:
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))


def get_the_last_buyer_name():
    """
    Returns the customer name of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    # your code
    return crm.get_name_by_id(sales.get_customer_id_by_sale_id(sales.get_item_id_sold_last()))

    #ui.print_tbl_c (tbl_c ,["Cmr ID","Cmr Name","Cmr Email","Bought item ID"])
#kész^
def get_the_last_buyer_id():
    """
    Returns the customer id of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """
    # your code
    return sales.get_customer_id_by_sale_id(sales.get_item_id_sold_last())
#kész^    

def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's name who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """
    # your code
    dicc=sales.get_all_sales_ids_for_customer_ids()
    lmao=[]
    for key, value in dicc.items():
        temp=[key,value]
        lmao.append(temp)
    sums=[]
    for i in range(len(lmao)):
        for j in range(len(lmao[i])):
            sums.append(sales.get_the_sum_of_prices(lmao[i][j]))

    highest=sums[0]
    place=0
    for i in range(len(sums)):
        if highest<sums[i]:
            highest=sums[i]
            place=i-1
    ID=lmao[place][0]
    andhisnameisJOHNCENA=crm.get_name_by_id(ID)
    reli=[andhisnameisJOHNCENA,highest]
    return tuple(reli)    
#kész^
def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's id who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """
    
    # your code
    dicc=sales.get_all_sales_ids_for_customer_ids()
    lmao=[]
    for key, value in dicc.items():
        temp=[key,value]
        lmao.append(temp)
    sums=[]
    for i in range(len(lmao)):
        for j in range(len(lmao[i])):
            sums.append(sales.get_the_sum_of_prices(lmao[i][j]))

    highest=sums[0]
    place=0
    for i in range(len(sums)):
        if highest<sums[i]:
            highest=sums[i]
            place=i-1
    ID=lmao[place][0]
    reli=[ID,highest]
    return tuple(reli)    
#kész^
def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 😎 , ('Missy Stoney', 3)]
    """
    
    # your code
    dicc=sales.get_all_sales_ids_for_customer_ids()
    lmao=[]
    for key, value in dicc.items():
        temp=[key,value]
        lmao.append(temp)
   
    #lmao=[['jH34Jk#&', ['kH34Ju#&', 'jH34Ju#&', 'tH34Ju#&', 
    # 'eH34Ju#&', 'kH14Ju#&', 'kH35Ju#&', 'kH38Ju#&', 'kH94Ju#&', 
    # 'tH34Jl#&', 'eH34Jy#&', 'bH34Jx#&']], 
    # ['kH14Jt#&', ['bH34Ju#&', 'vH34Ju#&', 'kH34Ji#&', 'vH34Jz#&',
    #  'kH14Jt#&', 'kH35Jr#&', 'kH38Je#&', 'kH94Jw#&']],
    # ['kH14Jh#&', ['jH34Jk#&']]]
    sums=[]
    for i in range(len(lmao)):
        for j in range(len(lmao[i])):
            n=0
            for k in range(len(lmao[i][j])):
                    
                n+=1
            sums.append(n)
    #sums=[8, 11, 8, 8, 8, 1]
    nums=[]
    n=0
    while n!=len(sums):
        nums.append(sums[n+1])
        n+=2
    #nums=[11,8,1]
    ids=[lmao[0][0],lmao[1][0],lmao[2][0]]
    #ids=['jH34Jk#&', 'kH14Jt#&', 'kH14Jh#&'] 
    names=[]
    for i in range(len(ids)):
        names.append(crm.get_name_by_id(ids[i]))
    #names=['Missy Stoney', 'Sadye Hession', 'Kanesha Moshier']
    lsd={}
    for i in range(num):
        nameplusnum=[nums[i],names[i]]
        lsd.update({nameplusnum[1]:nameplusnum[0]})
    reli=[]
    for key, value in lsd.items():
        temp=(key,value)
        reli.append(temp)
    return (reli)
def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 😎, (bH34Jq#&, 3)]
    """

    # your code
    dicc=sales.get_all_sales_ids_for_customer_ids()
    lmao=[]
    for key, value in dicc.items():
        temp=[key,value]
        lmao.append(temp)
   
    #lmao=[['jH34Jk#&', ['kH34Ju#&', 'jH34Ju#&', 'tH34Ju#&', 
    # 'eH34Ju#&', 'kH14Ju#&', 'kH35Ju#&', 'kH38Ju#&', 'kH94Ju#&', 
    # 'tH34Jl#&', 'eH34Jy#&', 'bH34Jx#&']], 
    # ['kH14Jt#&', ['bH34Ju#&', 'vH34Ju#&', 'kH34Ji#&', 'vH34Jz#&',
    #  'kH14Jt#&', 'kH35Jr#&', 'kH38Je#&', 'kH94Jw#&']],
    # ['kH14Jh#&', ['jH34Jk#&']]]
    sums=[]
    for i in range(len(lmao)):
        for j in range(len(lmao[i])):
            n=0
            for k in range(len(lmao[i][j])):
                    
                n+=1
            sums.append(n)
    #sums=[8, 11, 8, 8, 8, 1]
    nums=[]
    n=0
    while n!=len(sums):
        nums.append(sums[n+1])
        n+=2
    #nums=[11,8,1]
    ids=[lmao[0][0],lmao[1][0],lmao[2][0]]
    #ids=['jH34Jk#&', 'kH14Jt#&', 'kH14Jh#&'] 
    names=[]
    for i in range(len(ids)):
        names.append(crm.get_name_by_id(ids[i]))
    #names=['Missy Stoney', 'Sadye Hession', 'Kanesha Moshier']
    lsd={}
    for i in range(num):
        nameplusnum=[nums[i],ids[i]]
        lsd.update({nameplusnum[1]:nameplusnum[0]})
    reli=[]
    for key, value in lsd.items():
        temp=(key,value)
        reli.append(temp)
    return (reli)
def choose(menu):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        ui.print_result(get_the_last_buyer_name(),"The last buyer's name is:")
        
    elif option == "2":
        ui.print_result(get_the_last_buyer_id(), "The last buyer's ID is:")
    elif option == "3":
        res_tuple = get_the_buyer_name_spent_most_and_the_money_spent()
        ui.print_result(res_tuple[0], "The name of the customer spent most is:")
        ui.print_result(res_tuple[1], "The money spent (in dollars) is:")
    elif option == "4":
        ui.print_result(get_the_most_frequent_buyers_names(num=1)[0][0], "The most frequent buyers name is:")
    elif option == "5":
        ui.print_result(get_the_most_frequent_buyers_ids(num=1)[0][0], "The most frequent buyers name is:")
    elif option == "0":
        return False

    else:
        raise KeyError("There is no such option.")
    return True

def handle_menu():
    options = ["Last buyers name", "Last buyers id", "Buyers name spent most and the money_spent",
               "Frequent buyers names", "Frequent buyers IDs"]# Do not modify this file

    ui.print_menu("Data Analyser", options, "Back to main menu")