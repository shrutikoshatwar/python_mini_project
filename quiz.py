# ==========================================
# QUIZ AND EXAMINATION SYSTEM
# File Name: quiz_system.py
# ==========================================

import random

# Question Bank (Tuple Format)
def load_questions():
    questions = [
        ("Which data type is immutable in Python?",
         "List", "Dictionary", "Tuple", "Set", "C"),

        ("Which keyword is used to define a function?",
         "func", "define", "def", "function", "C"),

        ("Which loop is used when iterations are known?",
         "while", "for", "do-while", "repeat", "B"),

        ("Which symbol is used for comments?",
         "//", "#", "/* */", "$", "B"),

        ("Which function takes user input?",
         "print()", "scan()", "input()", "read()", "C"),

        ("Which data structure stores key-value pairs?",
         "List", "Tuple", "Dictionary", "Set", "C"),

        ("What is the output type of 10 / 2 in Python?",
         "int", "float", "string", "boolean", "B"),

        ("Which module is used to generate random values?",
         "math", "random", "time", "os", "B"),

        ("Which keyword is used for conditional branching?",
         "switch", "loop", "if", "case", "C"),

        ("Which collection does not allow duplicate values?",
         "List", "Tuple", "Dictionary", "Set", "D")
    ]

    random.shuffle(questions)   # Bonus Feature
    return questions


# Grade Function
def calculate_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B+"
    elif percent >= 60:
        return "B"
    elif percent >= 50:
        return "C"
    else:
        return "F"


# Display Question
def display_question(question, number):

    print(f"\nQ{number}: {question[0]}")
    print("A.", question[1])
    print("B.", question[2])
    print("C.", question[3])
    print("D.", question[4])


# Get Valid Answer
def get_answer():

    while True:

        answer = input("Your Answer (A/B/C/D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer

        print("Invalid Input! Enter A, B, C or D.")


# Wrong Answer Review
def show_wrong_answers(wrong_answers):

    if not wrong_answers:
        print("\nExcellent! No wrong answers.")
        return

    print("\n====== WRONG ANSWERS REVIEW ======")

    for item in wrong_answers:

        print("\nQuestion:", item["question"])
        print("Your Answer:", item["user"])
        print("Correct Answer:", item["correct"])


# Result Report
def show_report(name, roll, score, total, wrong_answers):

    percent = (score / total) * 100
    grade = calculate_grade(percent)

    result = "PASS" if percent >= 50 else "FAIL"

    print("\n====== RESULT REPORT ======")
    print("Name :", name)
    print("Roll :", roll)
    print("Score :", score, "/", total)
    print("Percent : {:.2f}%".format(percent))
    print("Grade :", grade)
    print("Result :", result)

    show_wrong_answers(wrong_answers)


# Quiz Evaluation
def evaluate_quiz():

    print("===== PYTHON QUIZ SYSTEM =====")

    name = input("Enter Student Name: ")

    while True:
        try:
            roll = int(input("Enter Roll Number: "))
            break
        except ValueError:
            print("Please enter a valid roll number!")

    questions = load_questions()

    score = 0
    wrong_answers = []

    for i, q in enumerate(questions, start=1):

        display_question(q, i)

        answer = get_answer()

        if answer == q[5]:
            score += 1
            print("✓ Correct!")
        else:
            print("✗ Incorrect!")

            wrong_answers.append({
                "question": q[0],
                "user": answer,
                "correct": q[5]
            })

    show_report(
        name,
        roll,
        score,
        len(questions),
        wrong_answers
    )


# Main Program
evaluate_quiz()