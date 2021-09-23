# reading from file using for loop
with open("jack_and_jill.txt",  'r') as f1:
    for lines in f1:
        print(lines,end="")
