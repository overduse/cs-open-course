#!/bin/sh
find . -type f --name "*.html" | xarg -d '\n' tar -cvzf html.zip
