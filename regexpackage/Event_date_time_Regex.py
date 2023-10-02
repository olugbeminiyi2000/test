#!/usr/bin/python3
import json
import re

def EventDateTimeRegex(data):
        matches = re.findall(r'\b[A-Z][a-z]{2}\s\d{2},\s\d{4}\s-\s\d{2}:\d{2}\s(?:AM|PM)\b', data);
        print(matches)
        with open("Event-date-time.json", "a", encoding="utf-8") as ep:
            json.dump(matches, ep)
            print("Succesfully saved Events date and time in json format")

if __name__ == "__main__":
    import re
    import json
    import sys
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as fp:
            data = fp.read()
        matches = re.findall(r'\b[A-Z][a-z]{2}\s\d{2},\s\d{4}\s-\s\d{2}:\d{2}\s(?:AM|PM)\b', data);
        print(matches)
        with open("Event-date-time.json", "a", encoding="utf-8") as ep:
            json.dump(matches, ep)
            print("Succesfully saved Events date and time in json format")
    except FileNotFoundError as err:
        print(err)
    except IndexError as err:
        print(err)
        print("Make sure you put the full file path as the command line argument after your shell script")
