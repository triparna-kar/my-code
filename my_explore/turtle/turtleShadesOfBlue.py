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
trip.forward(700)
trip.left(180)
trip.down()
colors = ['aquamarine','aquamarine1','aquamarine2','aquamarine3','aquamarine4',
          'azure','azure1','azure2','azure3','azure4','AliceBlue','blue','blue1',
          'blue2','blue3','blue4','blue violet','CadetBlue','CadetBlue1',
          'CadetBlue1','CadetBlue2','CadetBlue3','CadetBlue4',
          'CornflowerBlue','cyan','cyan1','cyan2',
          'cyan3','cyan4','DarkBlue','DarkCyan','DarkSeaGreen','DarkSlateBlue',
          'DarkTurquoise','DarkViolet','DeepSkyBlue','DeepSkyBlue1',
          'DeepSkyBlue2','DeepSkyBlue3','DeepSkyBlue4','DodgerBlue',
          'DodgerBlue1','DodgerBlue2','DodgerBlue3','DodgerBlue4','lavender',
          'LavenderBlush','LavenderBlush1','LavenderBlush2','LavenderBlush3',
          'LavenderBlush4','LightBlue','LightBlue1','LightBlue2','LightBlue3',
          'LightBlue4','LightCyan','LightCyan1','LightCyan2','LightCyan3','LightCyan4',
          'LightSkyBlue','LightSkyBlue1','LightSkyBlue2','LightSkyBlue3','LightSkyBlue4',
          'LightSlateBlue','LightSteelBlue','LightSteelBlue1','LightSteelBlue2',
          'LightSteelBlue3','LightSteelBlue4','MediumAquamarine','MediumBlue',
          'MediumSeaGreen','MediumSlateBlue','MediumTurquoise','MidnightBlue','navy',
          'NavyBlue','PaleTurquoise','PaleTurquoise1','PaleTurquoise2','PaleTurquoise3',
          'PaleTurquoise4','PowderBlue','SeaGreen','SeaGreen1','SeaGreen2','SeaGreen3',
          'SeaGreen4','SkyBlue','SkyBlue1','SkyBlue2','SkyBlue3','SkyBlue4','SlateBlue',
          'SlateBlue1','SlateBlue1','SlateBlue2','SlateBlue3','SlateBlue4','SlateBlue',
          'SlateBlue1','SlateBlue2','SlateBlue3','SlateBlue4','SteelBlue','SteelBlue1',
          'SteelBlue2','SteelBlue3','SteelBlue4','turquoise','turquoise1','turquoise2',
          'turquoise3','turquoise4','RoyalBlue','RoyalBlue1','RoyalBlue2','RoyalBlue3',
          'RoyalBlue4'
          ]
count = 0
for s_color in colors:
    if (count>1) and (count%35==0):
        trip.up()
        trip.forward(350)
        trip.right(90)
        trip.forward(600)
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

'''
