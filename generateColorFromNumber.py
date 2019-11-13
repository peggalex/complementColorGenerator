import turtle

screen=turtle.getscreen()
screen.colormode(255)

turtlesHard = []
turtlesSoft = []

# from numbers 0<i<255*6 (=1530),
# you can generate unique colors
# that cover the color wheel
# (does not do combinations of ALL of red green AND blue)

# this can generate distinct colors on opposite sides
# of the color wheel, so you can obtain a set of sudo-random colors
# that are still distinct from each other

#stop any loop with sig kill (ctrl c)

def _getColorsAll(_i):
    #precond: _i in [0,1]
    
    #all colors on colorwheel
    #includes pure red, green & blue

    # Given i belongs to the domain [0,255*6],
    # then i//255 can take on values in [0,5].
    # Let stage = i//255.
    # There 2 basic cases:
    #   case 1: current index is 255, next index going up from 0->255
    #   case 2: next index is 255, current index is decreasing from 255->0
    # => 2 stages * 3 indices for each color rgb = 6 stages in [0,5]
    
    # These cases alternate, and the indices shift 3 times.
    # I enumerated it so that even stages are case 1, and odd stages are case 2
    # This generates an even distribution on the colorwheel, although it
    # does not cover all permutations using 3 indices.

    i = int(_i*255*6)
    rgb = [0,0,0]
    index = (i//(2*255))%3
    indexNext = index+1 if index!=2 else 0
    
    if (i//255)%2==1:
        rgb[index] = 255-(i%255)
        rgb[indexNext] = 255
    else:
        rgb[index] = 255
        rgb[indexNext] = i%255
        
    return rgb

def _getSoftColors(_i):
    #pure red green and blue are kind of ugly
    #get rid of these by limiting rgb value domain to
    #[127,255], from [0,255]

    #let i belong to the domain [0,128*6]
    #read the intuition behind the code in comments
    #for the above function _getColorsAll(i: int)
    i = int(_i*128*6)
    rgb = [127,127,127]
    index = (i//(2*128))%3
    indexNext = index+1 if index!=2 else 0
    
    if (i//128)%2==1:
        rgb[index] = 255-(i%128)
        rgb[indexNext] = 255
    else:
        rgb[index] = 255
        rgb[indexNext] = 127+(i%128)
        
    return rgb


def resetScreen():
    global turtlesHard, turtlesSoft
    turtle.resetscreen()
    turtle.hideturtle()
    for t in turtlesHard+turtlesSoft:
        t.hideturtle()
    turtlesHard, turtlesSoft = [],[]


def demonstrateRange():
    resetScreen()
    while True:
        for i in range(0,128*6,3):
            screen.bgcolor(_getSoftColors(i))


def demonstrateComplements(complements=9):
    resetScreen()
    for i in range(complements):
        for y,lst in ((-10,turtlesHard),(10,turtlesSoft)):
            t = turtle.Turtle()
            t.penup()
            t.shape('turtle')
            t.speed('fastest')
            t.goto((i-complements//2)*30, y)
            lst.append(t)

    _setColorSoft = lambda t,i: t.color(*_getSoftColors(i))
    _setColorHard = lambda t,i: t.color(*_getColorsAll(i))


    while True:
        for _i in range(75):
            i = _i/75
            for j in range(complements):
                i = (i+j/complements)%1
                _setColorHard(turtlesHard[j],i)
                _setColorSoft(turtlesSoft[j],i)


if __name__ == "__main__":
        print('''Use demonstrateComplements(n) to show how you can generate n unique colors
on opposite sides of a soft color wheel. Use demonstrateRange() to just
show the full range of soft colors.

The reason for the soft colors is when exploring 3 color complements,
sometimes the 3 colors generated would be close to pure red, green and blue;
which looked pretty basic - like a 90s powerpoint. With soft colors, you can
still generate complements, but with lighter hues that are
more modern and appealing imo.

Press ctrl c (sig kill) to end a turtle demonstration.''')
