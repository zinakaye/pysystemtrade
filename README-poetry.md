_Although we installed Anaconda, and downgraded to python 3.8, we are actually installing jupyter locally with poetry so that the kernel recognises the packages._

# Installing
```
$ poetry init
$ poetry add --group dev jupyter
$ poetry add $(requirements.txt)
```

## Running
```
$ cd ~/Documents/Trading/pysystemtrade
$ poetry shell
$ poetry run jupyter notebook
```

## Running the Dashboard
```
$ cd ~/Documents/Trading/pysystemtrade
$ poetry shell
$ poetry run python -m dashboard.app
```

## Getting upstream changes from Rob 
```

$ git remote upstream https://github.com/robcarver17/pysystemtrade.git
$ git fetch upstream   
$ git diff upstream/master 
$ git merge upstream/master
```

