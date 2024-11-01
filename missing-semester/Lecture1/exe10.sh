#!/bin/sh
touch ~/last-modified.txt

# ls -l /tmp/missing/semester | cut -d " " -f 6-8 | tee  ~/last-modified.txt
ls -l /tmp/missing/semester | cut -d " " -f 6-8 > ~/last-modified.txt

cat ~/last-modified.txt
