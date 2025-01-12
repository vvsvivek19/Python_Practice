import json
try:
    filePath = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\sample.json"

    data = [{"Name": "Alice", "Age": 25, "City": "New York", "Country": "USA", "Profession": "Software Engineer"},
        {"Name": "Bob", "Age": 30, "City": "Los Angeles", "Country": "USA", "Profession": "Data Scientist"}]

    #Reading the existing data of json file
    try:
        with open(filePath,"r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    for item in data:
        existing_data.append(item)
    #updating the json file with new data
    with open(filePath, "w") as file:
        json.dump(existing_data,file,indent=4)
    
    # Read and modify JSON data
    with open(filePath,"r") as file:
        new_data = json.load(file)
    #Updating Bob's Age
    for record in new_data:
        if record["Name"] == "Bob":
            record["Age"] = 31
    #Saving updated data
    with open(filePath, "w") as file:
        json.dump(new_data,file,indent=4)
except Exception as msg:
    print(msg)