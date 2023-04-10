names = ["inbar", "lanir", "eran", "kfir", "alina"]
numbers = [1, 2, 3, 4, 5, 6, 7, ]
print(list(range(20, 1, -3)))

for name in names:
    print(name, end=',')

for i in range(30):
    print(i)
# wont work -
for name in names:
    name = "liran"
# change index
for i in range(len(names)):
    names[i] = "liran"
    print(names[i])

a = 0
while a < 5:
    print(a)
    a = a + 1
else:
    print("finished")

for number in numbers:
    if number == 3:
        continue
    if number == 2:
        break
    print(number)
else:
    print("finished")


