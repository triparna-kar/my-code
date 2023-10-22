import turtle
import random

#initialize tree parameters
make_leaves = True
branch_len =70
branch_width = 13
branch_width_for_leaf = 7
#leaf_size = random.randrange(5,15)
trunk_colors = ['saddle brown', 'firebrick', 'chocolate4', 'tan4']
leaf_colors1 = ['DarkGreen','DarkOliveGreen4','green','PaleGreen4']
leaf_colors2 = ['green3','LawnGreen','LimeGreen','PaleGreen3']
leaf_colors3 = ['YellowGreen','green1','GreenYellow','DarkOliveGreen1','PaleGreen1']

#leaf_colors = [random.choice(leaf_colors1)]+leaf_colors3
leaf_colors = leaf_colors1 + leaf_colors2


#initialize turtle object
t = turtle.Turtle()             #loop it in main to make many trees
my_win = turtle.Screen()
t.left(90)
t.up()
t.backward(300)
t.down()
wood_color = random.choice(trunk_colors)
#leaf_color = random.choice(leaf_colors)
t.color(wood_color)
t.speed(0)

def leaves(branch_width, branch_len):
    t.color(random.choice(leaf_colors))
    blen=0
    backward_dist = 5

    if branch_width == 1 :
        twig_width = 1
    elif branch_width <=3:
        twig_width = 2
    else:
        twig_width = 3

    t.pensize(twig_width)   
    t.dot(random.randrange(5,20),random.choice(leaf_colors))
    branch_end, blen = go_back_in_branch(backward_dist, blen, branch_len)
    
    if branch_end:
        t.color(wood_color)
        t.pensize(branch_width)
        return
    else:
        while (not branch_end):
            #set twig length
            twig_len = random.randrange(2,25)
            
            #right leaf
            t.right(70)
            t.forward(twig_len)
            t.dot(random.randrange(5,20), random.choice(leaf_colors))
            t.up()
            t.backward(twig_len)
            t.down()
            t.left(70)

            #set twig length
            twig_len = random.randrange(5,25)

            #left leaf
            t.left(70)
            t.forward(twig_len)
            t.dot(random.randrange(5,20), random.choice(leaf_colors))
            t.up()
            t.backward(twig_len)
            t.down()
            t.right(70)

            #go back
            branch_end, blen = (go_back_in_branch(backward_dist, blen, branch_len))
        else:
            t.color(wood_color)
            t.pensize(branch_width)
            return


def go_back_in_branch(travel, blen, branch_len):
    if (travel+blen)<branch_len:
        dist = travel
        branch_end = False
    elif (travel+blen)==branch_len:
        dist=travel
        branch_end = True
    else:
        dist = branch_len - blen
        branch_end = True

    blen = blen+dist
    t.up()
    t.backward(dist)
    t.down()
    return branch_end, blen


def branches(length, width):
    if width>0:
        #initialize parameters
        t.pensize(width)
        new_branch_len1 = random.randrange(5, 70)       #put more conditions: big tree, small tree
        new_branch_len2 = random.randrange(5, 70)
        branch_angle1 = random.randrange(7, 25)
        branch_angle2 = random.randrange(7, 25)

        #*****make main branch*****
        t.forward(length)

        #***right branch***
        t.right(branch_angle1)
        branches(new_branch_len1, width-2)
        t.left(branch_angle1)

        #***left branch***
        t.left(branch_angle2)
        branches(new_branch_len2, width-2)
        t.right(branch_angle2)

        if make_leaves:
            if width<branch_width_for_leaf:
                leaves(width, length)
                t.pensize(width)
            else:
                t.up()
                t.backward(length)
                t.down()
        else:
            t.up()
            t.backward(length)
            t.down()
        

branches(branch_len, branch_width)

my_win.exitonclick()
