# food = ["fattoush", "wings", "pizza", "brownie", "cookie"]
#print(food[-1])

# food.append("hummus")
# food.insert(0, "apple")
# food.remove("wings")
# #print(len(food))

#for i in food:
#    print(i.upper())
# # had an error or wasn't returning what i wanted it to because i originally wrote print(i.upper). resolved by adding parantheses after upper

# # food_new = [food[0], food[-1]]
# # print(food_new)

# if "potato" in food:
#     print("A potato!")
# else:
#     print("No potato :(")

# ## 3.2: Slicing and Striding
# numbers = list(range(21))
# #print(numbers)

def get_first_15(numbers):
     lst = numbers[:15]
     return lst

# # print(get_first_15(numbers))

# # error: list inidces must be integers or slices, not tuple
# #originally had first_15 = list(numbers[0,15])
# #changed to first_15 = numbers[:15]

def get_every_5th(lst):
    every_5th = lst[::5]
    return every_5th


def reverse_and_stride(lst):
    reversed_lst = lst[::-1]
    return reversed_lst[::3]

# step1 = get_first_15(numbers)
# step2 = get_every_5th(step1)
# step3 = reverse_and_stride(step2)
# print(step3)


# 3.3 Nested Lists
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
 ]

#print(numbers[2][:])
#print(numbers[1][1])
# numbers.append([10, 11, 12])

def sum_nested(lst):
     total = 0
     for row in lst:
         for num in row:
             total += num
     return total

# #print(sum_nested(numbers))
def create_grid():
    grid = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        grid.append(row)
    return grid
#grid = create_grid()

#debug: was showing a grid of 1's because i had num =+1 instead of =+ 1

def mult_3(lst):
    new_grid = []
    for row in lst:
        new_row = []
        for entry in row:
            if entry % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(entry)
        new_grid.append(new_row)

    return new_grid

#print(grid)

#print(mult_3(grid))

def sum_spec(lst):
    total = 0
    for row in lst:
        for value in row:
            if value != "?":
                total += value
    return total

# step1 = mult_3(grid)
# step2 = sum_spec(step1)
# print(step2)

## 4.1 Dictionary Operations
# ages = {
#     "katie": 30,
#     "mariam": 42,
#     "safia": 25,
#     "mira": 48
# }

#print(ages["katie"])
# ages["mira"] = 100
# ages["milana"] = 52
# del ages["mariam"]

# for name, age in ages.items():
#     print(name, "is", age, "years old")

#debug: forgot to add a colon after first line
