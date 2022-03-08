#!/bin/python3

from pathlib import Path
from anipy_cli import misc, history, query, download, url_handler, player, config, cli
import dmenu
import typing

# Other functions

def error(msg: str) -> typing.NoReturn:
    # Tell the user the message
    dmenu.show([], prompt="Error: " + msg)
    exit(1)

def warning(msg: str) -> None:
    # Tell the user the message
    dmenu.show([], prompt="Warning: " + msg)

def get_list_of_str_nums(start: int, end: int) -> list[str]:
    """Returns a list of strings of numbers between the start and end.
    The start and end are inclusive"""

    return [str(i) for i in range(start, end + 1)]


# Helper functions for using dmenu


def show_select(links_and_names: tuple[list[str], list[str]] | typing.Literal[0]) -> str:
    """Lets user select the show from the list provided by anipy_cli.query.query.get_links
    Returns the link for the selected show (without the gogoanime part)"""

    if links_and_names == 0: error("Invaild input into show_select (links_and_names == 0)")

    names: list[str] = links_and_names[1]
    links: list[str] = links_and_names[0]

    # Show user selction for names
    selected_name = dmenu.show(names)
    if selected_name == None: exit(0)

    # Now get the link the corresponding to the name selected
    location = names.index(selected_name)

    return links[location]


def ep_select(entry: misc.entry) -> misc.entry:
    """Lets the user pick which episode number they want
    Returns an entry with .ep filled 
    Requires .catagory_url to be filled"""
    
    ep_class = url_handler.epHandler(entry)
    ep_class.get_latest()

    # Get options for avalible episodes
    if ep_class.entry.latest_ep < 1:
        error("No episodes avalible (entry.lastest_ep is a value less than 1)")
    
    ep: str | None = dmenu.show(get_list_of_str_nums(1, ep_class.entry.latest_ep))
    # Make sure it is valid
    if ep == None: exit(0)
    if not ep.isdigit(): error("Episode number chosen is not a number (ep.isdigit() return False)")
    if int(ep) > ep_class.entry.latest_ep: error("Episode number chosen is too big (ep > latest_ep)")
    if int(ep) < 1: error("Episode number chosen is too small (ep < 1)")

    ep_class.entry.ep = int(ep)
    return ep_class.gen_eplink()
    

# Functions for eaiser use in sub-commands

def save_entry(entry: misc.entry) -> None:
    """Save an entry to the cache file. Used for playing next."""
    save_path = Path.home() / ".cache" / "anipy_dmenu_ep"
    try:
        save_path.parent.mkdir(exist_ok=True)
    except PermissionError:
        warning(f"Unable to make the folder the save file should be in (PermissionError when running mkdir on: {str(save_path)})")
        exit(1)

    save_data: list[str] = [
            entry.category_url,
            str(entry.ep)
            ]
    try:
        with save_path.open('w') as save_file:
            for piece in save_data:
                save_file.write(piece + '\n')
    except PermissionError:
        warning(f"Unable to save episode (PermissionError when writing to: {str(save_path)})")
        return

def load_entry() -> misc.entry:
    """Loads an entry from the cache file"""
    save_path = Path.home() / ".cache" / "anipy_dmenu_ep"
    
    try:
        with save_path.open('r') as save_file:
            save_data = save_file.read()
    except PermissionError:
        warning(f"Unable to read episode (PermissionError when reading: {str(save_path)})")
        exit(1)

    if save_data == "": error("Failed to load entry (got nothing from reading save_file in load_entry")
    # TODO: Fix this later
    data = save_data.split('\n')
    return misc.entry(category_url=data[0], ep=int(data[1]))

def main() -> None:
    entry: misc.entry = misc.entry()

    # Get the user's query
    user_query = dmenu.show(items=[], prompt="Enter anime query: ")
    if user_query == None: exit(0)
    gogo_query = query.query(user_query, entry)

    # Get the presise show 
    entry.category_url = config.gogoanime_url + show_select(gogo_query.get_links())

    # Get the ep and ep_url
    entry = ep_select(entry)

    # Get the stream_url 
    url_class = url_handler.videourl(entry, None)
    url_class.stream_url()
    entry = url_class.get_entry()

    save_entry(entry)

    # Play it
    sub_proc = player.mpv(entry)
    menu = cli.menu(entry, [], sub_proc, entry.quality)
    
    menu.start_ep()


if __name__ == '__main__':
    main()
