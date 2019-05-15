#!/usr/bin/python3
"""
Russell Zachary Feeser
rzfeeser@gmail.com || rzfeeser@alta3.com

Training & consultant available for: [Python, Ansible, Network Automation, 5G, Kubernetes, SIP, SDN,
                                     IP Multimedia Subsystem (IMS), Avaya, Wireshark]

Course catalog: "https://alta3.com"

Training inquiries: rzfeesr@alta3.com

This project queries the https://poweroutage.us database and returns those counties within the United States
experiencing outages set above the THRESHHOLD.

This script is not intended for commercial use and is intended only for educational purposes.

https://poweroutage.us provides a RESTFUL API for commercial users.

Commercial users should navigate to https://poweroutage.us/products and provide support to this project. It is the
**ONLY** source of near-real-time aggregated electric grid data available within the US. Please support the project.

Installation considerations:
    Before running this script, you must install the requests library. This can be accomplished with the command:
        python3 -m pip install requests

    For more information about the requests library, check out:
        - https://2.python-requests.org/en/master/
        - https://pypi.org/project/requests/


If you do use this script, I only ask that you leave my original proof of authorship. Oh, and maybe hire me to be your
next trainer or consultant :)

Thanks,
  -Zach
"""
import requests

THRESHHOLD = 50

# God bless America, and all the ships at sea
STATES = {"al": "Alabama", "ak": "Alaska", "az":"Arizona", "ar":"Arkansas", "ca":"California", "co":"Colorado",
          "ct":"Connecticut", "de":"Delaware", "ga":"Georgia", "fl":"Florida", "hi": "Hawaii", "id":"Idaho",
          "il":"Illinois", "in":"Indiana", "ia":"Iowa", "ks":"Kansas", "ky":"Kentucky", "la":"Louisiana", "me":"Maine",
          "md":"Maryland", "ma":"Massachusetts", "mi":"Michigan", "mn":"Minnesota", "ms":"Mississippi", "mo":"Missouri",
          "mt":"Montana", "ne":"Nebraska", "nv":"Nevada", "nh": "New Hampshire", "nj": "New Jersey",
          "nm": "New Mexico", "ny": "New York", "nc": "North Carolina", "nd": "North Dakota", "oh": "ohio",
          "ok": "Oklahoma", "or": "Oregon", "pa": "Pennsylvania", "ri": "Rhode Island", "sc":"South Carolina",
          "sd": "South Dakota", "tn": "Tennessee", "tx": "Texas", "ut": "Utah", "vt": "Vermont", "va": "Virginia",
          "wa": "Washington", "wv": "West Virginia", "wi": "Wisconsin", "wy": "Wyoming"}

def electricsheep(batch):  # batch = list
    """query on poweroutage.us/api/web/counties"""
    for state in batch:  # loop across the list passed
        print('\nREPORTING FOR ' + state)
        res = requests.get(r'https://poweroutage.us/api/web/counties?key=18561563181588&countryid=us&statename='+state)
        jres = res.json()  # decode the response
        for county in jres['WebCountyRecord']:  # loop across all counties in that state
            if county["OutageCount"] > THRESHHOLD:   # display those results above the THRESHHOLD
                print(county["CountyName"], county["OutageCount"])  # display the country and number of outages

def main():
    """runtime code"""
    batch = input("Input a state abbreviation or type 'all': ").lower()  # collect input as lower from user
    if batch.lower() == 'all':
        batch = STATES.values()  # create an iterable (list-ish) of all the values
    else:
        batch = [STATES[batch]]  # create a list of the single state
    electricsheep(batch)  # real sheep were not used in the testing of electricsheep!
    input("Press Enter to exit")

if __name__ == "__main__":
    main()
