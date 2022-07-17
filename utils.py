"""

    Utility functions for the main application

"""

import json


def read_details_json(*args):
    """

        Read json configuration files in order to generate a dictionary

    :param args: A variable number of .json filenames
    :return: A dictionary containing the data within all the files
    """
    all_data = {}

    for current_arg in args:
        with open(current_arg, encoding='UTF-8') as current_file:
            current_data = json.load(current_file)
            all_data.update(current_data)

    return all_data
