# search for the all occurrences of "e"
# and print the index number
# and add the letter z to every other letter except "e"
list1 = ["a", "g", "e", "d", "y", "e", "h", "q", "p"]
i = 0
while i < 9:
    if list1[i] == "e":
        print(i)
        i+=1
        continue
    list1[i] = list1[i] + "z"
    i += 1
print(list1)
