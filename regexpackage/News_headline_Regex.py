#!/usr/bin/python3
import re
import json

def NewsHeadlineRegex(data):
    matches = re.findall('^[A-Z].*:.*\w$', data, flags=re.MULTILINE);
    print(matches)
    with open("News-headline.json", "a", encoding="utf-8") as np:
        json.dump(matches, np)
        print("Succesfully saved News headline in json format")

if __name__ == "__main__":
    import re
    import json
    import sys
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as fp:
            data = fp.read()
        matches = re.findall('^[A-Z].*:.*\w$', data, flags=re.MULTILINE);
        print(matches)
        with open("News-headline.json", "a", encoding="utf-8") as np:
            json.dump(matches, np)
            print("Succesfully saved News headline in json format")
    except FileNotFoundError as err:
        print(err)
    except IndexError as err:
        print(err)
        print("Make sure you put the full file path as the command line argument after your shell script")
