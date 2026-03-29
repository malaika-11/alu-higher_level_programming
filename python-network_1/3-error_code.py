#!/usr/bin/python3
"""Fetch URL and print HTTP status code when urllib raises HTTPError."""

import sys
import urllib.error
import urllib.request


def main():
    """Send a GET request and print body or formatted HTTP error code."""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))


if __name__ == "__main__":
    main()
