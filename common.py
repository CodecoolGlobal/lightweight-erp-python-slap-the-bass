""" Common module
implement commonly used functions here
"""
from ui import print_table, get_inputs, print_error_message, print_result
import random
from data_manager import get_table_from_file, write_table_to_file


def generate_random(table):

    generated = ''

    up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
          "W", "X", "Y", "Z"]
    lo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z"]
    nu = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sp = ["+", "!", "%", "/", "=", "(", ")", "|", "<", ">", "#", "&", "@", "{", "}", "*"]
    w = [1, 2, 3, 4, 5, 6, 7, 8]
    while len(generated) != 8:
        generated = ''
        while len(w) != 0:
            random.shuffle(w)
            n = w[0]
            if n == 1 or n == 2:
                l=up[random.randint(0, len(up)-1)]
                generated += l

            if n == 3 or n == 4:
                l=lo[random.randint(0, len(lo)-1)]
                generated += l

            if n == 5 or n == 6:
                l=str(nu[random.randint(0, len(nu)-1)])
                generated += l

            if n == 7 or n == 8:
                l=sp[random.randint(0, len(sp)-1)]
                generated += l


            w.remove(w[0])
        if generated not in table:
            return generated
        else:
            continue
    return generated

def add(table, res_table):
    list = []
    list.append(generate_random(table))
    for i in range(1, len(res_table)):
        list.append(res_table[i])
    table.append(list)
    return table


def update(table, id_, new_list):
    for list in range(len(table)):
        for item in table[list]:
            if item in id_:
                for i in range(1,len(table[list])):
                    table[list][i] = new_list[i]
    return table


def remove(table, id_):
    for list in table:
        for item in list:
            if item in id_:
                table.remove(list)
    return table


def show_table(title_list, table):
    print_table(table, title_list)

def sorting(list):
    sorted = False
    while sorted == False:
        sorted = True
        for obj in range(len(list) - 1):
            if list[obj] > list[obj + 1]:
                temp = list[obj]
                list[obj] = list[obj + 1]
                list[obj + 1] = temp
                sorted = False
    return list
