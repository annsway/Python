import turtle

def draw_square(some_turtle):
	# range(1,5) - this loop runs 4 times 
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90) # Turn 90 degrees


def draw_art():
	window = turtle.Screen()
	window.bgcolor("white")
	#Create the turtle Brad - Draws a sqaure 
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(2)
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)
	window.exitonclick()

draw_art()
