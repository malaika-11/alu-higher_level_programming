#!/bin/bash
# Display all HTTP methods the server will accept using OPTIONS
curl -s -I -X OPTIONS "$1" | grep -i "Allow:" | cut -d" " -f2-
