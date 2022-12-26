import turtle as ttl
import random

generating = True

while generating == True:
    heading = random.randint(-90, 90)
    try:
        ttl.setheading(heading)
    except:
        print("") 
    ttl.forward(random.randint(3,5))
