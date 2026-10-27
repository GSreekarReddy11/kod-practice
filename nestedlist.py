students=[
    ["Alice",85,90,78],["Bob",70,88,92],["Charlie",95,80,89],["David",60,75,68],
    ["Eva",88,92,95],["Frank",72,65,80],["Grace",90,85,91]
]
for student in students:
    name = student[0]
    scores = student[1:]
    avg = sum(scores) / len(scores)
    print(f"{name}: {avg:.2f}")
