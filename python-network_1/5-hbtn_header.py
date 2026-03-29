#!/usr/bin/python3
"""Fetch a URL and display the X-Request-Id response header using requests."""

import sys
import requests


def main():
    """Send a GET request and print the X-Request-Id header value."""
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
