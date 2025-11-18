import turtle
import random

t = turtle.Turtle()
r = random.randint(40, 100)
turtle.tracer(False)

def maçã(tamanho):

    t.speed(5)
    t.color("red")
    t.width(3)

    t.begin_fill()
    t.circle(tamanho)
    t.left(90)
    t.forward(r)
    t.end_fill()
    caule(tamanho)
    folha(tamanho)

def caule(tamanho):
    t.color("brown")
    t.penup()
    t.forward(tamanho)
    t.pendown()
    t.forward(tamanho * 0.9)

def folha(tamanho):
    t.color("forest green")
    t.begin_fill()
    t.circle(tamanho * 0.3)
    t.left(45)
    t.end_fill()


def spawnmaçã(cordX,cordy):
    t.penup()
    t.goto(cordX,cordy)
    t.pendown()
    size = random.randint(50,60)
    maçã(size)


turtle.onscreenclick(spawnmaçã,3)


turtle.done()