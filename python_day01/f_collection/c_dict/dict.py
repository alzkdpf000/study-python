student = {
    "name": "한동석",
    "email": "tedhan1204@gmail.com"
}

print(student["name"])
print(student.get("email"))
# print(student["phone"])
print(student.get("phone", "01012341234"))

if 'name' in student:
    student['email'] = 'test@gmail.com'

print(student)

if '한동석' in student.values():
    print('한동석님 어서오세요')

print(student.keys())

my_ditc = {
    1: "한동석",
    False: [10, 20, 30]
}

print(my_ditc[10 > 11])

for key, value in student.items():
    print(key, value)


