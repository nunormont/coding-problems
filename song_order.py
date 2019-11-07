'''
Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance.
Recently, he has decided to take a couple of old songs and make dubstep remixes from them.

Let's assume that a song consists of some number of words (that don't contain WUB).
To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first
word of the song (the number may be zero), after the last word (the number may be zero), and between words
(at least one between any pair of neighbouring words), and then the boy glues together all the words,
including "WUB", in one string and plays the song at the club.

For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot
transform into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to 
find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.
codewars link: https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python?fbclid=IwAR3MSn1tGHcxEkT7ZS2mxWiiyWUTSczAJd5wbefEb1gLrmaCJx8W98Gwgi4
'''

import re
def song_decoder(song):
    song=re.sub("\s*WUB\s*"," ",song)
    song=re.sub("\s+"," ",song)
    song=song.strip()
    return song
    return -1
