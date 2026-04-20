file_name = "output.txt"
with open(file_name, "w") as file:
    for i in range(100):
        file.write("Hello, World!\n")