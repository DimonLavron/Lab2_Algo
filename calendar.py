def compare(first, second):
    if first[0] == second[0]:
        return first[1] > second[1]
    return first[0] < second[0]

def quicksort(left, right):
    global points

    if right - left < 1:
        return

    left_idx = left + 1
    right_idx = right

    pivot = points[left]

    while True:
        while compare(points[left_idx], pivot) and left_idx < right:
            left_idx += 1

        while not compare(points[right_idx], pivot) and right_idx > left:
            right_idx -= 1

        if left_idx >= right_idx:
            break

        points[left_idx], points[right_idx] = points[right_idx], points[left_idx]

    points[left], points[right_idx] = points[right_idx], points[left]
    quicksort(left, right_idx - 1)
    quicksort(right_idx + 1, right)



input_file = open("input.txt", "r")
output_file = open("output.txt", "w")
input_data = (input_file.readline() + ",").split('),')

data = []
for i in input_data:
    if i == "":
        continue
    first, second = i.strip().split('(')
    data.append(second)

points = []
for i in data:
    first, second = i.split(', ')
    points.append((int(first), 1))
    points.append((int(second), -1))

quicksort(0, len(points) - 1)

cnt = 0
result = []
start = -1
for i in points:
    cnt += i[1]

    if cnt == 1 and i[1] == 1:
        start = i[0]

    if cnt == 0 and i[1] == -1:
        result.append((start, i[0]))
        start = -1

output_file.write(str(result))
