students = dict()
name = ["Alice", "Bob", "Charlie"]
score =[85, 90, 95]
students = dict(zip(name, score))
students.update({"David": 80})
students["Alice"] = 88
del students['Bob']
print(students)