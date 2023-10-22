import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("hi trip")

trip = turtle.Turtle()
trip.pensize(10)
trip.up()
trip.right(90)
trip.forward(330)
trip.right(90)
trip.forward(500)
trip.left(180)
trip.down()

colors = ['brown', 'brown1', 'brown2', 'brown3', 'brown4',
          'burlywood', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4',
          'chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4',
          'firebrick','firebrick1','firebrick2','firebrick3','firebrick4',
          'tan','tan1', 'tan2','tan3','tan4','wheat','wheat1','wheat2','wheat3',
          'wheat4','saddle brown','SaddleBrown','sandy brown','SandyBrown']

for s_color in colors:
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

wn.exitonclick()

'''
1. saddle brown; firebrick; chocolate4; tan4
'''
