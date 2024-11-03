
questions = [
    {
        "prompt": "What is the smalles prime number?",
        "options" : ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer" : "B"
    },
    {
        "prompt": "If 1=3, 2=3, 3=5, 4=4, 5=4, Then, 6=?",
        "options" : ["A. 4", "B. 2", "C. 6", "D. 3"],
        "answer" : "D"
    },
    {
        "prompt": "I am an odd number. Take away one letter and I become even. What number am I?",
        "options" : ["A. two", "B. five", "C. seven", "D. nine"],
        "answer" : "C"
    },
    {
        "prompt": "Which 3 numbers have the same answer whether they’re added or multiplied together?",
        "options" : ["A. 1,2,3", "B. 4,5,6", "C. 7,8,9", "D. 10,11,12"],
        "answer" : "A"
    }
]

def runQuiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("\nEnter your answer (A, B, C, D):  ")
        if answer == question["answer"]:
            print("Correct, horray!!\n")
            score += 1
        else:
            print("Sorry that's not right!! The correct answer was", question["answer"], "\n")

    print("You scored ", score,  "out of ", len(questions), "questions correct.")

runQuiz(questions)