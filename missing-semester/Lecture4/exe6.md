# EXERCISE 6

## QUESTION

> Find an online data set like [this one](https://stats.wikimedia.org/EN/TablesWikipediaZZ.htm#wikipedians). Fetch it using `curl` and extract out just two columns of numerical data. If you’re fetching HTML data, [pup](https://github.com/EricChiang/pup) might be helpful. For JSON data, try [jq](https://jqlang.github.io/jq/). Find the min and max of one column in a single command, and the difference of the sum of each column in another.

## ANSWER

```bash
curl 'https://stats.wikimedia.org/EN/TablesWikipediaZZ.htm#wikipedians' \
    | sed -n "/table1/,/<\/table>/p" \
    | grep "<tr" | sed "1,12d" | head -n -3 \
    | sed -E 's/(<[^>]*>)+/ /g' \
    | sed 's/&nbsp;//g' > data

awk '{print $1,$4,$5}' data | sort --key=2n | head -n 1

awk '{print $1,$4,$5}' data | sort --key=2n | tail -n 1

awk '{print $1,$4,$5}' data | awk '{print $2-$3}' | awk '{s+=$1} END {print s}'

```
