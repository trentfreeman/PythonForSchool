#
# turtle - class describing turtle objects that sit on a grid.
#

from grid import grid

class turtle:

    def __init__(self,nm,gd):
        """ Used to set the attributes of a newly-constructed turtle object.
            e.g. turtle('lou')
            Places turtle at the origin, facing east.
            
            nm -- the name of the turtle, a string object
            gd -- the world where the turtle lives, a grid object

        """ 
        self.name = nm
        self.x = 0       # sitting at the origin
        self.y = 0
        self.grid = gd   # place on the grid
        gd.place(self)
        self.angle = 0   # facing to the east
        self.draw = False
        self.ink = 4
        self.r = snapshot(self)

    def lower_pen(self):
        self.draw= True

    def raise_pen(self):
        self.draw = False

    def is_drawing(self):
        return self.draw

    def heading_of(self):
        h = { 0:'E', 90:'N', 180:'W', 270:'S' }
        return h[self.angle]
        # (ignore other angles)

    def forward(self):
        x1,y1 = self.x,self.y
        """ Moves a turtle forward one unit. """
        if self.angle == 0:
            self.x = self.x + 1
        elif self.angle == 90:
            self.y = self.y + 1
        elif self.angle == 180:
            self.x = self.x - 1
        elif self.angle == 270:
            self.y = self.y - 1
        x2,y2 = self.x,self.y
        # (ignore other angles)
        if self.is_drawing() and self.ink>0:
            self.ink = self.ink -1
            self.grid.mark(x1,y1,x2,y2)

    def replenish(self, n):
        if n>0:
            self.ink =self.ink+n

    def left(self):
        """ Reorients turtle +90 degrees (i.e. counterclockwise). """
        self.angle = self.angle + 90
        if self.angle == 360:
            self.angle = 0


    def right(self):
        """ Reorients turtle -90 degrees (i.e. clockwise). """
        if self.angle == 0:
            self.angle = 270
        else:
            self.angle -= 90

    def rename(self,new_name):
        """ This is a 'setter' method to change a turtle's name. """
        self.name = new_name

    def name_of(self):
        """ This is a 'getter' method to access a turtle's name. """
        return self.name

    def position_of(self):
        """ This is a 'getter' method to access a turtle's coordinates
            as a pair.
        """
        return (self.x, self.y)

    def teleport(self,to_x,to_y):
        """ Moves turtle on its grid. """
        self.x = to_x   
        self.y = to_y
    def save(self):
        self.r = snapshot(self)

    def restore(self):
        (self.x,self.y),y= self.r.give()  
        h = { 0:'E', 90:'N', 180:'W', 270:'S' }
        for i in h:
            if h[i] == y:
                self.angle = i
    
    def as_string(self):
        """ Returns a string that describes the turtle's status. """
        f = "'" + self.name_of() + "'"
        s = "at " + str(self.position_of())
        t = "headed " + self.heading_of()
        if self.draw:
            d = " drawing"
        else:
            d = " not drawing"
        if self.ink==1:
            i = " *low*"
        elif self.ink == 0:
            i = " *out*"
        else:
            i = ""
        return "< turtle " + f + " " + s + " " + t + d + i + " >"

    def __str__(self):
        """ Special hidden method used by Python 'print' and 'str' 
            functions.  Returns a string representation of the turtle.
        """
        return self.as_string()

    def __repr__(self):
        """ Special hidden method used by Python's interactive 
            session interpreter to display a turtle object's
            value.  Returns a string representation of the turtle.
        """
        return self.as_string()

    def __iadd__(self, a):
        self.replenish(a)
        return self

    def __invert__(self):
        return self.ink


class snapshot:
    def __init__(self,t):
        self.turtpos = t.position_of()
        self.turtface = t.heading_of()
    
    def restore(self):
        pass

    def give(self):
        return self.turtpos, self.turtface
