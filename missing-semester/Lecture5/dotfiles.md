# Dotfiles

## exe1

> Create a folder for your dotfiles and set up version control.

```bash
mkdir ~/dotfiles
```

## exe2

> Add a configuration for at least one program, e.g. your shell, with some customization (to start off, it can be something as simple as customizing your shell prompt by setting `$PS1`).

```zsh
git init ~/dotfiles

ls -a ~/dotfiles
#outputs:
# . .. .bashrc .zshrc .profile .tmux.conf and so on

```
## exe3

> Set up a method to install your dotfiles quickly (and without manual effort) on a new machine. This can be as simple as a shell script that calls ln -s for each file, or you could use a [specialized utility](https://dotfiles.github.io/utilities/).

```bash
 #!/bin/bash
 files=$(ls -a $1 | grep -E '.[^.]+' |grep -v .git)
 # 去掉 ls -a 返回结果中的 ". .. .git"
 for file in `echo $files`; do
     ln -s $1/$file ~/$file # 创建软链接
 done

```

