import webbrowser 

class Movie():
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, poster_image, 
				 trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

# *self* is not a Python keyword. 
# If you change all occurrences of the word "self" to another word, 
# say "test" in the media.py file, the code will still work. 

#class Movie():
# 	def __init__(test, movie_title, movie_storyline, poster_image, 
# 				 trailer_youtube):
# 		test.title = movie_title
# 		test.storyline = movie_storyline
# 		test.poster_image_url = poster_image
# 		test.trailer_youtube_url = trailer_youtube