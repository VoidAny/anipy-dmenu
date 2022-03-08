anipy-dmenu
===========

What is this?
-------------

`anipy-dmenu` is a Python 3.10 program that lets you watch anime with dmenu.

It uses [anipy-cli](https://github.com/sdaqo/anipy-cli) to interact with gogoanime to get the anime, [mpv](https://mpv.io) to play the anime, and [dmenu-python](https://github.com/allonhadaya/dmenu-python) to interact with dmenu.

Installing - Dependancies
========================

You will need to have dmenu installed. For the other dependencies, install them via the makefile as root. 

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