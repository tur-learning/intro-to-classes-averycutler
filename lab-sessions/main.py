from homework import Music

first = Music("Plant the Garden", "Melt", "Pop", "If There's a Heaven", "222")
first.info()
first.rewrite_length()
# the above code produces the title, artist, genre, album, and length in seconds of the inputted song
# the rewrite length command rewrites the length of the song in terms of minutes

second = Music("Piano Man", "Billy Joel", "Rock", "Piano Man", "340")
second.info()
second.rewrite_length()
second.change_artist("Elton John")
# the above code produces the title, artist, genre, album, and length in seconds of the inputted song
# the rewrite length command rewrites the length of the song in terms of minutes
# the last line of code replaces the artist of the song as Elton John instead of Billy Joel