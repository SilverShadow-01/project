import random

def generate_question(level):
    if level == "easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
    elif level == "medium":
        a, b = random.randint(10, 50), random.randint(10, 50)
    else:
        a, b = random.randint(50, 100), random.randint(1, 100)

    operation = random.choice(["+", "-", "*", "/"])
    if operation == "/":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
    question = f"{a} {operation} {b}"
    try:
        answer = eval(question)
    except Exception:
        answer = 0
    return question, round(answer, 2)

def quiz():
    print("Welcome to the Math Quiz Game!")
    level = input("Choose difficulty (easy, medium, hard): ").lower()
    score = 0
    for i in range(5):
        question, correct_answer = generate_question(level)
        print(f"Question {i+1}: {question}")
        try:
            user_answer = float(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {correct_answer}\n")
        except ValueError:
            print("Please enter a valid number.\n")
    print(f"Quiz finished! Your score: {score}/5")

if __name__ == "__main__":
    quiz()
