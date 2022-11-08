_Although we installed Anaconda, and downgraded to python 3.8, we are actually installing jupyter locally with poetry so that the kernel recognises the packages._

## Installing
```bash
$ poetry init
$ poetry add --group dev jupyter
$ poetry add $(requirements.txt)
```

### Configuring the environment

1. Edit `~/.zprofile`
```
MONGO_DATA="${HOME}/Documents/Trading/data/mongodb/"
PYSYS_CODE="${HOME}/Documents/Trading/pysystemtrade"
SCRIPT_PATH="${HOME}/Documents/Trading/pysystemtrade/sysproduction/linux/scripts"
ECHO_PATH="${HOME}/Documents/Trading/echos"
MONGO_BACKUP_PATH="${HOME}/Documents/Trading/mongo_backup"
```
1. Make the required directories
```
$ mkdir -p ../data/mongodb
$ mkdir ../echos
$ mkdir ../mongo_backup
```
1. Add `SCRIPT_PATH` to `PATH`
1. Symlink `.zprofile` to `.profile`
```bash
$ ln -s ~/.zprofile ~/.profile
```

### Installing mongo

1. Install Docker desktop
1. `$ docker-compose up`

### Install mongo shell for testing
```bash
$ brew tap mongodb/brew
$ brew install mongosh
```

### Connect to the docker container (testing)
```bash
$ docker exec -it pysystemtrade-mongodb-1 /bin/bash
```

### Connecting with the mongo shell (testing)
```bash
$ mongosh # Test that you can connect to the mongod running in Docker.
```

### Installing IB API gateway
1. Download from [here](https://interactivebrokers.github.io/#)
1. Unzip manually (as MacOS will fail)
```bash
$ unzip -d ./ ~/Downloads/[...filename]
```

## Running
```bash
$ cd ~/Documents/Trading/pysystemtrade
$ poetry shell
$ poetry run jupyter notebook
$ docker-compose up
```

### Load historic data
```bash
$ poetry shell
$ python sysinit/futures/repocsv_spotfx_prices.py
$ python sysproduction/update_fx_prices.py
```
or
```
% poetry run python -m sysinit.futures.repocsv_spotfx_prices
% poetry run python -m sysinit.futures.repocsv_adjusted_prices
```

#### Examine historic data
```mongosh
$ mongosh
test> use arctic_production;
switched to db arctic_production
arctic_production> db.spotfx_prices.find({})
arctic_production> db.futures_adjusted_prices.versions.find({})
```

### Load configuration

_Note: Rob mentions that some of this [configuration](https://github.com/zinakaye/pysystemtrade/blob/master/data/futures/csvconfig/instrumentconfig.csv) may be wrong (as he doesn't use it). Best take a look and maybe update the config and reimport._

```bash
% poetry run python -m sysinit.futures.repocsv_instrument_config
```

What is roll configuration?

```bash
% poetry run python -m sysinit.futures.roll_parameters_csv_mongo
```

#### Examine configuration
```mongo
test> use production;
production> db.futures_instruments.find();
```
r
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
$ :x # write message
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

## Connecting to IBKR/TWS API

Launch TWS
Open settings
Switch to API
Tick the Connect via sockets checkbox
Note the port
Edit the private config yaml
Put the port into the config (it's different to gateway--see below)

### IBKR API Gateway

Can only run one instance at once (Gateway or TWS)
Gateway port is 4001--set this in config

## @TODO

- We've imported [Rob's instrument configutration](https://github.com/zinakaye/pysystemtrade/blob/master/data/futures/csvconfig/instrumentconfig.csv) which he says " I don't actually trade or get prices for. Any configuration information for these may not be accurate and you use it at your own risk". Take a look and decide if we need to maintain our own instrument list.
- Do we know what [roll configuration](https://github.com/zinakaye/pysystemtrade/blob/master/docs/data.md#roll-parameter-configuration) is?
