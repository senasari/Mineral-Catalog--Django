# this module converts the given minerals.json file into a json file format that can be loaded to the database
import json


with open('../fixtures/minerals.json', 'r+') as mineral_file:
    data_list = json.load(mineral_file)
    data_dict = {}
    data_dict_list = []
    new_mineral_dict = {}  # with '_' in keys to conform it to the database

    with open('../fixtures/fixtures.json', 'w') as sff:
        # writes the data taken from the minerals.json file to the file called fixtures.json
        for count, mineral_dict in enumerate(data_list):
            for key, value in mineral_dict.items():
                new_key = "_".join(key.split(" "))
                new_mineral_dict[new_key] = value
            data_dict["model"] = "minerals_app.Mineral"
            data_dict["pk"] = count+1
            data_dict["fields"] = new_mineral_dict.copy()
            data_dict_list.append(data_dict.copy())
        json.dump(data_dict_list, sff, indent=4)
