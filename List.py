subjects =["C","C++","Java","Python"]

print(subjects)
print(len(subjects))
print(subjects[0])
print(subjects[2:])
print(subjects[-1])
subjects.append("Rubi")
print(subjects)
subjects.remove("Java")
print(subjects)
subjects.sort()
print(subjects)
subjects.pop()
print(subjects)
pip = subjects.index("Python")
print(pip)
pip = subjects.count("Python")
print(pip)

print("Swipt" in subjects)
print("python" not in subjects)

print(subjects + ["JavaScript","PHP",23])