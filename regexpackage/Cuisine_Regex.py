#!/usr/bin/python3
import re
import json

def CuisineRegex(data):
    matches = re.findall(r'(?P<cuisine>(?<=\s-\s)\w+)', data);
    print(matches)
    with open("Cuisine.json", "a", encoding="utf-8") as cp:
        json.dump(matches, cp)
        print("Succesfully saved Cuisine in json format")

if __name__ == "__main__":
    import re
    import json
    import sys
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as fp:
            data = fp.read()
        matches = re.findall(r'(?P<cuisine>(?<=\s-\s)\w+)', data);
        print(matches)
        with open("Cuisine.json", "a", encoding="utf-8") as cp:
            json.dump(matches, cp)
            print("Succesfully saved Cuisine in json format")
    except FileNotFoundError as err:
        print(err)
    except IndexError as err:
        print(err)
        print("Make sure you put the full file path as the command line argument after your shell script")
