import turtle as t

radius = int(input("Bullseye Radius: "))
target_location = input("Target Location (X Y): ")

x, y = target_location.split(" ")
x = int(x)
y = int(y)

t.pu()
t.goto(x, (radius * -4) + y)
t.pd()
t.fillcolor("Black")
t.begin_fill()
t.circle(radius * 4)
t.end_fill()

t.pu()
t.goto(x, (radius * -3) + y)
t.pd()
t.fillcolor("Blue")
t.begin_fill()
t.circle(radius * 3)
t.end_fill()

t.pu()
t.goto(x, (radius * -2) + y)
t.pd()
t.fillcolor("Red")
t.begin_fill()
t.circle(radius * 2)
t.end_fill()

t.pu()
t.goto(x, (radius * -1) + y)
t.pd()
t.fillcolor("Yellow")
t.begin_fill()
t.circle(radius)
t.end_fill()


hold = input("Press ENTER to exit.")