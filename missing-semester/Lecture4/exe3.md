# EXERCISE 3

## QUESTION

> To do in-place substitution it is quite tempting to do something like `sed s/REGEX/SUBSTITUTION/ input.txt > input.txt`. However this is a bad idea, why? Is this particular to `sed`? Use `man sed` to find out how to accomplish this.


## ANSWER

`sed s/REGEX/SUBSTITUTION/ input.txt > input.txt`, the later `input.txt` file will be clear firstly.
