import turtle

#initialize turtle object
t = turtle.Turtle()             #loop it in main to make many trees
my_win = turtle.Screen()

length = 50
t.color('brown')
t.forward(length)

l_len = length
t.dot(10, 'green')
t.backward(5)
l_len= l_len-5


while l_len > 0:
    
    t.right(90)
    t.forward(2)
    t.dot(10, 'green')
    t.backward(2)
    t.left(90)
    
    l_len= l_len-5
    t.backward(5)
    
    t.left(90)
    t.forward(2)
    t.dot(10, 'green')
    t.backward(2)
    t.right(90)
    
    l_len= l_len-5
    t.backward(5)
else:
    t.dot(10,'red')

my_win.exitonclick()
