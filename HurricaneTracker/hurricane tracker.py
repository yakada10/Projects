import csv
import turtle
import os
import glob
import tkinter
def graphical_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return t, wn, map_bg_img


import os


import os

def main():
    (t, wn, map_bg_img) = graphical_setup()
    storm_name = input('Enter Storm Name:')
    storm_input = f'data/{storm_name}.csv'

    if not os.path.exists(storm_input):
        print(f"Storm data file '{storm_name}.csv' does not exist.")
        exit(0)

    try:
        val = open(storm_input, 'r').readlines()
        val.pop(0)
        t.penup()
        for x in val:
            sub_strings = x.split(",")
            lat = float(sub_strings[2])
            lon = float(sub_strings[3])
            wind = int(sub_strings[4])

            t.goto(lon, lat)

            if wind >= 157:
                t.color("red")
                t.width(15)
                t.write('5')
            elif 130 <= wind < 157:
                t.color("orange")
                t.width(11)
                t.write('4')
            elif 111 <= wind < 130:
                t.color("yellow")
                t.width(7)
                t.write('3')
            elif 96 <= wind < 111:
                t.color("green")
                t.width(3)
                t.write('2')
            elif 74 <= wind < 96:
                t.color("blue")
                t.width(2)
                t.write('1')
            else:
                t.color("white")
                t.width(1)

            t.pendown()
    except:
        print('Error processing storm data.')

    wn.exitonclick()

if __name__ == "__main__":
    main()