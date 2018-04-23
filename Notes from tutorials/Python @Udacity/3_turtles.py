import turtle 

# Define a class 
def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90) # Turn 90 degrees
	
	## Or use while loop  
	# turns = 0
	# while turns < 4: 
	# 	brad.forward(100)
	# 	brad.right(90)
	# 	turns = turns + 1


	
def draw_circle():
	Ann = turtle.Turtle()
	Ann.shape("turtle")
	Ann.color("orange")
	Ann.circle(100)        # draw a circle with radius = 100

def draw_triangle():
	Steve = turtle.Turtle()
	Steve.shape("turtle")
	Steve.color("red")
	Steve.left(240)

	for x in range(3):
		Steve.forward(100)
		Steve.right(120)



def drawing():
	window = turtle.Screen()
	window.bgcolor("white")


	# Define an instance called "brad" of a class 
	brad = turtle.Turtle() # Initiate a turtle named brad 
	brad.shape("turtle")   
	brad.color("blue")
	brad.speed(2)
	draw_square(brad)	

	# Draw a circle 
	draw_circle()
	
	# Draw a triangle
	draw_triangle()
	
	window.exitonclick()


drawing()

