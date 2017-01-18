import webbrowser


class Movie():
    '''This class contains information about movies '''
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        '''creates framework for clickable movies into trailers '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''opens the webbrowser into the trailer '''
        webbrowser.open(self.trailer_youtube_url)
