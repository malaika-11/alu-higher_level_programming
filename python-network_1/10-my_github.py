#!/usr/bin/python3
"""Use GitHub API basic authentication to display the authenticated user id."""

import sys
import requests


def main():
    """Send authenticated request to GitHub API and print user id."""
    response = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2])
    )
    print(response.json().get("id"))


if __name__ == "__main__":
    main()
