# https://www.youtube.com/watch?v=Uh2ebFW8OYM --> Reading and writing to files

import csv
import classes

# open a file for reading. r indicates reading, w writing and r+ reading and writing
# remember to close file after finished with what you are doing otherwise can cause leaks
# this with block allows us to work with this file within this block of code and automatically
# close it for us once we are finished
with open(r'data\players.txt', 'r') as f:
    players = csv.reader(f, delimiter=',')
    for p in players:
    	print(p)
        #create a player object
player = classes.Player(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7])
print(player.get_name())
        




