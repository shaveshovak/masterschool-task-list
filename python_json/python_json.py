import json

# read the data from file
with open('students.json', 'r') as file:
    data = json.load(file)

print(data)
print(type(data))

data['age'] = 26

# modify json file
with open('students.json', 'w') as file:
    json.dump(data, file, indent=4)

print(data)
