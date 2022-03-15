anipy-dmenu
===========

What is this?
-------------

`anipy-dmenu` is a Python 3.10 program that lets you watch anime with dmenu.

It uses [anipy-cli](https://github.com/sdaqo/anipy-cli) to interact with gogoanime to get the anime, [mpv](https://mpv.io) to play the anime, and [dmenu-python](https://github.com/allonhadaya/dmenu-python) to interact with dmenu.

Installing - Dependancies
========================

You will need to have dmenu installed. If you don't, you can install it via the makefile. For the other dependencies, install them via the makefile as root. 

### Dmenu

To install dmenu, you have to build it from source. If you already have dmenu installed on your system, you can skip this step. If you do not have it installed, you can install Luke Smith's version by running command below as root:

`make dmenu`

In order to change any of the settings in dmenu, you will have to edit `/usr/local/src/dmenu/config.h` and then recompile and reinstall it with `sudo make clean install`.

### Arch/Artix

`make arch-dependencies`

### Gentoo

`make gentoo-dependencies`

Python Dependancies
-------------------

This installs all of the Python dependencies needed to run this script from PyPI. You should run this as the user that will be running this script.

`make dependencies`

Installing - Actually Installing
================================

Just run this command as root:

`make install`

You can now run this by using `anipy-dmenu`

Uninstall
=========

Just run 

`make uninstall`

as root.


Usage
=====

After install, anipy-dmenu can be used though dmenu itself, assuming you are using dwm.

Most command are prefixed with `apd`, which stands for AniPy-Dmenu.

Available Commands
------------------

`anipy-dmenu` - This lets you use dmenu to select an episode to watch.

`apd-next` - This lets you watch the episode after the one previously watched.
