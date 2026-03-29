#!/usr/bin/python3
"""Query local search API and print JSON result status."""

import sys
import requests


def main():
    """Send POST data to the search API and print parsed result status."""
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]

    response = requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": letter}
    )

    try:
        data = response.json()
        if isinstance(data, dict) and data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
