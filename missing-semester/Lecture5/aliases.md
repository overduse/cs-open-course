# Aliases

## exe1

> Create an alias `dc` that resolves to `cd` for when you type it wrongly.

add this line to '.zshrc' or '.bashrc'
```bash
alias dc="cd"
```

## exe2

> Run `history | awk '{$1="";print substr($0,2)}' | sort | uniq -c | sort -n | tail -n 10` to get your top 10 most used commands and consider writing shorter aliases for them. Note: this works for Bash; if you're using ZSH, use 'history 1' instead of just 'history'.

ZSH version
```zsh
history 1 | awk '{$1="";print substr($0,2)}' | sort | uniq -c | sort -n | tail -n 10

# output:
#  96 git status
# 145 rm -rf build
# 161 cmake -B build
# 170 make
# 185 cd
# 196 cd build
# 264 nvim
# 276 cd ..
# 516 ls
#1645 ll
```
