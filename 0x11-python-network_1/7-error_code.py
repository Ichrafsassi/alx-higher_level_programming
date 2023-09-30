#!/usr/bin/python3
""" displays the body of the response and handel error"""

if __name__ == "__main__":
    import requests
    import sys
    req = requests.get(sys.argv[1])
    if (req.ok):
        print(req.text)
    else:
        print(f"Error code: {req.status_code}")
