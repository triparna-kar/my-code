import turtle
def tree(branch_len, t):
    t.pensize(13)
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    
    tree(75, t)

    t.home()
    
    my_win.exitonclick()
main()

'''
    reduce_len1 = random.randrange(5,25)
    reduce_len2 = random.randrange(5,25)
    branch_angle1 = random.randrange(15, 45)
    branch_angle2 = random.randrange(15, 45)
    
    if branch_len > 5:
        t.pensize(pen_width)
        
        t.forward(branch_len)
        t.right(branch_angle1)
        tree(branch_len - reduce_len1, t, pen_width-3)
        t.left(branch_angle1)

        t.left(branch_angle2)
        tree(branch_len - reduce_len2, t, pen_width-3)
        t.right(branch_angle2)
        t.backward(branch_len)
'''
