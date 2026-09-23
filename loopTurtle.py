import turtle   
nbrSides = 6
for steps in range (nbrSides) :
    turtle.forward(100)
    turtle.right(360/nbrSides)
    for moresteps in range(nbrSides) :
        turtle.forward(50)
        turtle.right(360/nbrSides)