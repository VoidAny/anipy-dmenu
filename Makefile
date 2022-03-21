PREFIX := /usr/local

dependencies:
	python3 -m pip install -r requirements.txt

dmenu:
	mkdir -p "$(PREFIX)/src"
	cd "$(PREFIX)/src"
	git clone https://github.com/Lukesmithxyz/dmenu
	cd "$(PREFIX)/src/dmenu"
	make install

arch-dependencies:
	pacman -S python mpv

gentoo-dependencies:
	emerge -a dev-lang/python media-video/mpv

install: 
	mkdir -p "$(PREFIX)/bin"
	# Main library
	cp anipy_dmenu.py "$(PREFIX)/bin/anipy_dmenu.py"
	# The commands that can be run
	cp commands/anipy-dmenu.py "$(PREFIX)/bin/anipy-dmenu"
	cp commands/apd-next.py "$(PREFIX)/bin/apd-next"
	cp commands/apd-replay.py "$(PREFIX)/bin/apd-replay"
	cp commands/apd-previous.py "$(PREFIX)/bin/apd-previous"

uninstall:
	$(RM) "$(PREFIX)/bin/anipy_dmenu.py"
	$(RM) "$(PREFIX)/bin/anipy-dmenu"
	$(RM) "$(PREFIX)/bin/apd-next"
	$(RM) "$(PREFIX)/bin/apd-replay"
	$(RM) "$(PREFIX)/bin/apd-previous"

all: dependencies install

.PHONY: all dependencies install uninstall arch-dependencies gentoo-dependencies dmenu
