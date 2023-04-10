a = ["daniel", "shai", "roei"]
if a[0] == "inbar" or a[1] == "inbar" or a[2] == "inbar":
    print("inbar")

if "inbar" in a:
    print("inbar")

first_array = []
second_array = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
if first_array:  # false
    print("first has no items")
if second_array:  # true
    print("second array has items")
print(len(second_array))
if len(second_array) > 2:
    print("we have at least 3 items in second")

d = "inbar"
g = "inbar"
g = "havdala"
g = "inbar"
f = [1, 2, 3]
h = [1, 2, 3]
if d is g:
    print("d is g")
if f is h:
    print("f is h")
if type(d) is int:\
    print("d is int")
