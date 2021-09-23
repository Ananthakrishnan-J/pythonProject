# Python code to show how to make a copy of an image using file handling methods.
f1 = open("calvin_and_hobbes.png", 'rb')
f2 = open("new_image.png", 'wb')
f2.write(f1.read())
f1.close()
f2.close()
