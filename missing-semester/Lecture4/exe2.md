# INSTALL FILE

The file `/usr/share/dict/words` do not exsit in WSL2-Ubuntu environment.
You should install 'wamerican' package firstly.

```bash
sudo apt update
sudo apt install wamerican
```

And now, you can check if the file exsits.

```bash
ls /usr/share/dict/words
```


# EXERCISE

> Find the number of words (in `/usr/share/dict/words`) that contain at least three `a`s and don’t have a `'s` ending.
> What are the three most common last two letters of those words? `sed`’s `y` command, or the `tr` program, may help you with case insensitivity.
> How many of those two-letter combinations are there?
> And for a challenge: which combinations do not occur?


# SOLUTION

> Find the number of words (in `/usr/share/dict/words`) that contain at least three `a`s and don’t have a `'s` ending.

```bash
cat /usr/share/dict/words | tr "[:upper:]" "[:lower:]" | grep -E "^([^a]*a){3}.*$" | grep -v "'s$" | wc -l

```


> What are the three most common last two letters of those words?

```bash
cat /usr/share/dict/words | tr "[:upper:]" "[:lower:]" | grep -E "^([^a]*a){3}.*$" | grep -v "'s$" | sed -E "s/.*([a-z]{2})$/\1/" | sort | uniq -c | sort | tail -n3

# 54 as
# 63 ns
# 101 an
```


> How many of those two-letter combinations are there?

```bash
cat /usr/share/dict/words | tr "[:upper:]" "[:lower:]" | grep -E "^([^a]*a){3}.*$" | grep -v "'s$" | sed -E "s/.*([a-z]{2})$/\1/" | sort | uniq | wc -l

# 112
```


> And for a challenge: which combinations do not occur?

```bash
#!/bin/bash
for i in {a..z};do
    for j in {a..z};do
        echo "$i$j"
    done
done

# filename: ./all.sh
./all.sh > all.txt

cat /usr/share/dict/words | tr "[:upper:]" "[:lower:]" | grep -E "^([^a]*a){3}.*$" | grep -v "'s$" | sed -E "s/.*([a-z]{2})$/\1/" | sort | uniq > occurance.txt

diff --unchanged-group-format='' <(cat occurance.txt) <(cat all.txt) | wc -l
```
