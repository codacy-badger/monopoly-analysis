![](img/monopoly-logo.png)
# Monopoly Analysis
*version Alpha 0.1*

The famous fast-trading board game Monopoly meets decision support analysis.

> Monopoly, the fast-dealing property trading game where players buy, sell, dream and scheme their way to riches

**WARNING** This program **currently** have no user interface, as we released the Alpha 0.1.<br>
User that cannot troubleshoot Python code should not try the program until beta.

## ![](img/icons8-goal-24.png) Objective
This repository and project is created for **decision support** usage.<br>
Users can use this service in decisions-making purpose that could make the game more exciting.

The analysis will be based on information given, statistics calculations and many risks factor that other player have create.

Users that use this program will able to:
- Understand the risks of making a move
- Estimates the property values and upgrades
- Show risks and rewards throughout the gameplay

and of course, understand what is going to happen next, just like you do. Win.

## ![](img/icons8-features-list-24.png) Features
Play Monopoly in your way
- Edit the game rule to fit your game experiences
- Make your game more random with Speed Dice support
- Buy or sell a property and home with the interface

Also, this service can mame a suggestions on current game status
- Show property estimated values
- Show rent on a property valuations
- Probability of getting a bankrupt
- Probability to land on the desired space

Create a report on the game status and after-game

and many more!

## ![](img/icons8-downloading-updates-24.png) Installation
> To download and/or use this project, you have agreed and acknowledge of our [Terms of Use](https://github.com/sagelga/monopoly-analysis#boring-things-that-you-need-to-know).

Download this repository by cloning or click [here to download the .zip file](https://github.com/sagelga/monopoly-analysis/archive/master.zip).

> This program requires Python programming language and SQLite. Please download prior the launch of the program.

If you do not have Python or/and SQLite, you can run (for Linux)
```
sudo apt-get install python3
sudo apt-get install sqlite
```
and many other ways to install `python3` and `sqlite3`.<br>
Please check here later for more information about dependencies.

## ![](img/icons8-exe-24.png) How to start
You can checkout the `configuration.py` for edits on game settings, including starting money, jail penalty, etc.

If you have open the folder in Terminal, you can start by running this prompt
```
python3 main.py
```

Python supports Windows, MacOS, Linux Distributions. You can start the game from Command Prompt (Windows), Windows PowerShell (Windows) and Terminal (MacOS and Linux Distribution)

## ![](img/icons8-game-controller-24.png) How to use
> For more details, please check out our [user manual](https://sagelga.github.io/monopoly-analysis/).

We recommend you to play the Monopoly game on a real Monopoly board game <br>
and use this service to provide more information during the real-life gameplay. Our project goal is to support.

There is a few steps of the game that you need to follow. You will be asked for multiple inputs (eg. turns, decision made, dice rolls result) and there will be prompt in the command line (for current version)

Step 1: Type in **all** of the users.<br>
Step 2: Type in the orders that each user get (or skip if you liked to make us random)<br>
Step 3: Type in the rolls you get (or skip if you liked to make us random)<br>
Step 4: Choose to do any actions (Buy/Trade Property, Auction, Make/Redo Mortgage, Buy/Sell Assets or Finish Turn)<br>

and the process will repeat until we have the last man standing

The interface will show the current game status. You

## ![](img/icons8-user-manual-24.png) Documentation
The documentation on how to use/modify our modules, projects is available [here : https://sagelga.github.io/monopoly-analysis/](https://sagelga.github.io/monopoly-analysis/)

### Module distribution
This project is divided to 6 modules (Python file), which is<br>
[`main.py`](https://github.com/sagelga/monopoly-analysis/blob/master/main.py)
[`service.py`](https://github.com/sagelga/monopoly-analysis/blob/master/service.py)
[`actions.py`](https://github.com/sagelga/monopoly-analysis/blob/master/actions.py)
[`transaction.py`](https://github.com/sagelga/monopoly-analysis/blob/master/transaction.py)
[`database.py`](https://github.com/sagelga/monopoly-analysis/blob/master/database.py)
[`configuration.py`](https://github.com/sagelga/monopoly-analysis/blob/master/configuration.py)

which each module has it's own purpose
- main          : serves as program initiator + flow control
- service       : handle action made by user or asked for response from user
- action        : handle background action
- transaction   : prepare transaction to be made on database
- database      : create transaction directly to SQLite database
- configuration : user defined rules, which can **only** be retrieved.

User can edit the configuration to suit their game.

## ![](img/icons8-code-fork-24.png) Contribute
We welcome all of the developers into the development of this program.<br>
We have open the pull requests from all of the kind developers to improve this project.

For the new comers, please do as follows
1. Fork this repository
2. Create a new branch at the forked repository (as it will named as `your_username/monopoly-analysis`)
3. Create a pull request in this repository (sagelga/monopoly-analysis)
4. We will make a suggestions and merged your changes

## Other Stuff
### Edit your own game
Please check on the [documentation](https://github.com/sagelga/monopoly-analysis/wiki/Configurations) page on how you can edit the game parameters

> NOTE: You should able to read the Python Dictionary syntax to edit the file.

### Project Checker
**Fossa**<br>
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fsagelga%2Fmonopoly-analysis.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fsagelga%2Fmonopoly-analysis?ref=badge_large)

**Codacy**<br>
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fd8039eda0c844f6ac181689383a5dcf)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sagelga/monopoly-analysis&amp;utm_campaign=Badge_Grade)

**CircleCI**<br>
master<br>
[![CircleCI](https://circleci.com/gh/sagelga/monopoly-analysis/tree/master.svg?style=svg&circle-token=ce1cb3eb8a0730306315123563fc70bc5f635969)](https://circleci.com/gh/sagelga/monopoly-analysis/tree/master)

develop<br>
[![CircleCI](https://circleci.com/gh/sagelga/monopoly-analysis/tree/develop.svg?style=svg&circle-token=ce1cb3eb8a0730306315123563fc70bc5f635969)](https://circleci.com/gh/sagelga/monopoly-analysis/tree/develop)

### Boring things that you need to know
> We are covered our repository with Apache License version 2. 
Please check out the [LICENSE.md]() for more information.
You hereby agreed to know and understand that we (developers) and the project (sagelga/monopoly-analysis) does not affiliate Hasbro and/or Monopoly board game product line. And you hereby to release Hasbro, as well as any employees or agents, from any and all liability, corporate, or personal loss caused to you or others by the use of this project.

The project is fan-made and built in the purpose of **support** the players (user) into making the decisions along the game play.

This project can be used in non-commercial or/and non-profit purpose and requires the users to respect all the developers, copyright owner(s) and trademark owner(s). We are not response of trademark infringement or any legal actions against us.<br>
Make sure that you are following our license.

This project can be used in personal non-commercial purpose and requires the users (you) to respect all the developers, copyright owner(s) and trademark owner(s). We are not response of liability, personal loss and any affliations created by this project.<br>
If you liked to use our project in yours, make sure that you are **forking this repository and also crediting us and Hasbro** and also make sure that your legal terms are based on us.

If you liked to use this repository in a commercial or for-profit benefits, please contact me and respective game trademark owner.

[Monopoly](https://www.hasbro.com/en-us/brands/monopoly) is a trademark from Hasbro or its subsidiaries, licensors, licensees, suppliers and accounts.<br>

Icons inside this project's README file is from [icons8.com](https://icons8.com) and [ForTheBadge](https://forthebadge.com).

> We are currently open for your help on legal terms. Please **directly** contact me via email, provided in my profile page.

---

[![](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
[![](https://forthebadge.com/images/badges/contains-cat-gifs.svg)](https://forthebadge.com)
[![](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![](https://forthebadge.com/images/badges/powered-by-netflix.svg)](https://forthebadge.com)
