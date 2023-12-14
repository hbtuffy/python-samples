file_name = "friend_10.txt"

# open file for writing
with open(file_name, "w") as text_file:
    for i in range(1, 10):
        # writing the equation such as 2 + 8 = 10
        text_file.write("{0} + {1} = {2}\n".format(i, 10 - i, 10))
