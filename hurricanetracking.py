    
import turtle
import csv

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.
       :return: a tuple containing the Turtle and the Screen
       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    
    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

        

def irma():
    """Animates the path of hurricane Irma
    """
    # Do not change this line
    # t is the turtle, and you will not need the other variables
    (t, wn, map_bg_img) = irma_setup()
    hurricaneFile = "data/irma.csv"
    # The line below is a little magical. It opens the file,
    # with awareness of any errors that might occur.
    with open(hurricaneFile, 'r') as csvfile:
        # This line gives you an "iterator" you can use to get each line
        # in the file.
        pointreader = csv.reader(csvfile)

        # You'll need to add some code here, before the loop
        # One thing you'll need to figure out how to do is to
        # skip the first line of the file (which is the header).
        # You might use a boolean variable, or you can
        # look into Python's built-in next function
        #(https://docs.python.org/3/library/functions.html#next)
        # pointreader is an iterator
        next(pointreader)
        for row in pointreader:
            t.setpos(float(row[3]),float(row[2]))
            introw = float(row[4])
            # category 1 
            if introw >= 74 and introw <= 95:
                t.color('blue')
                t.width(1)
            # category 2
            elif introw >= 96 and introw <= 110:
                t.color('green')
                t.width(2)
            # category 3
            elif introw >= 111 and introw <= 129:
                t.color('yellow')

                t.width(4)
            # category 4
            elif introw >= 130 and introw <= 156:
                t.color('orange')
                t.width(8)
            # category 5
            elif introw >= 157:
                t.color('red')
                t.width(12)
            # category -1
            else:
                t.color('white')
                t.width(1)
            

            # row is a list representing each line in the csv file
            # Each comma separated element is in its own index position
            # This code just prints out the date and time elements of each
            # row in the file.
            # Make sure you understand what is happening here.
            # Then, you'll need to change this code
            print("Date:", row[0], "Time:", row[1])



    # Hack to make sure a reference to the background image stays around
    # Do not remove or change this line
    return map_bg_img


# Feel free to add "helper" functions here


if __name__ == "__main__":
    bg=irma()

turtle.done()