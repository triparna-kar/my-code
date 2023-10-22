import turtle

t = turtle.Turtle()
t.speed(0)

def square_spiral():
    for i in range(100):
        t.forward(i)
        t.left(91)


def pattern1():
    for i in range(500):
        t.forward(i)
        t.left(33)

def pattern2():
    for i in range(500):
        t.forward(i)
        t.left(1000)

def pattern3():
    for i in range(500):
        t.forward(i)
        t.left(51)

def fib(n:'upto n number')->int:
    l=[0,1]
    if n==0:
        return l[0]
    elif n==1:
        return l
    a=0
    b=1
    for i in range(0,n-1):
        b=a+b
        a=b-a
        l.append(b)
    return l

def pattern4():
    fibs = fib(50)
    for i in fibs:
        t.forward(i)
        t.left(108)

pattern4()
