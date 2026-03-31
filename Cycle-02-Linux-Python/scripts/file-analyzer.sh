#!/bin/bash

if [ -z "$1" ] || [ ! -d "$1" ]; then
    exit 1
fi

DIR="$1"

echo "Files and Sizes:"
ls -lh "$DIR" | grep ^- | awk '{print $5, $9}'

echo "-------------------------------"

echo -n "Total File Count: "
ls -lp "$DIR" | grep -v / | wc -l

echo -n "Total Directory Size: "
du -sh "$DIR" | cut -f1

echo -n "Largest File: "
ls -lS "$DIR" | grep ^- | head -n 1 | awk '{print $5, $9}'
