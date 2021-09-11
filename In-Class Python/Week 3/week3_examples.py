# name = input("What is your name?")
# print("hello", name)

# while not isinstance(num, int):
#     try:
#         age = int(input("What is your age?"))
#     except ValueError:
#         print("Invalid age value. Please enter an integer.")
# print("Next year you will be", age + 1)

print(1, 2, 3, 4, sep=', ', end=", ")
print(5, 6, 7, 8, sep=', ')

with open('top_ten_movies.txt', 'r') as file:
    for line in file:
        print(line, end="")

movies = []
with open('movies_only.txt', 'r') as file:
    for line in file:
        movies.append(line.rstrip())
print(movies)

with open('heights.txt', 'r') as file:
    for line in file:
        info = line.split()
        # print(info)
        print(info[0], info[1], "is", info[2], "inches tall.")



