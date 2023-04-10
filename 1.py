print("Hello World")
a = 4
b = 5
c = "inbar"
d = True
# lists
my_list = ["inbar", "havdala", 21, True]

# dictionary
my_dict = {"fname": "inbar",
           "lname": "havdala",
           "age": 21,
           "is_married": True}

# tuple - Permanent
my_tuple = ("inbar", "havdala", 21)
# won't work
my_tuple[2] = "inbar"

print(a + b)
print(my_list[0])
my_list[2] = 22  # update list
print(my_dict["age"])
