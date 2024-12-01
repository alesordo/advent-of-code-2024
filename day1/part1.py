list1 = []
list2 = []
with open('input', 'r') as file:
    for line in file:
        linenums = line.split()
        list1.append(int(linenums[0]))
        list2.append(int(linenums[1]))
list1.sort()
list2.sort()

distance = 0
for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])

print(distance)