import turtle


screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor('lightblue')
t=turtle.Turtle()
t.hideturtle()

t.penup()
t.goto(0,50)
t.pendown()
t.write("Turtle Presentation", font=("arial", 30 , "bold"),align="center")
t.penup()
t.goto(0,-50)
t.pendown()
t.write("Kassidy Reed" , font=("arial", 20, "bold"),align="center")

#favorite foods
enter = input("Press Enter to Switch Slides")
t.clear()
screen.bgcolor('silver')
t.setheading(0)
t.write("Favorite Foods", font=("arial", 25 , "bold"),align="center")



#hobbies
enter = input("Press Enter to Switch Slides")
t.clear()
screen.setup(500, 500)
screen.bgcolor('lightpink')
t.write("My Hobbies", font=("arial", 30 , "bold"),align="center")




#fav movie
enter = input("Press Enter to Switch Slides")
t.clear()
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('lightgreen')
t.write("Favorite Movie", font=("arial", 30 , "bold"),align="center")




#fav sport
enter = input("Press Enter to Switch Slides")
t.clear()
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('teal')
t.write("Favorite Sport", font=("arial", 30 , "bold"),align="center")



enter = input("Press Enter to Switch Slides")
t.clear()
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('yellow')
t.write("The End", font=("arial", 40 , "bold"),align="center")


