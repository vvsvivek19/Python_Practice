def read_line(fileName, lineNumber):
    try:
        with open(fileName,"r") as file:
            lines = file.readlines()
        total_lines = len(lines)
    except:
        print("Error Loading File")
        return

    if (lineNumber>total_lines):
        print(str(total_lines) + " file lines")
        print("Can't read line " + str(lineNumber) + "!")
    else:
        line = lines[lineNumber-1].rstrip('\n')
        print(line)

fName = input("File: ")
lNum = int(input("Line: "))
read_line(fName,lNum)