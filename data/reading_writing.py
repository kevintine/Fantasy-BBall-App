# https://www.youtube.com/watch?v=Uh2ebFW8OYM --> Reading and writing to files

# open a file for reading. r indicates reading, w writing and r+ reading and writing
# remember to close file after finished with what you are doing otherwise can cause leaks
# this with block allows us to work with this file within this block of code and automatically
# close it for us once we are finished
with open(r'data\players.txt', 'r') as f:
    for line in f:
        print(line, end='')

