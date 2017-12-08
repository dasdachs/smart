#! /usr/bin/env python2
# -*- coding: utf-8 -*- 
"""A cli app for writing a restaurant menu.
   
   The app uses no external library, as it is ment as
   an exercise. For a production app it would use at least 
   the `csv` module and probably `os`.

   Note that the original exercise uses a dict to store the items. 
   A real program would use a list or tuples.
"""
def get_table_params(items, header=("first row", "second row")):
    """A helper function for drawine a table. 
    
    :param items: a dictionary
    :param header: a tuple cotaining the names of the columns
    :return: a tuple with the cleaned data and the lengts of the columns
    """
    raw_data = [header] + items.items()
    # Stringify all the keys and values
    data = list(map(lambda x: (str(x[0]), str(x[1])), raw_data))
    one_len = sorted(data, key=lambda x: len(x[0]),reverse=True)[0]
    two_len = sorted(data, key=lambda x: len(x[1]), reverse=True)[0]

    col_one_len = len(one_len[0])
    col_two_len = len(two_len[1])
    return (data, col_one_len, col_two_len)

def sort_table(data):
    """Returns the table data in a sorted order.

    :param data: a list of tuples with strings
    :return: a list of tuples with strings
    """
    header = data[0]
    rows = data[1:]
    sorted_rows = sorted(rows, key=lambda x: x[0], reverse=True)
    return [header] + sorted_rows

def draw_row(item, one_len, two_len, header=False):
    """Draw a single table row.

    :param item: a tuple with two strings
    :param one_len: the length of the first column
    :param two_len: the length of the second column
    :param header: a boolena indicating if the row is a header
    :return row: a formated string representing a table row
    """
    border = "+-" + "-" * one_len + "-+-" + "-" * two_len + "-+\n"
    row = ""
    if header:
        row = border
    row += "| " + item[0].ljust(one_len)
    row += " | " + item[1].ljust(two_len) + " |\n"
    row += border
    return row

def draw_table(items, header=("first row", "second row"), sort=False):
    """Creates a table that looks better in the console.

    :param items: a dictionary
    :param header: a tuple cotaining the names of the columns
    :param sort: a boolean, if True the table is sorted alphabeticaly
    :return: a formated string representing the table
    """
    data, col_one_len, col_two_len = get_table_params(items, header=header)
    if sort:
        data = sort_table(data)
    # Draw table
    table = ""
    for item in data:
        if item == header:
            is_header = True
        table += draw_row(item, col_one_len, col_two_len, header=is_header)
    return table

def save_table(data, header, filename):
    """Writes the content of the table to a file.

    :param data: a dict containung the items
    :param header: a tuple with the name of the columns
    :param filename: a string representing the filename
    :return: None
    """
    extension = filename.split(".")[-1]
    if extension != "csv":
        to_write = draw_table(data, header=header, sort=True)
    else:
        data = get_table_params(data, header=header)[0]
        sorted_data = sort_table(data)
        to_write = "".join([x[0] + ";" + x[1] + "\n" for x in sorted_data])
    with open(filename, "w") as f:
        f.write(to_write)


def get_menu(header=("Jed", "Cena")):
    print "Hello! Let's create a menu."
    menu = {}
    while True:
        dish = raw_input("Please enter a dish: ")
        price = raw_input("Please enter the price: ")
        menu[dish] = price
        print draw_table(menu, header=header, sort=True)
        print "===="
        status = raw_input("Finished? (yes/no): ")

        if status.lower() == "yes":
            table = draw_table(menu, header=header, sort=True)
            print table
            save = raw_input("Save to file (yes/no): ")
            if save.lower() == "yes":
                filename = raw_input("Name the file (default 'menu.csv'): ")
                if not filename:
                    filename = "menu.csv"
                save_table(menu, header, filename)
            break

if __name__ == "__main__":
    get_menu()
    print "Fin"
