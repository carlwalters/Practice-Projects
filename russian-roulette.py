
import random

print("Play russian roulette, press enter to pull trigger")

# load bullet
chamber = random.randint(1, 6)


# barrel 
barrel = random.randint(1, 6)

n = 0

while True:
    trig = str(input("Press return to continue: "))
    if trig == "":
        n += 1
        if n == 7:
        
            n -= 6
    if n == chamber:
        print("BANG!!!")
        break
    else:
        print("click...")
    