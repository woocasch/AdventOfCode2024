with open("input.txt", "r") as file:
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    elements = [element for element in line.split(" ") if element]
    list1.append(int(elements[0]))
    list2.append(int(elements[1]))

list1.sort()
list2.sort()

totalDistance = 0
for index, value1 in enumerate(list1):
    value2 = list2.count(value1)
    distance = value1 * value2
    totalDistance += distance

print(totalDistance)