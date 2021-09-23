# using readlines()
"""with open("jack_and_jill.txt", 'r')as f1:
    list1 = f1.readlines()
    print(list1)"""
s = "hello world"
s = s.split(" ")
a = ""
for x in s:
    x = list(x)
    x[0] = x[0].upper()
    if x[0].isalpha()==False:
        x[1].upper()
    x = "".join(x)
    a += "".join(x) + " "
    print(a)
