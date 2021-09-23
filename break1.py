# search for first occurrences of "e"
# and print the index number
list1 = ["a", "g", "e", "d", "y", "e", "h", "q", "p"]
i = 0
while i < 9:
    if list1[i] == "e":
        print(i)
        break
    i += 1
