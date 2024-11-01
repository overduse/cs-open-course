#!/bin/sh
man ls

# includes all files, including hidden files
ls -la

# Sizes are listed in human readable format (e.g. 454M instead of 454279954)
ls -lh

# Files are ordered by recency
ls -lc

# Output is colorized
ls -l --color

# ALL in one, same as the sample output given.
ls -lahc --color
