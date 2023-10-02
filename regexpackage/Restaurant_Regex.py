#!/usr/bin/python3
import re
import json

def RestaurantRegex(data):
    matches = re.findall('(?:(([A-Z]\S+\s&\s)?(\S+\s\'n\')?([A-Z]\S+)?(\s[A-Z]\S+\s\S+)?(?=\s-\s)))', data)
    match_list = []
    for match in matches:
        if match[0] == "":
            continue
        else:
            match_list.append(match[0].lstrip())
    print(match_list)
    with open("Restaurant.json", "a", encoding="utf-8") as rp:
        json.dump(match_list, rp)
        print("Succesfully saved Restaurant in json format")

if __name__ == "__main__":
    import re
    import json
    import sys
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as fp:
            data = fp.read()
        matches = re.findall('(?:(([A-Z]\S+\s&\s)?(\S+\s\'n\')?([A-Z]\S+)?(\s[A-Z]\S+\s\S+)?(?=\s-\s)))', data)
        match_list = []
        for match in matches:
            if match[0] == "":
                continue
            else:
                match_list.append(match[0].lstrip())
        print(match_list)
        with open("Restaurant.json", "a", encoding="utf-8") as rp:
            json.dump(match_list, rp)
            print("Succesfully saved Restaurant in json format")
    except FileNotFoundError as err:
        print(err)
    except IndexError as err:
        print(err)
        print("Make sure you put the full file path as the command line argument after your shell script")
