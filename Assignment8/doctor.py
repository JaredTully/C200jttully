def has_appendicitis():
    questions = ["Do you have adominal pain: 1/0 ", "Do you have nausea: 1/0 ", "Do you have vomiting: 1/0 ", "Do you have fever: 1/0 ", "Do you have loss of appetite: 1/0 "]

    count = 0

    for x in questions:
        yesNo = str(input(x))
        if yesNo == "1":
            count += 1
        if count == 3:
            return "Appendicitis"

    return "No Appendicitis."

print(has_appendicitis())