# appending more lines to a file.
f2 = open("humpty_dumpty.txt", 'a')
f2.write("""
Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king’s horses and all the king’s men
Couldn't put Humpty together again.""")
f2.close()