	

import random


# The line below will "roll the dice" 20 times.
# Don't copy this 'for' loop into your program.
# It is just here so we can try this example over and over.
for i in range(50):

    # The line below will roll a random number 0-4.
    # If we roll a '0' then print that we encountered a dragon.
    if random.randrange(5) == 0:
        print("DRAGON!!!")
    else:
        print("No dragon.")
