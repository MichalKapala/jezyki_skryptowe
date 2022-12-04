
import os
import json

file = open(r"./menu.json", "r")
menu_data = json.load(file)

YAML_PATH = r"../data/menu.yml"

file2 = open(YAML_PATH, "w")

# Writes the headers(?), remember to change the lookup name
file2.write("version: \"3.1\"\nnlu:\n  - lookup: dish  \n    examples: |\n")

# Adds indent and dash to each line
for dish in menu_data["dish"]:
    file2.write("      - " + str(dish["name"]) + "\n")

# Closes the files
file.close()
file2.close()
