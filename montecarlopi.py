import random
import math

iterations = 100
samples = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]

for n in samples:
    x = 0
    errorsum = 0
    pisum = 0
    while x < iterations:
        i = 0
        inCircle = 0
        while i < n:
            tup = (random.random(), random.random())
            if ((tup[0]**2 + tup[1]**2) <= 1 ):
                inCircle += 1
            i += 1

        pi = inCircle * 4.0 / n
        error = math.fabs(pi - math.pi) * 100 / math.pi
        errorsum += error
        pisum += pi
        x += 1

    pisum = pisum / iterations
    errorsum = errorsum / iterations
    print "samples: " + str(n) + "\navg estimate: " + str(pisum) + "\navg % error: " + str(errorsum) + "\n"
print "Fin"
