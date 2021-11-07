import turtle
from turtle import *
import math


def starting_point():  # sets up the starting point of the drawing
    turtle.penup()
    turtle.goto(-400, 400)
    turtle.penup


def rectange(length, height, color):  # creates a rectangle
    turtle.setheading(0)  # sets pen angle to 0
    turtle.fillcolor(color)  # selects the color
    turtle.begin_fill()  # starts filling the color
    for i in range(2):
        turtle.forward(length)  # draw a line length units long
        turtle.left(90)  # change pen angle towards 90 degree left
        turtle.forward(height)  # draw a line heights units long
        turtle.left(90)  # change pen angle towards 90 degree left
    turtle.end_fill()  # ends filling the color


def star(size, color):  # draws the star
    turtle.fillcolor(color)  # selects the color
    turtle.begin_fill()  # starts filling color
    for i in range(5):
        turtle.right(144)  # change pen angle towards 144 degree right
        turtle.forward(size)
    turtle.end_fill()  # ends filling color


def circle(size, color):  # draws a circle
    turtle.fillcolor(color)  # selects the color
    turtle.begin_fill()  # starts filling color
    turtle.circle(size)
    turtle.end_fill()  # ends filling color


def square(size, color):  # draws a square
    turtle.fillcolor(color)  # selects the color
    turtle.begin_fill()  # starts filling color
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)  # change pen angle towards 90 degree left
    turtle.end_fill()  # ends filling color


def polygon(no_of_sides, size):  # draws a polygon based on number of sides
    angle = 360 / no_of_sides

    for i in range(no_of_sides):
        turtle.forward(size)
        turtle.left(angle)


def draw_flower(petals, size, color):  # draws a flower
    heading = turtle.heading()
    turtle.fillcolor(color)  # selects the color
    turtle.begin_fill()  # starts filling color
    for i in range(petals):
        heading = turtle.heading()
        turtle.circle(size, 60)  # draws a circle
        turtle.left(120)
        turtle.circle(size, 60)
        turtle.setheading(heading)
        turtle.left(360 / petals)

    turtle.end_fill()  # end filling color


#########################1st Pattern ##########################
def Flower_tile(size, length, color_1, color_2, color_3):
    turtle.speed(0)  # sets drawing speed to 0/ which is the fastest

    # creation of outer square
    square(size, color_1)  # creates a square

    # moves the pen to the next starting point of the inner square
    turtle.penup()
    turtle.forward(size / 4)
    turtle.left(90)
    turtle.forward(size / 4)
    turtle.right(90)
    turtle.pendown()

    # creation of inner square
    square(size / 2, color_2)  # creates one more square

    # moves the pen to the starting point of the flower
    turtle.penup()
    turtle.forward(size / 4)
    turtle.left(90)
    turtle.forward(size / 4)
    turtle.right(90)
    turtle.pendown()

    # creation of flower
    draw_flower(10, size / 4, color_3)  # draws the flower

    # moves the pen to the starting point of the next tile
    turtle.penup()
    turtle.forward(size / 2)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.pendown()


def Flower_tiles_Pattern(size, length, color_1, color_2, color_3):
    turtle.speed(0)
    if (length > 6):  # checks if the length entered is greater then 6
        x = int(length / 6)  # store the int value for length/6 in x
        y = length % 6  # store the modulus value for length%6 in y
        value = size  # store the size in value , so can be used later to move the pen below after 6 tiles
        for i in range(x):  # loops number of times x
            # sets the starting position for the tile
            turtle.penup()
            turtle.goto(-400, 200)
            turtle.right(90)
            turtle.forward(value)
            turtle.pendown()
            turtle.left(90)
            value += size

            for i in range(6):  # draws 6 tiles
                Flower_tile(size, length, color_1, color_2, color_3)

        # sets the starting position for the tile for the next line
        turtle.penup()
        turtle.goto(-400, 200)
        turtle.right(90)
        turtle.forward(value)
        turtle.pendown()
        turtle.left(90)
        value += size

        # draws number of remaining tiles
        for i in range(y):
            Flower_tile(size, length, color_1, color_2, color_3)


    else:  # if length enters is < 6 simply draws that numbers of tiles
        for i in range(length):
            turtle.penup()
            turtle.goto(-400, 0)
            turtle.pendown()
            Flower_tile(size, length, color_1, color_2, color_3)


######################### 2nd Pattern #########################
def v_shape(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    # starts making a V shape
    turtle.speed(0)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size * 2)
    turtle.left(135)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size * 2)
    turtle.right(45)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size * 2)
    turtle.right(135)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size * 2)
    # ends making a V shape
    turtle.end_fill()


def X_tile(perpen, height, color_1, color_2, mid_point, size):
    turtle.speed(0)
    rectange(perpen, height, color_1)  # draws a rectangle so the X shape can fit in
    turtle.penup()
    turtle.forward(mid_point)  # moves the pen to the center of the rectange so X shape can be made
    turtle.left(90)
    turtle.forward(height / 2)
    turtle.setheading(0)
    turtle.pendown()

    v_shape(size, color_2)  # Draws a V shape ,
    turtle.setheading(
        180)  # rotate the pen to 180 degree so that the another V shape can be made which will make it look like an X
    v_shape(size, color_2)  # Draws another V shape opposite to the first one
    turtle.setheading(0)  # Sets the pen direction back to normal (0 Degree)
    turtle.penup()  # moves the pen to the next point to so another tile can be made
    turtle.forward(perpen / 2)
    turtle.setheading(270)
    turtle.forward(height / 2)
    turtle.setheading(0)
    turtle.pendown()


def x_pattern_tile(size, length, color_1, color_2, shapes_in_one_row):
    turtle.speed(0)

    perpen = (math.sin(math.radians(45)) * (size * 2)) * 2 + (
                size * 2)  # gets the length of the rectangle for the X tile
    height = (math.sin(math.radians(45)) * (size * 2)) * 2  # gets the height of the rectangle  for the X tile
    mid_point = perpen / 2

    if (length > shapes_in_one_row):  # Checks if the length is less then shapes in one row
        x = int(length / shapes_in_one_row)  # store the int value for length/shapesInOnerow in x
        y = length % shapes_in_one_row  # store the modulus value for length%shapesInOneRow in y
        value = height  # store the size in value , so can be used later to move the pen below after 6 tiles
        for i in range(x):  # loops number of times x
            # sets the starting position for the tile
            turtle.penup()
            turtle.goto(-400, 200)
            turtle.right(90)
            turtle.forward(value)
            turtle.pendown()
            turtle.left(90)
            value += height

            for i in range(shapes_in_one_row):  # draws  x tiles
                if (length % 2 == 0):  # checks for the even number , so a alternation color pattern can be drawn
                    temp_color = color_1  # stores color_1 in a temporary variable
                    color_1 = color_2  # stores color_2 in color_1 variable
                    color_2 = temp_color  # stores temp_color to color_2
                    X_tile(perpen, height, color_1, color_2, mid_point, size)  # draws the x-tile

                else:
                    X_tile(perpen, height, color_1, color_2, mid_point, size)  # draws the x-tile

        # sets the position of the pen to the next line
        turtle.penup()
        turtle.goto(-400, 200)
        turtle.right(90)
        turtle.forward(value)
        turtle.pendown()
        turtle.left(90)
        value += height

        # draws number of remaining tiles
        for i in range(y):

            if (y % 2 == 0):
                X_tile(perpen, height, color_1, color_2, mid_point, size)
                temp_color = color_1
                color_1 = color_2
                color_2 = temp_color

            else:
                X_tile(perpen, height, color_1, color_2, mid_point, size)

    else:  # if the length is less the 6 , it will simply draws those tiles
        for i in range(length):
            if (length % 2 == 0):
                X_tile(perpen, height, color_1, color_2, mid_point, size)

            else:
                temp_color = color_1
                color_1 = color_2
                color_2 = temp_color

                X_tile(perpen, height, color_1, color_2, mid_point, size)


######################## 3rd Pattern #########################
def leaf(size, color, angle, pencolor):
    turtle.speed(0)  # sets the speed of drawing
    turtle.pencolor(pencolor)  # sets the pencolor
    for i in range(24):  # makes a curve like shape
        turtle.forward(size)
        turtle.right(3)
    for j in range(24):  # makes a curve like shape
        turtle.forward(5)
        turtle.left(3)

    turtle.dot(10)  # place a dot
    turtle.right(180)  # goes in opposite direction

    for i in range(24):  # makes a curve like shape
        turtle.forward(size)
        turtle.right(3)
    for j in range(24):  # makes a curve like shape
        turtle.forward(5)
        turtle.left(3)

    turtle.right(180)  # pen changes its direction to opposite
    turtle.left(angle)  # rotates to some degree so new petal could be drawn


def flower(size, color, petals, pencolor):
    turtle.speed(0)
    angle = 360 / petals  # gives you an angle to separate each petal from another to make it a complete circle when its completed
    turtle.left(28)

    turtle.fillcolor(color)  # selects the color
    turtle.begin_fill()  # start filling the color
    for i in range(petals):  # start drawing petals
        leaf(size, color, angle, pencolor)
    turtle.end_fill()  # stop filling color


##########################################4th Pattern###################################################
def spiral_stars(size, color_1, color_2, color_3, color_4, color_5, color_6, color_7, color_8, color_9, color_10):
    speed(0)  # set speed
    for i in range(18):
        penup()  # sets up the starting position
        goto(0, 0)
        pendown()
        s = size
        colors = [color_1, color_2, color_3, color_4, color_5, color_6, color_7, color_8, color_9,
                  color_10]  # list containing 10 different colors
        for color in colors:  # makes a curve like shape / will run no of times colors present in the list colors
            star(s, color)
            penup()
            turtle.forward(size * 10)
            pendown()
            turtle.right(10)
            s += size  # increase the size of star after each loop

    turtle.right(72)
    penup()
    goto(0, 0)
    pendown()

    #  creates the middle blue pattern in the center of all the stars
    sides = 16
    angle = 360 / sides
    for i in range(sides):
        turtle.left(angle)
        pencolor("blue")
        pensize(2)
        polygon(sides, 10)


########################## Main #########################
def reading_drawing(
        choice):  # gets the User choice and draws the pattern call in the functions to draw those patterns accordingly
    if choice == 1:
        first = []
        f = open("First_Pattern.txt", 'r')  # open up the file
        for line in f:
            first.append(line.replace('\n',
                                      ''))  # replace the new lines characters for the file ,  and store each line in a list.
        f.close()  # closes the file
        size = int(first[0].split(" : ")[1])  # gets the size from the list which we generated from the file
        length = int(first[1].split(" : ")[1])  # gets the length from the list which we generated from the file
        color_1 = first[2].split(" : ")[1]  # gets the color_1 from the list which we generated from the file
        color_2 = first[3].split(" : ")[1]  # gets the color_2 from the list which we generated from the file
        color_3 = first[4].split(" : ")[1]  # gets the color_3 from the list which we generated from the file

        Flower_tiles_Pattern(size, length, color_1, color_2, color_3)  # draws the pattern using the parameters above.
        print("Click on the screen to exit the program")
        turtle.exitonclick()  # exits on clicking the screen
        print("Thank you for using the program :) \n Good Bye")
        exit()  # exits the program

    # Same as the first choice
    elif choice == 2:
        second = []
        f = open("Second_Pattern.txt", 'r')
        for line in f:
            second.append(line.replace('\n', ''))
        f.close()
        size = int(second[0].split(" : ")[1])
        length = int(second[1].split(" : ")[1])
        color_1 = second[2].split(" : ")[1]
        color_2 = second[3].split(" : ")[1]
        shapesInOneRow = int(second[4].split(" : ")[1])

        x_pattern_tile(size, length, color_1, color_2, shapesInOneRow)
        print("Click on the screen to exit the program")
        turtle.exitonclick()
        print("Thank you for using the program :) \n Good Bye")
        exit()  # exits the program


    # Same as the first choice
    elif choice == 3:
        third = []
        f = open("Third_Pattern.txt", 'r')
        for line in f:
            third.append(line.replace('\n', ''))
        f.close()
        size = int(third[0].split(" : ")[1])
        petals = int(third[1].split(" : ")[1])
        color_1 = third[2].split(" : ")[1]
        color_2 = third[3].split(" : ")[1]

        flower(size, color_1, petals, color_2)
        print("Click on the screen to exit the program")
        turtle.exitonclick()
        print("Thankyou For using the program :) \n Good Bye")
        exit()  # exits the program


    # Same as the first choice
    elif choice == 4:
        forth = []
        f = open("Forth_Pattern.txt", 'r')
        for line in f:
            forth.append(line.replace('\n', ''))
        f.close()
        star_size = int(forth[0].split(" : ")[1])
        color_1 = forth[1].split(" : ")[1]
        color_2 = forth[2].split(" : ")[1]
        color_3 = forth[3].split(" : ")[1]
        color_4 = forth[4].split(" : ")[1]
        color_5 = forth[5].split(" : ")[1]
        color_6 = forth[6].split(" : ")[1]
        color_7 = forth[7].split(" : ")[1]
        color_8 = forth[8].split(" : ")[1]
        color_9 = forth[9].split(" : ")[1]
        color_10 = forth[10].split(" : ")[1]

        spiral_stars(star_size, color_1, color_2, color_3, color_4, color_5, color_6, color_7, color_8, color_9,
                     color_10)
        print("Click on the screen to exit the program")
        turtle.exitonclick()
        print("Thank you for using the program :) \n Good Bye")
        exit()  # exits the program

    else:
        print("Please Enter the correct Choice in range [1-4]")


def User_Custom_Creation():  # this fuction is used to enable user to create their own patterns by using already defined shapes in the program
    # This color is used to validate the user entered color using while loop
    colorList = ("red" , "yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white")
    print("Select the shape: \n 1)Circle \n 2)Square  \n 3)Polygon \n 4)Star \n 5)V-shape \n 6)flower")
    num = int(input("Enter the number of the shape you want to try : "))
    while num < 1 or num > 7:  # validates that the user input is between 1-6
        num = int(input("Incorrect selection please enter again :"))

    if (
            num == 1):  # if user selects this option, it will ask the user to enter the parameters to draw its respective shape
        x = float(input("Please enter the x - Coordinate where you want to draw : "))
        y = float(input("Please enter the y - Coordinate where you want to draw : "))
        size = int(input("Please enter the size: "))
        color = input("Please enter the color :").lower() # takes the color input and convert it into lowercase
        while(color not in colorList): # checks if the user enters the incorrect color and keeps on asking for user name until the entered color match on of the colors in the list
            color = input("Incorrect color , Please enter the correct color: ").lower


        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        circle(size, color)

    elif (
            num == 2):  # if user selects this option, it will ask the user to enter the parameters to draw its respective shape
        x = float(input("Please enter the x - Coordinate where you want to draw : "))
        y = float(input("Please enter the y - Coordinate where you want to draw : "))
        size = int(input("Please enter the size: "))
        color = input("Please enter the color :").lower()
        while (color not in colorList):  # checks if the user enters the incorrect color and keeps on asking for user name until the entered color match on of the colors in the list
            color = input("Incorrect color , Please enter the correct color: ").lower()
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        angle = float(input("Please enter the angle you want to rotate : "))
        setheading(angle)
        square(size, color)
        setheading(0)

    elif (
            num == 3):  # if user selects this option, it will ask the user to enter the parameters to draw its respective shape
        x = float(input("Please enter the x - Coordinate where you want to draw : "))
        y = float(input("Please enter the y - Coordinate where you want to draw : "))
        size = int(input("Please enter the size: "))
        sides = int(input("Please Enter the number of sides : "))
        color = input("Please enter the color :").lower()
        while ( color not in colorList):  # checks if the user enters the incorrect color and keeps on asking for user name until the entered color match on of the colors in the list
            color = input("Incorrect color , Please enter the correct color: ").lower()
        angle = float(input("Please enter the angle you want to rotate : "))
        setheading(angle)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        polygon(sides, size)
        turtle.end_fill()
        setheading(0)

    elif (
            num == 4):  # if user selects this option, it will ask the user to enter the parameters to draw its respective shape
        x = float(input("Please enter the x - Coordinate where you want to draw : "))
        y = float(input("Please enter the y - Coordinate where you want to draw : "))
        size = int(input("Please enter the size: "))
        color = input("Please enter the color :").lower()
        while (color not in colorList):  # checks if the user enters the incorrect color and keeps on asking for user name until the entered color match on of the colors in the list
            color = input("Incorrect color , Please enter the correct color: ").lower()
        angle = float(input("Please enter the angle you want to rotate : "))
        setheading(angle)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        star(size, color)
        setheading(0)

    elif (
            num == 5):  # if user selects this option, it will ask the user to enter the parameters to draw its respective shape
        x = float(input("Please enter the x - Coordinate where you want to draw : "))
        y = float(input("Please enter the y - Coordinate where you want to draw : "))
        size = int(input("Please enter the size: "))
        color = input("Please enter the color :").lower()
        while (color not in colorList):  # checks if the user enters the incorrect color and keeps on asking for user name until the entered color match on of the colors in the list
            color = input("Incorrect color , Please enter the correct color: ").lower()
        angle = float(input("Please enter the angle you want to rotate : "))
        setheading(angle)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        v_shape(size, color)
        setheading(0)

    elif (
            num == 6):  # if user selects this option, it will ask the user to enter the parameters to draw its respective shape
        x = float(input("Please enter the x - Coordinate where you want to draw : "))
        y = float(input("Please enter the y - Coordinate where you want to draw : "))
        size = int(input("Please enter the size: "))
        petals = int(input("Please input number of petals: "))
        color = input("Please enter the color :").lower()
        while (color not in colorList):  # checks if the user enters the incorrect color and keeps on asking for user name until the entered color match on of the colors in the list
            color = input("Incorrect color , Please enter the correct color: ").lower()
        angle = float(input("Please enter the angle you want to rotate : "))
        setheading(angle)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        draw_flower(petals, size, color)
        setheading(0)


def main_menu():  # Main menu function which displays the main interface of the program to user
    print("                    WELCOME TO PATTERN DESIGN                      ")
    print(" Select one of the option down below :-")
    print("1)4 Patterns")
    print("2)Create your own pattern")
    print("3)Exit")

    selection = int(input("Press 1, 2 or 3 to select your option : "))

    while selection != 1 and selection != 2 and selection != 3:
        print("Invalid Selection , Please choose the correct option : ")
        selection = int(input("Press 1 or 2 to select your option : "))

    if selection == 1:
        choice = int(input("Please select a number between [1-4] to get the pattern : "))
        while choice != 1 and choice != 2 and choice != 3 and choice != 4:
            print("Invalid Selection , Please choose the correct option between [1-4] : ")
            choice = int(input())

        reading_drawing(choice)

    elif selection == 2:
        User_Custom_Creation()
        select = int(input(
            "Do you want to create another shape ? \n Press 1 For Yes \n Press 2 to go back to main menu \n Press 3 to exit\n :"))
        while select == 1:
            User_Custom_Creation()
            select = int(input(
                "Do you want to create another shape ? \n Press 1 For Yes \n Press 2 to go back to main menu \n Press 3 to exit\n : "))
        if select == 2:
            main_menu()


        elif select == 3:
            print("Thank you for using the program :) \n Good Bye")
            exit()

        else:
            print("Invalid input , the program will exit now")

    else:
        print("Thank you For using the program :) \n Good Bye")
        exit()


main_menu()


