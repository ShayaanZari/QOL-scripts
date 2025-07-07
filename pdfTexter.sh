#!/bin/bash

TARGET="./textversions"

find . -type f -name '*.pdf' | while read -r file; do
    filename=$(basename "$file")
    out="$TARGET/${filename%.pdf}.txt"
    echo "working on $filename- searching for $out"
    if [ ! -e "$out" ]; then
	    pdftotext "$file" "$out"
	    echo "just pdftotexted $filename"
        else
	    echo "$filename already exists in $TARGET"
    fi
done
