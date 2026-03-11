import turtle

# ---------------- Screen ----------------
screen = turtle.Screen()
screen.setup(900,900)
screen.bgcolor("black")
screen.title("Radha Krishna Turtle Art")

turtle.tracer(0)

# ---------------- Radha ----------------
radha = turtle.Turtle()
radha.hideturtle()
radha.speed(0)
radha.color("#ff69b4")
radha.pensize(3)
radha.penup()

# hair curve
radha.goto(-200,120)
radha.pendown()
radha.circle(-120,60)

# head outline
radha.penup()
radha.goto(-180,40)
radha.pendown()
radha.circle(-80,200)

# eye
radha.penup()
radha.goto(-170,60)
radha.pendown()
radha.pensize(4)
radha.circle(6)

# bindi
radha.penup()
radha.goto(-160,80)
radha.color("red")
radha.begin_fill()
radha.circle(5)
radha.end_fill()

# nose
radha.penup()
radha.goto(-150,40)
radha.color("#ff69b4")
radha.pendown()
radha.circle(30,40)

# smile
radha.penup()
radha.goto(-165,20)
radha.pendown()
radha.circle(40,60)

# ---------------- Krishna ----------------
krishna = turtle.Turtle()
krishna.hideturtle()
krishna.speed(0)
krishna.color("gold")
krishna.penup()

# face
krishna.goto(120,50)
krishna.pendown()
krishna.begin_fill()
krishna.circle(100)
krishna.end_fill()

# eyes
krishna.penup()
krishna.goto(80,120)
krishna.pendown()
krishna.color("black")
krishna.circle(8)

krishna.penup()
krishna.goto(150,120)
krishna.pendown()
krishna.circle(8)

# smile
krishna.penup()
krishna.goto(95,70)
krishna.pendown()
krishna.circle(40,60)

# feather
krishna.penup()
krishna.goto(170,200)
krishna.color("#00cc99")
krishna.pendown()

krishna.begin_fill()
krishna.circle(60,80)
krishna.circle(20,120)
krishna.circle(-80,80)
krishna.end_fill()

# feather eye
krishna.penup()
krishna.goto(200,230)
krishna.color("#0047ab")
krishna.begin_fill()
krishna.circle(15)
krishna.end_fill()

# ---------------- Border ----------------
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.color("gold")
border.pensize(5)

border.penup()
border.goto(-420,-350)
border.pendown()

for i in range(2):
    border.forward(840)
    border.left(90)
    border.forward(700)
    border.left(90)

# ---------------- Finish ----------------
turtle.update()
turtle.done()