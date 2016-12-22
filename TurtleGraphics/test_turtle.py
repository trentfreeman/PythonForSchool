
from turtle import turtle
from grid import grid

g = grid(-4,-4)

t1 = turtle('lou',g)
print(t1)
t1.left()
t1.forward()
print(t1)
t1.lower_pen()
t1.forward()
print(t1)

t2 = turtle('pat',g)
print(t2)
t2.lower_pen()
t2.right()
t2.right()
t2.forward()
t2.forward()
print(t2)
t2.left()
t2.forward()
t1.raise_pen()
print(t2)


