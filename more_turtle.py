import turtle

t = turtle.Pen()

t.reset()
for x in range(1,19):
    t.forward(100)
    if x%2==0:
        t.left(175)
    else:
        t.left(225)

'''
t.reset()
for x in range(1,5):
    t.forward(50)
    t.left(90)

    
t.reset()
for x in range(1,31):
    t.forward(300)
    t.left(125)
    
'''
