#!/bin/bash
# Made with Bing AI
# Does not currently work
# Should remove leading numbers from all filenames in a given directory

for file in [0-9]*; do
    if [[ -f "$file" ]]; then
        mv -- "$file" "${$file##*[!0-9 ]*}"
    fi
done
