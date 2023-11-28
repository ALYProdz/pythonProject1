import turtle
bob = turtle.Turtle()
print(bob)
bob.color('blue')
#bob.lt(90)
#bob.fd(100)
for i in range(4):
    bob.bk(100)
    bob.lt(-90)
    bob.fd(-100)
    bob.circle((100))
    print(i)
bob.pen(100)

#print(bob.circle(3))
print(bob.fd(90))
print(bob.tiltangle(90))
bob.clone(T)
