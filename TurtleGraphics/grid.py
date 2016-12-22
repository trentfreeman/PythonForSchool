#
# grid - class describing an objects that carries turtles and the marks
#        they make
#

class grid:

    def __init__(self,w,h):
        """ Initializes a grid, one that holds a collection of turtles.  Its
            range of visible positions have an x-coordinate range from
            -w to w, and a y-coordinate range from -h to h.

            w -- maximum x-cooordinate value, a positive integer
            h -- maximum y-cooordinate value, a positive integer
        """
        self.width  = w
        self.height = h
        self.turtles = []
        self.marks= []

    def width_of(self):
        """ Get the maximum x-coordinate value of the grid.  """
        return self.width


    def height_of(self):
        """ Get the maximum y-coordinate value of the grid.  """
        return self.height


    def place(self,t):
        """ Include the turtle on the grid.
            
            t -- a turtle object
        """
        self.turtles.append(t)                      

    def mark(self,x1,y1,x2,y2):
        self.marks.append((x1,y1,x2,y2))

    def has_mark(self,x1,y1,x2,y2):
        if (x1,y1,x2,y2) in self.marks:
            return True
        elif (x2,y2,x1,y1) in self.marks:
            return True
        return False

    def has_drawer(self,x,y):
        for t in self.turtles:
            if t.position_of() == (x,y) and t.is_drawing():
                return True
        return False

    def has_heading(self, direction,x,y):
        for t in self.turtles:
            if t.position_of() == (x,y):
                if t.heading_of() == direction:
                    return True
        return False

    def as_string(self):
        """ Render the grid, and its turtles, as a series of text 
            characters. 
        """

        # Keep a list of the positions of all the turtles on this grid.
        positions = [ t.position_of() for t in self.turtles ]

        # The string returned by this method, built below.
        all = ""

        # For each row of the grid, with y from [height,-height]...
        for y in range(self.height,-self.height-1,-1):
            
            # Build a text-based visualization of that horizontal 
            # slice of the grid.

            # Each y-coordinate of the grid is rendered as a series of 
            # three rows of characters.  I build the y-th row in the 
            # loop below.

            row1 = ""
            row2 = ""
            row3 = ""
            for x in range(-self.width,self.width+1):

                # The code below builds a "cell" of the grid, centered at
                # the given x,y position.

                if y == 0:
                    # This cell is sitting on the x-axis.
                    horiz = "-"
                else:
                    horiz = " "

                left = horiz
                right = horiz

                if x == 0:
                    # This cell is sitting on the y-axis.
                    verti = "|"
                else:
                    verti = " "

                above = verti
                below = verti

                if self.has_mark(x,y,x+1,y):
                    right = "-"
                if self.has_mark(x,y,x-1,y):
                    left = "-"
                if self.has_mark(x,y,x,y+1):
                    above = "|"
                if self.has_mark(x,y,x,y-1):
                    below = '|'

                if (x,y) in positions:
                    # There's a turtle at this position. Render it.
                    center = "@"
                    if self.has_drawer(x,y):
                        left= '('
                        right = ')'
                    head = ["N","E",'S','W']
                    for h in head:
                        if self.has_heading(h,x,y):
                            if h =='N':
                                above ='^'
                            elif h == 'E':
                                right = '>'
                            elif h == "S":
                                below = 'v'
                            else: 
                                left = '<'
                elif x == 0 and y == 0:
                    # We're at the origin. Render it.
                    center = "+"
                else:
                    # We're renderedering some unoccupied cell within the grid.
                    center = "*"

                # Description of the cell, using the above:
                row1 = row1 + " "   + above  + " "
                row2 = row2 + left  + center + right
                row3 = row3 + " "   + below  + " "


            # Add those three rows to the description of the grid.
            all = all + row1 + "\n"
            all = all + row2 + "\n"
            all = all + row3 + "\n"

        # Return the lines of the grid's description, as a string.
        return all

    def __str__(self):
        return self.as_string()

    def __repr__(self):
        return self.as_string()
