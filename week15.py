# 畫出幾何圖案(一):六角型
import turtle
shelly = turtle.Turtle()
# 重複6次:前進並轉彎
for i in range(6):
    shelly.forward(100)
    shelly.left(60)
# 畫出幾何圖案(二):重複六角型
import turtle
shelly = turtle.Turtle()
for n in range(36):
# 重複6次:前進並轉彎
     for i in range(6):
         shelly.forward(100)
         shelly.left(60)
     shelly.right(10) #加入轉彎
## 畫出幾何圖案(三):彩虹重複六角型
import turtle
shelly = turtle.Turtle()
turtle.bgcolor("black") #把背景變黑

# 畫出36個六角形,各隔10度
for n in range(36):
# 重複6次來畫六角形
    colors = ["red", "yellow", "blue", "orange", "green",
"purple"] # 選擇六角形顏色順序
    for i in range(6):
        shelly.color(colors[i]) #選擇i位置的顏色
        shelly.forward(100)
        shelly.left(60)
# 在畫下一個六角形前轉彎
    shelly.right(10)
## 畫出幾何圖案(四):小圓圈彩虹重複六角型
# 畫36個小圓圈
shelly.penup()
shelly.color("white")
# 重複36次,找到對應的六角形
for i in range(36):
    shelly.forward(220)
    shelly.pendown()
    shelly.circle(5)
    shelly.penup()
    shelly.backward(220)
    shelly.right(10)
# 隱藏海龜
shelly.hideturtle()


# 完整的英文程式碼
# make a geometric rainbow pattern
import turtle
# pick order of colors for the hexagon
colors = ['red', 'yellow', 'blue', 'orange', \
'green', 'red']
shelly = turtle.Turtle()
turtle.bgcolor('black') # turn background black
# make 36 hexagons, each 10 degrees apart
for n in range(36):
# make hexagon by repeating 6 times
    for i in range(6):
        shelly.color(colors[i]) # pick color at position i
        shelly.forward(250)
        shelly.left(60)
    # add a turn before the next hexagon
    shelly.right(10)
# get ready to draw 36 circles
shelly.penup()
shelly.color('white')
# repeat 36 times to match the 36 hexagons
for i in range(36):
    shelly.forward(450)
    shelly.pendown()
    shelly.circle(5)
    shelly.penup()
    shelly.backward(450)
    shelly.right(10)
# hide turtle to finish the drawing
shelly.hideturtle()
## 圖案1:畫出幾何彩虹圖案,畫出一排彩色正方形
# (1) 準備工作(色彩)
import turtle
shelly = turtle.Turtle()
turtle.bgcolor("black") #把背景變黑
# (2) 畫出6個正方形,各差30步
for n in range(6): # 畫六個正方形
    colors = ["red", "green","blue", "gold", "purple",
"yellow"]
    shelly.color(colors[n]) # A. 選擇第n個正方形的顏色
    for i in range(4): # B. 畫一個尺寸為25的正方形
        shelly.forward(25)
        shelly.left(90)
    shelly.penup() # C. 畫下一個正方形,前進30步(25+5=30)
    shelly.forward(30)
    shelly.pendown()
# (3) 隱藏海龜
shelly.hideturtle()

#圖案2:畫出房子


