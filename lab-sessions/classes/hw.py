class Music:
    def __init__(self, title, artist, genre, record, length_sec):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.record = record
        self.length = length_sec

    def info(self):
        print(self.title, self.artist, self.genre, self.record, self.length)
    
    def change_artist(self, new_artist):
        self.artist = new_artist
        print(self.title, self.artist, self.genre, self.record, self.length)

    def rewrite_length(self):
        minutes = int(self.length)/60
        print(self.title, self.artist, self.genre, self.record, minutes)