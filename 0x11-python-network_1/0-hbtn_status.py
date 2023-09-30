#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        response_content = response.read()
        print("Body response:")
        print(f"\t- type: {type(response_content)}")
        print(f"\t- content: {response_content}")
        print(f"\t- utf8 content: {response_content.decode()}")
