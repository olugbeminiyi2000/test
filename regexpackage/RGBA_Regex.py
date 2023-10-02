#!/usr/bin/python3
import re
import json

def RGBARegex(data):
    matches = re.findall('rgba?\(\d+,\s\d+,\s\d+,?\s?\d?\.?\d?\)', data);
    print(matches)
    with open("RGBA.json", "a", encoding="utf-8") as rp:
        json.dump(matches, rp)
        print("Succesfully saved RGBA colors in json format")

if __name__ == "__main__":
    import re
    import json
    import sys
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as fp:
            data = fp.read()
        matches = re.findall('rgba?\(\d+,\s\d+,\s\d+,?\s?\d?\.?\d?\)', data);
        print(matches)
        with open("RGBA.json", "a", encoding="utf-8") as rp:
            json.dump(matches, rp)
            print("Succesfully saved RGBA colors in json format")
    except FileNotFoundError as err:
        print(err)
    except IndexError as err:
        print(err)
        print("Make sure you put the full file path as the command line argument after your shell script")
