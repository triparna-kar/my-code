import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("hi trip")

trip = turtle.Turtle()
trip.pensize(10)
trip.up()
trip.right(90)
trip.forward(300)
trip.right(90)
trip.forward(500)
trip.left(180)
trip.down()
colors = ['sea green','SeaGreen','SeaGreen1','SeaGreen2','SeaGreen3',
          'SeaGreen4','spring green','SpringGreen','SpringGreen1',
          'SpringGreen2','SpringGreen3','SpringGreen4','yellow green',
          'YellowGreen','dark green','dark olive green','dark sea green',
          'DarkGreen','DarkOliveGreen','DarkOliveGreen1','DarkOliveGreen2',
          'DarkOliveGreen3','DarkOliveGreen4','DarkSeaGreen','DarkSeaGreen1',
          'DarkSeaGreen2','DarkSeaGreen3','DarkSeaGreen4','forest green',
          'ForestGreen','green','green yellow','green1','green2','green3',
          'green4','GreenYellow','lawn green','LawnGreen','light green',
          'light sea green','LightGreen','LightSeaGreen','lime green',
          'LimeGreen','medium sea green','medium spring green','MediumSeaGreen',
          'MediumSpringGreen','pale green','PaleGreen','PaleGreen1',
          'PaleGreen2','PaleGreen3','PaleGreen4']
count = 0
for s_color in colors:
    if count == int(len(colors)/2):
        trip.up()
        trip.forward(500)
        trip.right(90)
        trip.forward(550)
        trip.left(90)
        trip.down()
    trip.color(s_color)
    trip.forward(200)
    trip.write(s_color)
    trip.up()
    trip.left(90)
    trip.forward(20)
    trip.left(90)
    trip.forward(200)
    trip.right(180)
    trip.down()
    count = count + 1

wn.exitonclick()

'''
1. DarkGreen; DarkOliveGreen4
2. green; PaleGreen4; 
3. green3; LawnGreen; LimeGreen; PaleGreen3; YellowGreen
4. green1; GreenYellow; DarkOliveGreen1; PaleGreen1; 
'''
