#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""Helper library for drawinf cli tables."""


# Export only the draw table method
__all__ = ["draw_table"]


def get_table_params(items):
    """A helper function for drawine a table.

    :param items: a list of lists, 2-D array
    :return: a tuple with the cleaned data and the lengts of the columns
    """
    data = []
    for index, item in enumerate(items):
        print item
        if index == 0:
            data.append(["Id"] + item)
        else:
            data.append([str(index)] + item)

    column_widths = []
    for index in range(len(data[0])):
        col_width = max(map(lambda x: len(x[index]), data))
        column_widths.append(col_width)

    return (data, column_widths)


def draw_row(items, column_widths):
    """Draw a single table row.

    :param items: a list with the data
    :param widths: the widths of the columns
    :return row: a formated string representing a table row
    """
    # Start the borders and the row
    border = "+-"
    data = "|"

    for length in range(len(column_widths)):
        border += "-" * column_widths[length]
        data += " " + items[length].ljust(column_widths[length]) + " |"

    # Finish the border and the row
    border += "-+\n"
    data += "\n"

    # Combine the strings into a single string
    row = ""
    # The first element of the items list is the index
    # We treat index 0 as the header and add the border
    # to the top as well
    if items[0] == 0:
        row += border
    row += data
    row += border
    return row


def draw_table(items=[], headers=[], sort=False):
    """Creates a table that looks better in the console.
    It assumes that the first item in items is the header

    :param items: a 2-D array with the data
    :param header: a list with the headers
    :param sort: a boolean, if True the table is sorted alphabeticaly
    :return: a formated string representing the table
    """
    # TODO: add different styles
    # Assert that the none of the items has more elements than the header
    header = headers if headers else items[0]
    have_more_elements = [x for x in items if len(x) > len(header)]
    assert not have_more_elements, "The headers don't match the data."
    # Prepare the data
    for_processing = []
    for_processing.append(header)
    for_processing.append(items)
    data, column_widths = get_table_params(for_processing)
    table = ""
    for item in data:
        table += draw_row(item, column_widths)
    return table
