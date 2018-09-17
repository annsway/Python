#Define instances of the class called media 
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
avatar = media.Movie("Avatar", 
					 "A marine on an alien planet", 
					 "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", 
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#avatar.show_trailer()

logan = media.Movie("Logan", 
					"A story of X-Man Logan's life when he gets old",
					"https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
					"https://www.youtube.com/watch?v=DekuSxJgpbY")

#print(logan.storyline)
#logan.show_trailer()

school_of_rock = media.Movie("School of Rock", 
							 "Using rock music to learn", 
							 "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
							 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")


rataouille = media.Movie("Ratatouille", "A rat is a chef in Paris", 
						 "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
						 "https://www.youtube.com/watch?v=niD-jahFURU")

midnight_in_paris = media.Movie("Midnight in Paris", 
								"Going back in time to meet authors", 
								"https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/220px-Midnight_in_Paris_Poster.jpg",
								"https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [toy_story, avatar, logan, school_of_rock, rataouille, midnight_in_paris]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

#print module: media
print(media.Movie.__module__)


#print name: Movie
print(media.Movie.__name__)

































