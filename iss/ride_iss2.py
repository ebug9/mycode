#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()

    # show that at this point, our data is str
    # we want to convert this to list / dict
    #print(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))

    #print(helmetson["people"])
    namelist = ["Eddie Kopra", "James Peake", "Yuri Kopra", "Buzz Aldrin"]
    inspacecount = 0
    for person in helmetson["people"]:
        if person["name"] in namelist:
            print(f"{person['name']} on the {person['craft']}")
            inspacecount += 1
    print(f"People in space: {inspacecount}")

if __name__ == "__main__":
    main()

