#!/usr/bin/python3
"""Fetch URL and print HTTP error code when status is >= 400."""

import sys
import requests


def main():
    """Send a GET request and print body or a formatted HTTP error code."""
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    main()
