import csv
import turtle
import os
import glob

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

def main():

    (t, wn, map_bg_img) = graphical_setup()
    storm_input = ('data\\') + input('Enter Storm Name:') + ('.csv')
    storm_data = glob.glob('data/*')
    try:
        val = open(storm_input, 'r').readlines()
        val.pop(0)
        for x in val:
            sub_strings = x.split(",")
            lat = float(sub_strings[2])
            lon = float(sub_strings[3])
            wind = int(sub_strings[4])
            t.pendown()
            t.goto(lon, lat)
            if wind >= 157:
                t.color("red")
                t.write('5')
                t.width(15)
            elif 130 <= wind < 157:
                t.color("orange")
                t.write('4')
                t.width(11)
            elif 111 <= wind < 130:
                t.color("yellow")
                t.write('3')
                t.width(7)
            elif 96 <= wind < 111:
                t.color("green")
                t.write('2')
                t.width(3)
            elif 74 <= wind < 96:
                t.color("blue")
                t.write('1')
                t.width(2)
            else:
                t.color("white")
                t.width(1)


    # also you'll need to fix the call below so that it calls
    # the track_storm function
    # wn, map_bg_img = track_storm('storm_input')

    # the line below needs to be the last line of main()
    # you'll need to get the wn from track_storm
    except:
        print('Invalid storm name.')
        exit(0)
    wn.exitonclick()


if __name__ == "__main__":
    main()