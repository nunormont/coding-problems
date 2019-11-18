#problem in https://www.codewars.com/kata/551dc350bf4e526099000ae5

import re
def song_decoder(song):
    song=re.sub("\s*WUB\s*"," ",song)
    song=re.sub("\s+"," ",song)
    song=song.strip()
    return song
    return -1
