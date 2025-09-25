#!/bin/bash
# Script to create a file, add a line, and move it to logs

FILENAME="tempfile.txt"

touch "$FILENAME"
echo "Hello world" > "$FILENAME"
mv "$FILENAME" "../logs/"
