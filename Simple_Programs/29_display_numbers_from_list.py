numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item % 5 == 0:
        if item > 150:
            continue
        elif item > 500:
            break
        else:
            print(item)