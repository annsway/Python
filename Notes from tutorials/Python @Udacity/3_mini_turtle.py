import turtle 

def draw_rhombus(some_turtle): 
	for i in range(1,5): 
		some_turtle.forward(100)
		some_turtle.right(45)
		some_turtle.forward(100)
		some_turtle.right(135)

def draw_line(some_line): 
	for i in range(1,2):
		some_line.right(90)
		some_line.forward(300)

def draw_art():
	window=turtle.Screen()
	window.bgcolor("white")
	Ann = turtle.Turtle() 
	Ann.shape("turtle")
	Ann.color("blue")
	Ann.speed(0.5)
	for i in range(1,37):
		draw_rhombus(Ann)
		Ann.right(10)
	draw_line(Ann)
	window.exitonclick()

draw_art()
