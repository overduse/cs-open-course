# EXERCISE 4

## QUESTION

> Find your average, median, and max system boot time over the last ten boots.
> Use journalctl on Linux and log show on macOS, and look for log timestamps near the beginning and end of each boot.

```bash
#!/bin/bash
for i in {0..9}; do
    journalctl -b-$i | grep "Startup finished in"
done

./getlog > starttime.txt

# attain the longest time
cat starttime.txt | grep "systemd\[1\]" | sed -E "s/.* in (.*)ms\.$/\1/"| sort | tail -n1

# attain the shortest time
cat starttime.txt | grep "systemd\[1\]" | sed -E "s/.* in (.*)ms\.$/\1/"| sort -r | tail -n1

# attain avg time
cat starttime.txt | grep "systemd\[1\]" | sed -E "s/.* in (.*)ms\.$/\1/"| paste -sd+ | bc -l | awk '{print $1/10 ms}'

# attain the median
cat starttime.txt | grep "systemd\[1\]" | sed -E "s/.* in (.*)ms\.$/\1/"| paste -sd+ | bc -l | awk '{print $1/10 ms}'

```
