#!/usr/bin/python3
"""Shows the X-Request-Id variable's value located within the response header.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    commits = get(url).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
