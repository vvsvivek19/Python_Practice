# Sample dictionary
sample_dict = {
    "name": "John Doe",
    "age": 30,
    "is_employed": True,
    "skills": ["Python", "JavaScript", "SQL"],
    "education": {
        "high_school": "Springfield High",
        "university": "State University",
        "degree": "Bachelor of Science in Computer Science"
    },
    "projects": [
        {"title": "E-commerce Website", "duration": "6 months", "team_size": 4},
        {"title": "Inventory Management System", "duration": "4 months", "team_size": 3}
    ],
    "address": {
        "city": "New York",
        "zip_code": "10001",
        "coordinates": {"latitude": 40.7128, "longitude": -74.0060}
    }
}
print(f"Name: {sample_dict['name']} and Age: {sample_dict['age']}")
print(sample_dict["skills"])
sample_dict["skills"].append('C++')
print(sample_dict["skills"])
sample_dict["is_employed"] = True
print(sample_dict['is_employed'])
print(sample_dict["education"]["university"])
print(sample_dict["address"]["coordinates"]["latitude"])
sample_dict["projects"].append({"title": "Student Management System", "duration": "2 months", "team_size": 2})
print(sample_dict["projects"][2])
del(sample_dict["address"])
print(sample_dict)

for i in sample_dict:
    print(i)
    print(f"{i}:{sample_dict[i]}")
    
def find_project(name):
    for i in range(len(sample_dict["projects"])):
        if(sample_dict["projects"][i]["title"]==name):
            print("Yes project exists")
            exit()
    print("Project doesn't exist")
find_project("Law Management System")

def find_avg_duration():
    project_dur = []
    total_sum = 0
    avg = 0
    for project in sample_dict["projects"]:
        duration = int(project["duration"].split()[0])
        project_dur.append(duration)
    total_sum = sum(project_dur) 
    avg = total_sum / len(project_dur)
    print(f"Average project duration is: {avg} months")
find_avg_duration()
    
            