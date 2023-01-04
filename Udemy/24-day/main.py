# with open("C:/Users/Esteban/Desktop/SF/Curso-Udemy/Udemy/24-day/my_file.txt") as file:

#     contents = file.read()

#     print(contents)
# To avoid typing this close method, we use the with open as "name" keywords like above
# file.close()

# Write in a file
# This "w" (write mode) mode deletes anything that were in the file before.
with open("Udemy/24-day/my_file.txt", mode="w") as file:
    file.write("New text.")

# The write mode also works for creating new files if you "open" a file that doesn't exists

# If you want to append some text into a file, use mode = "a" (append)
with open("Udemy/24-day/my_file.txt", mode="a") as file:
    file.write("\nAppending some text.")

