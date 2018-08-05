![](img/monopoly-logo.png)
# Monopoly Analysis
*version Alpha 0.1*

The famous fast-trading board game Monopoly meets decision support analysis.

> Monopoly, the fast-dealing property trading game where players buy, sell, dream and scheme their way to riches

**WARNING** This program is still in Alpha. There will be a lot of hickups along the way. Sorry for the inconveninece.

**WARNING** This program **currently** have no user interface. User that cannot troubleshoot Python code should not try the program until beta.

## ![](img/icons8-goal-24.png) Objective
This repository and project is created for **decision support** usage.<br>
Users can use this project in decisions-making purpose that could change the game aspects or leaders.

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

Create a suggestions on current game status
- Show property valuations
- Show rent on a property valuations
- Probability of getting a bankrupt

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

I recommended that you play on the real Monopoly board game, and use this service to provide more information about the game. We are not the game itself.

There is a few steps of the game that you need to follow. You will be asked for multiple inputs (eg. turns, decision made, dice rolls result) and there will be prompt in the command line (for current version)

Step 1: Type in **all** of the users.<br>
Step 2: Type in the orders that each user get (or skip if you liked to make us random)<br>
Step 3: Type in the rolls you get (or skip if you liked to make us random)<br>
Step 4: Choose to do any actions (Buy/Trade Property, Auction, Make/Redo Mortgage, Buy/Sell Assets or Finish Turn)<br>

and the process will repeat until we have the last man standing

The interface will show the current game status. You

## ![](img/icons8-user-manual-24.png) Documentation
The documentation on how to use/modify our modules, projects will be available shortly in GitHub Pages.

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
We welcome all of the developers into the development of this program. Please contact me for more information or to enroll.

----
## Other Stuff
### Configuration structure
Please check on the [documentation](https://sagelga.github.io/monopoly-analysis) page for more information.

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
The project is fan-made and built in the purpose of **support** the players (user) into making the decisions along the game play.

You hereby agreed to know and understand that we (developers) and the project (sagelga/monopoly-analysis) does not affiliate Hasbro and/or Monopoly board game product line. And you hereby to release Hasbro, as well as any employees or agents, from any and all liability, corporate, or personal loss caused to you or others by the use of this project.

This project can be used in personal non-commercial purpose and requires the users (you) to respect all the developers, copyright owner(s) and trademark owner(s). We are not response of liability, personal loss and any affliations created by this project.<br>
If you liked to use our project in yours, make sure that you are **forking this repository and also crediting us and Hasbro** and also make sure that your legal terms are based on us.

If you liked to use this repository in a commercial or for-profit benefits, please contact me and respective game trademark owner.

[Monopoly](https://www.hasbro.com/en-us/brands/monopoly) is a trademark from Hasbro or its subsidiaries, licensors, licensees, suppliers and accounts.<br>

Icons inside this project's README file is from [icons8.com](icons8.com) and [ForTheBadge](https://forthebadge.com).

> We are currenly open for your help on legal terms. Please **directly** contact me via email, provided in my profile page.

---

[![](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
[![](https://forthebadge.com/images/badges/contains-cat-gifs.svg)](https://forthebadge.com)
[![](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![](https://forthebadge.com/images/badges/powered-by-netflix.svg)](https://forthebadge.com)
