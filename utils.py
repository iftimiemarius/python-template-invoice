import json


def read_details_json(*args):
    all_data = {}

    for current_arg in args:
        current_file = open(current_arg)
        current_data = json.load(current_file)
        all_data.update(current_data)
        current_file.close()

    return all_data
