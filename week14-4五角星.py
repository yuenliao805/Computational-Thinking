import turtle
turtle.colormode(255)
shelly = turtle.Turtle()
shelly.color(255, 215, 0)
shelly.pensize(5)
# 將筆向前移動100個單位,向右轉144度,做五次畫五角星。
for i in range(5):
    shelly.forward(250)
    shelly.right(144)