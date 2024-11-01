# EXERCISE 5

## QUESTION


> Look for boot messages that are not shared between your past three reboots (see `journalctl`’s `-b` flag). Break this task down into multiple steps.
> First, find a way to get just the logs from the past three boots. There may be an applicable flag on the tool you use to extract the boot logs, or you can use `sed '0,/STRING/d'` to remove all lines previous to one that matches `STRING`.
> Next, remove any parts of the line that always varies (like the timestamp).
> Then, de-duplicate the input lines and keep a count of each one (`uniq` is your friend).
> And finally, eliminate any line whose count is 3 (since it was shared among all the boots).

## SOLUTION


```bash
#!/bin/bash
for i in {0..3}; do
    journalctl -b-$i
done

./getlog.sh > last3start.txt

# A1 is the last 2 letters of my PC name of WSL2
cat last3start.txt | sed -E "s/.*A1 (.*)/\1/" | sort | uniq -c | sort | awk '$1!=3  { print }'
```

