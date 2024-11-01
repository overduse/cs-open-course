# Version Control

## exe1

> If you don’t have any past experience with Git, either try reading the first couple chapters of [Pro Git](https://git-scm.com/book/en/v2) or go through a tutorial like [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN). As you’re working through it, relate Git commands to the data model.


## exe2

> Clone the [repository for the class website](https://github.com/missing-semester/missing-semester).
> 1.Explore the version history by visualizing it as a graph.
> 2.Who was the last person to modify README.md? (Hint: use git log with an argument).
> 3.What was the commit message associated with the last modification to the `collections:` line of `_config.yml`? (Hint: use `git blame` and `git show`).


```bash
#!/bin/sh

# Clone the repository for the class website
git clone https://github.com/missing-semester/missing-semester.git

cd missing-semester
# Explore the version history by visualizing it as a graph.
git log --graph

# last person to modify README.md
git log --p README.md
# OUTPUT: commit 9ef9db72 author Anish Athalye

# commit message associated with the last modification
git blame _config.yml | grep collections
# OUTPUT: a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 18) collections:
git show a88b4eac
# OUTPUTS: Redo lectures as a collections

```


## exe3

> One common mistake when learning Git is to commit large files that should not be managed by Git or adding sensitive information. Try adding a file to a repository, making some commits and then deleting that file from history (you may want to look at [this](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)).

```bash
#!/bin/sh

# add sensitive information into git repository
echo "MyPassword" > my_password
git add .
git commit -m "add password123 to file"
git log HEAD

# using git filter-branch to clear commit history
 git filter-branch --force --index-filter\
 'git rm --cached --ignore-unmatch ./my_password' \
 --prune-empty --tag-name-filter cat -- --all

```


## exe4

> Clone some repository from GitHub, and modify one of its existing files. What happens when you do `git stash`? What do you see when running `git log --all --oneline`? Run `git stash pop` to undo what you did with `git stash`. In what scenario might this be useful?

```bash
#!/bin/sh

git stash

git log --all --oneline

git stash pop

```


## exe5

> Like many command line tools, Git provides a configuration file (or dotfile) called `~/.gitconfig`. Create an alias in `~/.gitconfig` so that when you run `git graph`, you get the output of `git log --all --graph --decorate --oneline`. You can do this by directly [editing](https://git-scm.com/docs/git-config#Documentation/git-config.txt-alias) the `~/.gitconfig` file, or you can use the git config command to add the alias. Information about git aliases can be found [here](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases).

```bash
git config --global alias.graph "log --all --graph --decorate --oneline"

```


## exe6

> You can define global ignore patterns in `~/.gitignore_global` after running `git config --global core.excludesfile` `~/.gitignore_global`. Do this, and set up your global gitignore file to ignore OS-specific or editor-specific temporary files, like .DS_Store.

```bash
git config --global core.excludesfile ~/.gitignore .DS_Store

```


## exe7

> Fork the [repository for the class website](https://github.com/missing-semester/missing-semester), find a typo or some other improvement you can make, and submit a pull request on GitHub (you may want to look at [this](https://github.com/firstcontributions/first-contributions)). Please only submit PRs that are useful (don’t spam us, please!). If you can’t find an improvement to make, you can skip this exercise.

```bash
git clone https://github.com/your_id/missing-semester.git

# modify the fork repository and pull request

```
