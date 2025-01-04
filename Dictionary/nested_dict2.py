data = {
    "id": 101,
    "name": "Alice",
    "projects": [
        {"title": "Project X", "duration": "6 months"},
        {"title": "Project Y", "duration": "3 months"}
    ],
    "contact": {"email": "alice@example.com", "phone": "123-456-7890"}
}
for x in data["projects"]:
    print(x["title"])

data["contact"]["phone"] = input("Enter New Phone number: ")
print(data["contact"])

project_details = ["title","duration"]
projects_dict = {}
projects_dict = projects_dict.fromkeys(project_details)
projects_dict["title"] = input("Enter New project title")
projects_dict["duration"] = input("Enter project duration")
data["projects"].append(projects_dict)
print(data["projects"])