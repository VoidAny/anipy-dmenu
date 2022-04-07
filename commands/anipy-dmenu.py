#!/bin/python3
import anipy_dmenu 

def main() -> None:
    entry: anipy_dmenu.anipy_cli.entry = anipy_dmenu.anipy_cli.entry()

    # Get the user's query
    user_query = anipy_dmenu.dmenu.show(items=[], prompt="Enter anime query: ")
    if user_query == None: exit(0)
    gogo_query = anipy_dmenu.anipy_cli.query(user_query, entry)

    # Get the presise show 
    entry.category_url = anipy_dmenu.anipy_cli.config.gogoanime_url + anipy_dmenu.show_select(gogo_query.get_links())

    # Get the ep and ep_url
    entry = anipy_dmenu.ep_select(entry)

    # Get the stream_url 
    url_class = anipy_dmenu.anipy_cli.videourl(entry, None)
    url_class.stream_url()
    entry = url_class.get_entry()

    anipy_dmenu.save_entry(entry)

    # Play it
    anipy_dmenu.play_entry(entry)


if __name__ == "__main__": main()
