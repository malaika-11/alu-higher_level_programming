#!/usr/bin/python3
"""Fetch and display intranet status response details with requests."""

import requests


def main():
    """Send a GET request and print response body details."""
    response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
