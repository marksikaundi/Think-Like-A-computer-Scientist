# The step is to add a length parameter to square. below is the solution
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 100)