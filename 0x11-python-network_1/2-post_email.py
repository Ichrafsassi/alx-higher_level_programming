#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
