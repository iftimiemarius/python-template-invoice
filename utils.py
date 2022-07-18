"""

    Utility functions for the main application

"""

import json
from openpyxl import load_workbook


def read_json(filename):
    with open(filename, encoding='UTF-8') as current_file:
        current_data = json.load(current_file)

    return current_data


def read_xlsx(filename):
    current_data = {}

    workbook = load_workbook(filename=filename)

    for current_sheet in workbook.worksheets:
        sheet_iterator = iter(current_sheet.rows)

        next(sheet_iterator)  # Skip the first entry (header)

        for current_row in sheet_iterator:
            key = current_row[0].value
            value = current_row[1].value
            current_data[key] = value

    return current_data


def read_details(*args):
    """

        Read json configuration files in order to generate a dictionary

    :param args: A variable number of .json filenames
    :return: A dictionary containing the data within all the files
    """
    all_data = {}

    for current_arg in args:
        data = {}
        if current_arg.endswith('.json'):
            data = read_json(current_arg)
        elif current_arg.endswith('.xlsx'):
            data = read_xlsx(current_arg)

        all_data.update(data)
    return all_data
