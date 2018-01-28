"""
Polycarpus works as a DJ in the best Berland nightclub, 
and he often uses dubstep music in his performance. 
Recently, he has decided to take a couple of old songs 
and make dubstep remixes from them.

Let's assume that a song consists of some number of words.
To make the dubstep remix of this song, Polycarpus inserts a
certain number of words "WUB" before the first word of the song
(the number may be zero), after the last word (the number may
be zero), and between words (at least one between any pair of
neighbouring words), and then the boy glues together all the
words, including "WUB", in one string and plays the song at the club.

For example, a song with words "I AM X" can transform into a
dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot
transform into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track, 
but since he isn't into modern music, he decided to find out what
was the initial song that Polycarpus remixed. 
Help Jonny restore the original song.

Input

The input consists of a single non-empty string, consisting only
of uppercase English letters, the string's length doesn't exceed
200 characters

Output

Return the words of the initial song that Polycarpus used to
make a dubsteb remix. Separate the words with a space.

Examples    

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB") 
# => WE ARE THE CHAMPIONS MY FRIEND

"""
def song_decoder(song):
    dub = 'WUB'
    return ' '.join([i for i in song.split(dub) if i])
     



Test.assert_equals(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
Test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
Test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")
Test.assert_equals(song_decoder("RWUBWUBWUBLWUB"), "R L")
Test.assert_equals(song_decoder("WUBJKDWUBWUBWBIRAQKFWUBWUBYEWUBWUBWUBWVWUBWUB"), "JKD WBIRAQKF YE WV")
Test.assert_equals(song_decoder("WUBKSDHEMIXUJWUBWUBRWUBWUBWUBSWUBWUBWUBHWUBWUBWUB"), "KSDHEMIXUJ R S H") Test.assert_equals(song_decoder("QWUBQQWUBWUBWUBIWUBWUBWWWUBWUBWUBJOPJPBRH"), "Q QQ I WW JOPJPBRH") Test.assert_equals(song_decoder("WUBWUBOWUBWUBWUBIPVCQAFWYWUBWUBWUBQWUBWUBWUBXHDKCPYKCTWWYWUBWUBWUBVWUBWUBWUBFZWUBWUB"), "O IPVCQAFWY Q XHDKCPYKCTWWY V FZ") Test.assert_equals(song_decoder("WUBYYRTSMNWUWUBWUBWUBCWUBWUBWUBCWUBWUBWUBFSYUINDWOBVWUBWUBWUBFWUBWUBWUBAUWUBWUBWUBVWUBWUBWUBJB"), "YYRTSMNWU C C FSYUINDWOBV F AU V JB") Test.assert_equals(song_decoder("WUBKSDHEMIXUJWUBWUBRWUBWUBWUBSWUBWUBWUBHWUBWUBWUB"), "KSDHEMIXUJ R S H") Test.assert_equals(song_decoder("AWUBWUBWUB"), "A") Test.assert_equals(song_decoder("AWUBBWUBCWUBD"), "A B C D") Test.assert_equals(song_decoder("WUBWWUBWUBWUBUWUBWUBBWUB"), "W U B") Test.assert_equals(song_decoder("WUWUBBWWUBUB"), "WU BW UB") Test.assert_equals(song_decoder("WUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUABWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUB"), "WUAB") Test.assert_equals(song_decoder("U"), "U") Test.assert_equals(song_decoder("WUWUB"), "WU") Test.assert_equals(song_decoder("UBWUB"), "UB") Test.assert_equals(song_decoder("WUWUBUBWUBUWUB"), "WU UB U") Test.assert_equals(song_decoder("WUBWWUBAWUB"), "W A") Test.assert_equals(song_decoder("WUUUUU"), "WUUUUU") Test.assert_equals(song_decoder("WUBWUBA"), "A")


