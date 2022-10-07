_Although we installed Anaconda, and downgraded to python 3.8, we are actually installing jupyter locally with poetry so that the kernel recognises the packages._

# Installing
```bash
$ poetry init
$ poetry add --group dev jupyter
$ poetry add $(requirements.txt)
```

## Running
```bash
$ cd ~/Documents/Trading/pysystemtrade
$ poetry shell
$ poetry run jupyter notebook
```

## Running the Dashboard
```bash
$ cd ~/Documents/Trading/pysystemtrade
$ poetry shell
$ poetry run python -m dashboard.app
```

## Getting upstream changes from Rob 
```bash
$ git remote upstream https://github.com/robcarver17/pysystemtrade.git # do once
$ git fetch upstream   # get but don't merge rob's changes
$ git diff upstream/master # compare with rob
$ git merge upstream/master # merge in rob's changes
```

## Git commands
```bash
$ git status # what's changed in my repo
$ git add [filename] # stage a change
$ git add -p # interactively stage some chunks in all changed files. Y to accept changes
$ git commit -m "[commit message]" # commiting a change set with a message
$ git push # push change sets to remote origin
$ git log # show recent commits

```
