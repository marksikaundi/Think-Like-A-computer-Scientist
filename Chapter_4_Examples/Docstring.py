## doctstring is a string at the beginning of a function that xplains the interface ("doc" is short for "documentation"). Below is the example
def polyline(t, n, length, angle):
    """Draw n line segment wth the given leangth and angle (in degrees) between them. t is a turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)