import turtle as t
import colorsys as c
t.setup(900,900)
t.speed(0)
t.tracer(8)
t.width(1)
t.bgcolor("black")
colors=["yellow","red","yellow","red"]
for f in range(30):
    for g in range(20):
     t.color(c.hsv_to_rgb(f/20,g/30,1))
     t.right(90)
     t.circle(200-g*4,90)
     t.left(90)
     t.circle(200-g*4,90)
     t.right(180)
     t.circle(10,24)
t.hiddenturtle()
t.done()