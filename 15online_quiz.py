# 15. Create a Python program for an online quiz system. 
# Implement classes for quizzes, questions, and users. 
# Include methods for taking quizzes, scoring, & displaying results.

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer.lower()

    def is_correct(self, user_answer):
        return user_answer.lower() == self.answer


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self, user):
        score = sum(question.is_correct(input(f"{question.text}: ")) for question in self.questions)
        self.display_results(user, score)

    def display_results(self, user, score):
        print(f"\nResults for {user}: You scored {score} out of {len(self.questions)}")


class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


questions = [
    Question("What is the capital of France?", "Paris"),
    Question("What is the largest planet in our solar system?", "Jupiter"),
    Question("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
]

sample_quiz = Quiz("General Knowledge", questions)

user = User(input("Enter your name: "))

print(f"\nWelcome, {user}! Let's start the {sample_quiz.name} quiz.")
sample_quiz.take_quiz(user)
