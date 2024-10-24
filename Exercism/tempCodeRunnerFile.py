def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    new_list = []
    for index, marks in enumerate(student_scores):
        new_list.append(f"{index+1}. {student_names[index]}: {marks}")
    return new_list
student_scores = [100, 99, 90, 84, 66, 53, 47]
student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
print(student_ranking(student_scores, student_names))