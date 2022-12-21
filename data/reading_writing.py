# https://www.youtube.com/watch?v=Uh2ebFW8OYM --> Reading and writing to files

import csv
import classes
# open a file for reading. r indicates reading, w writing and r+ reading and writing
# remember to close file after finished with what you are doing otherwise can cause leaks
# this with block allows us to work with this file within this block of code and automatically
# close it for us once we are finished
players = []
playerslist = []
workingplayerslist = ["Lebron James", "Ben Simmons"]

with open(r'data\players.txt', 'r') as f:
    playerstxt = csv.reader(f, delimiter=',')
    for p in playerstxt:
        players.append(classes.Player(p[0]))
        playerslist.append(p)

for p in workingplayerslist:
    print(p)
    print("Space")
for p in players:
    print(p.get_name())
    print("Space")
for p in playerslist:
    print(p)
    print("Space")
    	

        




