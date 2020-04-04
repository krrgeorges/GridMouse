## Project Description

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) [![Version](https://badge.fury.io/gh/tterb%2FHyde.svg)](https://badge.fury.io/gh/tterb%2FHyde)


### GridMouse

GridMouse is a utility for accessing mouse actions through keyboard. It works by using mode toggle.

There are two modes available for switching between normal keyboard use and using keyboard for mouse actions, toggled by Alt+X.

The monitor is divided into 3x3 grid.



It provides a set of commands that, when triggered can act on those commands accordingly. These commands are sent by the user through the telegram bot they will create (through [ @BotFather](https://telegram.me/BotFather)) for remotely controlling the desktop.

### Why should I use this?

Want to remote control your desktop for achieving tasks and monitoring processes but don't want to incur higher processing overhead by using general software applications for remote control and desktop sharing? This utility can help you with that. Since this runs on cmd and uses the win32 dlls through win32 utilities for python, the processing overhead with respect to other scripts and actions you want to overlook remotely is low.

### Features

#### Remote controls
* Can shut down workstation.
* Can take a screenshot of the system or start a stream of screenshots.
* Can run CMD commands.
* Can switch active windows.
* Can type keys or hotkeys or shortcut combinations.
* Can display all running processes.
* Can display all active window titles.

#### General

* Easily controlled by commands.
* Only a workstation and a mobile device containing the Telegram android app needed.
* No processing, streaming and bandwidth overhead. 

### Requirements

Requires Python -v > 3.6.0 

### Installation

```python
$ pip install dspc_bot_ctrl
```

### Initial Preparations


Since the controller relies on Telegram and its messaging ecosystem to communicate and get commands from user, the Telegram Android app must be installed in your android device.

In order to create a bot for yourself that responds to your message, create your bot using @BotFather. Contact BotFather throught the Telegram Android App and type in /newbot. Follow the instructions and note the HTTP API token it provides and it is used to initialize the bot in first run.


### Using dspc_bot_ctrl


#### Importing Bot Class
```python
from dspc_bot_ctrl.dspc_bot import DSPCBOT
```
#### Initializing and Deploying The Bot

```python
DSPCBOT().init()
```

If you are running the controller for the first time, it would ask for the HTTP API token that you have noted down when you created the bot. Once you feed in the token, it would be saved and subsequent runs would not need the token. If you want to revoke the saved token for a new bot, type in 'revoke' in the password field.

For every run, the controller would ask you for a password. Once the password is inputed, the controller would look out for a identification message from you. Find the bot by the name you have provided for the bot through BotFather and send message  'identify_me <password\>' to the bot through the Telegram Client. Once the controller receives the identification message with the correct password, It will start polling for messages and you can use the bot as you please.

In order to acheive your tasks and activities quicker, you can search for keyboard shortcuts for the particular task or sub-task you want acheived and use the necessary commands to send the keys to your keyboard.
