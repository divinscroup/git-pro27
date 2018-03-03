import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')
avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'https://is2-ssl.mzstatic.com/image/thumb/Video69/v4/8f/f3/e3/8ff3e3ff-483b-b097-4b1e-5bea8cb7c536/source/1200x630bb.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

school_of_rock = media.Movie('School Of Rock',
                             'a teacher who loved rock and teach it in school',
                             'https://images-na.ssl-images-amazon.com/images/I/81m0ywBJ67L._SY445_.jpg',
                             'https://www.youtube.com/watch?v=3PsUJFEBC74')

ratatouille = media.Movie('Ratatouille', ' a rat who love to being a chef',
                          'https://i.ytimg.com/vi/eh62Ri60lXI/movieposter.jpg',
                          'https://www.youtube.com/watch?v=8jT8YAY96oA')

midnight_in_paris = media.Movie('Midnight in Paris', 'woman fall in love',
                                'https://images-na.ssl-images-amazon.com/images/I/91n1dXALrML._SL1500_.jpg',
                                'https://www.youtube.com/watch?v=FAfR8omt-CY')

hunger_game = media.Movie('The Hunger Game', 'a girl trying to survive',
                          'https://images-na.ssl-images-amazon.com/images/I/91ikvZgoHZL._SL1500_.jpg',
                          'https://www.youtube.com/watch?v=mfmrPu43DF8')

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_game]


fresh_tomatoes.open_movies_page(movies)


