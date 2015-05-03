import webbrowser

class Video():
    """  Class Video is the parent class for movies and tv shows, with attributes
        title and duration, and a class list called BBFC_RATING with the possible ratings
    """
    BBFC_RATING = ["U", "PG", "12A", "12", "15", "18", "R18"]
    RATING_URL = ["http://upload.wikimedia.org/wikipedia/en/thumb/8/88/BBFC_U.svg/100px-BBFC_U.svg.png",
                  "http://upload.wikimedia.org/wikipedia/en/thumb/b/b5/BBFC_PG.svg/100px-BBFC_PG.svg.png",
                  "http://upload.wikimedia.org/wikipedia/en/thumb/8/87/BBFC_12A.svg/100px-BBFC_12A.svg.png",
                  "http://upload.wikimedia.org/wikipedia/en/thumb/8/84/BBFC_12.svg/100px-BBFC_12.svg.png",
                  "http://upload.wikimedia.org/wikipedia/commons/thumb/0/03/BBFC_15.svg/100px-BBFC_15.svg.png",
                  "http://upload.wikimedia.org/wikipedia/en/thumb/9/9f/BBFC_18.svg/100px-BBFC_18.svg.png",
                  "http://upload.wikimedia.org/wikipedia/en/thumb/9/90/BBFC_R18.svg/100px-BBFC_R18.svg.png"]

    def __init__(self, title, duration,classification_url):
        self.title = title
        self.duration = duration
        if classification_url in Video.BBFC_RATING:
            position = Video.BBFC_RATING.index(classification_url)
            self.classification_url = Video.RATING_URL[position]
        else:
            self.classification_url = "http://upload.wikimedia.org/wikipedia/en/thumb/4/4f/BBFC_Logo.svg/300px-BBFC_Logo.svg.png"

class Movie(Video):
    """
    Movies is the subclass of Video
    """
    def __init__(self, title, duration,classification_url, story_line, poster_image_url, movie_trailer):
        Video.__init__(self,title,duration,classification_url)
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.youtube_trailer_url = movie_trailer



    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)

    def print_info(self):
        print("Title is          : " + self.title)
        print("Duration is       : " + self.duration)
        print("Story line        : "+ self.story_line)
        print("Poster URL        : " + self.poster_image_url)
        print("Movie trailer url : " + self.youtube_trailer_url)
