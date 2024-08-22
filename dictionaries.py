person = {
    "first_name": "Barra",
    "last_name": "Harrison",
    "age": 26,
}

print(person["first_name"], person["last_name"], person["age"])

new_dict = person.copy()

print(new_dict.pop("last_name"))
print(new_dict)

new_dict.update({"Height": 6.0})
print(new_dict)

tasks = {
    "task": {
        "name": "Study Korean",
        "priority": "high",
        "status": "incomplete"
    }
}

print(tasks)

