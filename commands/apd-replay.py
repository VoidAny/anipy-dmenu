#!/bin/python3
import anipy_dmenu

def main() -> None:
    entry = anipy_dmenu.load_entry()

    # Play it
    anipy_dmenu.play_from_cached_entry_data(entry)


if __name__ == "__main__": main()
