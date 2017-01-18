import media
import fresh_tomatoes


toy_story = media.Movie(
    'Toy Story',
    "A story of a boy who's toys come to life",
    'http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg',
    'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://static.independent.co.uk/s3fs-public/thumbnails/image/2012/12/11/20/pg-24-avatar-1-capital.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

dumbanddumber = media.Movie(
    "Dumb and Dumber",
    "2 guys travel to Colorado to find a woman who one drove to the airport",
    "http://ia.media-imdb.com/images/M/MV5BMTIzNDI5MTc0M15BMl5BanBnXkFtZTYwMjM5NDU5._V1_SX640_SY720_.jpg", # noqa
    "https://www.youtube.com/watch?v=l13yPhimE3o")

starwars = media.Movie(
    "Star Wars",
    "Light vs Dark, Good vs Evil in space",
    "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/10/star-wars-force-awakens-official-poster.jpg", # noqa
    "https://www.youtube.com/watch?v=sGbxmsDFVnE")

lotr = media.Movie(
    "Lord of the Rings",
    "A Hobbit returns a powerful ring back to it's home",
    "http://img2.wikia.nocookie.net/__cb20060223102804/lotr/images/7/74/LOTRFOTRmovie.jpg", # noqa
    "https://www.youtube.com/watch?v=V75dMMIW2B4")

harrypotter = media.Movie(
    "Harry Potter",
    "A boys journey through wizaeding school",
    "https://typeset-beta.imgix.net/2016%2F7%2F3%2Fhp-cae3c33a-4904-4266-8f09-e5ef38f6a33b.jpg", # noqa
    "https://www.youtube.com/watch?v=L_50eAXYgAg")

movies = [toy_story, avatar, dumbanddumber, starwars, lotr, harrypotter]
'''fresh_tomatoes takes in the list of movies
and outputs a website with clickable pictures'''
fresh_tomatoes.open_movies_page(movies)
