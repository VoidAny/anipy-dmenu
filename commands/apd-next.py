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
    sub_proc = anipy_dmenu.player.mpv(entry)
    menu = anipy_dmenu.cli.menu(entry, [], sub_proc, None)
    
    menu.start_ep()


if __name__ == "__main__": main()
