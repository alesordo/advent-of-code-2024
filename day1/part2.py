
list1 = []
list2 = []
with open('input', 'r') as file:
    for line in file:
        linenums = line.split()
        list1.append(int(linenums[0]))
        list2.append(int(linenums[1]))

list2dict = {}
for num in list2:
    if not num in list2dict:
        list2dict[num] = 1
    else:
        list2dict[num] = list2dict[num] + 1

similarity = 0
for num in list1:
    if num in list2dict:
        similarity += list2dict[num] * num

print(similarity)