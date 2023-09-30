#!/usr/bin/python3
"""display the id variable found in the header of the response."""

if __name__ == "__main__":
    import requests
    import sys
    headers = {'Authorization': f'Bearer {sys.argv[2]}',
               'X-GitHub-Api-Version': '2022-11-28',
               'Accept': 'application/vnd.github.v3+json'}
    url = 'https://api.github.com/user'
    req = requests.get(url, headers=headers)
    print(req.json().get('id'))
