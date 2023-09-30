#!/usr/bin/python3
""" displays the body of the response and handel error"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode())
    except urllib.error.URLError as error:
        print(f"Error code: {error.code}")
