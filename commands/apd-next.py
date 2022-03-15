#!/bin/python3
import anipy_dmenu

def main() -> None:
    entry = anipy_dmenu.load_entry()

    entry.ep += 1
    
    entry = anipy_dmenu.url_handler.epHandler(entry).gen_eplink()

    url_class = anipy_dmenu.url_handler.videourl(entry, None)
    url_class.stream_url()
    entry = url_class.get_entry()

    anipy_dmenu.save_entry(entry)

    # Play it
    anipy_dmenu.play_entry(entry)


if __name__ == "__main__": main()
