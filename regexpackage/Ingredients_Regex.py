#!/usr/bin/python3
import json
import re

def IngredientRegex(data):
    matches = re.findall('(?<=Ingredients: ).*?\.', data);
    print(matches)
    with open("Ingredients.json", "a", encoding="utf-8") as ip:
        json.dump(matches, ip)
        print("Succesfully saved Ingredients in json format")

if __name__ == "__main__":
    import re
    import json
    import sys
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as fp:
            data = fp.read()
        matches = re.findall('(?<=Ingredients: ).*?\.', data);
        print(matches)
        with open("Ingredients.json", "a", encoding="utf-8") as ip:
            json.dump(matches, ip)
            print("Succesfully saved Ingredients in json format")
    except FileNotFoundError as err:
        print(err)
    except IndexError as err:
        print(err)
        print("Make sure you put the full file path as the command line argument after your shell script")
