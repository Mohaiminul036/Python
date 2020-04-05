import turtle
t = turtle.Pen()                #创建一支画笔

iCirclesCount = 30          
for x in range(iCirclesCount):  #循环30次
    t.color("red")      
    turtle.begin_fill()
    t.circle(100)               #画一个直径为100的圆
    t.end_fill()
    t.left(360/iCirclesCount)
    print(t.position())   #向左转 360 / 30 = 12度
   
