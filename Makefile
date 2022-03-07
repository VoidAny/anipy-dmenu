PREFIX := /usr/local

dependencies:
	python3 -m pip install -r requirements.txt

arch-dependencies:
	pacman -S python mpv

gentoo-dependencies:
	emerge -a dev-lang/python media-video/mpv

install: 
	mkdir -p "$(PREFIX)/bin"
	cp anipy_dmenu.py "$(PREFIX)/bin/anipy-dmenu"

uninstall:
	$(RM) "$(PREFIX)/bin/anipy-dmenu"

all: dependencies install

.PHONY: all dependencies install uninstall
