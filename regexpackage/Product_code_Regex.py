#!/usr/bin/python3
import re
import json

def ProductCodeRegex(data):
    matches = re.findall(r'\b[A-Za-z]{3}\d{3}\b', data);
    print(matches)
    with open("product-code.json", "a", encoding="utf-8") as pp:
        json.dump(matches, pp)
        print("Succesfully saved Product codes in json format")

if __name__ == "__main__":
    import re
    import json
    import sys
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as fp:
            data = fp.read()
        matches = re.findall(r'\b[A-Za-z]{3}\d{3}\b', data);
        print(matches)
        with open("product-code.json", "a", encoding="utf-8") as pp:
            json.dump(matches, pp)
            print("Succesfully saved Product codes in json format")
    except FileNotFoundError as err:
        print(err)
    except IndexError as err:
        print(err)
        print("Make sure you put the full file path as the command line argument after your shell script")
